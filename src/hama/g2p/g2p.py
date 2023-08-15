from hama import char_types

from .korean import Phonemizer as KoreanPhonemizer


class Phonemizer:
    def __init__(self):
        self.korean_phonemizer = KoreanPhonemizer()
        self.english_phonemizer = EnglishPhonemizer()
        self.number_phonemizer = NumberPhonemizer()

    def get_phonemizer(self, char_type):
        if char_type == HANGUL:
            return self.korean_phonemizer
        else:
            raise TypeError(f"Phonemizer type not defined for {ctype}")

    def __call__(self, text):
        prev_chunk_type, prev_chunk_text = None, None
        for chunk_type, start, end in self.chunker.chunk(text):
            chunk_text = text[start:end+1]
            #phonemizer = self.get_phonemizer(chunk_type)
            #phonemes, recovery_map = phonemizer(chunk_text)

            if chunk_type == char_types.HANGUL:
                phonemes, recovery_map = self.korean_phonemizer(chunk_text)
            elif chunk_type == char_types.ENGLISH:
                # Add and shred bos, eos tokens.
                phonemes, recovery_map = self.english_phonemizer('#' + chunk_text + '#')
                phonemes, recovery_map = phonemes[1:-1], recovery_map[1:-1]
            elif chunk_type == char_types.HANJA:
                korean = hanja_to_korean(chunk_text)
                phonemes, recovery_map = self.korean_phonemizer(korean)
            elif chunk_type == char_types.NUMBER:
                # Consider prev and next context.
                phonemes, recovery_map = self.number_phonemizer(chunk_text)
                pass
            else:
                
