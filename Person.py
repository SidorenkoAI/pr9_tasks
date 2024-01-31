class Person:
    def __init__(self):
        self.name = {}
        self.firstname = {}

    def ChangeFirstName(self, year, first_name):
        self.firstname[year]=first_name
    def ChangeLastName(self, year, last_name):
        self.name[year]=last_name

    def GetFullName(self, year):
        iFN=0
        iLN=0
        if year in self.firstname == True:
            iFN=True
        else:
            iFN=False
        if year in self.name == True:
            iLN=True
        else:
            iLN=False
        if iFN==True and iLN==True:
            return f'{self.name[year]} {self.firstname[year]}'
        elif iFN==True and iLN==False:
            return 'last_name with unknown first name'
        elif iFN==False and iLN==True:
            return 'first_name with unknown last name'
        else:
            return 'Incognito'