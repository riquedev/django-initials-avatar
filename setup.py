import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_initials_avatar",
    version="0.0.6",
    author="Henrique da Silva Santos",
    author_email="henrique.santos@4u360.com.br",
    description="A ridiculously simple avatar generator with initials from names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/riquedev/django-initials-avatar",
    keywords="letter, initials, avatar, django",
    project_urls={
        "Bug Tracker": "https://github.com/riquedev/django-initials-avatar/issues",
        "Repository": "https://github.com/riquedev/django-initials-avatar",
    },
    install_requires=[
        'Django>=3.2.14',
    ],
    classifiers=[
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    packages=setuptools.find_packages(
        exclude=["tests", "DjangoLetterAvatar", 'manage.py']
    ),
    include_package_data=True,
    python_requires=">=3.6"
)
