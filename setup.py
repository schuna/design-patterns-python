from setuptools import find_packages, setup
import io


def long_description():
    with io.open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    return readme


setup(
    name="design_patterns",
    version="0.1.0",
    description="design patterns in python",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="",
    author="jiyong.lee",
    author_email="jiyong1972@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
