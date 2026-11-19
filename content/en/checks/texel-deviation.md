# Inconsistent Texel Density

## What it checks

Estimated pixel density varies considerably between faces.

## How detection works

Estimates px/m from UV and world-space face areas using an area-weighted median.

## Why it matters for UE5

Texture detail may appear inconsistent across the asset.

## How to fix

Inspect UV scale. These measurements are estimates based on the chosen texture size.

## Important exceptions

The estimate depends on chosen texture resolution, UVs, and scene scale.
