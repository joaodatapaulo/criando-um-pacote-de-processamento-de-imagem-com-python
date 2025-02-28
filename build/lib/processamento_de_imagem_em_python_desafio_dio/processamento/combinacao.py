# Tratar e fazer combinações com mais de uma imagem.

import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."

    # Converte as imagens para escala de cinza.
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)

    #Calcula a similaridade estrutural
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images:", score)

    # Normaliza a imagem de diferença.
    normalized_difference_image = (difference_image - np.min(difference_image))/(np.max(difference_image) - np.min(difference_image))

    # Converte para um formato adequado para exibição
    normalized_difference_image = (normalized_difference_image * 255).astype(np.uint8)
    return normalized_difference_image

def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2)
    return matched_image