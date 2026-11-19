# Pivot / Origin position

## What it checks

The object origin is not at the configured expected location.

## How detection works

Compares origin with chosen bounds center, bounds bottom, or world origin.

## Why it matters for UE5

This can affect snapping, placement, and rotation of Static Meshes in UE5.

## How to fix

Check project conventions, then place the origin using Origin tools.

## Important exceptions

Origin placement is project-specific, not governed by a universal rule.
