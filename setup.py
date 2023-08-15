import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = '0.0.0'

REPOSITORY= "Chicken-Disease-Classification"
AUTHOR= "ideepankarsharma2003"
SRC_REPOSITORY= "ChickenDiseaseClassifier"
AUTHOR_EMAIL= "deepankarsharma2003@gmail.com"



setuptools.setup(
    name="Chicken-Disease-Classification",
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Chicken Disease Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPOSITORY}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPOSITORY}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')

)