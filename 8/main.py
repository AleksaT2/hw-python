import cv2
import numpy as np
from Image import PNGImage, JPEGImage, MonochromeImage, ColorImage
from BaseImageProcessor import MonochromeImageProcessor, ColorImageProcessor
from ImageFactory import ImageFactory
from ImageConverter import ImageConverter
from Image import ColorImage, BinaryImage, MonochromeImage

def main():

    binary_data = np.array([[0, 255], [255, 0]], dtype=np.uint8)
    monochrome_data = cv2.imread('./mono.jpg', cv2.IMREAD_GRAYSCALE)
    color_data = cv2.imread("cat.jpg")

    binary_image = BinaryImage(binary_data)
    monochrome_image = MonochromeImage(monochrome_data)
    color_image = ColorImage(color_data)

    if isinstance(color_image, ColorImage):
        color_processor = ColorImageProcessor()
        processed_image = color_processor.process(color_image)
        cv2.imshow('',  processed_image.data)
    elif isinstance(color_image, MonochromeImage):
        monochrome_processor = MonochromeImageProcessor()
        processed_image = monochrome_processor.process(color_image)
        cv2.imshow( '', processed_image.data)



if __name__ == "__main__":
    main()
