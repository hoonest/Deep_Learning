import numpy as np
from PIL import Image

x = np.random.rand(10, 2, 28, 28) * 255


for i in range(10):
    for j in range(2):
        img = x[i][j].reshape(28, 28)
        pil_img = Image.fromarray(np.uint8(img))
        pil_img.show()
        print(x[i])


