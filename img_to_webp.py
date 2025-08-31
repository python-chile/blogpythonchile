import os
from pathlib import Path
from PIL import Image

# Path raíz de todas las imágenes
IMG_DIR = Path("content/img")
IMG_EXTENSIONS = [".png", ".jpg", ".jpeg"]

def convert_images_to_webp(img_dir: Path):
    if not img_dir.exists():
        print(f"Directorio {img_dir} no existe.")
        return

    # Recorre sub-directorios
    for img_path in img_dir.rglob("*"):
        if img_path.suffix.lower() in IMG_EXTENSIONS:
            webp_path = img_path.with_suffix(".webp")

            try:
                with Image.open(img_path) as img:
                    img.save(webp_path, "webp")
                print(f"Convertido: {img_path} → {webp_path}")

            except Exception as e:
                print(f"⚠️ Error para convertir {img_path}: {e}")

if __name__ == "__main__":
    convert_images_to_webp(IMG_DIR)
