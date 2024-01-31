class Person:
    def __init__(self):
        self.name = {}
        self.firstname = {}
    def __str__(self):
        return f'{self.name}, {self.firstname}'
    def ChangeFirstName(self, year, first_name):
        self.firstname[year]=first_name
    def ChangeLastName(self, year, last_name):
        self.name[year]=last_name

    def GetFullName(self, year):
        iFN=0
        iLN=0
        fkeys=self.firstname.keys()
        lkeys=self.name.keys()
        if year in fkeys:
            iFN=True
        else:
            iFN=False
        if year in lkeys:
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
