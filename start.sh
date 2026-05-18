#!/bin/bash
set -e

echo "Stopping old container..."
docker compose down || true

echo "Building and starting new container..."
docker compose up -d --build

echo "Deployment successful on EC2 instance"