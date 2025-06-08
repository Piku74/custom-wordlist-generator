import itertools

def get_input():
    print("=== Custom Wordlist Generator (Massive Mode) ===")
    name = input("Victim's Name: ").strip()
    dob = input("DOB (DDMMYYYY): ").strip()
    pet = input("Pet Name: ").strip()
    hobbies = input("Hobbies (comma-separated): ").strip().split(',')
    fav = input("Favorite word or place: ").strip()

    year = dob[-4:] if len(dob) == 8 else ''
    short_dob = dob[:4]
    extras = ['123', '@', '!', '#', '00', '01', '1234', '2023', '2024', year, short_dob]

    words = [name, dob, pet, fav] + hobbies
    words = [w.strip() for w in words if w.strip()]
    return words, extras

def all_variants(word):
    return [word.lower(), word.upper(), word.capitalize()]

def generate_big_wordlist(words, extras, max_words=4):
    base_words = []
    for word in words:
        base_words.extend(all_variants(word))

    wordlist = set()

    for r in range(1, max_words + 1):
        for combo in itertools.product(base_words, repeat=r):
            base = ''.join(combo)
            if 6 <= len(base) <= 20:
                wordlist.add(base)
                for ext in extras:
                    wordlist.add(base + ext)
                    wordlist.add(ext + base)

    return wordlist

def save_to_file(wordlist, filename="massive_wordlist.txt"):
    with open(filename, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")
    print(f"[+] Saved {len(wordlist)} words to {filename}")

if __name__ == "__main__":
    words, extras = get_input()
    wordlist = generate_big_wordlist(words, extras)
    save_to_file(wordlist)

