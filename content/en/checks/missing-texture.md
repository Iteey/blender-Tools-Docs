# Missing external textures

## What it checks

Some referenced external image files cannot be found.

## How detection works

Checks whether external FILE image paths exist; packed images are accepted.

## Why it matters for UE5

Textures may be lost when moving the Blender project.

## How to fix

Fix image paths or pack assets using File > External Data > Pack Resources.

## Important exceptions

UDIM pattern paths are not specifically resolved, so false warnings are possible.
