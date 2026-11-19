# UV overlap

## What it checks

Some UV triangles overlap with a positive area.

## How detection works

Triangulates UV faces and tests positive-area intersections, with triangle and pair safety caps.

## Why it matters for UE5

Overlaps are fine for mirroring and tiling but unsuitable for unique baking or lightmaps.

## How to fix

Inspect the UV Editor. Separate islands only in channels that require unique coverage.

## Important exceptions

Overlap can be intentional (mirrored/stacked UV). Complexity limits yield SKIP, not PASS.
