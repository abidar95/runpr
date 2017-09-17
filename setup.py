from setuptools import setup

setup(
    name="Run Project",
    version="1.0",
    py_modules=["runpr"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        runpr=runpr:run
    """)
