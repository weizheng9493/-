#!/usr/bin/env python3
"""Summarize Hanglv flight review CSV data for problem radar input."""

from __future__ import annotations

import argparse
import collections
import csv
import json
import re
from pathlib import Path


DEFAULT_KEYWORDS = [
    "价格",
    "票价",
    "报销",
    "发票",
    "行程单",
    "客服",
    "退款",
    "退票",
    "改签",
    "支付",
    "保险",
    "搭售",
    "航班",
    "搜索",
    "筛选",
    "舱位",
    "下单",
    "出票",
    "Bug",
    "重新搜索",
]


def open_csv(path: Path):
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            f = path.open(newline="", encoding=encoding)
            sample = f.read(4096)
            f.seek(0)
            dialect = csv.Sniffer().sniff(sample)
            return f, encoding, dialect
        except Exception:
            try:
                f.close()
            except Exception:
                pass
    raise RuntimeError(f"Unable to read CSV: {path}")


def split_labels(value: str) -> list[str]:
    return [x.strip() for x in re.split(r"[;；]", value or "") if x.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--sample", type=int, default=20)
    parser.add_argument("--keywords", default=",".join(DEFAULT_KEYWORDS))
    args = parser.parse_args()

    path = Path(args.csv_path)
    keywords = [x.strip() for x in args.keywords.split(",") if x.strip()]

    f, encoding, dialect = open_csv(path)
    with f:
        reader = csv.DictReader(f, dialect=dialect)
        headers = reader.fieldnames or []
        rows = list(reader)

    score_counter: collections.Counter[str] = collections.Counter()
    object_counter: collections.Counter[str] = collections.Counter()
    label_counter: collections.Counter[str] = collections.Counter()
    neg_label_counter: collections.Counter[str] = collections.Counter()
    keyword_counter: collections.Counter[str] = collections.Counter()
    keyword_samples: dict[str, list[dict[str, str]]] = {k: [] for k in keywords}
    neg_samples: list[dict[str, str]] = []
    content_rows = 0
    neg_rows = 0
    neg_content_rows = 0

    for row in rows:
        score = (row.get("itemscore") or "").strip()
        content = (row.get("content") or "").strip()
        labels = split_labels(row.get("merged_labels") or "")
        text = f"{content};{row.get('merged_labels') or ''}"

        if score:
            score_counter[score] += 1
        if row.get("objectid"):
            object_counter[(row.get("objectid") or "").strip()] += 1
        if content:
            content_rows += 1

        is_neg = score in {"1", "2"}
        if is_neg:
            neg_rows += 1
            if content:
                neg_content_rows += 1
                if len(neg_samples) < args.sample:
                    neg_samples.append(
                        {
                            "score": score,
                            "time": row.get("createtime", ""),
                            "labels": row.get("merged_labels", ""),
                            "content": content[:300],
                        }
                    )

        for label in labels:
            label_counter[label] += 1
            if is_neg:
                neg_label_counter[label] += 1

        lowered = text.lower()
        for keyword in keywords:
            if keyword.lower() in lowered:
                keyword_counter[keyword] += 1
                if content and len(keyword_samples[keyword]) < 3:
                    keyword_samples[keyword].append(
                        {
                            "score": score,
                            "time": row.get("createtime", ""),
                            "labels": row.get("merged_labels", ""),
                            "content": content[:220],
                        }
                    )

    output = {
        "file": str(path),
        "encoding": encoding,
        "headers": headers,
        "total_rows": len(rows),
        "content_rows": content_rows,
        "negative_rows_1_2": neg_rows,
        "negative_content_rows": neg_content_rows,
        "score_distribution": dict(sorted(score_counter.items())),
        "objectid_distribution": dict(object_counter.most_common()),
        "top_labels": label_counter.most_common(args.top),
        "top_negative_labels": neg_label_counter.most_common(args.top),
        "keyword_counts": keyword_counter.most_common(args.top),
        "negative_samples": neg_samples,
        "keyword_samples": {k: v for k, v in keyword_samples.items() if v},
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
