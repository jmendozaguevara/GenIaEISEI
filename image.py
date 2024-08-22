import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
from IPython.display import display


def DisplayFractal(a, fmt='jpeg'):
    a_cyclic = (6.28*a/20.0).reshape(list(a.shape)+[1])
    img = np.concatenate([10+20*np.cos(a_cyclic),
                          30+50*np.sin(a_cyclic),
                          155-80*np.cos(a_cyclic)], 2)
    img[a==a.max()] = 0
    a = img
    a = np.uint8(np.clip(a, 0, 255))
    Image.fromarray(a).show()