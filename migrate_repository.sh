#!/bin/bash

echo "Migrating Repository"

echo "Cloning Repository..."
git clone https://github.com/akin-mustapha/demo_python_fastapi_server.git

echo "Changing Directory..."
cd demo_python_fastapi_server

echo "Removing git folder"
rm -rf .git