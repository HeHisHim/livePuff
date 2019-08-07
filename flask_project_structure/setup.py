from setuptools import setup, find_packages

setup(
    name="flask_project_structure",
    version='0.0.1',
    author="yoyboy",
    author_email="534411590@qq.com",
    url="whatever",
    description="flask_project_structure demo",
    install_requires=open('requirements.txt', 'r').read().split(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=find_packages(".", exclude=("*tests*",)),
    python_requires=">=3.6",
    license="MIT",
    zip_safe=False,
)