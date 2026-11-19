# Nearby vertices

## What it checks

Some vertices are very close to one another.

## How detection works

Uses BMesh find_doubles with a configurable radius and vertex-count safety limit.

## Why it matters for UE5

They may be unmerged duplicates, or intentional seams and gaps.

## How to fix

Inspect the selected vertices. Merge by Distance only if merging will not harm the model.

## Important exceptions

Close vertices at seams may be intentional; the scan has a size limit.
