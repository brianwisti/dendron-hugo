---
created: '2024-02-10 14:43:52'
description: ''
fname: pub.card.remove-a-file-from-git-history
id: igygigdoax7e0hw4klcvx6i
tags:
- process
title: Remove a File from Git History
updated: '2024-02-10 14:44:12'
---

Oops I had `.envrc` in my [Git]({{< relref "/card/git.md" >}}) repo.  Fixing it with `git-filter-repo`.

```shell
git clone URL ~/tmp/
cd ~/tmp/REPO
git filter-repo --invert-paths --path .envrc
echo ".envrc" >> .gitignore
git commit -m 'ignore direnv files'
git remote add origin URL
git push origin --force --all
```

It had zero eyes on it that I know of, but I better delete and refresh any associated tokens just in case. One can be pretty sure there's scrapers out there specifically looking for silly mistakes like this.

# Related

-

[GitHub - newren/git-filter-repo: Quickly rewrite git repository history (filter-branch replacement)](https://github.com/newren/git-filter-repo)