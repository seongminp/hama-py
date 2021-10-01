from .assemble_machine import Assembler
from .constants import (
    chosung_set,
    chosungs,
    jongsung_set,
    jongsungs,
    joongsung_set,
    joongsungs,
)


def disassemble(text, out_type=list, include_position=False, include_whitespace=False):
    """
    Deconstruct input text into Korean consonants and vowels.

    Args:
        text                (str): Input string to deconstruct.
        out_type           (type): [Optional, default: list] Output type. 
                                   One of list and str.
        include_position   (bool): [Optional, default: False] Include position tags 
                                   (/o for onset, /n for nucleus, /c for coda).
        include_whitespace (bool): [Optional, default: False] Include whitespace in output.
                                   False by default to match other libraries.

    Returns:
        list/str: List of consonants and vowels. Symbols and foreign 
                  languages are returned as-is.
        list: List that maps each index of disassembled component to 
              its original character index.
    """
    if out_type == list:
        out = list()
    elif out_type == str:
        out = ""
    else:
        raise Exception(f"Wrong output type: {out_type}.")
    recovery_map = list()

    for i, c in enumerate(text):

        if c.isspace() and not include_whitespace:
            continue

        code = ord(c)

        # Unicode hangul range.
        if 0xAC00 <= code <= 0xD7A3:

            chosung_code = chosungs[(code - 0xAC00) // (28 * 21)]
            joongsung_code = joongsungs[(code - 0xAC00) % (28 * 21) // 28]
            jongsung_code = jongsungs[(code - 0xAC00) % (28 * 21) % 28]

            # Add position markers.
            if include_position:
                chosung_code += "/o"
                joongsung_code += "/n"
                if jongsung_code:
                    jongsung_code += "/c"

            disassembled = [chosung_code, joongsung_code]
            if jongsung_code:
                disassembled.append(jongsung_code)

        else:
            position_marker = "w" if c.isspace() else "x"
            disassembled = [f"{c}/{position_marker}" if include_position else c]

        for item in disassembled:
            if out_type == list:
                out.append(item)
                recovery_map.append(i)
            else:
                out += item
                recovery_map.extend([i] * len(item))

    return out, recovery_map


def assemble(jamo_list):
    """
    Reassemble Korean consonants and vowels into text.

    Args:
        jamo_list (list): Input jamo list to reassemble.

    Returns:
         str: Reconstructed string.
        list: List that maps each index of original deconstructed text 
              to its constructed string index.
    """

    assembler = Assembler()
    return "".join(assembler.assemble(jamo_list))
