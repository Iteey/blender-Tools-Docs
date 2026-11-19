# Negative/mirrored Scale

## What it checks

The world transform has a negative determinant (mirrored orientation).

## How detection works

Checks the sign of the object world-matrix determinant.

## Why it matters for UE5

Mirroring can alter triangle orientation when exporting.

## How to fix

Inspect Face Orientation and the imported mesh; apply scale and recalculate normals only if required.

**Steps and shortcuts (Blender default keymap):**

1. In **Object Mode**, inspect negative `Scale` components in the Transform sidebar (`N`).
2. If the pipeline requires positive scale, use `Ctrl + A` → **Scale** and inspect the result.
3. In **Edit Mode**, `Shift + N` (**Recalculate Outside**) may help on a regular closed shell; confirm **Face Orientation** and UE5 import.

## Important exceptions

Mirroring may be intentional; verify final normals after export.
