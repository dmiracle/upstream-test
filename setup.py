from setuptools import setup

setup(
    name='projectr',
    version='0.0.1',
    py_modules=['projectr'],
    install_requires=[
        'click',
        'python-decouple',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        projectr=projectr.projectr:cli
    ''',
)