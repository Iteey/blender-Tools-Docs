# Inverted normals (closed shells)

## What it checks

A closed outer shell has negative signed volume: its faces may all point inward.

## How detection works

Uses signed volume to analyze closed shells; open and nested shells are ambiguous.

## Why it matters for UE5

The exterior can be culled, and the wrong side of the surface may be visible in UE5.

## How to fix

Select flagged faces and inspect Blender Face Orientation. Use Shift+N for an ordinary closed shell; manually review nested cavities and special cases.

## Important exceptions

Open meshes, cavities, and nested shells may not have a reliably classified exterior. Negative Scale is checked separately.
