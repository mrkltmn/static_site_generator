from enum import Enum


class TextType(Enum):
    TEXT_PLAIN = "plain text"
    TEXT_BOLD = "bold text"
    TEXT_ITALIC = "italic text"
    TEXT_CODE = "code text"
    LINKS = "links"
    IMAGES = "images"


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self):
