just-text
=========

Similar to Restructured Text and Markdown, just-text converts plain text to HTML.
Dissimilar to those programs, just-text aims to format literary texts
(as opposed to technical texts, which use bullets, code blocks, hyperlinks, etc.).

Goals:
* Simple, intuitive markup syntax.
* Generate screen and print-quality HTML documents with CSS.
* Support for pagination, page breaks.
* Readability.
* Inline HTML for everything else.

Usage:
```sh
$ ./jt.py < in.txt > out.html
```

Overview:

```
#:title: A Tale of Two Cities
#:author: Charles Dickens

#- {title}, by {author}

#-- Chapter 1

It was the best of times, it was the worst of times.
It was the age of wisdom, it was the age of foolishness.
It was the epoch of belief, it was the epoch of incredulity.
It was the season of light, it was the season of darkness.
It was the spring of hope, it was the winter of despair.
...
```