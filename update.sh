#!/bin/bash

root=`git rev-parse --show-toplevel`
echo "Building stubs"
stubgen "$root/returns" -o "$root/stubs"
echo "Downgrading source files"
3to2 --write --no-diffs "$root/returns"
echo "Moving stubs beside source files"
cp -RT "$root/stubs/returns" "$root/returns"
rm -R "$root/stubs"
