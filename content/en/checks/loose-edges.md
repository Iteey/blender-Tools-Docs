# Loose edges

## What it checks

Some edges do not belong to any polygon face.

## How detection works

Finds edges that do not belong to any polygon.

## Why it matters for UE5

They do not form a drawable surface in a typical game mesh.

## How to fix

Remove unnecessary loose geometry after checking whether it is still needed for modeling.
