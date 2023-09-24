from PIL import Image

def resize_keep_aspect_ratio(img, size):
    img.thumbnail(size, Image.Resampling.LANCZOS)
    background = Image.new('RGB', size, (0, 0, 0, 0))
    background.paste(img, (int(
        (size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
    return background
