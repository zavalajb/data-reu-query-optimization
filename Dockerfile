FROM ollama/ollama

RUN apt-get update && apt-get install -y curl
COPY pull_model.sh /pull_model.sh
RUN chmod +x /pull_model.sh

# Modify your entrypoint to pull the model first
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]