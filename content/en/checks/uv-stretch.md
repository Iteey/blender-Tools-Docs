# UV distortion

## What it checks

Relative edge lengths differ substantially between UV and 3D geometry.

## How detection works

Compares UV/3D triangle edge-length ratios against a configurable threshold.

## Why it matters for UE5

The texture may look stretched; sometimes the distortion is intentional.

## How to fix

Test with a checker texture, then relax or re-unwrap problematic islands.

## Important exceptions

This is a geometric test; it cannot measure the final UE5 material appearance.
