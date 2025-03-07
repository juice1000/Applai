#!/bin/bash

# Start Ollama server
echo "Starting Ollama server..."
ollama serve &

# Start Python backend in the background
echo "Starting Python backend..."
/Users/julienlook/Documents/Coding/job-application-assistant/.venv/bin/python \
/Users/julienlook/Documents/Coding/job-application-assistant/backend/src/main.py &


# Start npm dev server in the background
echo "Starting npm dev server..."
cd /Users/julienlook/Documents/Coding/job-application-assistant/frontend || exit
npm run dev &


# Wait for both processes to finish
wait