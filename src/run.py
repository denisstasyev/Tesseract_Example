import os

from app import clean_up_image, image_to_text


if __name__ == "__main__":
    # image = input("Type image source: ")
    # image = "tmp/example_01.png"
    # filename = clean_up_image(image, True)

    # text = image_to_text(filename)
    # os.remove(filename) # deleting the temporary file
    # print(text)

    paths = ["tmp/passport/eng_data/", "tmp/passport/rus_data/", "tmp/bank/"]
    
    for path in paths:
        print("------------------------------------------")

        images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        for image in images:
            print("-------" + path + image + "-------")
            filename = clean_up_image(path + image, True, True)

            text = image_to_text(filename)
            os.remove(filename) # deleting the temporary file
            print(text)
            print("-------" + str(images.index(image) + 1) + "/" + str(len(images)) + "-------")

