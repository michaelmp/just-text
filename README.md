just-text
=========

Similar to Restructured Text and Markdown, just-text converts plain text to HTML.
Dissimilar to those programs, just-text aims to format basic literary texts
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