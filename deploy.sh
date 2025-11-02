#!/bin/bash

# Build and deploy using SAM
echo "Building SAM application..."
sam build

echo "Validate SAM application..."
sam validate

echo "Deploying SAM application..."
sam deploy

echo "Deployment completed!"
