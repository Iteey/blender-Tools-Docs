# Unapplied Scale

## What it checks

The object Scale differs from (1, 1, 1).

## How detection works

Compares Scale components to 1.0 (tolerance: 0.0001).

## Why it matters for UE5

Unexpected scale can affect export, collisions, and modifiers.

## How to fix

If the pipeline requires unit scale, use Object Mode > Ctrl+A > Scale; verify dimensions afterward.
