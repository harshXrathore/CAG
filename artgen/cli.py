import argparse
from .core import generate_art

def main():
    parser = argparse.ArgumentParser(description="Cryptographic Art Generator CLI")
    parser.add_argument("--text", required=True, help="Input text or hash")
    parser.add_argument("--out", default="output.png", help="Output PNG file")
    args = parser.parse_args()

    img = generate_art(args.text)
    img.save(args.out)
    print(f"Saved art to {args.out}")

if __name__ == "__main__":
    main()
