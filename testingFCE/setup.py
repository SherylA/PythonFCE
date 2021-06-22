from setuptools import setup

setup(
    name='testpy1',
    version='0.1.0',    
    description='Testing Python package',
    url='https://github.com/SherylA/testingFCE',
    author='Sheryl Avenaño',
    author_email='sheryl.avendano@udea.edu.co',
    license='BSD 2-clause',
    packages=['testpy1'],
    install_requires=['numpy', 'pandas'           
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.8',
    ],
)