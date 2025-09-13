import hashlib, random
from PIL import Image, ImageDraw, PngImagePlugin

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
        x0, x1 = sorted([x0, x1])
        y0, y1 = sorted([y0, y1])
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

def save_art(img, filename: str, text: str, algo="sha256"):
    """Save art with embedded metadata in PNG."""
    meta = PngImagePlugin.PngInfo()
    meta.add_text("InputText", text)
    meta.add_text("Algorithm", algo)
    img.save(filename, pnginfo=meta)

def extract_metadata(filename: str) -> dict:
    """Extract metadata from PNG file."""
    with Image.open(filename) as img:
        return img.info
