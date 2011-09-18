from setuptools import setup

setup(
    name='asciipy',
    version='0.0.0',
    author='Sven Hendriks',
    author_email='hendriks.sven@googlemail.com',
    packages=['asciipy',
             ],
    scripts=['asciipy/scripts/asciipy',
    ],
    install_requires=[
        'pil>=1.1.7,<1.2',
    ],
)

