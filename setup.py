from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="image_processor",  # Alterado para corresponder ao nome do pacote
    version="0.1.0",
    author="Seu Nome",
    author_email="seuemail@example.com",
    description="Processamento de imagens com extração de canais RGB e CLAHE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "Pillow>=9.0.0",  # Atualizado para versão mais recente
        "numpy>=1.21.0",
        "opencv-python>=4.5.0"
    ],
    tests_require=[
        "pytest>=6.0",
    ],
)
