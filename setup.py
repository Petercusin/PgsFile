# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:03:48 2023

@author: Petercusin
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PgsFile",
    version="0.2.4",
    author="Pan Guisheng",
    author_email="895284504@qq.com",
    description="This module streamlines Python package management, script execution, file handling, web scraping, multimedia downloads, data cleaning, and NLP tasks such as word tokenization and POS tagging. It also assists with generating word lists and plotting data, making these tasks more accessible and convenient for literary students. Whether you need to scrape data from websites, clean text, or analyze language, this module provides user-friendly tools to simplify your workflow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mp.weixin.qq.com/s/12-KVLfaPszoZkCxuRd-nQ?token=1589547443&lang=zh_CN",
    license="Educational free",
    install_requires=["chardet", "pandas", "python-docx", "pip", "requests", "fake-useragent", "lxml", "pimht", "pysbd", "nlpir-python","pillow"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free For Educational Use",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)