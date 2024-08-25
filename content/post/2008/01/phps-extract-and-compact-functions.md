---
aliases:
- /blogspot/2008/01/30_php-extract-and-compact-functions.html
- /post/2008/php-extract-and-compact-functions/
- /2008/01/30/phps-extract-and-compact-functions/
created: '2024-02-19 01:23:25'
date: 2008-01-30 08:00:00+00:00
description: ''
fname: pub.post.2008.01.phps-extract-and-compact-functions
id: sxlfvokxt5edbxj5oqnhwjn
slug: phps-extract-and-compact-functions
tags:
- php
- blogspot
title: PHP's Extract and Compact Functions
updated: '2024-08-07 18:33:41'
---

I've been brushing up on my [PHP]({{< relref "/card/php.md" >}}) basics lately. Why? Well, it never hurts to revisit things you think you already know. There is a good chance you will discover something you didn't know after all. For example: this time I learned about the `extract` and `compact` functions.

<!--more-->

[`extract`](http://us3.php.net/manual/en/function.extract.php) takes an associative array and creates local variables on the fly, named for the keys in the array and with the corresponding values matched up. [`compact`](http://us3.php.net/manual/en/function.compact.php) is the corresponding function for taking a collection of variables and stuffing them into an associative array.

``` php
<?php
  $book = array(
      "title"     => "Dad's Own Cookbook",
      "author"    => "Bob Sloan",
  );

  extract($book);
  echo $title . " was written by " . $author . "\n";

  $first = "Brian";
  $last  = "Wisti";
  $keys  = array("first", "last");
  $my_name = compact($keys);
  print_r($my_name);
?>
```

Running this code:

```console
$ php -f extract-compact.php
Dad's Own Cookbook was written by Bob Sloan
Array
(
    [first] => Brian
    [last] => Wisti
)
```

`extract` is the more immediately useful of the two for my purposes, because it simplifies a common tactic I use for creating local variables based on database lookups.

Instead of manually creating local variables, like this:

``` php
<?php
    # ...
    while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
        $author = $row["author"];
        $title  = $row["title"];
        # ...
    }
?>
```

I can save myself a little effort with `extract`.

``` php
<?php
    # ...
    while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
        extract($row);
        # ...
    }
?>
```

I realize that there may be an even easier way to do it, but just this will make my life noticeably easier as long as I don't abuse it. I would mainly tuck a call like this off in a function and probably use it in conjunction with a SQL query or something else where I knew exactly what names I would end up with.

Why didn't I know about this before? Well, the manual approach was good enough. And since what I had was good enough, I didn't think of looking for a better approach. Then again, finds like this are exactly why I *do* go back and review what I thought I already knew.