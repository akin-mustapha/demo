#!/bin/bash

echo "Migrating Repository"

echo "Cloning Repository..."
git clone https://github.com/akin-mustapha/demo_CRUD_server_with_data_persistence.git

echo "Changing Directory..."
cd demo_CRUD_server_with_data_persistence

echo "Removing git folder"
rm -rf .git