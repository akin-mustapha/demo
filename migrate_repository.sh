#!/bin/bash

echo "Migrating Repository"

echo "Cloning Repository..."
git clone https://github.com/akin-mustapha/demo_prefect_flow_consume_t212_api.git

echo "Changing Directory..."
cd demo_prefect_flow_consume_t212_api

echo "Removing git folder"
rm -rf .git