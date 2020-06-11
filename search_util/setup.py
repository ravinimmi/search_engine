import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ravinimmi",
    version="0.0.1",
    author="Ravi Kumar Nimmi",
    author_email="nimmi.ravikumar@gmail.com",
    description="Search Utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ravinimmi/search_engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
