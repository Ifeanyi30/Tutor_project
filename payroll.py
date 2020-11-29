
class Payroll(object):

    def __init__(self, name, idNumber, hourlyRate, hoursWorked, grossPay):
        self.name = name
        self.idNumber = idNumber
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked
        self.grossPay = grossPay

    def getName(self):
        return self.name

    def getIdNumber(self):
        return self.idNumber


    def getHourlyRate(self):
        return self.hourlyRate

    def getHoursWorked(self):
        return self.hoursWorked

    def getGrossPay(self):
        return self.hoursWorked * self.hourlyRate

    def setName(self, nameGiven):
        self.name = nameGiven

    def setIdNumber(self, idNumberGiven):
        self.idNumber = idNumberGiven

    def setHourlyRate(self, rateGiven):
        self.hourlyRate = rateGiven

    def setHoursWorked(self, hoursGiven):
        self.hoursWorked = hoursGiven