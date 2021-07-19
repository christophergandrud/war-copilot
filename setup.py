import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WarSim",
    version="0.0.1",
    author="Christopher Gandrud",
    author_email="christopher.gandrud@gmail.com",
    description="Simulate outcomes for the game war. Written with the help of GitHub Copilot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/christophergandrud/war-copilot",
    project_urls={
        "Bug Tracker": "https://github.com/christophergandrud/war-copilot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: The Unlicense",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)