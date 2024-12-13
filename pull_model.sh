#!/bin/bash
set -e
#curl https://ollama.ai/install.sh | sh


#echo "Waiting for Ollama to be ready..."
#while ! curl -s http://ollama:11434 > /dev/null; do
#    echo "Still waiting for Ollama..."
#    sleep 5
#done

#echo "Ollama is ready! Pulling llama3.1 model..."
#ollama serve &
# Wait a moment to ensure the service starts
#sleep 5

#ollama pull llama3.1

#echo "Model pulled successfully! Starting application..."
#exec "$@"

#!/bin/bash
set -e

# Start Ollama service
ollama serve &

sleep 5

# Check if the model is already pulled
if ! ollama list | grep -q llama3.1; then
    echo "Pulling llama3.1 model..."
    ollama pull llama3.1
    echo "Model pulled successfully!"
fi



# If no arguments are provided, keep the container running
if [ $# -eq 0 ]; then
    # Keep the container running
    tail -f /dev/null
else
    # Execute the provided command
    exec "$@"
fi