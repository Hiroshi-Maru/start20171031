#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>��M�����f�[�^��\��</title>
<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<h1>%s</h1>
</body>
</html>
"""

form = cgi.FieldStorage()
text = form.getvalue('text','')
html_body = unicode(html_body,'utf-8')

print(html_body % (text))
