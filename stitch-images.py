from imutils import paths
import cv2
import imutils
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True, help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True, help="path to output image")
args=vars(ap.parse_args())

print("[INFO] loading images")
# Load your input images
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)

# Create a Stitcher object
stitcher = cv2.Stitcher.create() if imutils.is_cv3() else cv2.Stitcher_create()

# Stitch the images
result = stitcher.stitch(images)

if result[0] == cv2.Stitcher_OK:
    # Display the result
    stitched_image = result[1]
    cv2.imshow('stitched_image.jpg', stitched_image)
    cv2.imwrite('stitched_image.jpg', stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image stitching failed ({})".format(result))