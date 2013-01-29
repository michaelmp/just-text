just-text
=========

A text/plain syntax for generating pretty HTML documents.

Features:
* Simple markup syntax.
    !myfunction: Hello world!
    !myfunction
* Generates HTML for `screen` and `print` media.

Goals:
* Cross-references.
* Smart pagination.
* Support for books, resumes, and technical documents.

---

Usage:
```sh
$ ./jt.py < in.txt > out.html
```

Overview:

```
!title A Tale of Two Cities
!author Charles Dickens

!part 1 Recalled to Life

!chapter 1 The Period

It was the best of times, it was the worst of times.
It was the age of wisdom, it was the age of foolishness.
It was the epoch of belief, it was the epoch of incredulity.
It was the season of light, it was the season of darkness.
It was the spring of hope, it was the winter of despair.
```
