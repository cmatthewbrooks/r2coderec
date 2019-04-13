from setuptools import setup

setup(

    name = 'r2coderec',
    version = '0.1',
    author = 'cmatthewbrooks',
    author_email = 'me@cmatthewbrooks.com',
    keywords = [
        'radare2',
        'code-recognition',
        'reverse-engineering',
        'disassembly'
        ],
    packages = ['r2coderec'],
    entry_points = {
        'console_scripts': [
        'r2coderec = r2coderec.r2sigs:main',
        ]
    },
    install_requires = [
        'r2pipe'
    ]

)
