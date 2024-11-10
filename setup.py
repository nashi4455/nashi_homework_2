from setuptools import setup, find_packages

setup(
    name='my_package',  # Name of the package
    version='0.1.0',    # Package version
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[  # Any dependencies your package requires
        'requests',  # Example: replace with actual dependencies
    ],
    classifiers=[  # Optional: classifiers to help categorize the package on PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
