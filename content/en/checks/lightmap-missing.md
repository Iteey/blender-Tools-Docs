# Missing lightmap UV

## What it checks

The required lightmap UV channel is missing.

## How detection works

Checks for the selected UV channel when baked-lightmap checking is enabled.

## Why it matters for UE5

Baked lighting may fail when the project relies on lightmap UVs.

## How to fix

Create the expected channel, or disable this audit if you use fully dynamic lighting.

## Important exceptions

Lightmap audit is off by default; fully dynamic lighting may not need this channel.
