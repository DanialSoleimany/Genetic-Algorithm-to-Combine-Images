import numpy as np
from PIL import Image

def chromosome(image_path):
    image = Image.open(rf"Images\{image_path}")
    resized_image = image.resize((3000, 3000))
    image_arr = np.array(resized_image)
    green_channel = image_arr[:, :, 1]
    image_flatten = list(green_channel.flatten()) 
    return image_flatten

def population(image_paths):
    flatten_images = []
    for image_path in image_paths:
        image_flatten = chromosome(image_path).copy()
        flatten_images.append(image_flatten)

    return flatten_images

def extract_genome(ch, x_points): 
    extracted_genomes = []
    start = 0
    for x_point in x_points:
        genome = ch[start:x_point]
        extracted_genomes.append(genome)
        start = x_point

    last_genome = ch[start:]
    extracted_genomes.append(last_genome)

    if extracted_genomes[-1] == []:
        extracted_genomes.remove([])

    return extracted_genomes

def cross_over(population, x_points):

    children = []
    for i in range(0, len(population)-1, 2):
        extracted_genomes_1 = extract_genome(population[i], x_points)
        extracted_genomes_2 = extract_genome(population[i + 1], x_points)

        extracted_genomes_1_copy = extracted_genomes_1.copy()
        extracted_genomes_2_copy = extracted_genomes_2.copy()

        for j in range(1, len(extracted_genomes_1_copy), 2):
            extracted_genomes_1_copy[j] = extracted_genomes_2[j]
            extracted_genomes_2_copy[j] = extracted_genomes_1[j]

    children.append(extracted_genomes_1_copy)
    children.append(extracted_genomes_2_copy)

    return children