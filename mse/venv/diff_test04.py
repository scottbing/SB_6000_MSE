# import the necessary packages
#from skimage.measure import structural_similarity as ssim
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
from PixelFunctions import *
import cv2
import os

GENUINE1 = '/tinygenuine-01.jpg'
GENUINE2 = '/tinygenuine-02.jpg'
FORGED = '/tinyforged-01.jpg'


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# end of function lcs

# taken from: https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, imageX, imageY, title):
    # compute the mean squared error and structural similarity
    # index for the images
    print("before mse:")
    m = mse(imageA, imageB)
    print("mse:", m)
    # s = ssim(imageA, imageB)
    # s = ssim(imageA, imageB)
    s = measure.compare_ssim(imageA, imageB)
    print("ssim:", s)
    X = imageX
    Y = imageY
    l = lcs(X, Y)
    print("Length of LCS between " + title + " is ", l)

    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f, LCS: %.2f" % (m, s, l))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    # show the images
    plt.show()


def main():
    # set up for LCS
    author_21 = '021'
    training_folder = os.path.join('data/training/', author_21)
    test_folder = os.path.join('data/test/', author_21)

    print('open is assigned to %r' % open)
    # load image piixels
    with Image.open(training_folder + GENUINE1) as im1:
        imageX = storePixels(im1)
    with Image.open(training_folder + GENUINE2) as im2:
        imageY = storePixels(im2)
    with Image.open(training_folder + FORGED) as im3:
        fd_pixels = storePixels(im3)
        print("stored")


    # load the images -- the original, the original + contrast,
    # and the original + photoshop
    genuine1 = cv2.imread("data/training/021/tinygenuine-01.png")
    genuine2 = cv2.imread("data/training/021/tinygenuine-02.png")
    forged = cv2.imread("data/training/021/tinyforged-01.png")

    # convert the images to grayscale
    genuine1 = cv2.cvtColor(genuine1, cv2.COLOR_BGR2GRAY)
    genuine2 = cv2.cvtColor(genuine2, cv2.COLOR_BGR2GRAY)
    forged = cv2.cvtColor(forged, cv2.COLOR_BGR2GRAY)

    # initialize the figure
    fig = plt.figure("Images")
    images = ("Genuine1", genuine1), ("Genuine2", genuine2), ("Forged", forged)
    # loop over the images
    for (i, (name, image)) in enumerate(images):
        # show the image
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap=plt.cm.gray)
        plt.axis("off")
    # show the figure
    plt.show()

    # compare the images
    print("begin compare_image")
    compare_images(genuine1, genuine1, imageX, imageY, "Genuine vs. Genuine")
    compare_images(genuine1, forged, imageX, fd_pixels, "Genuine vs. Forged")
    compare_images(genuine2, forged, imageY, fd_pixels, "Genuine vs. Forged")


if __name__ == '__main__':
    main()