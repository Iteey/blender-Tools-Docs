# Degenerate geometry

## What it checks

Some faces have almost zero surface area.

## How detection works

Finds faces with area at or below 1e-12 in Blender units.

## Why it matters for UE5

These can produce artifacts during triangulation or import.

## How to fix

Select the affected faces, remove degenerate geometry, and inspect the repaired mesh.

**Steps and shortcuts (Blender default keymap):**

1. In **Edit Mode**, locate the reported geometry. Use `1`/`2`/`3` (number row) for vertex/edge/face selection modes.
2. For coincident vertices, select the area and use `M` → **By Distance** with a small threshold.
3. For remaining zero-area geometry, use `F3` → **Degenerate Dissolve**. Inspect the result before accepting changes.
