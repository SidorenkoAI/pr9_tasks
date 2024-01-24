class Person:

    def init(self):
        self.name_changes = {}
        self.lastname_changes = {}


    def ChangeFirstName(self, year, first_name):
        self.name_changes[year] = first_name


    def ChangeLastName(self, year, last_name):
        self.lastname_changes[year] = last_name


    def GetFullName(self, year):
        first_name = None
        last_name = None

        for key, value in self.name_changes.items():
            if key <= year:
                first_name = value

        for key, value in self.lastname_changes.items():
            if key <= year:
                last_name = value

        if first_name is None and last_name is None:
            return "Incognito"
        elif first_name is not None and last_name is None:
            return first_name + " with unknown last name"
        elif first_name is None and last_name is not None:
            return last_name + " with unknown first name"
        else:
            return first_name + " " + last_name



