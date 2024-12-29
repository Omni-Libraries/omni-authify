from setuptools import find_packages, setup

setup(
    name="omni-authify",
    version="1.1.8",
    license="MIT",
    download_url="https://github.com/Omni-Libraries/omni-authify.git",
    changelog="https://omni-libraries.mukhsin.space/installation",
    documentation="https://omni-libraries.mukhsin.space",
    bug="https://github.com/Omni-Libraries/omni-authify/issues",
    description="A Python library for OAuth2 authentication across frameworks and providers",
    long_description=open("docs/index.md").read(),
    long_description_content_type="text/markdown",
    author="Mukhsin Mukhtorov",
    author_email="mukhsinmukhtorov@arizona.edu",
    maintainer="Mukhsin Mukhtorov",
    maintainer_email="mukhsinmukhtorov@arizona.edu",
    url="https://github.com/Omni-Libraries/omni-authify.git",
    keywords='Oauth2, facebook-login, instagram-login, twitter-login, x-login, github-login, google-login, '
             'linkedin-login, telegram-login, oauth2-django, oauth2-djangorestframework, oauth2-fastapi, oauth2-flask',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests",
        "python-dotenv>=1.0.1"
    ],
    extras_require={
        'django':['Django>=4.2'],
        'drf':['djangorestframework>=3.12.3'],
        'flask':['Flask>=3.0.0'],
        'fastapi':['fastapi>=0.115.0'],
    }
)
