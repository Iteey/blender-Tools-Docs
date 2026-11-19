# UV distortion

## What it checks

Relative edge lengths differ substantially between UV and 3D geometry.

## How detection works

Compares UV/3D triangle edge-length ratios against a configurable threshold.

## Why it matters for UE5

The texture may look stretched; sometimes the distortion is intentional.

## How to fix

Test with a checker texture, then relax or re-unwrap problematic islands.

**Steps and shortcuts (Blender default keymap):**

1. In the **UV Editor**, enable **Overlays → Stretch** and inspect problematic areas; a checker texture can help.
2. Place seams as needed with `F3` → **Mark Seam** on selected edges, then select faces and use `U` → **Unwrap**.
3. In the UV Editor, try `F3` → **Minimize Stretch** when suitable.
4. Some distortion is acceptable; judge it against visual results and asset purpose.

## Important exceptions

This is a geometric test; it cannot measure the final UE5 material appearance.
