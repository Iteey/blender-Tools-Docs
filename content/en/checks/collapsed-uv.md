# Collapsed UV faces

## What it checks

Some UV polygons have nearly zero area.

## How detection works

Computes polygon area in the active UV map.

## Why it matters for UE5

The texture can collapse to a line or point on those faces.

## How to fix

Select and unwrap the faces again if they must receive texture detail.
