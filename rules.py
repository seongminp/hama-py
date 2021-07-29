cons = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

change = {}
change["ㄲ"] = "ㄱ"
change["ㅋ"] = "ㄱ"
change["ㅅ"] = "ㄷ"
change["ㅆ"]= "ㄷ"
change["ㅈ"]= "ㄷ"
change["ㅊ"]= "ㄷ"
change["ㅌ"]= "ㄷ"
change['ㅍ'] = "ㅂ"
print('9')
for c in ['ㄲ','ㅋ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ', 'ㅍ']:
    for cc in cons:
        #print(f"- {c}/c + {cc}/o -> {change[c]}/c + {cc}/o")
        pass

change = {}
change["ㄳ"] = "ㄱ"
change["ㄵ"] = "ㄴ"
change["ㄼ"] = "ㄹ"
change["ㄽ"]= "ㄹ"
change["ㄾ"]= "ㄹ"
change["ㅄ"]= "ㅂ"
print('10')
for c in ['ㄳ','ㄵ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㅄ']:
    for cc in cons:
        #print(f"- {c}/c + {cc}/o -> {change[c]}/c + {cc}/o")
        pass

print('10 다만')
for cc in cons:
    #print(f"- ㅂ/o + ㅏ/n + ㄼ/c + {cc}/o -> ㅂ/o + ㅏ/n + ㄼ/c + {cc}/o")
    pass
for cc in cons:
    #print(f"- ㄴ/o + ㅓ/n + ㄼ/c + {cc}/o -> ㄴ/o + ㅓ/n + ㅂ/c + {cc}/o")
    pass

print('11')
change = {}
change["ㄺ"] = "ㄱ"
change["ㄻ"] = "ㅁ"
change["ㄿ"] = "ㅂ"
for c in ['ㄺ','ㄻ', 'ㄿ']:
    for cc in cons:
        print(f"- {c}/c + {cc}/o -> {change[c]}/c + {cc}/o")
        pass



