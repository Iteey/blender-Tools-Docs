# Missing UV map

## What it checks

The mesh has no active UV map.

## How detection works

Checks for an active UV layer.

## Why it matters for UE5

Most image-textured materials need UVs in UE5, but procedural approaches may not.

## How to fix

Create and inspect UVs if the asset requires image textures.

**Steps and shortcuts (Blender default keymap):**

1. In **Edit Mode**, select relevant faces (`A`) and use `U` → **Unwrap** (after placing appropriate seams).
2. For a quick starting point, choose `U` → **Smart UV Project**, or find it using `F3`.
3. Open **UV Editing** and review the islands, stretching, and margins.

## Important exceptions

Procedural and world-space materials may not need UVs.
