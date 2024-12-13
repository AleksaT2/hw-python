import cv2
import numpy as np
from Image import MonochromeImage, ColorImage

class BaseImageProcessor:
    def process(self, image):
        self.validate_image(image)
        self.apply_filters(image)
        return image
    def validate_image(self, image):
        raise NotImplementedError("Must implement validate_image")

    def apply_filters(self, image):
        raise NotImplementedError("Must implement apply_filters")

class MonochromeImageProcessor(BaseImageProcessor):
    def validate_image(self, image):
        if not isinstance(image, MonochromeImage):
            raise TypeError("Input must be a MonochromeImage")

    def apply_filters(self, image):
        # Применение фильтра Гаусса
        image.data = cv2.GaussianBlur(image.data, (5, 5), 0)
        # Применение детектора границ Canny
        image.data = cv2.Canny(image.data, 100, 200)

class ColorImageProcessor(BaseImageProcessor):
    def validate_image(self, image):
        if not isinstance(image, ColorImage):
            raise TypeError("Input must be a ColorImage")

    def apply_filters(self, image):
        # Конвертация в градации серого
        gray_image = cv2.cvtColor(image.data, cv2.COLOR_BGR2GRAY)
        distance_transform = cv2.distanceTransform(gray_image, cv2.DIST_L2, 5)

