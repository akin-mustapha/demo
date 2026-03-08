#!/bin/bash

echo "Migrating Repository"

echo "Cloning Repository..."
git clone https://github.com/akin-mustapha/demo_design_patterns.git

echo "Changing Directory..."
cd demo_design_patterns

echo "Removing git folder"
rm -rf .git