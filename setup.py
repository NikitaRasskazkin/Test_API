import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cur_api_pkj_Rasskazkin",
    version="0.0.2",
    author="Rasskazkin",
    author_email="rasskazkin64@gmail.com",
    description="Test API project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NikitaRasskazkin/Test_API.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        'Flask==1.1.2',
        'Flask-RESTful==0.3.8',
        'pymodm==0.4.3',
        'pymongo==3.11.2',
        'pytest==6.2.1'
    ]
)
