# Duplicate faces

## What it checks

Multiple faces use the same set of vertex indices.

## How detection works

Compares unordered sets of vertex indices used by faces.

## Why it matters for UE5

Coincident faces can produce flicker, baking errors, and unnecessary geometry.

## How to fix

Find duplicates and remove extra faces without damaging the desired surface.

**Steps and shortcuts (Blender default keymap):**

1. Click **Duplicate faces** in the checklist to select flagged faces. If needed, press `Tab` for **Edit Mode** and `3` for face selection.
2. Toggle **X-Ray** with `Alt + Z` and confirm that two faces really overlap. You may hide a selection with `H` and reveal it with `Alt + H`.
3. Select **only the extra** face (not both) and press `X` → **Only Faces**. This removes the face without unnecessarily deleting surrounding vertices and edges.
4. Run the check again. `M` → **By Distance** can fix coincident vertices but **does not guarantee** removal of duplicate faces sharing the exact same vertex indices.
