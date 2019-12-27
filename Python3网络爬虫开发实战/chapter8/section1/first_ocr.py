import tesserocr
from PIL import Image

image = Image.open('../data/1.jpg')
image = image.convert('L')
threshold = 80
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image.point(table, '1')
image.show()
result = tesserocr.image_to_text(image)
print(result)
