# Missing UV map

## What it checks

The mesh has no active UV map.

## How detection works

Checks for an active UV layer.

## Why it matters for UE5

Most image-textured materials need UVs in UE5, but procedural approaches may not.

## How to fix

Create and inspect UVs if the asset requires image textures.

## Important exceptions

Procedural and world-space materials may not need UVs.
