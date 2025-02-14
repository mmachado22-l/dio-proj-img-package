from image_processor.processor import ImageProcessor
from PIL import Image
import numpy as np
import os

def get_test_dir():
    # Obtém o diretório de testes
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(os.path.dirname(current_dir), 'tests')
    return test_dir

def main():
    test_dir = get_test_dir()
    
    # Criar diretório para resultados se não existir
    results_dir = os.path.join(test_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)
    
    # Caminhos dos arquivos
    test_image_path = os.path.join(test_dir, 'test.jpg')
    
    # Criar uma imagem de teste se não existir
    if not os.path.exists(test_image_path):
        test_image = np.random.randint(0, 255, (300, 300, 3), dtype=np.uint8)
        test_image = Image.fromarray(test_image)
        test_image.save(test_image_path)

    # Inicializar o processador
    processor = ImageProcessor()

    # Testar extração de canais
    print("Testando extração de canais...")
    
    # Carregar imagem
    image = processor.load_image(test_image_path)
    
    # Testar diferentes combinações de canais
    combinations = [
        ['R'], ['G'], ['B'],
        ['R', 'G'], ['R', 'B'], ['G', 'B'],
        ['R', 'G', 'B']
    ]
    
    for channels in combinations:
        print(f"Processando canais: {channels}")
        result = processor.extract_channel(image, channels)
        filename = os.path.join(results_dir, f"test_{''.join(channels)}.jpg")
        processor.save_image(result, filename)
        print(f"Salvo como: {filename}")
    
    # Testar CLAHE
    print("\nTestando CLAHE...")
    clahe_result = processor.apply_clahe(image)
    clahe_filename = os.path.join(results_dir, 'test_clahe.jpg')
    processor.save_image(clahe_result, clahe_filename)
    print(f"CLAHE aplicado e salvo como: {clahe_filename}")

if __name__ == "__main__":
    main()
