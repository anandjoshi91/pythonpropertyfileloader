from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='property',
      version='2.6.2',
      packages=['properties'],
      url='https://github.com/anandjoshi91/pythonpropertyfileloader',
      description=""" A python module to load property files. Recursively define properties, load from env.""",
      long_description_content_type='text/markdown',
      long_description=long_description,
      author='Anand Joshi',
      author_email='anandhjoshi@outlook.com',
      keywords= ["property", "read-property-file", "property-interpolation"],
      license='MIT',
      classifiers=["License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10"],
      download_url='https://github.com/anandjoshi91/pythonpropertyfileloader/archive/refs/tags/2.6.2.zip'
      )
