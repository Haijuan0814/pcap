# Scenario
# Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
# The methods are delivered by the following classes:
# scan(), delivered by the Scanner class;
# print(), delivered by the Printer class;
# send() and print(), delivered by the Fax class.
# Each method should print a message indicating its purpose and origin, like:
# 'print() method from Printer class'
# 'send() method from Fax class'
# create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
# create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
# on each object call the methods: scan(), print(), send();



class Scanner:
    def scan(self):
        print('Scanner scan')
    
class Printer:
    def pri(self):
        print('Printer print')

class Fax:
    def send(self):
        print('Fax send')
        
    def pri(self):
        print('Fax print')

class MFD_SPF(Scanner , Printer , Fax):
    pass

class MFD_SFP(Scanner , Fax , Printer):
    pass

MFD_SPF().scan()
MFD_SPF().pri()
MFD_SPF().send()

MFD_SFP().scan()
MFD_SFP().pri()
MFD_SFP().send()
        