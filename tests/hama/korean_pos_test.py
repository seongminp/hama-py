import pytest
import hama


def test_ches():
    text = ""
    assert (hama.nouns(text) == hama.ches(text))


def test_yongs():
    text = ""
    assert (hama.predicates(text) == hama.yongs(text))


def test_soos():
    text = ""
    assert (hama.modifiers(text) == hama.soos(text))


def test_doks():
    text = ""
    assert (hama.orthotones(text) == hama.doks(text))


def test_jos():
    text = ""
    assert (hama.postpositions(text) == hama.jos(text))


def test_eoms():
    text = ""
    assert (hama.suffixes(text) == hama.eoms(text))


def test_jubs():
    text = ""
    assert (hama.affixes(text) == hama.jubs(text))
