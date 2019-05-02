#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cgi
form = cgi.FieldStorage()

DIR = "./data"
result = "nothing"

if "file" in form:
    item = form["file"]
    output_path = os.path.join(DIR, os.path.basename(item.filename))
    with open(output_path, "wb") as fo:
        while True:
            chunk = item.file.read(100000)
            if not chunk:
                break
            fo.write(chunk)
        result = "up"

str = '''
Content-Type: text/html

<html><body>{ret}</body><html>
'''.format(ret=result).strip()
print(str)
