import os 
import random as rn 
import numpy as np
from PIL import Image
from GA import *

image_dir = "directory of images"
image_paths = os.listdir(image_dir)

flatten_images = population(image_paths)
n_cross_points = 8999998
n_pixels = 3000 * 3000

x_points = rn.sample(range(1, n_pixels-1), n_cross_points)
x_points.sort()


children = cross_over(flatten_images, x_points)

for i in range(len(children)):
    reduced_children = []
    
    for gen in children[i]:
        reduced_children.extend(gen)

    reshaped_child = np.array(reduced_children).reshape(3000, 3000)
    child_image = Image.fromarray(reshaped_child)
    child_image.show()