class Employee:

    def __init__(self, name, IDnumber):
        self.__name = name
        self.__IDnumber = IDnumber

    def set_name(self, name):
        self.__name = name

    def set_IDnumber(self, IDnumber):
        self.__IDnumber = IDnumber

    def get_name(self):
        return self.__name
    
    def get_IDnumber(self):
        return self.__IDnumber
    
class ProductionWorker(Employee):

    def __init__(self, name, IDnumber, ShiftNumber, HourlyPay):
        Employee.__init__(self, name, IDnumber)
        self.__ShiftNumber = ShiftNumber
        self.__HourlyPay = HourlyPay

    def set_ShiftNumber(self, ShiftNumber):
        self.__ShiftNumber = ShiftNumber

    def set_HourlyPay(self, HourlyPay):
        self.__HourlyPay = HourlyPay

    def get_ShiftNumber(self):
        return self.__ShiftNumber
    
    def get_HourlyPay(self):
        return self.__HourlyPay
    
def main():

    worker1 = ProductionWorker("Jaden Tran",1234,2,23.0)
    print(f"The production worker name is: {worker1.get_name()}.")
    print(f"The production worker ID number is: {worker1.get_IDnumber()}.")
    print(f"The production worker shift number is: {worker1.get_ShiftNumber()}.")
    print(f"The production worker hourly pay is: ${worker1.get_HourlyPay()} an hour.")

main()