import setuptools

VERSION = "0.1.2"
DESCRIPTION = "Do simple operations for files easier"
with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="simple-file-ops",
    version=VERSION,
    author="Cube Riser",
    author_email="cuberiser@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages(),
    install_requires=[""],
    keywords=[
        "python",
        "file operations",
        "files",
        "fileops",
        "file-operations",
        "simple file ops",
        "file ops",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license="MIT",
)
