# Pivot / Origin position

## What it checks

The object origin is not at the configured expected location.

## How detection works

Compares origin with chosen bounds center, bounds bottom, or world origin.

## Why it matters for UE5

This can affect snapping, placement, and rotation of Static Meshes in UE5.

## How to fix

Check project conventions, then place the origin using Origin tools.

**Steps and shortcuts (Blender default keymap):**

1. In **Object Mode**, select the object and place the 3D Cursor at the desired location (for example, `Shift + S` → **Cursor to Selected** with an appropriate selection).
2. Run `F3` → **Origin to 3D Cursor**.
3. Verify rotation/pivot behavior after import into UE5. The ideal origin depends on the mesh's purpose.

## Important exceptions

Origin placement is project-specific, not governed by a universal rule.
