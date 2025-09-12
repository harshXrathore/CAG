# 🔐 CAG (Cryptographic Art Generator)

The Cryptographic Art Generator takes any user input (like a name, email, password, file hash, or random string), applies cryptographic functions, and then transforms the cryptographic output into a unique abstract piece of digital art.The same input always generates the same art (deterministic, like a fingerprint).Different inputs produce completely different art.

It doubles as both a fun visual hash tool and an artistic security concept.
---

## ✨ Features

* 🔑 Deterministic: same input → same output
* 🎨 Multiple shape types (ellipses, rectangles, polygons, lines, arcs)
* 🖼 Save generated artwork as PNG
* 🌐 Web demo (p5.js + Web Crypto API)
* 🐍 Python CLI for local use
* 🔒 Cryptography-inspired — makes a great hash visualizer for security enthusiasts

---

## 📦 Installation

### 1. Clone this repo

```bash
git clone https://github.com/harshXrathore/CAG.git
cd CAG
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
│   ├── cli.py       # CLI interface
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

