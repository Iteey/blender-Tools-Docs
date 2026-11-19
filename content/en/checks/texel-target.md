# Texel Density target

## What it checks

Estimated pixel density differs from the configured target.

## How detection works

Compares estimated density to the configured px/m target; provides information when unset.

## Why it matters for UE5

The asset may not meet the project’s texel-density convention.

## How to fix

Adjust island scale or update the target if the setting does not match the project.

## Important exceptions

No compliance check is possible when the target is unset.
