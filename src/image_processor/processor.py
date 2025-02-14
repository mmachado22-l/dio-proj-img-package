import numpy as np
from PIL import Image
import cv2

class ImageProcessor:
    def __init__(self):
        self.image = None

    def load_image(self, path):
        """Carrega uma imagem do caminho especificado."""
        self.image = Image.open(path)
        return self.image

    def extract_channel(self, image, channels):
        """
        Extrai canais específicos da imagem.
        channels: lista de canais ('R', 'G', 'B')
        """
        if image is None:
            image = self.image
            
        img_array = np.array(image)
        result = np.zeros_like(img_array)
        
        channel_map = {'R': 0, 'G': 1, 'B': 2}
        
        for channel in channels:
            if channel in channel_map:
                idx = channel_map[channel]
                result[:,:,idx] = img_array[:,:,idx]
        
        return Image.fromarray(result)

    def apply_clahe(self, image=None, clip_limit=2.0, grid_size=(8,8)):
        """
        Aplica CLAHE (Contrast Limited Adaptive Histogram Equalization)
        """
        if image is None:
            image = self.image
            
        # Converter para LAB color space
        img_array = np.array(image)
        lab = cv2.cvtColor(img_array, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        
        # Aplicar CLAHE no canal L
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
        cl = clahe.apply(l)
        
        # Mesclar canais e converter de volta para RGB
        limg = cv2.merge((cl,a,b))
        result = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
        
        return Image.fromarray(result)

    def save_image(self, image, path):
        """Salva a imagem processada em um caminho especificado."""
        image.save(path)