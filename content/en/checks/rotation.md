# Unapplied Rotation

## What it checks

The object has unapplied rotation.

## How detection works

Tests rotation against identity across object rotation modes.

## Why it matters for UE5

The imported orientation may differ from project expectations.

## How to fix

Use Ctrl+A > Rotation only when needed. Avoid blindly applying rotation to rigged or linked objects.

**Steps and shortcuts (Blender default keymap):**

1. In **Object Mode**, select the object and press `Ctrl + A` → **Rotation**.
2. Check that object orientation, rigs, and children remain correct.
3. Applying rotation is not mandatory for every static mesh; follow your pipeline requirements.
