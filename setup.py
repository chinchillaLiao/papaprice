import setuptools 

setuptools.setup(
    name='papaprice',
    version='0.0.3',
    author='GaryLiao',
    description='crawl the name and price of each product from e-commerce websites in Taiwan.',
    url='https://github.com/chinchillaLiao/papaprice',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author_email='chinchillaliao@gmail.com',
    license='MIT',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['requests','bs4','js2py'],
    python_requires=">=3.6",
    zip_safe=False)
