from setuptools import setup, find_packages

setup(
    name="protection_model",
    version="1.0.0",
    description="This library contains protection models for different operating systems and utilities for patching ELF files with access rights.",
    author="Tobias Thornfeldt Nissen",
    author_email="tobias.nissen@gmail.com",
    license="MIT",
    packages=find_packages(
        include=['base', 'utilities', 'sel4cp']
    ),
    install_requires=[
        "abc"
        "os"
        "struct"
        "pathlib"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ]
)
