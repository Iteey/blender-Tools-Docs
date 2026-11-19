# N-gons

## What it checks

Some faces have five or more vertices.

## How detection works

Counts faces with more than four vertices.

## Why it matters for UE5

Triangulation during import can change the shape and shading.

## How to fix

Inspect the flagged faces. Split them into quads or triangles where necessary; an N-gon is not automatically wrong.

**Steps and shortcuts (Blender default keymap):**

1. Click the issue in the checklist to select affected faces; enter **Edit Mode** with `Tab` when needed.
2. Use `Ctrl + T` (**Triangulate Faces**) on selected faces if the pipeline requires triangles.
3. For manual edge placement, try `K` (**Knife**) or `J` (**Connect Vertex Path**) with suitable selections.
4. Avoid triangulating everything automatically: a flat N-gon is often intentional.

## Important exceptions

A planar N-gon may be valid; inspect triangulation and shading before export.
