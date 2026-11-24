"""The Dog Ate My Homework: Funniest Excuse.

The dog explains, in its own voice, why the homework got eaten:
it was protecting its human from question four.
"""

LINE = "I ate it to protect you from question four. You're welcome."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
