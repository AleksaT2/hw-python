import numpy as np
from Image import MonochromeImage, ColorImage, BinaryImage

class ImageConverter:
    @staticmethod
    def monochrome_to_monochrome(image: MonochromeImage):
        return image

    @staticmethod
    def color_to_color(image: ColorImage):
        return image

    @staticmethod
    def binary_to_binary(image: BinaryImage):
        return image

    @staticmethod
    def color_to_monochrome(image: ColorImage):
        if not isinstance(image, ColorImage):
            raise TypeError("Input image must be a ColorImage")
        gray_data = np.mean(image.data, axis=2).astype(np.uint8)
        return MonochromeImage(gray_data)

    @staticmethod
    def monochrome_to_color(image: MonochromeImage, palette):
        if not isinstance(image, MonochromeImage):
            raise TypeError("Input image must be a MonochromeImage")
        if not isinstance(palette, np.ndarray):
            raise TypeError("Palette must be a NumPy array")
        if not palette.ndim == 2 or not palette.shape[1] == 3:
            raise ValueError("Palette must be a 2-dimensional array with shape (num_colors, 3)")
        if not np.all((palette >= 0) & (palette <= 255)):
            raise ValueError("Palette values must be in range 0-255")

        color_data = np.zeros((*image.data.shape, 3), dtype=np.uint8)
        for i in range(len(palette)):
            color_data[image.data == i, :] = palette[i]
        return ColorImage(color_data)

    @staticmethod
    def monochrome_to_binary(image: MonochromeImage, threshold=128):
        if not isinstance(image, MonochromeImage):
            raise TypeError("Input image must be a MonochromeImage")
        _, binary_data = cv2.threshold(image.data, threshold, 255, cv2.THRESH_BINARY)
        return BinaryImage(binary_data)

    @staticmethod
    def binary_to_monochrome(image: BinaryImage):
        distance_transform = cv2.distanceTransform(image.data, cv2.DIST_L2, 5)
        distance_transform = (distance_transform / np.max(distance_transform) * 255).astype(np.uint8)
        return MonochromeImage(distance_transform)

    @staticmethod
    def color_to_binary(image: ColorImage, threshold=128):
        monochrome_image = ImageConverter.color_to_monochrome(image)
        return ImageConverter.monochrome_to_binary(monochrome_image, threshold)

    @staticmethod
    def binary_to_color(image: BinaryImage, palette):
        monochrome_image = ImageConverter.binary_to_monochrome(image)
        return ImageConverter.monochrome_to_color(monochrome_image, palette)
