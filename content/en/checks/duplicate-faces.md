# Duplicate faces

## What it checks

Multiple faces use the same set of vertex indices.

## How detection works

Compares unordered sets of vertex indices used by faces.

## Why it matters for UE5

Coincident faces can produce flicker, baking errors, and unnecessary geometry.

## How to fix

Find duplicates and remove extra faces without damaging the desired surface.
