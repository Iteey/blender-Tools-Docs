# Degenerate geometry

## What it checks

Some faces have almost zero surface area.

## How detection works

Finds faces with area at or below 1e-12 in Blender units.

## Why it matters for UE5

These can produce artifacts during triangulation or import.

## How to fix

Select the affected faces, remove degenerate geometry, and inspect the repaired mesh.
