from croatian.characterMappings import CHARACTER_MAPPINGS, BANNED_CHARACTERS
import enchant

with open('rijecnik.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

newLines = []
for line in lines:
    line = line.lower()
    line = line.translate(line.maketrans(CHARACTER_MAPPINGS))
    newLines.append(line)
lines = newLines
# with open('noviRijecnik.txt', 'w', encoding="utf8") as file:
#     for line in newLines:
#         file.write(line)

words = []
for line in lines:
    lineWords = line.split(" ")
    word = lineWords[0]
    if len(word) >= 2 and not any(char.isdigit() or char in BANNED_CHARACTERS for char in word):
        words.append((word, lineWords[1:]))
words.sort()

wordsDir = {}
pokazivac = words[0][0][:3]
wordsDir[pokazivac] = [0, 0]
for i, (word, _) in enumerate(words):
    trenutni = word[:3]
    if trenutni != pokazivac:
        pokazivac = trenutni
        wordsDir[pokazivac] = [i, i]
    wordsDir[pokazivac][1] = i

edges = []

print()
for i, (word1, definicija) in enumerate(words):
    if i % 100 == 0:
        print("\r", i, "/", len(words), end="")
    # if i % 1000 == 999:
    #     break
    for word2 in definicija:
        if any(char.isdigit() or char in BANNED_CHARACTERS for char in word2):
            continue
        trenutni = word2[:3]
        if trenutni in wordsDir:
            l = wordsDir[trenutni][0]
            d = wordsDir[trenutni][1]
            _, j = min([
                (enchant.utils.levenshtein(word2, words[k][0]), k)
                for k in range(l, d + 1)
            ])
            edges.append((i, j))
print()

print("Saving files")
with open('index.txt', 'w', encoding="utf8") as file:
    for word, _ in words:
        file.write(word + "\n")
with open('dico.txt', 'w', encoding="utf8") as file:
    for edge in edges:
        file.write(str(edge[0] + 1) + " " + str(edge[1] + 1) + "\n")
