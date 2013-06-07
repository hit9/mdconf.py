# coding=utf8
#
# Python implementation for visionmedia's mdconf,
# the markdown driven configuration::
#   https://github.com/visionmedia/mdconf
# This module was built on the top of misaka:
#   https://github.com/FSX/misaka


import misaka
from misaka import HtmlRenderer

MAP = 11
LIST = 12


class MdconfRenderer(HtmlRenderer):
    """misaka renderer for mdconf"""

    def __init__(self, *args, **kwargs):
        super(MdconfRenderer, self).__init__(*args, **kwargs)
        self.reset_vars()

    def reset_vars(self):
        """reset conf retult"""
        self.conf = {}  # the return var
        self.keys = []  # current group's position

    def put(self, text, type=MAP):
        """put text to the right position in conf"""
        last = None
        crt = self.conf

        for key in self.keys:
            last = crt
            crt = crt.setdefault(key, {})

        if type == LIST:
            if not isinstance(last[key], list):
                last[key] = []
            last[key].append(text.strip())
        elif type == MAP:
            index = text.find(":")
            assert index > 0  # index should > 0
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
        if ":" in text:
            self.put(text, type=MAP)
        else:
            self.put(text, type=LIST)

    def block_code(self, text, lang):
        self.put(text, type=LIST)


class MdconfParser(object):

    def __init__(self, extensions=(
            misaka.EXT_FENCED_CODE |
            misaka.EXT_NO_INTRA_EMPHASIS |
            misaka.EXT_AUTOLINK
        )
    ):
        self.renderer = MdconfRenderer()
        self.markdown = misaka.Markdown(self.renderer, extensions=extensions)

    def parse(self, text):
        self.renderer.reset_vars()
        self.markdown.render(text)
        return self.renderer.conf


parser = MdconfParser()  # build a quick use parser


def parse(text):
    return parser.parse(text)
