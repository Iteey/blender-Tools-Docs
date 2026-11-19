# Nanite / LOD Advisor

## What it does

**UE5 Tools v0.4.2** includes a separate advisor for choosing an optimization approach for a Static Mesh. It produces a **preliminary recommendation**, not an Unreal Engine performance measurement.

Unlike mesh checks, the advisor **does not generate temporary LODs, run Decimate, or compare silhouettes**. It uses evaluated triangle count and assumed asset characteristics.

## Inputs

Evaluated triangle count, target platform, geometry class (solid, cards, foliage, deforming), surface type (opaque, masked, translucent), World Position Offset, expected screen coverage, and number of instances. Some inputs are chosen manually because Blender cannot infer the eventual UE5 material or how often the asset appears in a level.

## Possible outcomes

- **Nanite candidate** — worthwhile to benchmark Nanite in UE5.
- **Conventional LODs** — prioritize traditional LODs or a fallback.
- **Keep simple** — relatively lightweight mesh, extra LODs may not be needed.
- **Compare** — insufficient evidence to choose.
- **Unknown** — evaluated triangle count was unavailable.

## Decision logic

The implementation uses a heuristic score. Thresholds of 20,000 and 80,000 triangles are discussion hints, **not official Epic Games limits**. Translucency, target-platform compatibility, and deformation can shift the result toward conventional LODs. A detailed rigid opaque mesh may be proposed as a Nanite candidate.

**This is not a performance benchmark.** High triangle count or a visually good Decimate result cannot prove that either solution is faster.

## How to validate in UE5

Compare Nanite and conventional LOD setups in the same level, with identical camera positions and rendering settings. Review `stat gpu`, GPU Profiler, `stat unit`, Nanite Triangles and Overdraw visualizations, and VRAM usage. Repeat for typical distances and instance counts.

## Important limitation

In v0.4.2 the advisor is a **guidance feature**, separate from the 36 diagnostic checks. AAA-level optimization decisions require measurements in the actual UE5 project.
