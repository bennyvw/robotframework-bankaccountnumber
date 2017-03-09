*** Settings ***
Library    BankAccountNumber
Library    Collections

*** Test Cases ***
Generate Bank Account Number
    ${number}=    Generate NL Bank Account Number
    Log To Console    \n${number}

Generate Bank Account Number List
    @{numbers}=    Generate NL Bank Account Number    total=5
    Log List To Console    ${numbers}

Generate IBAN Account Number
    ${iban}=      Generate IBAN Account Number
    Log To Console    \n${iban}

Generate IBAN Account Number using an existing Account Number
    ${iban}=      Generate IBAN Account Number    accountNumber=993267483
    Log To Console    \n${iban}

Generate IBAN Account Number for German Bank
    ${iban}=      Generate IBAN Account Number    DE    37040044
    Log To Console    \n${iban}

Generate IBAN Account Number ING Bank and create IBAN for it
    ${number}=    Generate NL Bank Account Number
    ${iban}=      Generate IBAN Account Number    NL    INGB    ${number}
    Log To Console    \n${iban}

Generate IBAN Account Number for ING bank
    ${iban}=      Generate IBAN Account Number    bankCode=INGB
    Log To Console    \n${iban}

Check IBAN Account Number
    ${pass}=    Check IBAN Account Number    NL67INGB0763159700
    ${fail}=    Check IBAN Account Number    NL68INGB0763159700

*** Keywords ***
Log List To Console
    [Arguments]    ${list}
    ${count}=    Get Length    ${list}
    Log To Console    \nList length is ${count} and it contains the following items:
    :FOR    ${index}    IN RANGE    0    ${count}
    \    Log To Console    ${index}: @{list}[${index}]