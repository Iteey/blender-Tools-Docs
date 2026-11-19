# Lightmap UV overlap

## What it checks

Lightmap UV islands overlap.

## How detection works

Checks for intersecting triangles in the selected lightmap UV, subject to scan limits.

## Why it matters for UE5

Baked lighting can show illumination artifacts.

## How to fix

Separate islands and leave appropriate padding between them.

**Steps and shortcuts (Blender default keymap):**

1. In **UV Editing**, switch to the lightmap UV channel and inspect overlapping islands.
2. If necessary, unwrap with `U` → **Smart UV Project** or **Unwrap**, then use `F3` → **Pack Islands** with an appropriate **Margin**.
3. Check again. Unlike texture UVs, overlapping lightmap UVs typically cause baked-lighting artifacts.

## Important exceptions

Does not validate padding against lightmap resolution. Scan size is bounded.
