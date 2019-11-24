import cv2
import os


def view_image(image, name_of_window):
    """
    This function can show the image via OpenCV
    """
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(1000) # show image for 1 second
    cv2.destroyAllWindows()


def clean_up_image(image, view_steps = False):
    """
    This function will clean up background of the image via OpenCV
    """
    preprocesses = ["thresh", "blur"]

    # convert image to shades of gray
    input_image = cv2.imread(image) # load image as BGR, not RGB
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 
    if view_steps:
        view_image(gray_image, "Gray image")

    # applying image preprocessing
    for preprocess in preprocesses:
        # threshold is conversion into black and white colors (no shades of gray)
        if preprocess == "thresh":
            # gray_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            #    cv2.THRESH_BINARY, 11, 2)
            gray_image = cv2.threshold(gray_image, 0, 255,
                cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # median blur to remove noise
        elif preprocess == "blur":
            gray_image = cv2.medianBlur(gray_image, 3)
    if view_steps:
        view_image(gray_image, "Preprocess image")

    # save the temporary picture with preprocess so that you can apply OCR to it
    filename = "tmp/output/{}.png".format(os.getpid())
    cv2.imwrite(filename, gray_image)
    return filename

