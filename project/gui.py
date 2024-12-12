import tkinter as tk
from tkinter import filedialog, messagebox
from image_augmenter import ImageAugmenter


class ImageAugmenterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Augmenter")

        # Входные и выходные директории
        self.input_dir = ""
        self.output_dir = ""

        # Создание элементов интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Метка для входной директории
        self.input_label = tk.Label(self.root, text="Input Directory:")
        self.input_label.pack(pady=5)

        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack(pady=5)

        self.browse_input_button = tk.Button(self.root, text="Browse", command=self.browse_input)
        self.browse_input_button.pack(pady=5)

        # Метка для выходной директории
        self.output_label = tk.Label(self.root, text="Output Directory:")
        self.output_label.pack(pady=5)

        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.pack(pady=5)

        self.browse_output_button = tk.Button(self.root, text="Browse", command=self.browse_output)
        self.browse_output_button.pack(pady=5)

        # Поле для уровня шума
        self.noise_label = tk.Label(self.root, text="Noise Level (0-255):")
        self.noise_label.pack(pady=5)

        self.noise_entry = tk.Entry(self.root)
        self.noise_entry.pack(pady=5)

        # Поле для количества изображений
        self.num_images_label = tk.Label(self.root, text="Number of Augmented Images:")
        self.num_images_label.pack(pady=5)

        self.num_images_entry = tk.Entry(self.root)
        self.num_images_entry.pack(pady=5)

        # Кнопка для запуска аугментации
        self.augment_button = tk.Button(self.root, text="Augment Images", command=self.augment_images)
        self.augment_button.pack(pady=20)

    def browse_input(self):
        self.input_dir = filedialog.askdirectory()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.input_dir)

    def browse_output(self):
        self.output_dir = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_dir)

    def augment_images(self):
        try:
            noise_level = int(self.noise_entry.get())
            num_images = int(self.num_images_entry.get())

            if not (0 <= noise_level <= 255):
                raise ValueError("Noise level must be between 0 and 255.")

            if num_images <= 0:
                raise ValueError("Number of images must be greater than 0.")

            # Создание экземпляра ImageAugmenter и запуск аугментации
            augmenter = ImageAugmenter(self.input_dir, self.output_dir)
            augmenter.augment_images(noise_level, num_images)

            messagebox.showinfo("Success", "Image augmentation completed successfully!")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageAugmenterGUI(root)
    root.mainloop()
