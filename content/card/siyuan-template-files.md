---
created: '2024-02-10 14:52:01'
description: ''
fname: pub.card.siyuan-template-files
id: uurt3a4f7bj2lj283h2hcm6
title: Siyuan Template Files
updated: '2024-02-10 14:52:42'
---

Using template snippets to insert predefined content to [Siyuan Note]({{< relref "/card/siyuan-note.md" >}})

## Templates

- Markdown files. You put them in data/templates​​.
- Templating logic with Go's text/template​​.
  - `​.action{action}`​​ instead of `{{action}}`​​
  - Additional functionality via Sprig
  - Remember Go's thing about date formatting

### Template Variables

Beyond whatever's defined by Sprig

|Variable|Description|
|---|---|
|`​title​​` |current document's name|
|`​id`​​ |current document's id|
|`​name​​` |current document name 🤔|
|`​alias`​​ |current document alias|
|`​queryBlocks`​​ |result of a db query as blocks|
|`​querySpans​​` |result of a db query as spans|
|`​parseTime`​​ |parse a string into time.Time​​|

### Template Invocation

Command: `/Template​​`

1. Invoking `/Template`​​ pulls up template list along with expected output.
2. Select template
3. Template is entered at point

### Resources

- [template package - text/template - Go Packages](https://pkg.go.dev/text/template)

## Date Formatting

Date formatting in templates.

via [time package constants](https://pkg.go.dev/time#pkg-constants)

```go
const (
 Layout      = "01/02 03:04:05PM '06 -0700" // The reference time, in numerical order.
 ANSIC       = "Mon Jan _2 15:04:05 2006"
 UnixDate    = "Mon Jan _2 15:04:05 MST 2006"
 RubyDate    = "Mon Jan 02 15:04:05 -0700 2006"
 RFC822      = "02 Jan 06 15:04 MST"
 RFC822Z     = "02 Jan 06 15:04 -0700" // RFC822 with numeric zone
 RFC850      = "Monday, 02-Jan-06 15:04:05 MST"
 RFC1123     = "Mon, 02 Jan 2006 15:04:05 MST"
 RFC1123Z    = "Mon, 02 Jan 2006 15:04:05 -0700" // RFC1123 with numeric zone
 RFC3339     = "2006-01-02T15:04:05Z07:00"
 RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00"
 Kitchen     = "3:04PM"
 // Handy time stamps.
 Stamp      = "Jan _2 15:04:05"
 StampMilli = "Jan _2 15:04:05.000"
 StampMicro = "Jan _2 15:04:05.000000"
 StampNano  = "Jan _2 15:04:05.000000000"
)
```

## Sprig

Useful template functions for Go Templates

Pasting from their front page until I dig deeper on my own:

The Sprig library provides over 70 template functions for Go's template language.

- [String Functions](http://masterminds.github.io/sprig/strings.html): trim​​, wrap​​, randAlpha​​, plural​​, etc.
  - [String List Functions](http://masterminds.github.io/sprig/string_slice.html): splitList​​, sortAlpha​​, etc.
- [Integer Math Functions](http://masterminds.github.io/sprig/math.html): add​​, max​​, mul​​, etc.
  - [Integer Slice Functions](http://masterminds.github.io/sprig/integer_slice.html): until​​, untilStep​​
- [Float Math Functions](http://masterminds.github.io/sprig/mathf.html): addf​​, maxf​​, mulf​​, etc.
- [Date Functions](http://masterminds.github.io/sprig/date.html): now​​, date​​, etc.
- [Defaults Functions](http://masterminds.github.io/sprig/defaults.html): default​​, empty​​, coalesce​​, fromJson​​, toJson​​, toPrettyJson​​, toRawJson​​, ternary​​
- [Encoding Functions](http://masterminds.github.io/sprig/encoding.html): b64enc​​, b64dec​​, etc.
- [Lists and List Functions](http://masterminds.github.io/sprig/lists.html): list​​, first​​, uniq​​, etc.
- [Dictionaries and Dict Functions](http://masterminds.github.io/sprig/dicts.html): get​​, set​​, dict​​, hasKey​​, pluck​​, dig​​, deepCopy​​, etc.
- [Type Conversion Functions](http://masterminds.github.io/sprig/conversion.html): atoi​​, int64​​, toString​​, etc.
- [Path and Filepath Functions](http://masterminds.github.io/sprig/paths.html): base​​, dir​​, ext​​, clean​​, isAbs​​, osBase​​, osDir​​, osExt​​, osClean​​, osIsAbs​​
- [Flow Control Functions](http://masterminds.github.io/sprig/flow_control.html): fail​​
- Advanced Functions
  - [UUID Functions](http://masterminds.github.io/sprig/uuid.html): uuidv4​​
  - [OS Functions](http://masterminds.github.io/sprig/os.html): env​​, expandenv​​
  - [Version Comparison Functions](http://masterminds.github.io/sprig/semver.html): semver​​, semverCompare​​
  - [Reflection](http://masterminds.github.io/sprig/reflection.html): typeOf​​, kindIs​​, typeIsLike​​, etc.
  - [Cryptographic and Security Functions](http://masterminds.github.io/sprig/crypto.html): derivePassword​​, sha256sum​​, genPrivateKey​​, etc.
  - [Network](http://masterminds.github.io/sprig/network.html): getHostByName​​

## Related

- [Masterminds / sprig](https://github.com/Masterminds/sprig)