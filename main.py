f = open("kanji.txt", encoding="utf-8")
kanji_list = f.readline()
f.close()
for i in kanji_list:
    for j in kanji_list:
        print("{}{}".format(i, j))
