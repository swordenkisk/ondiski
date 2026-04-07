#!/usr/bin/env python3
"""
Setup script for Content Strategy & Hook Generator Tool
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="content-strategy-tool",
    version="1.0.0",
    author="Content Strategy Team",
    author_email="contact@example.com",
    description="A comprehensive tool for generating hooks and analyzing content scripts",
    long_description=read_file("TOOL_SUMMARY.txt") if os.path.exists("TOOL_SUMMARY.txt") else "",
    long_description_content_type="text/plain",
    url="https://github.com/swordenkisk/content-strategy-tool",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Content Creators",
        "Topic :: Content Creation :: Marketing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    entry_points={
        "console_scripts": [
            "content-strategy=main:main",
        ],
    },
    keywords="content marketing hooks viral scripts youtube shorts tiktok",
    project_urls={
        "Bug Reports": "https://github.com/swordenkisk/content-strategy-tool/issues",
        "Source": "https://github.com/swordenkisk/content-strategy-tool",
    },
)
