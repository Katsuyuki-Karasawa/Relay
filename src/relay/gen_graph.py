import matplotlib.pyplot as plt
from collections import Counter

# 日本語単語リストと英単語リストの例（ローマ字と英単語）
ja_words = ["nihon", "tokyo", "sakura"]  # ローマ字での日本語単語
en_words = ["japan", "tokyo", "cherry"]  # 英単語

# 両方のリストを結合
words = ja_words + en_words

# アルファベットの出現頻度を計算
alphabet_count = Counter("".join(words))

# アルファベットと出現回数のリストを取得し、アルファベット順にソート
alphabet, counts = zip(*sorted(alphabet_count.items()))

# グラフの作成
plt.figure(figsize=(10, 8))
plt.bar(alphabet, counts)
plt.xlabel("Alphabet")
plt.ylabel("Frequency")
plt.title("Frequency of Alphabet in Japanese (Romaji) and English Words")
plt.savefig("./graph.jpg")
