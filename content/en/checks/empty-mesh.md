# Empty mesh

## What it checks

The mesh contains no polygon faces.

## How detection works

Checks whether the source mesh contains any polygon faces.

## Why it matters for UE5

An empty Static Mesh has no drawable surface in UE5.

## How to fix

Inspect the object in Edit Mode and restore or create the intended geometry.

**Steps and shortcuts (Blender default keymap):**

1. Select the object and press `Tab` to enter **Edit Mode**. Check whether it contains vertices and faces.
2. If geometry was deleted, recover it with `Ctrl + Z` (if the operation is still in undo history) or reimport the correct mesh.
3. Use `Shift + A` (**Add**) in Edit Mode to create geometry when appropriate. Never add meaningless faces just to silence the check.
