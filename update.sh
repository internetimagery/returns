#!/bin/bash

root=`git rev-parse --show-toplevel`
echo "Building stubs"
stubgen "$root/returns" -o "$root/stubs"
echo "Downgrading source files"
3to2 --write --no-diffs "$root/returns"

