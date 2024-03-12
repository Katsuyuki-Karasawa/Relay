import cutlet

katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

input_file_path = "dataset.txt"
output_file_path = "alphabet.txt"

with open(input_file_path, "r", encoding="utf-8") as input_file:
    text = input_file.read()

converted_text = katsu.romaji(text)

with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(converted_text)

print("処理終了")
