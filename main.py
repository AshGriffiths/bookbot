def count_words(input: str) -> int:
    return len(input.split())


def count_chars(input: str) -> dict[str, int]:
    characters: dict[str, int] = {}
    input_lower = input.lower()
    for char in input_lower:
        if not char.isalpha():
            continue
        if characters.get(char):
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


filename: str = "books/frankenstein.txt"
with open(filename) as f:
    contents = f.read()
    print(f"--- Begin report of {filename} ---")
    print(f"{count_words(contents)} words found in this document")
    characters = count_chars(contents)
    sorted_keys: list[str] = sorted(
        characters, key=lambda char: characters[char], reverse=True
    )
    for char in sorted_keys:
        print(f"The '{char}' character was found {characters[char]} times")
