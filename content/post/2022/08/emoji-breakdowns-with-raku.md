---
created: '2024-02-11 18:30:59'
date: 2022-08-14 00:00:00+00:00
description: In which I write a Raku emoji reverse lookup tool.
fname: pub.post.2022.08.emoji-breakdowns-with-raku
id: 3e0qwcjz8vab627splwr845
slug: emoji-breakdowns-with-raku
syndication:
  mastodon: https://hackers.town/@randomgeek/108823061585109635
tags:
- raku-lang
title: Emoji Breakdowns with Raku
updated: '2024-08-07 19:12:24'
---

![console display of female surfer emoji broken down into its different code points](assets/img/2022/cover-2022-08-14.png "If you think that's weird, you should see what all these emoji have done to my neovim session.")

Had to share, but gotta make this quick because I am about three tangents removed from the stuff I planned to do today. This [Raku]({{< relref "/card/raku.md" >}}) script prints out code points for emoji characters with a little help from [Pretty::Table](https://raku.land/cpan:ANTONOV/Pretty::Table).

<!--more-->

```raku
#!/usr/bin/env raku

use Pretty::Table;

sub emoji-table(Str $emoji) {
  my $table = Pretty::Table.new:
    title => "Emoji Breakdown",
    field-names => [
      "Name",
      "Code",
      "Hex Code",
      "Emoji",
    ],
    border => False,
    align => %(
      Code => "r",
      "Hex Code" => "r",
    )
  ;

  for $emoji.ords -> $ord {
    my $chr = $ord.chr;
    $table.add-row: [
      $chr.uniname,
      $ord,
      $ord.base(16),
      $chr,
    ];
  }

  return $table;
}

sub MAIN(Str $emoji) {
  say "";
  say emoji-table($emoji);
}
```

And here's what it looks like in action:

``` text
bsh ❯ rakumoji 🦋

| Emoji Breakdown |
    Name      Code  Hex Code  Emoji
 BUTTERFLY  129419     1F98B    🦋
 ```

## Why?

So I'm doing a thing with a CSS stylesheet involving display of emojis. You don't want the emoji in a stylesheet though. More portable to use code points, the numeric value or values a computer uses to identify the character.

The problem: I don't know the code point. I use a convenient emoji picker. All it gives me is a character.

I've had some luck looking this stuff up online. But why spend 10 seconds [looking it up](https://unicode-table.com/en/1F98B/) when I could spend half an hour writing code and another hour rationalizing my decision in a blog post?

[`Str.ord`](https://docs.raku.org/type/Str#(Cool)_routine_ord) gets me the ordinal for a single character. That's not always what I need though. What looks like a single character could be composed of several codepoints.

Unicode is weird.

[`Str.ords`](https://docs.raku.org/type/Str#(Cool)_routine_ords) gives me a list of all code points in the string, whether one or several. I get the name of the emoji as well with [`str.uniname`](https://docs.raku.org/type/Str#(Cool)_routine_uniname). I can use that name with [`Str.uniparse`](https://docs.raku.org/type/Str#routine_uniparse) to get the emoji again.

```text
bsh ❯ raku -e 'say "butterfly".uniparse;'
🦋
```

Pretty::Table makes it look nice — or as nice as my terminal can manage — no matter how many code points are in the emoji.

``` text
bsh ❯ rakumoji 🏄‍♀️

| Emoji Breakdown |
          Name            Code  Hex Code  Emoji
         SURFER         127940     1F3C4    🏄
   ZERO WIDTH JOINER      8205      200D    ‍
      FEMALE SIGN         9792      2640    ♀
 VARIATION SELECTOR-16   65039      FE0F    ️
```

I helped the terminal out by putting the emoji character at the end of each line. Otherwise the pretty table layouts get offset weird.

Anyways I had fun. And now I'm only two tangents away from the day's intended tasks.