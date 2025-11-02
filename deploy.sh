#!/bin/bash

# Set stack name
STACK_NAME="fastapi-with-lambda-docker-runtime-stack"

# Build and deploy using SAM
echo "Building SAM application..."
sam build

echo "Validate SAM application..."
sam validate

echo "Deploying SAM application..."
sam deploy

echo "Deployment completed!"
