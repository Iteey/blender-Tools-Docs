# Loose edges

## What it checks

Some edges do not belong to any polygon face.

## How detection works

Finds edges that do not belong to any polygon.

## Why it matters for UE5

They do not form a drawable surface in a typical game mesh.

## How to fix

Remove unnecessary loose geometry after checking whether it is still needed for modeling.

**Steps and shortcuts (Blender default keymap):**

1. Enter **Edit Mode** (`Tab`), then `F3` → **Delete Loose**.
2. Check whether the mesh contains intentional helper edges: this command may remove those as well.
3. Alternatively, select only the unwanted reported edges and use `X` → **Edges**.
