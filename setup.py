from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='commandline user management utility',
    long_description=readme,
    author='Monte',
    author_email='mcrattray@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main',
        ]
    }
)
