from setuptools import setup, find_packages

setup(
    name="pymegasdkrest",
    version="0.6.9",
    description="MegaSDK-REST python wrapper",
    url="https://github.com/Oxhellfire/megasdkrest",
    packages=find_packages(),
    install_requires=["requests", "aiohttp"],
)
