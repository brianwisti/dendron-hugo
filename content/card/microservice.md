---
created: '2024-02-10 04:36:26'
description: ''
fname: pub.card.microservice
id: aijyy7v87bt6bpiszv6zr4y
title: Microservice
updated: '2024-02-10 04:36:51'
---

Software architecture that focuses on services which are:

- independently deployable
- loosely coupled

A microservice's responsibilities should focus on a specific business capability, and be small enough for one small team to own it. Anything the service itself needs is provided by other processes and services on the network. Its output can be used by still more services. It shouldn't have to care about the details of either end.

I come across [Unix Philosophy]({{< relref "/card/unix-philosophy.md" >}}) sort of thinking that a microservice should have exactly one responsibility. Except I don't see it all that often, and the elevator pitch definition I found doesn't mention it. The important bit is that you can setup and teardown one service without messing up the other services.

But it should probably aim for as few responsibilities as is practical, with "one" being the platonic ideal.

## Related

- [What are microservices?](https://microservices.io)
- [Microservices - Wikipedia](https://en.wikipedia.org/wiki/Microservices)