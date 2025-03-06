from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as fh:
    readme = fh.read()

setup(
    name="mercadopagovp",
    version="0.3.9",
    url="https://github.com/reinanbr/pix_plugin_mp_py",
    license="MIT",
    author="Reinan Br",
    author_email="slimchatuba@gmail.com",
    description="A library for managing PIX payments on MercadoPago",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="mercadopago pix payments",
    packages=find_packages(),
    install_requires=[
        "mercadopago",
        "python-dotenv",
        "qrcode",
        "pillow",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
