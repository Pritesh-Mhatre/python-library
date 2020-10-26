import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AutoTrader-Web-API-Stocks-Developer",
    version="1.1.0",
    author="Pritesh Mhatre",
    author_email="help@stocksdeveloper.in",
    description="Python library for multi-account automated trading on Zerodha, Upstox, AliceBlue, Finvasia, MasterTrust, Angel Broking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pritesh-Mhatre/python-library",
    packages=setuptools.find_packages(),
    install_requires=['requests'],    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Office/Business :: Financial :: Investment"
    ],
    python_requires='>=3.6',
)