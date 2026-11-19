# UV overlap

## What it checks

Some UV triangles overlap with a positive area.

## How detection works

Triangulates UV faces and tests positive-area intersections, with triangle and pair safety caps.

## Why it matters for UE5

Overlaps are fine for mirroring and tiling but unsuitable for unique baking or lightmaps.

## How to fix

Inspect the UV Editor. Separate islands only in channels that require unique coverage.

**Steps and shortcuts (Blender default keymap):**

1. Open **UV Editing** and inspect the affected islands; hover an island and press `L` to select linked UVs.
2. Move/rotate/scale islands with `G`, `R`, `S`, or use `F3` → **Pack Islands** after a proper unwrap.
3. Mirrored and shared UVs may be intentional for ordinary textures, but usually **not valid for lightmap UVs**.

## Important exceptions

Overlap can be intentional (mirrored/stacked UV). Complexity limits yield SKIP, not PASS.
