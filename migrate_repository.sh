#!/bin/bash

echo "Migrating Repository"

echo "Cloning Repository..."
git clone https://github.com/akin-mustapha/demo_github_actions.git

echo "Changing Directory..."
cd demo_github_actions

echo "Removing git folder"
rm -rf .git