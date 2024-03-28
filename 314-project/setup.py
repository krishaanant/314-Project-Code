from setuptools import find_packages, setup

setup(
    name="314_project",
    packages=find_packages(exclude=["314_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
