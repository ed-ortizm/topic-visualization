"""Install topicViz package."""""

from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as file:

    long_description = file.read()

setup(
    name="topicViz",
    version="0.0.1",
    author="Edgar Ortiz",
    author_email="ed.ortizm@gmail.com",
    packages=find_packages(
        where="src", include=["[a-z]*"], exclude=["old_code"]
    ),
    package_dir={"": "src"},
    description="Topic visualization of text data: posts, tweets, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ed-ortizm/topic-vizualization",
    license="MIT",
    keywords=(
        "NLP, topic modeling, visualization, text mining,"
        "machine learning, data science."
    ),
)
