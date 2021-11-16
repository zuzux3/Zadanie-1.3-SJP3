import re

phoneNumber = '345-03-02'
newPhoneNumber = re.sub('-', '', phoneNumber)

endStr = 'Numer przed modyfikacja: {}\nNumer po modyfikacji: {}\n'

print(endStr.format(phoneNumber, newPhoneNumber))