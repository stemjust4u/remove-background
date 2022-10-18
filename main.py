from rembg import remove
from PIL import Image

withoutBG = remove(Image.open('pics/test.JPG'))
withoutBG.save('pics/test_output.png')