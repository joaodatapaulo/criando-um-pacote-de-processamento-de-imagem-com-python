# Plotar a imagem.

import matplotlib.pyplot as plt

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    
    # Corrigindo a lista de nomes.
    names_lst = ['Image {}'.format(i) for i in range(1, number_images + 1)]
    
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')

    # Usando plt.tight_layout() ao invés de fig.tight_layout().
    plt.tight_layout()  
    plt.show()

def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    
    # Usando plt.tight_layout() ao invés de fig.tight_layout().
    plt.tight_layout()
    plt.show()