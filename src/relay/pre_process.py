import os
import re

# ディレクトリと出力ファイルのパスを指定
directory_path = "./"  # 'your_directory'は対象のディレクトリ名に置き換えてください
output_file_path = "./dataset.txt"


# 前処理関数
def preprocess_text(text):
    # 1行目のタイトルを削除
    lines = text.split("\n")[1:]
    # 不要な記号を削除し、漢字、ひらがな、カタカナのみを保持
    processed_lines = []
    for line in lines:
        if line.strip() and not line.startswith(
            "************************************************"
        ):
            # 不要な記号を除去
            line = re.sub(
                r"[^\u3000-\u303f\uff00-\uffef\u4e00-\u9faf\u3040-\u309f\u30a0-\u30ff]",
                "",
                line,
            )
            processed_lines.append(line.strip())

    return "\n".join(processed_lines)


# 出力ファイルを開き、書き込みモードで準備
with open(output_file_path, "w", encoding="utf-8") as output_file:
    # 指定されたディレクトリ内のすべてのtxtファイルを処理
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            # ファイルパスの構築
            file_path = os.path.join(directory_path, filename)
            # ファイルの読み込み
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                # テキストの前処理
                processed_text = preprocess_text(text)
                # 処理済みテキストの出力ファイルへの書き込み
                output_file.write(processed_text + "\n\n")  # ファイル間に空行を挿入

# 出力ファイルのパスを表示（確認用）
print(f"Processed texts have been combined and saved to: {output_file_path}")
