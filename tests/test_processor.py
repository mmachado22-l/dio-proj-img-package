import unittest
from image_processor.processor import ImageProcessor
import pytest
from PIL import Image
import numpy as np
import os

# Adicionar função para obter o caminho do arquivo de teste
def get_test_image_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test.jpg')

@pytest.fixture
def processor():
    return ImageProcessor()

@pytest.fixture
def sample_image():
    # Criar uma imagem de teste e salvá-la
    img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    img_pil = Image.fromarray(img)
    test_path = get_test_image_path()
    img_pil.save(test_path)
    return img_pil

def test_extract_channel(processor, sample_image):
    # Testar extração do canal vermelho
    red_channel = processor.extract_channel(sample_image, ['R'])
    assert isinstance(red_channel, Image.Image)
    
    # Verificar se apenas o canal vermelho tem valores
    img_array = np.array(red_channel)
    assert np.all(img_array[:,:,1:] == 0)  # Canais G e B devem ser zero

def test_apply_clahe(processor, sample_image):
    # Testar aplicação do CLAHE
    clahe_image = processor.apply_clahe(sample_image)
    assert isinstance(clahe_image, Image.Image)
    assert clahe_image.size == sample_image.size

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.test_image_path = get_test_image_path()

    def test_load_image(self):
        # Teste para verificar se a imagem é carregada corretamente
        image = self.processor.load_image(self.test_image_path)
        self.assertIsNotNone(image)

    def test_process_image(self):
        # Teste para verificar se a imagem é processada corretamente
        image = self.processor.load_image(self.test_image_path)
        processed_image = self.processor.extract_channel(image, ['R'])  # Exemplo usando extract_channel
        self.assertIsNotNone(processed_image)

    def test_save_image(self):
        # Teste para verificar se a imagem é salva corretamente
        save_path = os.path.join(os.path.dirname(self.test_image_path), 'test_saved.jpg')
        image = self.processor.load_image(self.test_image_path)
        processed_image = self.processor.extract_channel(image, ['R'])
        self.processor.save_image(processed_image, save_path)
        self.assertTrue(os.path.exists(save_path))
        
        # Limpar arquivo de teste criado
        if os.path.exists(save_path):
            os.remove(save_path)

if __name__ == '__main__':
    unittest.main()