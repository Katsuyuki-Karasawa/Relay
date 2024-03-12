import matplotlib.pyplot as plt
from collections import Counter

# 処理後のテキストファイルのパス
file_path = "alphabet.txt"

# ファイルからテキストを読み込み
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

total_characters = len(text.replace("\n", "").replace(" ", ""))

# アルファベットの出現頻度を計算
alphabet_count = Counter(text.replace("\n", "").replace(" ", "").lower())

# アルファベットと出現回数のリストを取得し、アルファベット順にソート
alphabet, counts = zip(*sorted(alphabet_count.items()))

# グラフの作成
plt.figure(figsize=(10, 8))
plt.bar(alphabet, counts)
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.title("Frequency of Alphabet in Converted Text")
plt.savefig("./graph.jpg")

print(f"Total characters (excluding spaces and newlines): {total_characters}")
