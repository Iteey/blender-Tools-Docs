# Lightmap UV outside 0-1

## What it checks

The lightmap UV channel contains out-of-bounds or zero-area faces.

## How detection works

Checks lightmap UVs for out-of-range coordinates and collapsed areas.

## Why it matters for UE5

Baked lighting can exhibit visible artifacts.

## How to fix

Make a valid 0–1 lightmap unwrap with non-collapsed islands.

## Important exceptions

Only applies when lightmap checking is on and the UV channel exists.
