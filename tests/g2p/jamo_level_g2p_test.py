import pytest

from hama import Phonemizer, disassemble


@pytest.fixture
def phonemizer():
    p = Phonemizer()
    return p


def test_rule_9(phonemizer):
    assert phonemizer.jamo_level_g2p("닦다") == disassemble("닥따")
    assert phonemizer.jamo_level_g2p("키읔") == disassemble("키윽")
    assert phonemizer.jamo_level_g2p("키읔과") == disassemble("키윽꽈")
    assert phonemizer.jamo_level_g2p("옷") == disassemble("옫")
    # Maybe the correct pronounciation is "우따" (according to rule 30.1).
    # We omit rule 24.
    # assert jamo_level_g2p("웃다") == disassemble("욷따")
    assert phonemizer.jamo_level_g2p("있다") == disassemble("읻따")
    assert phonemizer.jamo_level_g2p("젖") == disassemble("젇")
    assert phonemizer.jamo_level_g2p("빚다") == disassemble("빋따")
    assert phonemizer.jamo_level_g2p("꽃") == disassemble("꼳")
    assert phonemizer.jamo_level_g2p("쫓다") == disassemble("쫃따")
    assert phonemizer.jamo_level_g2p("솥") == disassemble("솓")
    assert phonemizer.jamo_level_g2p("뱉다") == disassemble("밷따")
    assert phonemizer.jamo_level_g2p("앞") == disassemble("압")
    assert phonemizer.jamo_level_g2p("덮다") == disassemble("덥따")


def test_rule_10(phonemizer):
    assert phonemizer.jamo_level_g2p("넋") == disassemble("넉")
    assert phonemizer.jamo_level_g2p("넋과") == disassemble("넉꽈")
    # We omit rule 24.
    # assert jamo_level_g2p("앉다") == disassemble("안따")
    assert phonemizer.jamo_level_g2p("여덟") == disassemble("여덜")
    # We omit rule 24.
    # assert jamo_level_g2p("넓다") == disassemble("널따")
    assert phonemizer.jamo_level_g2p("외곬") == disassemble("외골")
    # We omit rule 24.
    # assert jamo_level_g2p("핥다") == disassemble("할따")
    assert phonemizer.jamo_level_g2p("값") == disassemble("갑")
    # We omit rule 24.
    # assert jamo_level_g2p("없다") == disassemble("업따")


def test_rule_10_exception_1(phonemizer):
    assert phonemizer.jamo_level_g2p("밟다") == disassemble("밥따")
    assert phonemizer.jamo_level_g2p("밟소") == disassemble("밥쏘")
    assert phonemizer.jamo_level_g2p("밟지") == disassemble("밥찌")
    assert phonemizer.jamo_level_g2p("밟는") == disassemble("밤는")
    assert phonemizer.jamo_level_g2p("밟게") == disassemble("밥께")
    assert phonemizer.jamo_level_g2p("밟고") == disassemble("밥꼬")
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("넓죽하다")[0] == disassemble("넙쭈카다")[0]
    assert phonemizer.jamo_level_g2p("넓둥글다") == disassemble("넙뚱글다")


def test_rule_11(phonemizer):
    assert phonemizer.jamo_level_g2p("닭") == disassemble("닥")
    assert phonemizer.jamo_level_g2p("흙과") == disassemble("흑꽈")
    # We omit rule 24.
    # assert jamo_level_g2p("맑다") == disassemble("막따")
    assert phonemizer.jamo_level_g2p("늙지") == disassemble("늑찌")
    assert phonemizer.jamo_level_g2p("삶") == disassemble("삼")
    # We omit rule 24.
    # assert jamo_level_g2p("젊다") == disassemble("점따")
    assert phonemizer.jamo_level_g2p("읊고") == disassemble("읍꼬")
    # We omit rule 24.
    # assert jamo_level_g2p("읊다") == disassemble("읍따")


def test_rule_12_1(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("놓고")[0] == disassemble("노코")[0]
    assert phonemizer.jamo_level_g2p("좋던")[0] == disassemble("조턴")[0]
    assert phonemizer.jamo_level_g2p("쌓지")[0] == disassemble("싸치")[0]
    assert phonemizer.jamo_level_g2p("많고")[0] == disassemble("만코")[0]
    assert phonemizer.jamo_level_g2p("않던")[0] == disassemble("안턴")[0]
    assert phonemizer.jamo_level_g2p("닳지")[0] == disassemble("달치")[0]


def test_rule_12_1_addition_1(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("각하")[0] == disassemble("가카")[0]
    assert phonemizer.jamo_level_g2p("먹히다")[0] == disassemble("머키다")[0]
    assert phonemizer.jamo_level_g2p("밟히다")[0] == disassemble("발피다")[0]
    assert phonemizer.jamo_level_g2p("맏형")[0] == disassemble("마텽")[0]
    assert phonemizer.jamo_level_g2p("좁히다")[0] == disassemble("조피다")[0]
    assert phonemizer.jamo_level_g2p("넓히다")[0] == disassemble("널피다")[0]
    assert phonemizer.jamo_level_g2p("꽂히다")[0] == disassemble("꼬치다")[0]
    assert phonemizer.jamo_level_g2p("앉히다")[0] == disassemble("안치다")[0]


def test_rule_12_addition_2(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("옷 한 벌")[0] == disassemble("오탄벌")[0]
    assert phonemizer.jamo_level_g2p("낮 한때")[0] == disassemble("나탄때")[0]
    assert phonemizer.jamo_level_g2p("꽃 한 송이")[0] == disassemble("꼬탄송이")[0]
    assert phonemizer.jamo_level_g2p("숱하다")[0] == disassemble("수타다")[0]


def test_rule_12_2(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("닿소")[0] == disassemble("다쏘")[0]
    assert phonemizer.jamo_level_g2p("많소")[0] == disassemble("만쏘")[0]
    assert phonemizer.jamo_level_g2p("싫소")[0] == disassemble("실쏘")[0]


def test_rule_12_3(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("놓는")[0] == disassemble("논는")[0]
    assert phonemizer.jamo_level_g2p("쌓네")[0] == disassemble("싼네")[0]


def test_rule_12_3_addition_1(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("않네")[0] == disassemble("안네")[0]
    assert phonemizer.jamo_level_g2p("않는")[0] == disassemble("안는")[0]
    assert phonemizer.jamo_level_g2p("뚫네")[0] == disassemble("뚤레")[0]
    assert phonemizer.jamo_level_g2p("뚫는")[0] == disassemble("뚤른")[0]


def test_rule_12_4(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("낳은")[0] == disassemble("나은")[0]
    assert phonemizer.jamo_level_g2p("놓아")[0] == disassemble("노아")[0]
    assert phonemizer.jamo_level_g2p("쌓이다")[0] == disassemble("싸이다")[0]
    assert phonemizer.jamo_level_g2p("많아")[0] == disassemble("마나")[0]
    assert phonemizer.jamo_level_g2p("않은")[0] == disassemble("아는")[0]
    assert phonemizer.jamo_level_g2p("닳아")[0] == disassemble("다라")[0]
    assert phonemizer.jamo_level_g2p("싫어도")[0] == disassemble("시러도")[0]


def test_rule_13(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("깎아")[0] == disassemble("까까")[0]
    assert phonemizer.jamo_level_g2p("옷이")[0] == disassemble("오시")[0]
    assert phonemizer.jamo_level_g2p("있어")[0] == disassemble("이써")[0]
    assert phonemizer.jamo_level_g2p("낮이")[0] == disassemble("나지")[0]
    assert phonemizer.jamo_level_g2p("꽂아")[0] == disassemble("꼬자")[0]
    assert phonemizer.jamo_level_g2p("꽃을")[0] == disassemble("꼬츨")[0]
    assert phonemizer.jamo_level_g2p("쫓아")[0] == disassemble("쪼차")[0]
    assert phonemizer.jamo_level_g2p("밭에")[0] == disassemble("바테")[0]
    assert phonemizer.jamo_level_g2p("앞으로")[0] == disassemble("아프로")[0]
    assert phonemizer.jamo_level_g2p("덮이다")[0] == disassemble("더피다")[0]


def test_rule_14(phonemizer):
    assert phonemizer.jamo_level_g2p("넋이") == disassemble("넉씨")
    assert phonemizer.jamo_level_g2p("앉아") == disassemble("안자")
    assert phonemizer.jamo_level_g2p("닭을") == disassemble("달글")
    assert phonemizer.jamo_level_g2p("젊어") == disassemble("절머")
    assert phonemizer.jamo_level_g2p("곬이") == disassemble("골씨")
    assert phonemizer.jamo_level_g2p("핥아") == disassemble("할타")
    assert phonemizer.jamo_level_g2p("읊어") == disassemble("을퍼")
    assert phonemizer.jamo_level_g2p("값을") == disassemble("갑쓸")
    assert phonemizer.jamo_level_g2p("없어") == disassemble("업써")


# def test_rule_15:
#    assert jamo_level_g2p("아래") == disassemble("바다래")[0]
#    assert jamo_level_g2p("앞") == disassemble("느밥")[0]
#    assert jamo_level_g2p("젖어미") == disassemble("저더미")[0]
#    assert jamo_level_g2p("맛없다") == disassemble("마덥다")[0]
#    assert jamo_level_g2p("겉옷") == disassemble("거돋")[0]
#    assert jamo_level_g2p("헛웃음") == disassemble("허두슴")[0]
#    assert jamo_level_g2p("위") == disassemble("꼬뒤")[0]


def test_rule_17(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("곧이듣다")[0] == disassemble("고지듣따")[0]
    assert phonemizer.jamo_level_g2p("굳이")[0] == disassemble("구지")[0]
    assert phonemizer.jamo_level_g2p("미닫이")[0] == disassemble("미다지")[0]
    assert phonemizer.jamo_level_g2p("땀받이")[0] == disassemble("땀바지")[0]
    assert phonemizer.jamo_level_g2p("밭이")[0] == disassemble("바치")[0]
    assert phonemizer.jamo_level_g2p("벼훑이")[0] == disassemble("벼훌치")[0]


def test_rule_17_addition_1(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("굳히다")[0] == disassemble("구치다")[0]
    assert phonemizer.jamo_level_g2p("닫히다")[0] == disassemble("다치다")[0]
    assert phonemizer.jamo_level_g2p("묻히다")[0] == disassemble("무치다")[0]


def test_rule_18(phonemizer):
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("먹는") == disassemble("멍는")
    assert phonemizer.jamo_level_g2p("국물") == disassemble("궁물")
    assert phonemizer.jamo_level_g2p("깎는") == disassemble("깡는")
    assert phonemizer.jamo_level_g2p("키읔만") == disassemble("키응만")
    assert phonemizer.jamo_level_g2p("몫몫이") == disassemble("몽목씨")
    assert phonemizer.jamo_level_g2p("긁는") == disassemble("긍는")
    assert phonemizer.jamo_level_g2p("흙만") == disassemble("흥만")
    assert phonemizer.jamo_level_g2p("닫는") == disassemble("단는")
    assert phonemizer.jamo_level_g2p("짓는") == disassemble("진는")
    # 표준발음법 예시 틀림.
    assert phonemizer.jamo_level_g2p("옷맵시") == disassemble("온맵씨")
    assert phonemizer.jamo_level_g2p("있는") == disassemble("인는")
    assert phonemizer.jamo_level_g2p("맞는") == disassemble("만는")
    assert phonemizer.jamo_level_g2p("젖멍울") == disassemble("전멍울")
    assert phonemizer.jamo_level_g2p("쫓는") == disassemble("쫀는")
    assert phonemizer.jamo_level_g2p("꽃망울") == disassemble("꼰망울")
    assert phonemizer.jamo_level_g2p("붙는") == disassemble("분는")
    assert phonemizer.jamo_level_g2p("놓는") == disassemble("논는")
    assert phonemizer.jamo_level_g2p("잡는") == disassemble("잠는")
    assert phonemizer.jamo_level_g2p("밥물") == disassemble("밤물")
    assert phonemizer.jamo_level_g2p("앞마당") == disassemble("암마당")
    assert phonemizer.jamo_level_g2p("밟는") == disassemble("밤는")
    assert phonemizer.jamo_level_g2p("읊는") == disassemble("음는")
    assert phonemizer.jamo_level_g2p("없는") == disassemble("엄는")
    assert phonemizer.jamo_level_g2p("값매다") == disassemble("감매다")


def test_rule_18_addition_1(phonemizer):
    assert phonemizer.jamo_level_g2p("책넣는다") == disassemble("챙넌는다")
    assert phonemizer.jamo_level_g2p("흙말리다") == disassemble("흥말리다")
    # 표준발음법 예시 틀림.
    assert phonemizer.jamo_level_g2p("옷맞추다") == disassemble("온맏추다")
    assert phonemizer.jamo_level_g2p("밥먹는다") == disassemble("밤멍는다")
    assert phonemizer.jamo_level_g2p("값매기다") == disassemble("감매기다")


def test_rule_19(phonemizer):
    assert phonemizer.jamo_level_g2p("담력") == disassemble("담녁")
    assert phonemizer.jamo_level_g2p("침략") == disassemble("침냑")
    assert phonemizer.jamo_level_g2p("강릉") == disassemble("강능")
    assert phonemizer.jamo_level_g2p("항로") == disassemble("항노")
    assert phonemizer.jamo_level_g2p("대통령") == disassemble("대통녕")


def test_rule_19_addition_1(phonemizer):
    assert phonemizer.jamo_level_g2p("막론") == disassemble("망논")
    assert phonemizer.jamo_level_g2p("백리") == disassemble("뱅니")
    assert phonemizer.jamo_level_g2p("협력") == disassemble("혐녁")
    assert phonemizer.jamo_level_g2p("십리") == disassemble("심니")


def test_rule_20(phonemizer):
    assert phonemizer.jamo_level_g2p("난로") == disassemble("날로")
    assert phonemizer.jamo_level_g2p("신라") == disassemble("실라")
    assert phonemizer.jamo_level_g2p("천리") == disassemble("철리")
    assert phonemizer.jamo_level_g2p("광한루") == disassemble("광할루")
    assert phonemizer.jamo_level_g2p("대관령") == disassemble("대괄령")
    assert phonemizer.jamo_level_g2p("칼날") == disassemble("칼랄")
    assert phonemizer.jamo_level_g2p("물난리") == disassemble("물랄리")
    # We omit rule 24.
    # assert jamo_level_g2p("줄넘기") == disassemble("줄럼끼")
    assert phonemizer.jamo_level_g2p("할는지") == disassemble("할른지")


def test_rule_20_addition_1(phonemizer):
    assert phonemizer.jamo_level_g2p("닳는") == disassemble("달른")
    assert phonemizer.jamo_level_g2p("뚫는") == disassemble("뚤른")
    assert phonemizer.jamo_level_g2p("핥네") == disassemble("할레")


def test_rule_23(phonemizer):
    assert phonemizer.jamo_level_g2p("국밥") == disassemble("국빱")
    assert phonemizer.jamo_level_g2p("깎다") == disassemble("깍따")
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("넋받이")[0] == disassemble("넉빠지")[0]
    assert phonemizer.jamo_level_g2p("삯돈") == disassemble("삭똔")
    assert phonemizer.jamo_level_g2p("닭장") == disassemble("닥짱")
    assert phonemizer.jamo_level_g2p("칡범") == disassemble("칙뻠")
    assert phonemizer.jamo_level_g2p("뻗대다") == disassemble("뻗때다")
    assert phonemizer.jamo_level_g2p("옷고름") == disassemble("옫꼬름")
    assert phonemizer.jamo_level_g2p("있던") == disassemble("읻떤")
    assert phonemizer.jamo_level_g2p("꽂고") == disassemble("꼳꼬")
    assert phonemizer.jamo_level_g2p("꽃다발") == disassemble("꼳따발")
    assert phonemizer.jamo_level_g2p("낯설다") == disassemble("낟썰다")
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("밭갈이")[0] == disassemble("받까리")[0]
    assert phonemizer.jamo_level_g2p("솥전") == disassemble("솓쩐")
    assert phonemizer.jamo_level_g2p("곱돌") == disassemble("곱똘")
    assert phonemizer.jamo_level_g2p("덮개") == disassemble("덥깨")
    assert phonemizer.jamo_level_g2p("옆집") == disassemble("엽찝")
    # Source position of merged phonemes is ambiguous.
    assert phonemizer.jamo_level_g2p("넓죽하다")[0] == disassemble("넙쭈카다")[0]
    assert phonemizer.jamo_level_g2p("읊조리다") == disassemble("읍쪼리다")
    assert phonemizer.jamo_level_g2p("값지다") == disassemble("갑찌다")


def test_rule_24(phonemizer):
    # assert jamo_level_g2p("신고") == disassemble("신꼬")[0]
    # assert jamo_level_g2p("껴안다") == disassemble("껴안따")[0]
    # assert jamo_level_g2p("앉고") == disassemble("안꼬")[0]
    # assert jamo_level_g2p("얹다") == disassemble("언따")[0]
    # assert jamo_level_g2p("삼고") == disassemble("삼꼬")[0]
    # assert jamo_level_g2p("더듬지") == disassemble("더듬찌")[0]
    # assert jamo_level_g2p("닮고") == disassemble("담꼬")[0]
    # assert jamo_level_g2p("젊지") == disassemble("점찌")[0]
    pass


def test_rule_25(phonemizer):
    assert phonemizer.jamo_level_g2p("넓게") == disassemble("널께")
    assert phonemizer.jamo_level_g2p("핥다") == disassemble("할따")
    assert phonemizer.jamo_level_g2p("훑소") == disassemble("훌쏘")
    assert phonemizer.jamo_level_g2p("떫지") == disassemble("떨찌")


def test_rule_30_1(phonemizer):
    assert phonemizer.jamo_level_g2p("냇가") == disassemble(
        "내까"
    ) or phonemizer.jamo_level_g2p("냇가") == disassemble("낻까")
    assert phonemizer.jamo_level_g2p("샛길") == disassemble(
        "새낄"
    ) or phonemizer.jamo_level_g2p("샛길") == disassemble("샏낄")
    assert phonemizer.jamo_level_g2p("빨랫돌") == disassemble(
        "빨래똘"
    ) or phonemizer.jamo_level_g2p("빨랫돌") == disassemble("빨랟똘")
    assert phonemizer.jamo_level_g2p("콧등") == disassemble(
        "코뜽"
    ) or phonemizer.jamo_level_g2p("콧등") == disassemble("콛뜽")
    assert phonemizer.jamo_level_g2p("깃발") == disassemble(
        "기빨"
    ) or phonemizer.jamo_level_g2p("깃발") == disassemble("긷빨")
    assert phonemizer.jamo_level_g2p("대팻밥") == disassemble(
        "대패빱"
    ) or phonemizer.jamo_level_g2p("대팻밥") == disassemble("대팯빱")
    assert phonemizer.jamo_level_g2p("햇살") == disassemble(
        "해쌀"
    ) or phonemizer.jamo_level_g2p("햇살") == disassemble("핻쌀")
    assert phonemizer.jamo_level_g2p("뱃속") == disassemble(
        "배쏙"
    ) or phonemizer.jamo_level_g2p("뱃속") == disassemble("밷쏙")
    assert phonemizer.jamo_level_g2p("뱃전") == disassemble(
        "배쩐"
    ) or phonemizer.jamo_level_g2p("뱃전") == disassemble("밷쩐")
    assert phonemizer.jamo_level_g2p("고갯짓") == disassemble(
        "고개찓"
    ) or phonemizer.jamo_level_g2p("고갯짓") == disassemble("고갣찓")


def test_rule_30_2(phonemizer):
    assert phonemizer.jamo_level_g2p("콧날") == disassemble("콘날")
    assert phonemizer.jamo_level_g2p("아랫니") == disassemble("아랜니")
    assert phonemizer.jamo_level_g2p("툇마루") == disassemble("퇸마루")
    assert phonemizer.jamo_level_g2p("뱃머리") == disassemble("밴머리")


def test_rule_30_3(phonemizer):
    # assert jamo_level_g2p("베갯잇") == disassemble("베갠닏")
    # assert jamo_level_g2p("깻잎") == disassemble("깬닙")
    # assert jamo_level_g2p("나뭇잎") == disassemble("나문닙")
    # assert jamo_level_g2p("도리깻열") == disassemble("도리깬녈")
    # assert jamo_level_g2p("뒷윷") == disassemble("뒨뉻")
    pass
