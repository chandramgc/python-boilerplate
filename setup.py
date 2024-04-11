from setuptools import setup, find_packages
import os
import subprocess

# Create a virtual environment
if not os.path.exists('venv'):
    subprocess.run(['python', '-m', 'venv', 'venv'])

# Activate the virtual environment
if os.name == 'posix':
    subprocess.run(['source', 'venv/bin/activate'], shell=True)
elif os.name == 'nt':
    subprocess.run(['venv\\Scripts\\activate'], shell=True)

# Install the package
subprocess.run(['pip', 'install', '.'])

# python setup.py sdist

setup(
    name="python-boilerplate",
    version="1.0.0",
    description="A brief description of your package",
    author="Girish Mallula",
    author_email="chandramgc@gmail.com",
    url="https://github.com/chandramgc/python-boilerplate.git",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["wheel", "Flask", "pymongo"],
    # entry_points={
    #     "console_scripts": [
    #         "python-boilerplate=src:main",
    #     ],
    # },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        # Add more classifiers as needed
    ],
    project_urls={  # Optional
        "Bug Reports": "https://github.com/pypa/sampleproject/issues",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "http://saythanks.io/to/example",
        "Source": "https://github.com/pypa/sampleproject/",
    },
)
