# How to run
- create you own .env file
- generate the self-signed cert for n8n, run certs/gen-selfsigned-crt.sh
- start the docker compose - docker compose up
- pull the ollama models
  docker exec -it ollama ollama pull mistral:7b #tools
  docker exec -it ollama ollama pull gpt-oss:20b #tools, #thinking
  docker exec -it ollama ollama pull dolphin3:8b
  docker exec -it ollama ollama pull llama3.1:8b
  docker exec -it ollama ollama pull gemma3n:e4b
  docker exec -it ollama ollama pull gemma3:4b
- launch n8n web console at first time, and create a new admin account
  https://192.168.115.129:5678
- create a new webflow use ollama model