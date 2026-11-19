# Zero-length edges

## What it checks

Some edges join vertices at nearly identical positions.

## How detection works

Measures each edge’s endpoints (threshold: 1e-6 Blender units).

## Why it matters for UE5

Zero-length edges complicate processing and can affect normals.

## How to fix

Inspect the selected edges; use Merge by Distance only where the points should actually merge.

**Steps and shortcuts (Blender default keymap):**

1. Select the reported edges from the checklist and enter **Edit Mode** (`Tab`).
2. Use `M` → **By Distance** to merge coincident edge endpoints.
3. If an edge is unwanted loose geometry, try `X` → **Edges**; verify that required faces are preserved.
