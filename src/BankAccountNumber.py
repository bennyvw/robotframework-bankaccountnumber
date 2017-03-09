import string
import sys
import random
from iban import *
from version import *

class BankAccountNumber:
    """
    The Bank Account Number library provides keywords to generate NL specific
    bank account numbers that are 9 digits long and comply with the Elf Proef.
    
    Before the introduction of IBAN most of the Dutch bank account numbers adhered 
    to a mod 11 check, called the Elf proef. This check ensured that simple 
    mistakes  while inputting a bank account number were prevented.
    
    With the introduction of IBAN the mod 11 check became obsolete, as it has 
    its own mod 97 check. The keywords in this library can generate the old style
    account number, or include it in the IBAN format. 
    
    This library depends on the work done by Thomas Gunther <tom@toms-cafe.de>
    that is able to create the IBAN check digit from it's components: Country
    Code, Bank Code and Account Number. This completes the IBAN format:
    
    [Country Code] [Check Digit] [Bank Code] [Account Number]
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION
    
    NL_BANK_CODES = ['ABNA', 'ASNB', 'INGB', 'KNAB', 'FVLB', 'RABO', 'TRIO']

    def generate_NL_Bank_Account_Number(self, total=1):
        """
        Generate one or more NL Bank account numbers
        
        This keyword is able to generate one or more Elf Proef compliant account
        numbers. This can be of use for systems that have not yet complied with
        the SEPA and IBAN standards. It also aids with those systems who may
        still have this check in place for the IBAN account number part.
        
        The keyword can be called without any arguments when only a single account
        is needed. When multiple account numbers are required the `total` argument
        allows to specify the number of accounts that need to be returned. In
        this case a list is returned, otherwise a string.
        """
        count = 0
        accountNumbers = []
        
        """
        This loop is needed even when generating 1 number because the generated 
        randomly generate number may not be mod 11 valid and a second try is needed.
        """
        while (count < int(total)):
            bankAccountNumber = ""
            bankAccountNumber += str(random.randint(000000000, 999999999))
    
            if bankAccountNumber:
                  if self.NL_Bank_Account_Check(bankAccountNumber):
                    count += 1
                    accountNumbers.append(bankAccountNumber)
        """
        Return number as a string, or the list when more than one.
        """
        if(len(accountNumbers) > 1):
            return accountNumbers
        elif(len(accountNumbers)==1):
            return accountNumbers[0]
    
    def NL_Bank_Account_Check(self, bankAccountNumber):
        """
        Check if a provided number is a valid pre-IBAN Dutch bank account number.
        
        The performed check is a Mod 11 check that is used on bank account
        number of 9 or 10 digit length. Account numbers that do not have this
        length can not be checked, as the issuing bank did not use this check.
        
        Examples:
        Valid:         NL Bank Account Check    824043006
        Invalid:       NL Bank Account Check    824043008
        """
        if(len(bankAccountNumber)>8) and (len(bankAccountNumber)<11):
            checkDigit = len(bankAccountNumber)
        else:
            return  False
        sum = 0
        for number in bankAccountNumber:
            if number in string.digits:
                sum = sum + int(number) * checkDigit
                checkDigit = checkDigit - 1
        if divmod(sum, 11)[1] == 0:
            return  True
        return  False
    
    
    def generate_IBAN_account_number(self, countryCode='NL', bankCode=None, accountNumber=None):
        """
        Generate the IBAN compliant number.
        
        This keyword generates the IBAN check digit from it's components: Country
        Code, Bank Code and Account Number and return the result in the IBAN format:
    
        [Country Code] [Check Digit] [Bank Code] [Account Number]
        
        All three arguments are optional. In case none are provided default values 
        for the Country code and Bank Code are used, and the internal NL account
        generator creates the account number. The following examples are all valid
        
        Examples:
        Generate IBAN Account Number
        Generate IBAN Account Number    DE
        Generate IBAN Account Number    DE    37040044
        Generate IBAN Account Number    accountNumber=362202583
        Generate IBAN Account Number    bankCode=INGB
        """
        if(accountNumber==None):
            accountNumber = str(self.generate_NL_Bank_Account_Number())
 
        if(bankCode==None):
            bankCode = random.choice(self.NL_BANK_CODES)
 
        iban = create_iban(countryCode, bankCode, accountNumber)
        return iban
    
    def check_IBAN_account_number(self, ibanNumber):
        """
        Check if the provided IBAN account number is a valid one.
        
        This keyword takes one input in the form of an IBAN account number. The
        response will be either True or False. It checks to see if:
        - Country Code: valid code
        - Account Number: Length
        - Bank Account Number: Length
        - Check Digit: validates the check digit calculated across values.
        
        Examples:
        Valid:        NL67INGB0763159700     True
        Invalid:      NL68INGB0763159700     False
        """
        try:
            check_iban(ibanNumber)
            return  True
        except IBANError:
            return  False