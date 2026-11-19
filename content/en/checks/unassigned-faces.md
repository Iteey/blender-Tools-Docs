# Faces with missing material

## What it checks

Faces reference a missing or empty material slot.

## How detection works

Checks face material indices for missing or empty slots.

## Why it matters for UE5

Parts of the mesh may get the wrong material on import.

## How to fix

Select affected faces and assign a valid material.
