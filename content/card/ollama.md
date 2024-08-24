---
created: '2024-02-10 14:59:48'
description: ''
fname: pub.card.ollama
id: s43krrrrbgdqfsjna3hup5k
title: Ollama
updated: '2024-08-22 04:35:26'
---

Local [Large Language Model (LLM)]({{< relref "/card/ai/llm.md" >}}) host.

<!--more-->

## Installation

Linux and WSL. macOS is a direct download, and Windows native is not there yet.

```sh
curl https://ollama.ai/install.sh | sh
```

## Usage

```sh
ollama run MODEL_NAME
```

This runs an interactive session with the model, downloading it first if need be. Capabilities are limited by available models and your hardware. None of them are GPT-4 or anything — not on my machine anyways — but it's far more responsive than hosted solutions.

[Full list of supported models](https://ollama.ai/library).

Also provides a REST server, but I haven't messed with that yet.

## Integrations

- [ollama-python](https://github.com/ollama/ollama-python): official library for [Python]({{< relref "/card/python.md" >}})
- [ollama-js](https://github.com/ollama/ollama-js): official library for [JavaScript]({{< relref "/card/javascript.md" >}})
- [ollama-ai](https://github.com/gbaptista/ollama-ai): support for [Ruby]({{< relref "/card/ruby/_index.md" >}})

## Related

- <https://ollama.ai>
- [GitHub - ollama/ollama](https://github.com/ollama/ollama)