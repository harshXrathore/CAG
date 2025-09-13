# 🔐 CryptoArt (Cryptographic Art Generator)

The Cryptographic Art Generator takes any user input (like a name, email, password, file hash, or random string), applies cryptographic functions, and then transforms the cryptographic output into a unique abstract piece of digital art.The same input always generates the same art (deterministic, like a fingerprint).Different inputs produce completely different art.

It doubles as both a fun visual hash tool and an artistic security concept.
---

## ✨ Features

* 🔑 Hash-based art generation (SHA-256, SHA-512, SHA-1)
* 🎲 Random seed mode for unique abstract art
* 🖼️ Automatic image preview after generation
* 📜 Metadata embedding: Generated images store(Original input text/hash + Algorithm used)
* 🔍 Metadata extraction: Retrieve hidden info from any generated PNG
* 🎨 Interactive CLI with ASCII banner (figlet larry3d) + Rich UI

---

## 📦 Installation

### 1. Clone this repo

```bash
git clone https://github.com/harshXrathore/CryptoArt.git
cd CryptoArt
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Usage


### **Interactive Mode**

Launch the interactive CLI with the **Larry 3D banner**:

```bash
python -m artgen.interactive
```

You’ll see:

```
 ____                           __           ______         __      
/\  _`\                        /\ \__       /\  _  \       /\ \__   
\ \ \/\_\  _ __   __  __  _____\ \ ,_\   ___\ \ \L\ \  _ __\ \ ,_\  
 \ \ \/_/_/\`'__\/\ \/\ \/\ '__`\ \ \/  / __`\ \  __ \/\`'__\ \ \/  
  \ \ \L\ \ \ \/ \ \ \_\ \ \ \L\ \ \ \_/\ \L\ \ \ \/\ \ \ \/ \ \ \_ 
   \ \____/\ \_\  \/`____ \ \ ,__/\ \__\ \____/\ \_\ \_\ \_\  \ \__\
    \/___/  \/_/   `/___/> \ \ \/  \/__/\/___/  \/_/\/_/\/_/   \/__/
                      /\___/\ \_\                                   
                      \/__/  \/_/                                   

Cryptographic Art Generator 🎨🔐

Available algorithms: SHA-256, SHA-512, SHA-1


Choose an option:
1) Generate art from text
2) Generate art from random seed
3) Extract metadata from existing art
4) Exit

Enter your choice [1/2/3/4]: 
```

### CLI (Python)

Generate artwork from text:

```bash
python -m artgen.cli --text "Hello Kali" --out hello.png
```

Generate artwork from a hash:

```bash
python -m artgen.cli --text "5d41402abc4b2a76b9719d911017c592" --out hash.png
```

Custom size:

```bash
python -m artgen.cli --text "Cybersecurity Rocks" --out cyber.png --size 800
```

---

### Web Demo

Run a local server:

```bash
cd web
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser.
Enter text or a file hash → generate art → download PNG.

---

## 🧪 Testing

Run tests with:

```bash
pytest -q
```

---

## 🐳 Docker (optional)

Build and run without installing Python locally:

```bash
docker build -t crypto-art .
docker run --rm -v $(pwd):/data crypto-art --text "Hello Docker" --out /data/art.png
```

---

## 📂 Project Structure

```
cryptographic-art-generator/
│── artgen/          # Python package
│   ├── __init__.py
│   ├── core.py      # Core art generation logic
│   ├── cli.py
│   ├── intractive.py  # intractive CLI interface
│── tests/           # Unit tests
│── web/             # Web demo (HTML + JS)
│── requirements.txt
│── README.md
```

---

## 🌟 Example Output

| Input                   | Output (Preview) |
| ----------------------- | ---------------- |
| `"Alice"`               | 🎨 `alice.png`   |
| `"Hello Kali"`          | 🎨 `hello.png`   |
| SHA-256 of `"password"` | 🎨 `hash.png`    |

*(Each preview will look different depending on the input.)*

---

## 💡 Future Ideas

* Add more cryptographic algorithms (AES, RSA-based seeds)
* Support GIF generation (animated art)
* Export to SVG for vector graphics
* Integrate with a web API for hash visualization online

---

