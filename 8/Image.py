import numpy as np
import cv2

class Image:
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            raise TypeError("Image data must be a NumPy array")
        self.data = data

class BinaryImage(Image):
    def __init__(self, data):
        if not np.all(np.isin(data, [0, 255])):
            raise ValueError("Binary image data must contain only 0 or 255")
        super().__init__(data)

class MonochromeImage(Image):
    def __init__(self, data):
        if not np.all((data >= 0) & (data <= 255)):
            raise ValueError("Monochrome image data must be in range 0-255")
        super().__init__(data)

class ColorImage(Image):
    def __init__(self, data):
        if not data.ndim == 3 or not data.shape[2] == 3:
            raise ValueError("Color image data must be a 3-dimensional array with shape (height, width, 3)")
        if not np.all((data >= 0) & (data <= 255)):
            raise ValueError("Color image data must be in range 0-255")
        super().__init__(data)

class PNGImage(Image):
    def __init__(self, file_path):
        data = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        if data is None:
            raise ValueError("Could not read PNG image")
        super().__init__(data)

class JPEGImage(Image):
    def __init__(self, file_path):
        data = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        if data is None:
            raise ValueError("Could not read JPEG image")
        super().__init__(data)
