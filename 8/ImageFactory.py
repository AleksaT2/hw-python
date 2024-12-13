from Image import PNGImage, JPEGImage  # Предполагается, что эти классы определены
class ImageFactory:
    @staticmethod
    def create_image(file_path):
        if file_path.endswith('.png'):
            return PNGImage(file_path)
        elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
            return JPEGImage(file_path)
        else:
            raise ValueError("Unsupported image format")
