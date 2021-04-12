from setuptools import setup, find_packages

setup(
    name='athena',
    version='0.1.0',
    autor='giorgioskij',
    packages=find_packages(include=['athena']),
    install_requires=[
        'PyAudio',
        'speechrecognition',
        'snowboy',
        'beepy',
        'sounddevice'
    ],
    entry_points={
        'console_scripts': ['athena=src.athena:main']
    }
)