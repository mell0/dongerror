import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dongerror",
    version="0.0.1",
    author="mkirov",
    description="Silly exceptions with dongers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mell0/dongerror",
    packages=setuptools.find_packages()
)
