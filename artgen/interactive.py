import hashlib, random, os, platform, subprocess
from PIL import Image, ImageDraw
import pyfiglet
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from artgen.core import generate_art, save_art, extract_metadata

console = Console()

def text_to_hash(text: str, algo="sha256") -> str:
    h = hashlib.new(algo)
    h.update(text.encode("utf-8"))
    return h.hexdigest()

def generate_art(text: str, size: int = 512, algo="sha256") -> Image.Image:
    hexhash = text_to_hash(text, algo)
    seed = int(hexhash[:16], 16)
    random.seed(seed)

    img = Image.new("RGB", (size, size), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    for _ in range(100):
        x0, y0 = random.randint(0, size), random.randint(0, size)
        x1, y1 = random.randint(0, size), random.randint(0, size)
        x0, x1 = sorted([x0, x1])  # ensures x1 >= x0
        y0, y1 = sorted([y0, y1])  # ensures y1 >= y0
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        if random.random() < 0.5:
            draw.ellipse([x0, y0, x1, y1], fill=color)
        else:
            draw.rectangle([x0, y0, x1, y1], fill=color)

    return img

def open_image(filepath: str):
    """Open an image file with the default system viewer."""
    try:
        if platform.system() == "Windows":
            os.startfile(filepath)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", filepath])
        else:  # Linux & others
            subprocess.run(["xdg-open", filepath])
    except Exception as e:
        console.print(f"[red]Could not open image automatically: {e}[/red]")

def main():
    # Banner
    banner = pyfiglet.figlet_format("CryptoArt", font="slant")
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print("[bold yellow]Cryptographic Art Generator 🎨🔐[/bold yellow]\n")
    console.print("[green]Available algorithms: SHA-256, SHA-512, SHA-1[/green]\n")

    while True:
        console.print("\n[bold]Choose an option:[/bold]")
        console.print("1) Generate art from text")
        console.print("2) Generate art from random seed")
        console.print("3) Exit")

        choice = IntPrompt.ask("\nEnter your choice", choices=["1", "2", "3"])

        if choice == 1:
            text = Prompt.ask("Enter text or hash")
            algo = Prompt.ask("Choose algorithm", default="sha256")
            out_file = Prompt.ask("Output filename", default="art.png")

            img = generate_art(text, algo=algo)
            img.save(out_file)
            console.print(f"[bold green]✅ Art saved as {out_file}[/bold green]")
            open_image(out_file)

        elif choice == 2:
            seed_text = str(random.randint(100000, 999999))
            algo = "sha256"
            out_file = "random_art.png"

            img = generate_art(seed_text, algo=algo)
            img.save(out_file)
            console.print(f"[bold green]✨ Random art saved as {out_file}[/bold green]")
            open_image(out_file)

       elif choice == 3:
            filename = input("Enter PNG filename: ")
            if not os.path.exists(filename):
                print("❌ File not found.")
                continue
            meta = extract_metadata(filename)
            print("📜 Metadata extracted:")
            for k, v in meta.items():
                print(f"   {k}: {v}")

        elif choice == 4:
            console.print("[red]Exiting...[/red]")
            break

if __name__ == "__main__":
    main()
