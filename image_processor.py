from PIL import Image

from decorators import log_errors
from utils import cpp_map

@log_errors
def compress_image(image, quality, format):
    im = Image.open(image)

    if format in ['.jpeg', '.jpg']:
        im.save(f'compressed_{image}', format="JPEG", optimize=True ,quality=int(cpp_map(1, 100, 1, 60, quality)))
    else:
        im = im.convert('P', palette=Image.Palette.ADAPTIVE, colors=int(cpp_map(1, 100, 64, 256, quality)))
        im.save(f'compressed_{image}', format=format[1:].lower(), optimize=True, use_adaptive_filter=True)

    im.close()