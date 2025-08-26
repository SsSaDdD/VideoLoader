from setuptools import setup, find_packages

setup(
    name="ytfetch",
    version="0.1",
    packages=find_packages(),
    install_requires=["yt-dlp", "rich"],
    entry_points={
        "console_scripts": [
            "ytfetch=ytfetch.cli:main"
        ]
    },
)
