import os

from app import clean_up_image, image_to_text


if __name__ == "__main__":
    # image = input("Type image source: ")
    image = "tmp/input/example_02.png"
    filename = clean_up_image(image, True)

    text = image_to_text(filename)
    os.remove(filename) # deleting the temporary file
    print(text)
