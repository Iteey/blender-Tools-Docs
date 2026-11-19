# Empty material slots

## What it checks

Some material slots do not contain a material.

## How detection works

Counts material slots without a material datablock.

## Why it matters for UE5

Empty slots can cause confusion when assigning materials after import.

## How to fix

Fill required slots or remove those that are unnecessary.

**Steps and shortcuts (Blender default keymap):**

1. Select the object and open **Material Properties**.
2. Select the empty slot, choose a material from the dropdown, or remove the slot using **−**.
3. Confirm the slot is not required by the export pipeline; this is normally done in the Properties UI, not with a universal shortcut.
