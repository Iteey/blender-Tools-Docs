# Non-manifold edges

## What it checks

Some edges belong to more than two faces.

## How detection works

Finds edges connected to three or more faces. Boundary edges have a separate check.

## Why it matters for UE5

Complex topology can interfere with normals, baking, and mesh processing.

## How to fix

Inspect the edges; remove duplicated or unnecessary internal surfaces. Keep intended intersections if the pipeline permits them.

## Important exceptions

Open boundaries are not classified here as non-manifold; they have their own check.
