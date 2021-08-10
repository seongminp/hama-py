import pytest

from hama import assemble, disassemble


def test_assemble():
    assert assemble([]) == ""
    assert (
        assemble(
            [
                "5",
                "0",
                "0",
                "0",
                "ㅇ",
                "ㅝ",
                "ㄴ",
                "ㅇ",
                "ㅔ",
                "ㅎ",
                "ㅐ",
                "ㅈ",
                "ㅜ",
                "ㅅ",
                "ㅣ",
                "ㅁ",
            ]
        )
        == "5000원에해주심"
    )
    assert (
        assemble(["ㅋ", "ㅜ", "ㄹ", "ㄱ", "ㅓ", "ㄹ", "ㅐ", "ㄱ", "ㅏ", "ㄴ", "ㅡ", "ㅇ", "."])
        == "쿨거래가능."
    )
    assert assemble(["ㅁ", "ㅝ", "ㄹ", "ㅏ", "ㄱ", "ㅗ", "ㅇ", "ㅛ", "?"]) == "뭐라고요?"
    assert (
        assemble(
            ["ㅂ", "ㅣ", "ㅆ", "ㅏ", "ㄴ", "ㄱ", "ㅓ", "ㄱ", "ㅏ", "ㅌ", "ㅏ", "ㅅ", "ㅓ", ".."]
        )
        == "비싼거가타서.."
    )
    assert assemble(["ㅇ", "ㅏ", "ㄴ", "ㄷ", "ㅙ", "ㅇ", "ㅛ", "!"]) == "안돼요!"
    assert assemble(["ㅅ", "ㅣ", "ㅀ", "ㅇ", "ㅓ", "ㅇ", "ㅛ", "!"]) == "싫어요!"
    assert assemble(["ㄴ", "ㅣ", "ㅁ", "ㅅ", "ㅣ", "ㄴ", "ㄱ", "ㅗ", "ㅅ", "ㄱ"]) == "님신곳ㄱ"
    assert assemble(["ㅓ", "ㅐ", "ㅔ"]) == "ㅓㅐㅔ"


def test_disassemble():
    assert disassemble("")[0] == []
    assert disassemble("5000원에 해주심")[0] == [
        "5",
        "0",
        "0",
        "0",
        "ㅇ",
        "ㅝ",
        "ㄴ",
        "ㅇ",
        "ㅔ",
        "ㅎ",
        "ㅐ",
        "ㅈ",
        "ㅜ",
        "ㅅ",
        "ㅣ",
        "ㅁ",
    ]
    assert disassemble("쿨거래 가능.")[0] == [
        "ㅋ",
        "ㅜ",
        "ㄹ",
        "ㄱ",
        "ㅓ",
        "ㄹ",
        "ㅐ",
        "ㄱ",
        "ㅏ",
        "ㄴ",
        "ㅡ",
        "ㅇ",
        ".",
    ]
    assert disassemble("뭐라고요?")[0] == ["ㅁ", "ㅝ", "ㄹ", "ㅏ", "ㄱ", "ㅗ", "ㅇ", "ㅛ", "?"]
    assert disassemble("비싼거 가타서..")[0] == [
        "ㅂ",
        "ㅣ",
        "ㅆ",
        "ㅏ",
        "ㄴ",
        "ㄱ",
        "ㅓ",
        "ㄱ",
        "ㅏ",
        "ㅌ",
        "ㅏ",
        "ㅅ",
        "ㅓ",
        ".",
        ".",
    ]
    assert disassemble("안돼요!")[0] == ["ㅇ", "ㅏ", "ㄴ", "ㄷ", "ㅙ", "ㅇ", "ㅛ", "!"]
    assert disassemble("싫어요!")[0] == ["ㅅ", "ㅣ", "ㅀ", "ㅇ", "ㅓ", "ㅇ", "ㅛ", "!"]
    assert disassemble("님 신고 ㅅㄱ")[0] == [
        "ㄴ",
        "ㅣ",
        "ㅁ",
        "ㅅ",
        "ㅣ",
        "ㄴ",
        "ㄱ",
        "ㅗ",
        "ㅅ",
        "ㄱ",
    ]
    assert disassemble("ㅓㅐㅔ")[0] == ["ㅓ", "ㅐ", "ㅔ"]


def test_disassemble_with_position():
    assert disassemble("", include_position=True)[0] == []
    assert disassemble("5000원에 해주심", include_position=True)[0] == [
        "5/x",
        "0/x",
        "0/x",
        "0/x",
        "ㅇ/o",
        "ㅝ/n",
        "ㄴ/c",
        "ㅇ/o",
        "ㅔ/n",
        "ㅎ/o",
        "ㅐ/n",
        "ㅈ/o",
        "ㅜ/n",
        "ㅅ/o",
        "ㅣ/n",
        "ㅁ/c",
    ]
    assert disassemble("쿨거래 가능.", include_position=True)[0] == [
        "ㅋ/o",
        "ㅜ/n",
        "ㄹ/c",
        "ㄱ/o",
        "ㅓ/n",
        "ㄹ/o",
        "ㅐ/n",
        "ㄱ/o",
        "ㅏ/n",
        "ㄴ/o",
        "ㅡ/n",
        "ㅇ/c",
        "./x",
    ]
    assert disassemble("뭐라고요?", include_position=True)[0] == [
        "ㅁ/o",
        "ㅝ/n",
        "ㄹ/o",
        "ㅏ/n",
        "ㄱ/o",
        "ㅗ/n",
        "ㅇ/o",
        "ㅛ/n",
        "?/x",
    ]
    assert disassemble("비싼거 가타서..", include_position=True)[0] == [
        "ㅂ/o",
        "ㅣ/n",
        "ㅆ/o",
        "ㅏ/n",
        "ㄴ/c",
        "ㄱ/o",
        "ㅓ/n",
        "ㄱ/o",
        "ㅏ/n",
        "ㅌ/o",
        "ㅏ/n",
        "ㅅ/o",
        "ㅓ/n",
        "./x",
        "./x",
    ]
    assert disassemble("안돼요!", include_position=True)[0] == [
        "ㅇ/o",
        "ㅏ/n",
        "ㄴ/c",
        "ㄷ/o",
        "ㅙ/n",
        "ㅇ/o",
        "ㅛ/n",
        "!/x",
    ]
    assert disassemble("싫어요!", include_position=True)[0] == [
        "ㅅ/o",
        "ㅣ/n",
        "ㅀ/c",
        "ㅇ/o",
        "ㅓ/n",
        "ㅇ/o",
        "ㅛ/n",
        "!/x",
    ]
    assert disassemble("님 신고 ㅅㄱ", include_position=True)[0] == [
        "ㄴ/o",
        "ㅣ/n",
        "ㅁ/c",
        "ㅅ/o",
        "ㅣ/n",
        "ㄴ/c",
        "ㄱ/o",
        "ㅗ/n",
        "ㅅ/x",
        "ㄱ/x",
    ]
    assert disassemble("ㅓㅐㅔ", include_position=True)[0] == ["ㅓ/x", "ㅐ/x", "ㅔ/x"]
