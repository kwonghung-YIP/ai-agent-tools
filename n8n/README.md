# How to run
- create you own .env file
- generate the self-signed cert for n8n, run certs/gen-selfsigned-crt.sh
- start the docker compose - docker compose up
- pull the ollama models
  docker exec -it ollama ollama pull mistral:7b #tools
  docker exec -it ollama ollama pull gpt-oss:20b #tools, thinking
- launch n8n web console at first time, and create a new admin account
  https://192.168.115.129:5678
- create a new webflow use ollama model