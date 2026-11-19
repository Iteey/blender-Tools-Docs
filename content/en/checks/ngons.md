# N-gons

## What it checks

Some faces have five or more vertices.

## How detection works

Counts faces with more than four vertices.

## Why it matters for UE5

Triangulation during import can change the shape and shading.

## How to fix

Inspect the flagged faces. Split them into quads or triangles where necessary; an N-gon is not automatically wrong.

## Important exceptions

A planar N-gon may be valid; inspect triangulation and shading before export.
