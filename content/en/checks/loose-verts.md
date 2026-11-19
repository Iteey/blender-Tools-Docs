# Loose vertices

## What it checks

Some vertices are not connected to any edges.

## How detection works

Finds vertices without connected edges.

## Why it matters for UE5

Isolated vertices normally add no useful data to a Static Mesh export.

## How to fix

Select and delete unneeded isolated vertices.

**Steps and shortcuts (Blender default keymap):**

1. In **Edit Mode**, run `F3` → **Delete Loose** to remove stray geometry.
2. To preserve some vertices, select only the unwanted ones and use `X` → **Vertices**.
3. Re-run the check. Helper vertices are not automatically an error.
