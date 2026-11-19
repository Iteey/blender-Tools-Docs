# Lightmap UV outside 0-1

## What it checks

The lightmap UV channel contains out-of-bounds or zero-area faces.

## How detection works

Checks lightmap UVs for out-of-range coordinates and collapsed areas.

## Why it matters for UE5

Baked lighting can exhibit visible artifacts.

## How to fix

Make a valid 0–1 lightmap unwrap with non-collapsed islands.

**Steps and shortcuts (Blender default keymap):**

1. In **UV Editing**, select the actual lightmap UV channel, not the main texture UV channel.
2. Select islands (`A`), fit them into 0–1 with `G` and `S`, then use `F3` → **Pack Islands**.
3. Check that islands stay within bounds and retain padding; UDIMs and tiling are generally not suitable for lightmap UVs.

## Important exceptions

Only applies when lightmap checking is on and the UV channel exists.
