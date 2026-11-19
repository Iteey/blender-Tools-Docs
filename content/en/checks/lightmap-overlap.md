# Lightmap UV overlap

## What it checks

Lightmap UV islands overlap.

## How detection works

Checks for intersecting triangles in the selected lightmap UV, subject to scan limits.

## Why it matters for UE5

Baked lighting can show illumination artifacts.

## How to fix

Separate islands and leave appropriate padding between them.

## Important exceptions

Does not validate padding against lightmap resolution. Scan size is bounded.
