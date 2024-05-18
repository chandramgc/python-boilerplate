import setuptools


setuptools.setup(
    name="demo_file_reader",
    description="Tool to read various compressed/raw file formats",
    version="1.0.0",
    packages=setuptools.find_packages('src'),
    package_dir={
        '': 'src'
    }
)
