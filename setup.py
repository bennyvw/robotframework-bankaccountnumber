from setuptools import find_packages, setup
from src.BankAccountNumber.version import VERSION

setup(

    name = 'robotframework-bankaccountnumber',
    package_dir  = {'': 'src'},
    packages = find_packages('src'),
    version = VERSION,
    description = 'Bank Account Number Generator',
    long_description_content_type = 'text/x-rst',
    long_description = "Robot Framework Library for generating (mainly Dutch) IBAN bank account numbers. The Account Numbers pass the mod 11 and mod 97 checks.",
    author = 'Anne Kootstra', 
    author_email = 'kootstra@hotmail.com',
    maintainer = 'Benny van Wijngaarden',
    maintainer_email = 'benny@smaragd-it.nl',
    url = 'https://github.com/bennyvw/robotframework-bankaccountnumber',
    keywords = ['robotframework', 'iban', 'bankaccount'],
    license      = 'MIT License',
    platforms    = 'any',
    classifiers = [
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Framework :: Robot Framework :: Library",
            "Topic :: Software Development :: Testing",
            "Development Status :: 4 - Beta"
    ]
)
