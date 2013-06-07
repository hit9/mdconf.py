# coding=utf8

"""test unit fire up script"""

import mdconf
import json
from os import listdir as ls
from os.path import join


cases_dir = join("mdconf", "test", "cases")
for fn in ls(cases_dir):
    if fn.endswith(".md"):
        # file path
        md_fp = join(cases_dir, fn)
        json_fp = join(cases_dir, fn[:-3]+".json")
        # read
        md_s = open(md_fp).read()
        json_s = open(json_fp).read()
        # parse
        md_conf = mdconf.parse(md_s)
        json_result = json.loads(json_s)
        # assert
        try:
            assert md_conf == json_result
            print "OK: %s  ==  %s" % (md_fp, json_fp)
        except AssertionError:
            print md_conf
            raise AssertionError
