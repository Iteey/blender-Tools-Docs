# Strongly bent smooth faces

## What it checks

A smooth-shading transition crosses a steep angle between neighboring faces.

## How detection works

Compares geometric-normal angles between adjacent smooth faces.

## Why it matters for UE5

This can create unwanted highlights or normal artifacts.

## How to fix

Inspect the shading; mark an edge Sharp or adjust smoothing when necessary.

**Steps and shortcuts (Blender default keymap):**

1. In **Edit Mode**, inspect the flagged smooth faces and hard transitions.
2. If an edge should be sharp, switch to edge selection (`2`), select it, and use `F3` → **Mark Sharp**.
3. If shading remains wrong, inspect normals, topology, and **Shade Auto Smooth / Set Sharpness by Angle** options available in your Blender version.
4. Do not mark every edge sharp automatically; it can ruin intentionally smooth transitions.
