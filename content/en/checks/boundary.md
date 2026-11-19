# Open boundary edges

## What it checks

The mesh contains edges used by exactly one face.

## How detection works

Finds edges used by exactly one face. Runs in Advanced mode.

## Why it matters for UE5

These may indicate holes in closed props, but are normal for planes, leaves, and some other assets.

## How to fix

Review the edges. Close holes only if the asset is intended to form a closed shell.

**Steps and shortcuts (Blender default keymap):**

1. In **Edit Mode**, select the border of the hole (optionally `F3` → **Select Non Manifold**).
2. For a simple hole, select its surrounding edges/vertices and press `F` (**Fill**).
3. For a more complex border, try `F3` → **Grid Fill**, then review new faces and UVs.
4. Do not close intentionally open geometry such as planes, leaves, or open tubes.

## Important exceptions

Leaves, planes, and intentionally open surfaces are often valid.
