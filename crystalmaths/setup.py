import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AmyStegmann", 
    version="0.0.1",
    author="Example Author",
    author_email="amybrehm@uw.edu",
    description="Identify zone axis from a high res TEM image",
    long_description=Crystalmaths is a Data Science Project that was developed as a part of the DIRECT Program by a group of graduate students from the University of Washington in Seattle.
The goal of crystalmaths is to create a Python module that can make automate zone axis definition from a high resolution TEM images.
crystalmaths is a developing module with more improvements to come. Feel free to add your comments, notes, and recommendations in the issues of this repository.,
    long_description_content_type="text/markdown",
    url="https://github.com/crystalmaths/crystalmaths",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
