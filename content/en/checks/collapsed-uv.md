# Collapsed UV faces

## What it checks

Some UV polygons have nearly zero area.

## How detection works

Computes polygon area in the active UV map.

## Why it matters for UE5

The texture can collapse to a line or point on those faces.

## How to fix

Select and unwrap the faces again if they must receive texture detail.

**Steps and shortcuts (Blender default keymap):**

1. In **UV Editing**, select the affected faces and examine their UV coordinates.
2. Unwrap them again from **Edit Mode** in the 3D Viewport: `U` → **Unwrap** or **Smart UV Project**.
3. Make sure required UV faces are not collapsed to a line or point. Intentional collapsed UVs require manual judgment.
