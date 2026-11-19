# Faces with missing material

## What it checks

Faces reference a missing or empty material slot.

## How detection works

Checks face material indices for missing or empty slots.

## Why it matters for UE5

Parts of the mesh may get the wrong material on import.

## How to fix

Select affected faces and assign a valid material.

**Steps and shortcuts (Blender default keymap):**

1. Enter **Edit Mode** (`Tab`), choose face selection (`3`), and select the flagged faces.
2. In **Material Properties**, choose the intended material slot and click **Assign**.
3. Add/create a material first if no suitable slot exists.
