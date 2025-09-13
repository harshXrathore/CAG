import hashlib, random, math
from PIL import Image, ImageDraw
from PIL import PngImagePlugin, Image

def text_to_hash(text: str, algo="sha256") -> str:
    h = hashlib.new(algo)
    h.update(text.encode("utf-8"))
    return h.hexdigest()

def generate_art(text: str, size: int = 512, algo="sha256") -> Image.Image:
    hexhash = text_to_hash(text, algo)
    seed = int(hexhash[:16], 16)
    random.seed(seed)

    # Transparent background for layering
    img = Image.new("RGBA", (size, size), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img, "RGBA")

    center = size // 2
    num_shapes = 80

def save_art(img: Image.Image, filename: str, text: str, algo="sha256"):
    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("InputText", text)
    metadata.add_text("Algorithm", algo)
    img.save(filename, "PNG", pnginfo=metadata)

def extract_metadata(filename: str):
    img = Image.open(filename)
    info = img.info
    return {
        "InputText": info.get("InputText", None),
        "Algorithm": info.get("Algorithm", None)
    }

    for _ in range(num_shapes):
        # Position relative to center
        x0, y0 = random.randint(0, center), random.randint(0, center)
        w, h = random.randint(10, 150), random.randint(10, 150)
        x1, y1 = x0 + w, y0 + h

        # Random color with transparency
        color = (
            random.randint(50, 255),   # R
            random.randint(50, 255),   # G
            random.randint(50, 255),   # B
            random.randint(80, 200)    # Alpha
        )

        # Choose shape type
        shape_type = random.choice(["ellipse", "rectangle", "polygon", "arc"])

        if shape_type == "ellipse":
            draw.ellipse([x0, y0, x1, y1], fill=color)

        elif shape_type == "rectangle":
            draw.rectangle([x0, y0, x1, y1], fill=color)

        elif shape_type == "polygon":
            points = [(random.randint(0, center), random.randint(0, center)) for _ in range(random.randint(3, 6))]
            draw.polygon(points, fill=color)

        elif shape_type == "arc":
            start = random.randint(0, 360)
            end = start + random.randint(30, 180)
            draw.arc([x0, y0, x1, y1], start=start, end=end, fill=color, width=random.randint(2, 6))

        # Mirror across X and Y axis for symmetry
        mirrored_shapes = [
            (x0, y0, x1, y1),  # original
            (size - x1, y0, size - x0, y1),
            (x0, size - y1, x1, size - y0),
            (size - x1, size - y1, size - x0, size - y0),
        ]

        for coords in mirrored_shapes:
            if shape_type == "ellipse":
                draw.ellipse(coords, fill=color)
            elif shape_type == "rectangle":
                draw.rectangle(coords, fill=color)
            elif shape_type == "polygon":
                # Shift polygon points instead
                points = [(size - px, py) for px, py in points]
                draw.polygon(points, fill=color)
            elif shape_type == "arc":
                start = random.randint(0, 360)
                end = start + random.randint(30, 180)
                draw.arc(coords, start=start, end=end, fill=color, width=random.randint(2, 6))

    return img.convert("RGB")  # Final clean output
