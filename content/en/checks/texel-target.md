# Texel Density target

## What it checks

Estimated pixel density differs from the configured target.

## How detection works

Compares estimated density to the configured px/m target; provides information when unset.

## Why it matters for UE5

The asset may not meet the project’s texel-density convention.

## How to fix

Adjust island scale or update the target if the setting does not match the project.

**Steps and shortcuts (Blender default keymap):**

1. Verify your project's actual texel-density target and assumed texture resolution: the add-on uses estimated values.
2. In **UV Editing**, select relevant islands and scale with `S`, then run `F3` → **Pack Islands**.
3. Check again. Do not blindly match a generic threshold if the project uses another standard.

## Important exceptions

No compliance check is possible when the target is unset.
