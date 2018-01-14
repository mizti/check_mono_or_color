import numpy as np
import sys
from PIL import Image
from PIL import ImageFilter
import math

def get_image(filename):
    image = Image.open(filename)
    image_array = np.asarray(image).astype('float32')
    return image_array

# Check if designated file is monochrome or Colored
def is_colored(filename):
    print(filename)
    image_array = get_image(filename)
    r = image_array[:,:,0].flatten()
    g = image_array[:,:,1].flatten()
    b = image_array[:,:,2].flatten()
    if (np.corrcoef(r, g)[0,1] + np.corrcoef(r, b)[0,1] + np.corrcoef(b, g)[0,1])/ 3 > 0.96:
        return False
    else:
        return True

if __name__ == '__main__':
    print("colored")
    print(is_colored('pixiv_images/52777396_p0_master1200.jpg')) # colored
    print(is_colored('pixiv_images/3480160_p0_master1200.jpg')) # colored
    print(is_colored('pixiv_images/62147471_p0_master1200.jpg')) # colored
    print(is_colored('pixiv_images/28650926_p0_master1200.jpg')) # colored
    print(is_colored('pixiv_images/17542722_p0_master1200.jpg')) # colored
    print(is_colored('pixiv_images/59306857_p0.png')) # colored
    print("=================")
    print("monochrome")
    print(is_colored('pixiv_images/21179926_p0_master1200.jpg')) # monochrome
    print(is_colored('pixiv_images/49621944_p0_master1200.jpg')) # monochrome + alpha
    print(is_colored('pixiv_images/13741154_p0_master1200.jpg')) # monochrome + alpha
    print("=================")
    print("monocolor")
    print(is_colored('pixiv_images/39364160_p0_master1200.jpg')) # mono color
    print(is_colored('pixiv_images/37761583_p0_master1200.jpg')) # mono color
    print(is_colored('pixiv_images/21726531_p0_master1200.jpg')) # mono color
