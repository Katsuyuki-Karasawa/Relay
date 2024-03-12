import cutlet

katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False
output = katsu.romaji("カツカレーは美味しい")
print(output)
