# Nearby vertices

## What it checks

Some vertices are very close to one another.

## How detection works

Uses BMesh find_doubles with a configurable radius and vertex-count safety limit.

## Why it matters for UE5

They may be unmerged duplicates, or intentional seams and gaps.

## How to fix

Inspect the selected vertices. Merge by Distance only if merging will not harm the model.

**Steps and shortcuts (Blender default keymap):**

1. Inspect the flagged vertices closely to determine whether they are meant to be connected.
2. For accidental duplicates, use `M` → **By Distance** in **Edit Mode**; adjust the threshold in the last-operation panel (`F9`).
3. Do not merge nearby but intentionally separate components.

## Important exceptions

Close vertices at seams may be intentional; the scan has a size limit.
