from setuptools import find_packages, setup

setup(
    name='lifeladderpacking',
    version='1.0.5',
    description='Tool for LifeLadder packing',
    url='https://port-safety.com/',
    author='Christian Baun',
    author_email='baunbaun@gmail.com',
    packages=['lifeladderpacking'],
    package_data={'lifeladderpacking': ['templates/*.html','static/*.jpg']},
    zip_safe=False,
    install_requires=[
        'flask',
	    'binpacking',
    ],
)
