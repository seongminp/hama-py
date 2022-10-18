from .char_types import (
    ENGLISH,
    HANGUL,
    HANJA,
    NUMBER,
    OTHER,
    SYMBOL,
    WHITESPACE,
    get_type,
)


class Chunker:
    def __init__(self):
        self.type_codes = {
            "h": HANGUL,
            "o": OTHER,
            "c": HANJA,
            "n": NUMBER,
            "e": ENGLISH,
            "w": WHITESPACE,
            "s": SYMBOL,
        }

    def chunk(self, text, return_types="hocnews"):
        return_types = {self.type_codes[t] for t in return_types}
        prev_type, chunk_begin = None, 0
        for i, c in enumerate(text):
            curr_type = get_type(c)
            if prev_type is not None and curr_type != prev_type:
                if prev_type in return_types:
                    yield prev_type, chunk_begin, i - 1
                chunk_begin = i
            prev_type = curr_type
        if prev_type is not None and prev_type in return_types:
            yield prev_type, chunk_begin, i
