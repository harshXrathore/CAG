from artgen.core import text_to_hash, generate_art

def test_hash_determinism():
    assert text_to_hash("hello") == text_to_hash("hello")

def test_art_generation():
    img1 = generate_art("hello")
    img2 = generate_art("hello")
    assert list(img1.getdata()) == list(img2.getdata())
