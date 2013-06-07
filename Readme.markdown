mdconf.py
=========

Python implementation for [visionmedia's mdconf](https://github.com/visionmedia/mdconf) - Markdown driven configuration

[![Build Status](https://travis-ci.org/hit9/mdconf.py.png?branch=master)](https://travis-ci.org/hit9/mdconf.py)

Installation
------------

    $ pip install -e "git+git://github.com/hit9/mdconf.py.git#egg=mdconf.py" --upgrade


What's mdconf?
--------------

Please see https://github.com/visionmedia/mdconf.

API
---

```python
import mdconf
mdconf.parse("markdown string")
```

Example
--------

```
>>> import mdconf
>>> import json
>>> conf = mdconf.parse("""
... ## Upload
... 
...   - max: 200mb
...   - dir: /tmp
... """)
>>> print json.dumps(conf, indent=2)
{
  "Upload": {
    "max": "200mb", 
    "dir": "/tmp"
  }
}
```

License
-------

(The MIT License)

Copyright (c) 2013 TJ Holowaychuk <tj@vision-media.ca>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
