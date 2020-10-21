# import the necessary packages
#from skimage.measure import structural_similarity as ssim
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2

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


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    print("before mse:")
    m = mse(imageA, imageB)
    print("mse:", m)
    # s = ssim(imageA, imageB)
    # s = ssim(imageA, imageB)
    s = measure.compare_ssim(imageA, imageB)
    print("ssim:", s)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
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
    # load the images -- the original, the original + contrast,
    # and the original + photoshop
    original = cv2.imread("data/training/021/tinygenuine-01.png")
    contrast = cv2.imread("data/training/021/tinygenuine-02.png")
    shopped = cv2.imread("data/training/021/tinyforged-01.png")

    # convert the images to grayscale
    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
    shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

    # # initialize the figure
    # fig = plt.figure("Images")
    # images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)
    # loop over the images
    # for (i, (name, image)) in enumerate(images):
    #     # show the image
    #     ax = fig.add_subplot(1, 3, i + 1)
    #     ax.set_title(name)
    #     plt.imshow(image, cmap=plt.cm.gray)
    #     plt.axis("off")
    # # show the figure
    # plt.show()

    # compare the images
    print("begin compare_image")
    compare_images(original, original, "Original vs. Original")
    compare_images(original, contrast, "Original vs. Contrast")
    compare_images(original, shopped, "Original vs. Photoshopped")


if __name__ == '__main__':
    main()