def compute_hu_moments(func):
    def wrapper(image):
        moments = func(image)
        hu_moments = cv2.HuMoments(cv2.moments(image.data)).flatten()
        return moments, hu_moments
    return wrapper

class ImageDecorator:
    @compute_hu_moments
    def process_image(self, image):
        # Обработка изображения (используя процессор для монохромного или цветного изображения)
        return image
