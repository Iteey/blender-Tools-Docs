# Using the pre-export checklist

## First run

In Blender, open the **UE5** sidebar from the `N` panel. Select a Static Mesh, open **UE5 Pre-export Checklist**, and click **Run Pre-export Check**.

Enable **Selected meshes only** to scan your selection. With this option off, the add-on scans applicable meshes in the scene.

## Quick and Advanced

**Quick** runs core topology, transforms, normals, UV, material, texture, and triangle checks. **Advanced** adds open boundaries, nearby vertices, UV overlap and distortion, Texel Density, Pivot, and Lightmap UV.

Expensive UV scans have safety caps. When a limit is reached, the result is **SKIP / Not checked**, not **PASS**.

## Status meanings

- **PASS** — scan completed and no issue was found within that check's scope.
- **ERROR** — a potential defect needs attention.
- **WARN** — a suspicious condition that may still be intentional.
- **INFO** — advisory information, not necessarily an error.
- **SKIP** — not checked because of missing data or scan limits.
- **NA** — not applicable, for example when baked-lightmap auditing is disabled.

## Locate a finding in Blender

Click a finding's label: the add-on re-scans the mesh and selects affected vertices, edges or faces in **Edit Mode**. Use the `?` button for the in-app explanation. The add-on **does not repair geometry automatically**.

## What “Last scan completed” means

It is a stored result from the last scan. Re-run after editing the mesh. The automatic change indicator does not detect all vertex-coordinate edits, so the absence of a stale warning does not guarantee that the result is current.
