# coding=utf8
# Python implementation for visionmedia's mdconf,
# the markdown driven configuration::
#   https://github.com/visionmedia/mdconf
# This module was built on the top of misaka:
#   https://github.com/FSX/misaka


import misaka
from misaka import HtmlRenderer


class MdconfRenderer(HtmlRenderer):

    def __init__(self, *args, **kwargs):
        super(MdconfRenderer, self).__init__(*args, **kwargs)
        self.reset_vars()

    def reset_vars(self):
        """reset conf retult"""
        self.conf = {}  # the return var
        self.keys = []  # record current keys

    def normalize_text(func):
        """decorator to strip the second parameter of func"""
        def wrapper(self, text, *args, **kwargs):
            text = text.strip()
            return func(self, text, *args, **kwargs)
        return wrapper

    def slide_to(self, keys):
        """slide to given keys depth dict"""
        conf = self.conf
        for key in keys:
            conf = conf.setdefault(key, {})
        return conf

    @normalize_text
    def header(self, text, level):
        # polish keys to given depth
        while len(self.keys) >= level:
            self.keys.pop()
        self.keys.append(text)
        # check keys
        self.slide_to(self.keys)

    @normalize_text
    def list_item(self, text, is_ordered):
        index = text.find(":")  # try to find the first ':'
        # found, maps
        if index >= 0:
            key, value = (
                text[:index].strip(),
                text[:index+1].strip(),
            )
            conf = self.slide_to(self.keys)
            conf[key] = value
        else:  # not found, list
            pass


class MdconfParser(object):

    def __init__(self):
        extensions = (
            misaka.EXT_FENCED_CODE |
            misaka.EXT_NO_INTRA_EMPHASIS |
            misaka.EXT_AUTOLINK
        )
        self.renderer = MdconfRenderer()
        self.markdown = misaka.Markdown(self.renderer, extensions=extensions)

    def parse(self, text):
        self.renderer.reset_vars()
        self.markdown.render(text)
        return self.renderer.conf


parser = MdconfParser()  # build a quick use parser


def parse(text):
    return parser.parse(text)


## current tests

s = open("test.md").read()
print parse(s)
print parse("""
# heading
  - j: 99
""")
