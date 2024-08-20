# Combining Images Using Genetic Algorithms
*Overview*
This project utilizes a genetic algorithm (GA) to creatively merge two distinct images into one, blending details from both source images in a single output. The approach is inspired by biological processes, mimicking the way organisms evolve over time.

**Process Details**
*Initial Population*
- The genetic algorithm starts with two input images.
- Each image is resized to 3000x3000 pixels to enhance the resolution and detail in the final combined images.
*Crossover Mechanism*
- The GA employs an n-point crossover technique:
- Each image is flattened into a one-dimensional chromosome.
- During the crossover, specific segments of these chromosomes (representing sections of the image) are exchanged between the two parent images at predefined crossover points.
- After the crossover, the chromosomes are reshaped back into their original 2D form, resulting in new images that combine features from both parents.
*Mutation and Fitness*
- Mutation is intentionally excluded to avoid random changes that could significantly distort the images.
- A fitness function is not utilized, as the goal is purely to explore the combinatorial potential of the images without optimizing for any particular trait.
