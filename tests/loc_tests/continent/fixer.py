# -*- coding: utf-8 -*-
import glob

for testcase in glob.glob('case_*.py'):
    with open(testcase) as f:
        testfile = f.read().splitlines()
    newlines = []
    for line in testfile:
        if line.startswith('        d = {"question"'):
            newlines.append("       url = 'http://127.0.0.1:8003/f?q=%s' % question")
        elif line == "        req = urllib2.Request('http://127.0.0.1:8003/')":
            newlines.append("        response = simplejson.load(urllib.urlopen(url))")
        elif line == "        req.add_header('Content-Type', 'application/json')":
            newlines.append("       best_answer = response['best_answer'][0]")
        elif line == "        response = urllib2.urlopen(req, json.dumps(d)).read()":
            continue
        elif line == "        response = json.loads(response)":
            continue
        elif line == "        best_answer = response['best_answer']":
            continue
        elif line == "import urllib2":
            newlines.append('import urllib\nimport simplejson')
        elif line == "import urllib":
            newlines.append('import urllib\nimport simplejson')
        else:
            newlines.append(line)

    out = open(testcase, 'w')
    for item in newlines:
        out.write("%s\n" % item)