# Empty image nodes

## What it checks

Some Image Texture nodes have no image selected.

## How detection works

Finds Image Texture nodes with no image selected.

## Why it matters for UE5

The material may not display as intended.

## How to fix

Assign an image in Shader Editor or remove the unused node.

**Steps and shortcuts (Blender default keymap):**

1. Open the **Shading** workspace and select the material.
2. In **Shader Editor**, find an **Image Texture** node without an image; click **Open** or choose an existing image.
3. If the node is unnecessary, select it and press `X` to delete it (verify the shader still works).
