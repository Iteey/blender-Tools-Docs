# Strongly bent smooth faces

## What it checks

A smooth-shading transition crosses a steep angle between neighboring faces.

## How detection works

Compares geometric-normal angles between adjacent smooth faces.

## Why it matters for UE5

This can create unwanted highlights or normal artifacts.

## How to fix

Inspect the shading; mark an edge Sharp or adjust smoothing when necessary.
