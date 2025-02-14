# README.md

# Image Processing Package

Um pacote Python para processamento de imagens que permite extrair canais RGB e aplicar CLAHE.

## Instalação

Para instalar o pacote, você pode usar o seguinte comando:

```bash
pip install .
```

## Uso

Aqui está um exemplo de como usar o pacote:

```python
from image_processor.processor import ImageProcessor

# Crie uma instância do processador de imagens
processor = ImageProcessor()

# Carregue uma imagem
image = processor.load_image('caminho/para/imagem.jpg')

# Aplique um filtro ou transformação
processed_image = processor.process_image(image)

# Salve a imagem processada
processor.save_image(processed_image, 'caminho/para/imagem_processada.jpg')
```

## Testes

Para executar os testes, você pode usar o seguinte comando:

```bash
pytest tests/
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.