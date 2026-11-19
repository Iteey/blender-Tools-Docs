# Inconsistent face winding

## What it checks

Adjacent faces traverse the same shared edge in the same direction.

## How detection works

Compares traversal direction along two-face shared edges.

## Why it matters for UE5

This can cause inconsistent face normals and backface culling.

## How to fix

Select the flagged faces and inspect Face Orientation. For a regular continuous shell, try Shift+N (Recalculate Outside).

**Steps and shortcuts (Blender default keymap):**

1. Enter **Edit Mode** (`Tab`) and enable **Face Orientation** in **Viewport Overlays**.
2. For a normal closed shell, select relevant faces and press `Shift + N` (**Recalculate Outside**).
3. To invert a specific face, select it and use `Alt + N` → **Flip**.
4. Scan again. `Shift + N` may not resolve ambiguous open or non-manifold regions.

## Important exceptions

A completely inverted closed shell can pass this check; see Inverted Normals.
