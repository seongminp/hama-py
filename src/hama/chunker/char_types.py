HANGUL = 0
ENGLISH = 1
HANJA = 2
WHITESPACE = 3
SYMBOL = 4
NUMBER = 5
OTHER = 6


def get_type(c):
    code = ord(c)
    if c in {" ", "\t", "\n", "\r"}:
        return WHITESPACE
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
