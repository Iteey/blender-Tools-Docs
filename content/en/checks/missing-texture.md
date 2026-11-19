# Missing external textures

## What it checks

Some referenced external image files cannot be found.

## How detection works

Checks whether external FILE image paths exist; packed images are accepted.

## Why it matters for UE5

Textures may be lost when moving the Blender project.

## How to fix

Fix image paths or pack assets using File > External Data > Pack Resources.

**Steps and shortcuts (Blender default keymap):**

1. In **Shader Editor**, open the affected **Image Texture** node and choose the correct file with **Open**.
2. If the image files are accessible, use **File → External Data → Pack Resources** for portable projects.
3. For broken paths, look for **Find Missing Files** via `F3` if available in your version/context. Packing cannot recover a file that is missing.

## Important exceptions

UDIM pattern paths are not specifically resolved, so false warnings are possible.
