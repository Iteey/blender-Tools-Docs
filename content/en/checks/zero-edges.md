# Zero-length edges

## What it checks

Some edges join vertices at nearly identical positions.

## How detection works

Measures each edge’s endpoints (threshold: 1e-6 Blender units).

## Why it matters for UE5

Zero-length edges complicate processing and can affect normals.

## How to fix

Inspect the selected edges; use Merge by Distance only where the points should actually merge.
