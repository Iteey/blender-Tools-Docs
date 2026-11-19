# Non-manifold edges

## What it checks

Some edges belong to more than two faces.

## How detection works

Finds edges connected to three or more faces. Boundary edges have a separate check.

## Why it matters for UE5

Complex topology can interfere with normals, baking, and mesh processing.

## How to fix

Inspect the edges; remove duplicated or unnecessary internal surfaces. Keep intended intersections if the pipeline permits them.

**Steps and shortcuts (Blender default keymap):**

1. In **Edit Mode**, press `F3` and run **Select Non Manifold**. Inspect the selected edges.
2. For genuinely duplicated vertices, select the relevant area and use `M` → **By Distance**; check the merge threshold.
3. For unwanted internal faces, use `X` → **Only Faces**. To close an intended hole, select its border and press `F` (**Fill**).
4. Open edges on planes and foliage may be intentional. Do not seal them blindly.

## Important exceptions

Open boundaries are not classified here as non-manifold; they have their own check.
