import os
import numpy as np
from PIL import Image, ImageFilter, ImageOps

class ImageAugmenter:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

        # Проверка существования входной директории
        if not os.path.exists(input_dir):
            raise ValueError(f"Ошибка: Входная директория не существует: {input_dir}")

    def add_noise(self, image, noise_level=25):
        # Преобразование изображения в массив NumPy
        image_array = np.array(image)
        noise = np.random.normal(0, noise_level, image_array.shape).astype(np.uint8)
        noisy_image = Image.fromarray(np.clip(image_array + noise, 0, 255).astype(np.uint8))
        return noisy_image

    def remove_noise(self, noisy_image):
        # Применение медианного фильтра для удаления шума
        return noisy_image.filter(ImageFilter.MedianFilter(size=5))

    def histogram_equalization(self, image):
        # Эквализация гистограммы
        return ImageOps.equalize(image)

    def rotate_image(self, image, angle):
        # Поворот изображения на заданный угол
        return image.rotate(angle)

    def flip_image(self, image, flip_code):
        # Отражение изображения
        if flip_code == 0:  # Вертикальное отражение
            return image.transpose(Image.FLIP_TOP_BOTTOM)
        elif flip_code == 1:  # Горизонтальное отражение
            return image.transpose(Image.FLIP_LEFT_RIGHT)
        return image

    def scale_image(self, image, scale_factor):
        # Масштабирование изображения
        new_size = (int(image.width * scale_factor), int(image.height * scale_factor))
        return image.resize(new_size, Image.LANCZOS)  # Использование LANCZOS для высокого качества

    def save_image(self, image, filename):
        image.save(os.path.join(self.output_dir, filename))

    def augment_images(self, noise_level, num_images):
        for filename in os.listdir(self.input_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Поддержка нескольких форматов
                # Загрузка изображения в градациях серого
                image_path = os.path.join(self.input_dir, filename)
                image = Image.open(image_path).convert('L')

                # Проверка на успешную загрузку изображения
                if image is None:
                    print(f"Ошибка: Не удалось загрузить изображение {image_path}")
                    continue

                # Загрузка цветного изображения для цветокоррекции
                color_image = Image.open(image_path)  # Для цветокоррекции
                if color_image is None:
                    print(f"Ошибка: Не удалось загрузить цветное изображение {image_path}")
                    continue

                for i in range(num_images):
                    # Добавление шума
                    noisy_image = self.add_noise(image, noise_level)
                    self.save_image(noisy_image, f'noisy_{i}_{filename}')

                    # Удаление шума
                    denoised_image = self.remove_noise(noisy_image)
                    self.save_image(denoised_image, f'denoised_{i}_{filename}')

                    # Эквализация гистограммы
                    equalized_image = self.histogram_equalization(denoised_image)
                    self.save_image(equalized_image, f'equalized_{i}_{filename}')

                    # Геометрические преобразования
                    rotated_image = self.rotate_image(color_image, 45)  # Поворот на 45 градусов
                    self.save_image(rotated_image, f'rotated_{i}_{filename}')

                    flipped_image = self.flip_image(color_image, 1)  # Отражение по горизонтали
                    self.save_image(flipped_image, f'flipped_{i}_{filename}')

                    scaled_image = self.scale_image(color_image, 1.5)  # Масштабирование на 1.5
                    self.save_image(scaled_image, f'scaled_{i}_{filename}')