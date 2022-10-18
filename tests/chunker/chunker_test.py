import pytest

from hama import Chunker, char_types

HANGUL = char_types.HANGUL
ENGLISH = char_types.ENGLISH
HANJA = char_types.HANJA
WHITESPACE = char_types.WHITESPACE
SYMBOL = char_types.SYMBOL
NUMBER = char_types.NUMBER
OTHER = char_types.OTHER


def test_chunker_all():
    c = Chunker()
    assert list(c.chunk("안녕하세요")) == [(HANGUL, 0, 4)]
    assert list(c.chunk("안 녕 하 세 요")) == [
        (HANGUL, 0, 0),
        (WHITESPACE, 1, 1),
        (HANGUL, 2, 2),
        (WHITESPACE, 3, 3),
        (HANGUL, 4, 4),
        (WHITESPACE, 5, 5),
        (HANGUL, 6, 6),
        (WHITESPACE, 7, 7),
        (HANGUL, 8, 8),
    ]
    assert list(c.chunk("안녕하세요.")) == [(HANGUL, 0, 4), (SYMBOL, 5, 5)]
    assert list(c.chunk("안녕하세요123")) == [(HANGUL, 0, 4), (NUMBER, 5, 7)]
    assert list(c.chunk("안1녕2하3세요")) == [
        (HANGUL, 0, 0),
        (NUMBER, 1, 1),
        (HANGUL, 2, 2),
        (NUMBER, 3, 3),
        (HANGUL, 4, 4),
        (NUMBER, 5, 5),
        (HANGUL, 6, 7),
    ]
    assert list(c.chunk("안녕하세요hello")) == [(HANGUL, 0, 4), (ENGLISH, 5, 9)]
    assert list(c.chunk("hello world")) == [
        (ENGLISH, 0, 4),
        (WHITESPACE, 5, 5),
        (ENGLISH, 6, 10),
    ]
    assert list(c.chunk("hello")) == [(ENGLISH, 0, 4)]


def test_chunker_no_whitespace():
    c = Chunker()
    # assert(list(c.chunk("안녕하세요", return_types="chwen")) == [])
    # assert(list(c.chunk("안 녕 하 세 요")) == [])
    # assert(list(c.chunk("안녕하세요.")) == [])
    # assert(list(c.chunk("안녕하세요123")) == [])
    # assert(list(c.chunk("안1녕2하3세요")) == [])
    # assert(list(c.chunk("안녕하세요hello")) == [])
    # assert(list(c.chunk("hello world")) == [])
    # assert(list(c.chunk("hello")) == [])
