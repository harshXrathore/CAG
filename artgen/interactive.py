import os, platform, subprocess, random
import pyfiglet
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from artgen.core import generate_art, save_art, extract_metadata

console = Console()

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
    banner = pyfiglet.figlet_format("CryptoArt", font="larry3d")
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print("[bold yellow]Cryptographic Art Generator 🎨🔐[/bold yellow]\n")
    console.print("[green]Available algorithms: SHA-256, SHA-512, SHA-1[/green]\n")

    while True:
        console.print("\n[bold]Choose an option:[/bold]")
        console.print("1) Generate art from text")
        console.print("2) Generate art from random seed")
        console.print("3) Extract metadata from existing art")
        console.print("4) Exit")

        choice = IntPrompt.ask("\nEnter your choice", choices=["1", "2", "3", "4"])

        if choice == 1:
            text = Prompt.ask("Enter text or hash")
            algo = Prompt.ask("Choose algorithm", default="sha256")
            out_file = Prompt.ask("Output filename", default="art.png")

            img = generate_art(text, algo=algo)
            save_art(img, out_file, text, algo)
            console.print(f"[bold green]✅ Art saved as {out_file}[/bold green]")
            open_image(out_file)

        elif choice == 2:
            seed_text = str(random.randint(100000, 999999))
            algo = "sha256"
            out_file = "random_art.png"

            img = generate_art(seed_text, algo=algo)
            save_art(img, out_file, seed_text, algo)
            console.print(f"[bold green]✨ Random art saved as {out_file}[/bold green]")
            open_image(out_file)

        elif choice == 3:
            filename = Prompt.ask("Enter PNG filename")
            if not os.path.exists(filename):
                console.print("[red]❌ File not found.[/red]")
                continue
            meta = extract_metadata(filename)
            console.print("📜 Metadata extracted:")
            for k, v in meta.items():
                console.print(f"   [cyan]{k}[/cyan]: {v}")

        elif choice == 4:
            console.print("[red]Exiting...[/red]")
            break

if __name__ == "__main__":
    main()
