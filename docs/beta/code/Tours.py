#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "Sitemap" - a chapter of "The Fuzzing Book"
# Web site: https://www.fuzzingbook.org/html/Tours.html
# Last change: 2025-10-26 19:00:01+01:00
#
# Copyright (c) 2021-2025 CISPA Helmholtz Center for Information Security
# Copyright (c) 2018-2020 Saarland University, authors, and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

r'''
The Fuzzing Book - Sitemap

This file can be _executed_ as a script, running all experiments:

    $ python Tours.py

or _imported_ as a package, providing classes, functions, and constants:

    >>> from fuzzingbook.Tours import <identifier>

but before you do so, _read_ it and _interact_ with it at:

    https://www.fuzzingbook.org/html/Tours.html


For more details, source, and documentation, see
"The Fuzzing Book - Sitemap"
at https://www.fuzzingbook.org/html/Tours.html
'''


# Allow to use 'from . import <module>' when run as script (cf. PEP 366)
if __name__ == '__main__' and __package__ is None:
    __package__ = 'fuzzingbook'


# Sitemap
# =======

if __name__ == '__main__':
    print('# Sitemap')



from .bookutils import rich_output, InteractiveSVG

if __name__ == '__main__':
    sitemap = None
    if rich_output():
        sitemap = InteractiveSVG(filename='PICS/Sitemap.svg')
    sitemap

## The Pragmatic Programmer Tour
## -----------------------------

if __name__ == '__main__':
    print('\n## The Pragmatic Programmer Tour')



## The Page-by-Page Tours
## ----------------------

if __name__ == '__main__':
    print('\n## The Page-by-Page Tours')



## The Undergraduate Tour
## ----------------------

if __name__ == '__main__':
    print('\n## The Undergraduate Tour')



## The Graduate Tour
## -----------------

if __name__ == '__main__':
    print('\n## The Graduate Tour')



## The Black-Box Tour
## ------------------

if __name__ == '__main__':
    print('\n## The Black-Box Tour')



## The White-Box Tour
## ------------------

if __name__ == '__main__':
    print('\n## The White-Box Tour')



## The Researcher Tour
## -------------------

if __name__ == '__main__':
    print('\n## The Researcher Tour')



## The Author Tour
## ---------------

if __name__ == '__main__':
    print('\n## The Author Tour')



## Lessons Learned
## ---------------

if __name__ == '__main__':
    print('\n## Lessons Learned')


