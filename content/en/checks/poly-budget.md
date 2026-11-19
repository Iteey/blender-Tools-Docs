# Triangle budget

## What it checks

Triangle count after modifiers exceeds the configured budget.

## How detection works

Counts evaluated triangles after modifiers. Without a configured budget, reports information rather than failure.

## Why it matters for UE5

High triangle counts may be expensive in some scenes; Nanite and LOD suitability must be evaluated separately.

## How to fix

Check the asset role, project budget, and profiling results in UE5.

## Important exceptions

Triangle count alone does not predict FPS or Nanite efficiency.
