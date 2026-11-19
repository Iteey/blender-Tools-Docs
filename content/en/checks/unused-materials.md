# Unused material slots

## What it checks

Some material slots are present but no faces use them.

## How detection works

Compares material slots with the indices referenced by faces.

## Why it matters for UE5

Unused slots make the asset harder to maintain.

## How to fix

Remove unused slots only if they are not part of the established pipeline.
