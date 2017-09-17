from setuptools import setup

setup(
    name="Run Project",
    version="1.0",
    py_modules=["runpr"],
    install_requires=["Click"],
    description = 'CLI for running Python Project with Virtualenv via Visual Studio Code',
    author = 'Abidar El Mehdi',
    author_email = 'abidar.mehdi95@gmail.com',
    url = 'https://github.com/peterldowns/mypackage',
    download_url = 'https://github.com/abidar95/runpr', 
    keywords = ['running', 'managing'],
    classifiers = [],
    entry_points="""
        [console_scripts]
        runpr=runpr:run
    """)
