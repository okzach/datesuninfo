from setuptools import setup

setup(
    name='datesuninfo',
    version='0.1.0',
    packages=['datesuninfo'],
    url='https://github.com/okzach/datesuninfo/',
    license='',
    author='Zach Adams',
    author_email='zach@okzach.com',
    description='Mimics PHPs date_sun_info() using pyephem.',
    entry_points={
        'console_scripts': [
            'datesuninfo=datesuninfo:main'
        ]
    }
)
