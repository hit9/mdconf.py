import misaka
from misaka import HtmlRenderer


class MdconfRenderer(HtmlRenderer):

    def __init__(self, *args, **kwargs):
        super(MdconfRenderer, self).__init__(self, *args, **kwargs)
        self.reset()

    def reset(self):
        self.conf = {}
        self.keys = []

    def normalize_text(func):
        def wrapper(self, text, *args, **kwargs):
            text = text.strip()
            return func(self, text, *args, **kwargs)
        return wrapper

    def slide_to(self, keys):
        """slide to current section's dict"""
        conf = self.conf
        for key in self.keys:
            conf = conf.setdefault(key, {})
        return conf

    @normalize_text
    def header(self, text, level):

        while len(self.keys) >= level:
            self.keys.pop()
        self.keys.append(text)
        self.slide_to(self.keys)

    @normalize_text
    def list_item(self, text, is_ordered):
        index = text.find(":")
        key, value = text[:index].strip(), text[index+1:].strip()
        conf = self.slide_to(self.keys)
        conf[key] = value

renderer = MdconfRenderer()

extensions = (
    misaka.EXT_FENCED_CODE |
    misaka.EXT_NO_INTRA_EMPHASIS |
    misaka.EXT_AUTOLINK
)


md = misaka.Markdown(renderer, extensions=extensions)


def parse(text):
    renderer.reset()
    md.render(text)
    return renderer.conf

## current tests

s = open("test.md").read()
print parse(s)
print parse("""
# heading
  - j: 99
""")
