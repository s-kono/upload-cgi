#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
form = cgi.FieldStorage()

result = "nothing"

if form.getvalue('textcontent'):
    with open("./data/msg.txt", "w") as fo:
        fo.write(form.getvalue('textcontent'))
        result = "up"

str = '''
Content-Type: text/html

<html><body>{ret}</body><html>
'''.format(ret=result).strip()
print(str)
