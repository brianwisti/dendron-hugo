---
created: '2024-02-10 14:46:37'
description: ''
fname: pub.card.devops
id: 0qlzhd7o76n71yw854w39v6
title: Devops
updated: '2024-02-10 14:47:23'
---

Integrated development and IT Operations as primary responsibility, with focus on automating the fiddly bits of IT.

# Jots

Gives a context for some of the bigger tech changes over the last couple decades

- A whole-ass *inbox.microservice* architecture is more complicated than a monolith, but its individual components are easier to update, deploy, or phase out completely.
- You can use an orchestrator like *inbox.kubernetes* to configure, fire up, and tear down *inbox.container* collections as a matter of routine, whereas doing the same with a monolith requires greater planning and communication.
- *inbox.terraform* and similar *inbox.infrastructure-as-code* tools, using a structured language to describe architecture, and *inbox.git* or whatever version control system you prefer to see the changing needs over time (and roll back if you screw up)

[Ymmv]({{< relref "/card/ymmv.md" >}}) because the added complexity means more brains dedicated to maintaining that whole thing — one team can manage one microservice, but with lots of services you'll end up needing a few teams — and a tiny shop would likely be better off having an architecture that can fit in fewer heads: monolith on a server is the easy example. Or they can pay somebody else to think about it, of course.

# Related

- [DevOps - Wikipedia](https://en.wikipedia.org/wiki/DevOps)
- [What is DevOps? | Atlassian](https://www.atlassian.com/devops)
- [DevOps Roadmap: Learn to become a DevOps Engineer or SRE](https://roadmap.sh/devops)