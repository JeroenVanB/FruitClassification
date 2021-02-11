import numpy as np
# import tensorflow as tf
import pathlib

def get_images():
    x = pathlib.Path('.')
    print('path : ', x)
    image_count = len(list(x.glob('*/*.jpg')))
    print(image_count)
    pass


get_images()