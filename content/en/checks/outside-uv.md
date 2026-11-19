# UV outside 0-1

## What it checks

Some UV coordinates lie outside the 0–1 tile.

## How detection works

Finds active UV coordinates outside 0–1.

## Why it matters for UE5

This is valid for tiling and UDIMs, but may be unsuitable for a unique 0–1 atlas.

## How to fix

Check your intended UV workflow. Move islands to 0–1 only when a single atlas is required.

**Steps and shortcuts (Blender default keymap):**

1. In **UV Editor**, select the relevant islands (`L` under an island, or `A` for all UVs).
2. Move them with `G` and scale with `S` to fit into 0–1 if your atlas requires it.
3. With **UDIMs**, tiling textures, or intentional offset UVs, outside-0–1 coordinates may be correct.

## Important exceptions

Tiled materials and UDIMs need not remain inside 0–1.
