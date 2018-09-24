from setuptools import setup

setup(
    name='subsworld',
    version='1.0',
    url='https://github.com/mugdhaadhav/subsworld',
    license='MIT License',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
    ],
    keywords='subtitles wrapper',
    author='mugdhaadhav',
    author_email='mugdha.adhav@yahoo.com',
    description='Subtitle wrapper',
    install_requires=['beautifulsoup4',
                      'fuzzywuzzy'
                      'requests'],
    entry_points={
        'console_scripts': [
            'subsworld=subsworld.__init__:subsworld',
        ],
    }
)
