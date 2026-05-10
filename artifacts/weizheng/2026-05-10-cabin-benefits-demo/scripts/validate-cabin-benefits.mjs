import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dataPath = path.resolve(__dirname, '../data/cabin-benefits.mock.json');
const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

const errors = [];

if (!data.flight) {
  errors.push('missing flight');
}

if (!Array.isArray(data.cabins)) {
  errors.push('cabins must be an array');
}

const cabins = Array.isArray(data.cabins) ? data.cabins : [];

if (cabins.length < 3) {
  errors.push('at least 3 cabins are required');
}

const selectableCabins = cabins.filter(cabin => cabin.selectable);
const unavailableCabins = cabins.filter(cabin => !cabin.selectable);

if (selectableCabins.length < 2) {
  errors.push('at least 2 selectable cabins are required');
}

if (unavailableCabins.length < 1) {
  errors.push('at least 1 unavailable cabin is required');
}

for (const cabin of cabins) {
  for (const field of ['cabinId', 'name', 'price', 'currency', 'sortOrder']) {
    if (cabin[field] === undefined || cabin[field] === null || cabin[field] === '') {
      errors.push(`cabin ${cabin.cabinId || '<unknown>'} missing ${field}`);
    }
  }

  if (!Array.isArray(cabin.benefits)) {
    errors.push(`cabin ${cabin.cabinId || '<unknown>'} benefits must be an array`);
    continue;
  }

  if (cabin.selectable && cabin.benefits.length < 3) {
    errors.push(`selectable cabin ${cabin.cabinId} must have at least 3 benefits`);
  }

  if (!cabin.selectable && !cabin.unavailableReason) {
    errors.push(`unavailable cabin ${cabin.cabinId} missing unavailableReason`);
  }

  for (const benefit of cabin.benefits) {
    for (const field of ['benefitId', 'name', 'summary']) {
      if (!benefit[field]) {
        errors.push(`benefit in cabin ${cabin.cabinId} missing ${field}`);
      }
    }
  }
}

if (errors.length > 0) {
  console.error('Cabin benefits mock data validation failed:');
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log('Cabin benefits mock data validation passed.');
console.log(`Cabins: ${cabins.length}`);
console.log(`Selectable cabins: ${selectableCabins.length}`);
console.log(`Unavailable cabins: ${unavailableCabins.length}`);
