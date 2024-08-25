---
created: '2024-02-10 05:09:32'
description: ''
fname: pub.config.shell.taskwarrior
id: 5g72q2wn4vq16tvkuq7k6wd
title: Taskwarrior
updated: '2024-02-10 05:09:50'
---

How I use [Taskwarrior]({{< relref "/card/taskwarrior.md" >}}).

Oh I need to go through and explain this.

```config
//- file:taskrc

// ==> Define contexts.
// ==> Set verbosity.
// ==> Adjust task urgency.
// ==> Configure a 'top' report.
// ==> Define a 'points' UDA.
// ==> Configure a 'pointed' report.
// ==> Configure an 'unpointed' report.
// ==> Configure sync.
// ==> Adjust reviewed report.

include ~/Dropbox/Settings/task/dark-green-256.theme
```

## task/contexts

```config
//- Define contexts
context.blog=-Work -pay -finances -personal
context.bucket=+idea
context.focused=(priority:H or priority:M) -idea -shelved -finances urgency > 5.0
context.work=+Work -idea -personal
context.offwork=-Work
```

## task/set-verbosity

```config
//- Set verbosity
verbose=header,footnote,label,new-id,affected,edit,special,project,filter,unwait
```

## task/adjust-urgency

```config
//- Adjust task urgency
urgency.user.tag.work.coefficient=2.0
urgency.user.tag.idea.coefficient=0.5
```

## task/top-report

The most important tasks, presented in a useful format for me.

```config
//- Configure a 'top' report
report.top.columns=id,priority,project,tags,description.count
report.top.description='Minimal details of tasks'
report.top.filter=status:pending (priority:H or priority:M)
report.top.labels=ID,Pri,Project,Tags,Description
report.top.sort=priority-/,project-,description+
```

## task/points-for-tasks

The idea was to give me a little practice with task estimates.
I haven't used it since the first week I tried it out.

```config
//- Define a 'points' UDA
uda.points.type=numeric
uda.points.label=Points
```

## Display pending tasks that have been pointed

```config
//- Configure a 'pointed' report
report.pointed.description='Open tasks that have point estimates'
report.pointed.columns=id,points,priority,due,description
report.pointed.sort=urgency-
report.pointed.filter=status:pending points > 0
```

## Display pending tasks that have *not* been pointed

```config
//- Configure an 'unpointed' report
report.unpointed.description='Open tasks that have point estimates'
report.unpointed.columns=id,project,tags,priority,due,description
report.unpointed.sort=urgency-
report.unpointed.filter=status:pending -idea points:
```

## task/sync

Since inthe.AM and freecinc have both shut down, I'm not using any kind of sync right now. I may eventually set up my own `taskd` server on the Raspberry Pi again.

## Adjust reviewed report

```config
//- Adjust reviewed report
uda.reviewed.type=date
uda.reviewed.label=Reviewed
report._reviewed.description=Tasksh review report.  Adjust the filter to your needs.
report._reviewed.columns=uuid
report._reviewed.sort=reviewed+,modified+
report._reviewed.filter=( reviewed.none: or reviewed.before:now-6days ) and ( +PENDING or +WAITING )
```