setup(
    name='example',
    version='0.1.0',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'PyYAML',
        'pandas==0.25.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',
        'jupyter'
    ]
)