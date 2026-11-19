# Inconsistent Texel Density

## What it checks

Estimated pixel density varies considerably between faces.

## How detection works

Estimates px/m from UV and world-space face areas using an area-weighted median.

## Why it matters for UE5

Texture detail may appear inconsistent across the asset.

## How to fix

Inspect UV scale. These measurements are estimates based on the chosen texture size.

**Steps and shortcuts (Blender default keymap):**

1. Open **UV Editing**, select relevant islands (`L` under the pointer), and adjust scale with `S`.
2. Check visual density with a checker texture, then re-run the Texel Density check.
3. Different density can be intentional (hero details or hidden surfaces); this is a judgment call.

## Important exceptions

The estimate depends on chosen texture resolution, UVs, and scene scale.
