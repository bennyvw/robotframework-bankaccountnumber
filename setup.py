from setuptools import find_packages, setup
from src.BankAccountNumber.version import VERSION

setup(
    name = 'robotframework-dutchbankaccountnumber',
    package_dir  = {'': 'src'},
    packages = find_packages('src'),
    version = VERSION,
    description = 'Dutch Bank Account Generator',
    long_description_content_type = 'text/x-rst',
    long_description = "Robot Framework Library for generating pre and post IBAN period bank account numbers. The Account Numbers pass the mod 11 and mod 97 checks.",
    author = 'Anne Kootstra', 
    author_email = 'kootstra@hotmail.com',
    url = 'https://github.com/kootstra/robotframework-dutchbankaccountnumber',
    keywords = ['robotframework', 'iban', 'bankaccount'],
    license      = 'MIT License',
    platforms    = 'any',
    download_url = 'https://github.com/kootstra/robotframework-dutchbankaccountnumber/tarball/' + VERSION,
    classifiers = [
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Framework :: Robot Framework :: Library",
            "Topic :: Software Development :: Testing",
            "Development Status :: 4 - Beta"
    ],
)
