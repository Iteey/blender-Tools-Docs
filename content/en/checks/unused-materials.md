# Unused material slots

## What it checks

Some material slots are present but no faces use them.

## How detection works

Compares material slots with the indices referenced by faces.

## Why it matters for UE5

Unused slots make the asset harder to maintain.

## How to fix

Remove unused slots only if they are not part of the established pipeline.

**Steps and shortcuts (Blender default keymap):**

1. In **Material Properties**, inspect slots not used by any faces.
2. Remove unnecessary slots with **−**, or try `F3` → **Remove Unused Slots** if the operator is available in your context.
3. Preserve slots used intentionally by scripts, exporters, or other pipeline systems.
