class Person:
    def __init__(self):
        self.first_names = {}
        self.last_names = {}


    def ChangeFirstName(self, year, first_name):
        self.first_names[year] = first_name

    def ChangeLastName(self, year, last_name):
        self.last_names[year] = last_name

    def GetFullName(self, year):
        first_name = None
        last_name = None

        for key, value in self.first_names.items():
            if key <= year:
                first_name = value

        for key, value in self.last_names.items():
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

    def GetFullNameWithHistory(self, year):
        first_name = self.GetNameWithHistory(year, self.first_names)
        last_name = self.GetNameWithHistory(year, self.last_names)
        if not first_name and not last_name:
            return "Incognito"
        elif not first_name:
            return f"{last_name} with unknown first name"
        elif not last_name:
            return f"{first_name} with unknown last name"
        else:
            return f"{first_name} {last_name}"

    def GetName(self, year, names):
        name = ""
        for y in sorted(names.keys()):
            if y <= year:
                name = names[y]
            else:
                break
        return name

    def GetNameWithHistory(self, year, names):
        names_history = []
        for y in sorted(names.keys()):
            if y <= year:
                if not names_history or names_history[-1] != names[y]:
                    names_history.append(names[y])
            else:
                break
        if names_history:
            name = names_history[-1]
            names_history.pop()
            if names_history:
                name_history = ", ".join(reversed(names_history))
                name += f" ({name_history})"
            return name
        return ""
