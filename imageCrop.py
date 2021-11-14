from PIL import Image
import sys
import glob
from PIL import ImageOps
import numpy as np

# python imageCrop.py folder padding
# python imageCrop.py example 0

def main():
    try:
        folderName = sys.argv[1]
        padding = int(sys.argv[2])
        padding = np.asarray([-1*padding, -1*padding, padding, padding])
    except:
        raise

    filePath = glob.glob(folderName + "/*.png")

    for singleFilePath in filePath:
        try:
            image = Image.open(singleFilePath)
            image.load()
            imageSize = image.size

            invert_im = image.convert("RGB")
            invert_im = ImageOps.invert(invert_im)
            imageBox = invert_im.getbbox()
            imageBox = tuple(np.asarray(imageBox)+padding)

            cropped = image.crop(imageBox)
            print(singleFilePath)
            cropped.save(singleFilePath)
        except:
            print("FAILED: " + singleFilePath)
            pass

if __name__ == '__main__':
    main()