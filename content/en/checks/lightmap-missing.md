# Missing lightmap UV

## What it checks

The required lightmap UV channel is missing.

## How detection works

Checks for the selected UV channel when baked-lightmap checking is enabled.

## Why it matters for UE5

Baked lighting may fail when the project relies on lightmap UVs.

## How to fix

Create the expected channel, or disable this audit if you use fully dynamic lighting.

**Steps and shortcuts (Blender default keymap):**

1. In **Object Data Properties → UV Maps**, click **+** to add a separate lightmap UV channel.
2. Enter **Edit Mode**, select faces (`A`), and unwrap uniquely using `U` → **Smart UV Project** or **Unwrap**.
3. In UE5, check the Lightmap Coordinate Index and auto-generation options. Fully dynamic lighting may not require a separate channel.

## Important exceptions

Lightmap audit is off by default; fully dynamic lighting may not need this channel.
