# Triangle budget

## What it checks

Triangle count after modifiers exceeds the configured budget.

## How detection works

Counts evaluated triangles after modifiers. Without a configured budget, reports information rather than failure.

## Why it matters for UE5

High triangle counts may be expensive in some scenes; Nanite and LOD suitability must be evaluated separately.

## How to fix

Check the asset role, project budget, and profiling results in UE5.

**Steps and shortcuts (Blender default keymap):**

1. Enable **Overlays → Statistics** in the 3D Viewport to see triangle counts.
2. For a trial simplification, add a **Decimate** modifier (Collapse mode) to a duplicate (`Shift + D`) and adjust **Ratio**.
3. For Nanite vs LOD, compare performance in UE5: polygon count alone cannot prove which is faster.

## Important exceptions

Triangle count alone does not predict FPS or Nanite efficiency.
