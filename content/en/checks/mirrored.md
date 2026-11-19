# Negative/mirrored Scale

## What it checks

The world transform has a negative determinant (mirrored orientation).

## How detection works

Checks the sign of the object world-matrix determinant.

## Why it matters for UE5

Mirroring can alter triangle orientation when exporting.

## How to fix

Inspect Face Orientation and the imported mesh; apply scale and recalculate normals only if required.

## Important exceptions

Mirroring may be intentional; verify final normals after export.
