from setuptools import setup, find_packages

setup(
    name="Topsis-Raghav-102203745",
    version="0.1.1",
    author="Raghav Jindal",
    author_email="rjindal_be22@thapar.edu",
    description="A Python package for implementing the TOPSIS decision-making method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/raghav-jindal/topsis_python_package",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "openpyxl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
