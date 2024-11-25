from setuptools import setup, find_packages

setup(
    name="omni-authify",
    version="0.1.0",
    description="A Python library for OAuth2 authentication across frameworks and providers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mukhsin Mukhtorov",
    author_email="mukhsinmukhtorov@arizona.edu",
    url="https://github.com/Omni-Libraries/omni-authify",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        # Add other dependencies like Django, Flask, etc., as you implement them
    ],
)
