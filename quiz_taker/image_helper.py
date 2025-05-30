# Helps to find image

from PIL import Image, ImageTk

class ImageHelper:
    @staticmethod
    def load(path, size=None):
        try:
            image = Image.open(path)
            if size:
                image = image.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as error:
            print(f"Image load failed: {error}")
            return None
