# python-nvidia-nemotron

[![Open In Devspace](https://www.jetify.com/img/devbox/open-in-devspace.svg)](https://auth.jetify.com/devspace/templates/Nvidia-Nemotron)

This repo is an example that sets up a devbox environment with Python and pip. It uses Fast API to set up API endpoints listed below and calls NVIDIA API to allow interactions with nemotron LLM model.

![image](https://raw.githubusercontent.com/jetify-examples/python-nvidia-nemotron/d8fb932c4ec7c96a035bf97abe7ff33e961e2dfa/static/screenshot.png)

## Setup

### Prerequisites

To setup this repo make sure to have [devbox](https://www.jetify.com/devbox/docs/installing_devbox/) installed and have access to your NVIDIA's [API key](https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct?snippet_tab=Python&signin=true&api_key=true).

### Steps

1. Clone this repo `git clone https://github.com/jetify-examples/python-nvidia-nemotron.git`.
2. `cd python-nvidia-nemotron` and then run `devbox run install`
3. Copy your NVIDIA's API key in key in devbox.json's `"env"` section.
4. run `devbox run start`

## Usage

Once the server is setup and running, you can access to static page by visiting `localhost:8080`

### API

The app also makes an API endpoint available to interact with NVIDIA's nemotron. The endpoint responds to POST requests to `/api/prompt`. Below is an example request and response:

Example request:

```bash
curl --location 'http://127.0.0.1:8080/api/prompt' \
--header 'Content-Type: application/json' \
--data '{
    "prompt": "What is the circumference of Earth?"
}'
```

Example response:

```json
{
  "message": {
    "content": "The circumference of Earth is approximately 24,901 miles (40,075 kilometers).",
    "refusal": null,
    "role": "assistant",
    "function_call": null,
    "tool_calls": null
  }
}
```

## Development

To use this project as a skeleton and develop on it, you can utilize the references for Fast API [docs](https://fastapi.tiangolo.com/#create-it), more specifically, routes and handlers. As well as NVIDIA's [API Reference](https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_1-nemotron-70b-instruct).
