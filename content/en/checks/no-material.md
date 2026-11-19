# No material assigned

## What it checks

No Blender material is assigned in any slot.

## How detection works

Checks if any object material slot contains a material.

## Why it matters for UE5

You may need to assign materials manually after UE5 import.

## How to fix

Assign a material if the export pipeline expects it.

**Steps and shortcuts (Blender default keymap):**

1. Select the object in **Object Mode**, open **Material Properties** (red sphere icon), and click **New**.
2. Configure the material or select an existing one from the material dropdown.
3. `F3` opens Blender's operator search, but assigning a material is generally clearer through Properties.
