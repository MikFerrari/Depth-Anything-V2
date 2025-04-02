from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
requirements = []
if os.path.isfile(req_file):
    with open(req_file) as f:
        requirements = f.read().splitlines()

setup(
    name="depth_anything_v2",
    version="0.1.0",
    description="Depth Anything V2: Monocular depth estimation model",
    author="Contributors",
    author_email="your.email@example.com",
    url="https://github.com/username/Depth-Anything-V2",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)