from setuptools import setup

setup(

    name = 'r2sigs',
    version = '0.1',
    author = 'cmatthewbrooks',
    author_email = 'me@cmatthewbrooks.com',
    keywords = ['radare2'],
    packages = ['r2sigs'],
    entry_points = {
        'console_scripts': [
        'r2sigs = r2sigs.r2sigs:main',
        'r2autoanalyze = r2sigs.r2autoanalyze:main',
        'r2compileranalysis = r2sigs.r2compileranalysis:main'
        ]
    },
    install_requires = [
        'r2pipe'
    ]

)
