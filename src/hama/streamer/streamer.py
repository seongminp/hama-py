SEPARATOR = -1
SPACE = 0
HANGUL = 1
HANJA = 2
ENGLISH = 3
NUMBER = 4
SYMBOL = 5
OTHER = 6


def get_type(c):
    code = ord(c)
    if c == " ":
        return SPACE
    elif 0xAC00 <= code <= 0xD7A3:
        return HANGUL
    elif 0x2B820 <= code <= 0x2CEAF:
        return HANJA
    elif 0x41 <= code <= 0x7A:
        return ENGLISH
    elif c.isdigit():
        return NUMBER
    elif c in {
        '"',
        "/",
        "?",
        "!",
        ",",
        ".",
        "\\",
        "~",
        "`",
        "*",
        "&",
        "|",
        "(",
        ")",
        "^",
        "%",
        "$",
        "#",
        "@",
        "+",
        "=",
        "-",
        "_",
        "[",
        "]",
        "{",
        "}",
    }:
        return SYMBOL
    else:
        return OTHER


def chunk(text):
    prev_type = None
    for i, c in enumerate(text):
        curr_type = get_type(c)
        if prev_type is None:
            yield i, c, curr_type
        else:
            if curr_type != prev_type:
                yield None, None, SEPARATOR
            yield i, c, curr_type
        prev_type = curr_type
