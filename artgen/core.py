import hashlib, random
from PIL import Image, ImageDraw

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
    for _ in range(50):
        x0, y0 = random.randint(0, size), random.randint(0, size)
        x1, y1 = random.randint(0, size), random.randint(0, size)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        draw.ellipse([x0, y0, x1, y1], fill=color)
    return img
