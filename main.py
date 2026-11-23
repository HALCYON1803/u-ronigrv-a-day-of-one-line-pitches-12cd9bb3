import os

os.makedirs("/output", exist_ok=True)

LINE = "I typed one line. The AI shipped the app — free."

open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
