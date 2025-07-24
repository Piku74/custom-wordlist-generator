# 🔐 Custom Wordlist Generator (Massive Mode)

This Python script generates a **large personalized wordlist** by combining common password elements like names, dates, pet names, hobbies, and more.

⚠️ **For educational and ethical use only. Do not use for unauthorized access.**

---

## ✨ Features

- Combines personal information to create thousands of potential password guesses
- Supports word variation: lowercase, uppercase, and capitalized
- Adds common suffixes (like `123`, `@`, `2024`, etc.)
- Saves the final wordlist to a `.txt` file

---

## 🚀 How It Works

You’ll be prompted to enter:

- Victim’s Name
- Date of Birth (DDMMYYYY)
- Pet Name
- Hobbies (comma-separated)
- Favorite Word or Place

The script then creates combinations using 1 to 4 words and appends/prepends common extras.

---

## 🛠️ Usage

### Step 1: Run the Script

```bash
python3 word_gen3.py
```

### Step 2: Provide Inputs When Prompted

```
Victim's Name: Alice
DOB (DDMMYYYY): 15081999
Pet Name: Simba
Hobbies (comma-separated): reading,travel,music
Favorite word or place: Tokyo
```

### Step 3: Output File

Generated combinations are saved in:

```
massive_wordlist.txt
```

Example output:
```
alicemusic
Tokyo1999
Simba123
reading@Alice
...
```

---

## 📁 File Info

- **File**: `word_gen3.py`
- **Output**: `massive_wordlist.txt`
- **Python Version**: 3.x

---

## ✅ Requirements

No external libraries needed — runs on core Python only.

---

## 🛡️ Disclaimer

This tool is for **cybersecurity awareness and educational purposes only**. Do **NOT** use it to break into accounts, systems, or networks without permission.

---

