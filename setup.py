from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='pyalgorithm',
    version='0.0.4',
    packages=['pyalgorithm'],
    author="lvyunze",
    author_email="17817462542@163.com",
    description="Python algorithms and data structures",
    keywords="algorithms、data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lvyunze/keyword_extract_links",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
