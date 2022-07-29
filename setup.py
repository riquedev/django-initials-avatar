import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facebookcloudapi",
    version="0.0.4",
    author="Henrique da Silva Santos",
    author_email="henrique.santos@4u360.com.br",
    description="Integration SDK for Facebook / Meta Cloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KoterIA/FacebookCloudAPI",
    project_urls={
        "Bug Tracker": "https://github.com/KoterIA/FacebookCloudAPI/issues",
        "Repository": "https://github.com/KoterIA/FacebookCloudAPI",
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    packages=setuptools.find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires=">=3.8"
)
