---
created: '2024-02-10 14:58:16'
description: ''
fname: pub.card.ai.llm
id: ajfmo31gxg9b7xusy0hpmeg
title: Large Language Model (LLM)
updated: '2024-08-22 04:34:56'
---

A particular technology of [Artificial Intelligence (AI)]({{< relref "/card/ai/_index.md" >}})

<!--more-->

Language models describe a language in terms of probability. Given these tokens, what are the most likely next tokens? That bit's like a Markov chain. LLMs apply billions of parameters to that probability, producing extremely plausible token prediction — at a high computational and energy cost — that can be refined based on responses to user prompts.

Token prediction is not the same as correctness. They only work with the data they have, and lack understanding of context. Great for summarizing text input or telling you what an answer should *look* like, but terrible for things like legal case history or "what does this weird growth on my face mean?" Unless maybe you trained it primarily on case history or weird face growths. But even then I wouldn't assume.

Couple problems with probability-based token generation:

- it's gonna give you something that looks like its training data, which puts a tight constraint on creative / novel token generation
- trends and biases from training data will be reflected in generated tokens

So it's pretty easy to end up with your LLM offering you racist oatmeal. Cleaning up training data can help, but even then you'll end up seeing responses that feel like microaggressions.

[Retrieval Augmented Generation]({{< relref "/card/retrieval-augmented-generation.md" >}}) can improve the factual quality of generated tokens by providing access to external APIs.

## Code Assistants

LLM applications trained on code samples, intended to simplify writing and understanding code. Plenty of questions about where those code samples come from. There's GPL code in there for sure.

### Implementations and Related Editor Extensions

Not all of them. Dear god no. Just what I played with.

- GitHub Copilot
  - <https://marketplace.visualstudio.com/items?itemName=GitHub.copilot>
  - <https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat>
- Codeium
  - <https://marketplace.visualstudio.com/items?itemName=Codeium.codeium>
- Cody

## Related

- [Language model - Wikipedia](https://en.wikipedia.org/wiki/Language_model)
- [Large language model - Wikipedia](https://en.wikipedia.org/wiki/Large_language_model)
- [Markov chain - Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)