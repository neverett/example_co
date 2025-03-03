from setuptools import find_packages, setup

setup(
    name="example_co",
    packages=find_packages(exclude=["example_co_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
