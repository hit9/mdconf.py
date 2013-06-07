# coding=utf8
#
# Python implementation for visionmedia's mdconf,
# the markdown driven configuration::
#   https://github.com/visionmedia/mdconf
# This module was built on the top of misaka:
#   https://github.com/FSX/misaka


import misaka
from misaka import HtmlRenderer


class MdconfRenderer(HtmlRenderer):
    """misaka renderer for mdconf"""

    def __init__(self, *args, **kwargs):
        super(MdconfRenderer, self).__init__(*args, **kwargs)
        self.reset_vars()

    def reset_vars(self):
        """reset conf retult"""
        self.conf = {}  # the return var
        self.keys = []  # current group's position

    def put(self, text):
        """put text to the right position in conf"""
        last = None
        crt = self.conf

        for key in self.keys:
            last = crt
            crt = crt.setdefault(key, {})

        index = text.find(":")  # try to find the first ':'

        if index == -1:  # list
            if not isinstance(last[key], list):
                last[key] = []
            last[key].append(text.strip())
        else:  # map
            key, value = (
                text[:index].strip(),
                text[index+1:].strip(),
            )
            crt[key] = value

    def header(self, text, level):

        # polish keys to given depth
        while len(self.keys) >= level:
            self.keys.pop()
        self.keys.append(text.strip())

    def list_item(self, text, is_ordered):
        self.put(text)

    def block_code(self, text, lang):
        self.put(text)


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
