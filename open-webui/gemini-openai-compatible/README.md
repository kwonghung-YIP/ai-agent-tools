# How to run
- create the **open-webui/gemini/.env** file and add the entries below:
  VM_IP_ADDRESS=
  OPENAI_API_KEY= #obtain from [Google AI Studio](https://aistudio.google.com/api-keys)
- spin up the docker compose
  ```bash
  docker compose up
  ```
- launch open WebUI console at first time, and create a new admin account
  http://<<VM_IP_ADDRESS>>:8080