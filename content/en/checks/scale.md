# Unapplied Scale

## What it checks

The object Scale differs from (1, 1, 1).

## How detection works

Compares Scale components to 1.0 (tolerance: 0.0001).

## Why it matters for UE5

Unexpected scale can affect export, collisions, and modifiers.

## How to fix

If the pipeline requires unit scale, use Object Mode > Ctrl+A > Scale; verify dimensions afterward.

**Steps and shortcuts (Blender default keymap):**

1. In **Object Mode**, select the object and press `Ctrl + A` → **Scale**.
2. Verify geometry, modifiers, child objects, and animations after applying scale.
3. If the project intentionally uses non-unit scale, keep it and ensure export settings match.
