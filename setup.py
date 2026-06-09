# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:03:48 2023

@author: Petercusin
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgsfile",
    version="0.7.5",
    author="Dr. Guisheng Pan",
    author_email="panguisheng@sufe.edu.cn",
    description="PgsFile is an all-in-one Python toolkit for web scraping, file management, AI-powered text analysis, and data visualization, helping students and researchers collect, process, and analyze data with minimal code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Petercusin/PgsFile", 
    license="Educational free",
    install_requires=["pandas", "python-docx", "pip", "requests", "fake-useragent", "lxml", "pimht", "pysbd", "nlpir-python", "pillow", "liwc"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free For Educational Use",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)