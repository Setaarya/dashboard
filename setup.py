from setuptools import setup, find_packages

setup(
    name='my_package',
    version='3.9',
    author='Yulianto Aryaseta',
    author_email='yuliantoseta@gmail.com',
    description='Dashboard',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Daftar ketergantungan
        'pandas',
    ],
)
