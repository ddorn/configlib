from distutils.core import setup

setup(
    name='configlib',
    version='1.0.0',
    packages=['configlib'],
    url='https://github.com/ddorn/configlib',
    license='MIT',
    author='Diego Dorn',
    author_email='diego.dorn@free.fr',
    description='Configuration for python made easy',
    install_requires=['click=6', 'pygments>=2.2']
)