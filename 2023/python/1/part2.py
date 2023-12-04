import re

lines = open("input.txt", "r").readlines()

translations = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9"
}
translations_reverse = {k[::-1]: v for k, v in translations.items()}

pattern = re.compile(r"|".join(translations.keys()))
pattern_reverse = re.compile(r"|".join(translations_reverse.keys()))

num = 0

for line in lines:
    translation = lambda x: translations[x.group()]
    first = pattern.sub(translation, line, 1)

    translation_reverse = lambda x: translations_reverse[x.group()]
    last = pattern_reverse.sub(translation_reverse, line[::-1], 1)
    num += int(re.search(r"\d", first).group() \
        + re.search(r"\d", last).group())
print(num)