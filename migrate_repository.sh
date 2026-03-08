#!/bin/bash

echo "Migrating Repository"

echo "Cloning Repository..."
git clone https://github.com/akin-mustapha/demo_ble_connection.git

echo "Changing Directory..."
cd demo_ble_connection

echo "Removing git folder"
rm -rf .git