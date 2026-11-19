# Inconsistent face winding

## What it checks

Adjacent faces traverse the same shared edge in the same direction.

## How detection works

Compares traversal direction along two-face shared edges.

## Why it matters for UE5

This can cause inconsistent face normals and backface culling.

## How to fix

Select the flagged faces and inspect Face Orientation. For a regular continuous shell, try Shift+N (Recalculate Outside).

## Important exceptions

A completely inverted closed shell can pass this check; see Inverted Normals.
