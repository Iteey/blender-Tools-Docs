# Oversized textures

## What it checks

An image exceeds the configured maximum resolution.

## How detection works

Checks image dimensions against the configured maximum.

## Why it matters for UE5

Very large textures can increase VRAM and disk use.

## How to fix

Compare resolution to the asset’s screen-space usage and project budget; downsize only when justified.
