# Zero Scale

## What it checks

One or more scale components are nearly zero.

## How detection works

Finds near-zero scale components or a near-degenerate world matrix.

## Why it matters for UE5

The geometry may collapse or import incorrectly.

## How to fix

Restore valid scale values before exporting.

**Steps and shortcuts (Blender default keymap):**

1. In **Object Mode**, open the Transform sidebar (`N`) and inspect **Scale X/Y/Z**.
2. Enter a meaningful non-zero value (often `1` if appropriate for this asset).
3. Do not apply zero scale blindly: applying a collapsed dimension can destroy recoverable geometry.
