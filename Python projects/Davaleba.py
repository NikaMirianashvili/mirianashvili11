import sys
from PIL import Image, ImageOps
from os.path import splitext

allowed_extensions = ['.jpg', '.jpeg', '.png']
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    extension1 = splitext(sys.argv[1])[1].lower()
    extension2 = splitext(sys.argv[2])[1].lower()
if extension1 not in allowed_extensions and extension2 not in allowed_extensions:
    sys.exit('Invalid extension')
if extension1 == extension2:
    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])
        size = shirt.size
        photo = ImageOps.fit(photo, size, bleed=0.0, centering=(0.5,0.5))
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")
else:
    sys.exit("Input and output have different extensions ")

