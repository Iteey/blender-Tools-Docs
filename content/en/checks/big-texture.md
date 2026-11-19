# Oversized textures

## What it checks

An image exceeds the configured maximum resolution.

## How detection works

Checks image dimensions against the configured maximum.

## Why it matters for UE5

Very large textures can increase VRAM and disk use.

## How to fix

Compare resolution to the asset’s screen-space usage and project budget; downsize only when justified.

**Steps and shortcuts (Blender default keymap):**

1. Open **Image Editor** and inspect image dimensions against the project budget.
2. If clearly oversized, resize in an external editor or use **Image → Resize** when available for the active image.
3. Save the new version and verify sharpness in UE5. There is no single safe universal hotkey for downscaling textures.
