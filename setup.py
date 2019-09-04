import setuptools

setuptools.setup(
    name='soulsCalc',
    version='0.1',

    description='Dark Souls Calculator',
    license=' GNU',

    # Allow UTF-8 characters in README with encoding argument.
    long_description=open('README.md', encoding="utf-8").read(),
    keywords=['python'],

    author='Carlos Monnazzi (Dreamblader)',
    url='https://github.com/dreamblader/SoulsCalculator',

    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},

    entry_points={
        'console_scripts': ['souls=soulscalc.main_window:main'],
    }
)