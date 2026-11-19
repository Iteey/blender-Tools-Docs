# Zero Scale

## What it checks

One or more scale components are nearly zero.

## How detection works

Finds near-zero scale components or a near-degenerate world matrix.

## Why it matters for UE5

The geometry may collapse or import incorrectly.

## How to fix

Restore valid scale values before exporting.
