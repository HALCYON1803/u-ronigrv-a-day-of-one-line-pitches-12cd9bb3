import os

os.makedirs("/output", exist_ok=True)

LINE = "Tell an AI your app idea — it builds it free on make.fun."

open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
