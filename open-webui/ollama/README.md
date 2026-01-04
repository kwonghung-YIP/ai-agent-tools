# How to run
- create you own .env file
- start the docker compose - docker compose up
- pull the ollama models
  docker exec -it ollama ollama pull mistral:7b #tools
  docker exec -it ollama ollama pull gpt-oss:20b #tools, thinking
- launch open WebUI console at first time, and create a new admin account
  http://192.168.115.129:8080