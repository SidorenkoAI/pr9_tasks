class Person:
    # '''
    # Реализуйте класс для человека, поддерживающий историю изменений человеком своих фамилии и имени.
    # Считайте, что в каждый год может произойти не более одного изменения
    # фамилии и не более одного изменения имени.
    # При этом с течением времени могут открываться всё новые факты из прошлого человека,
    # поэтому года́ в последовательных вызовах методов *ChangeLastName* и *ChangeFirstName*
    # не обязаны возрастать.
    # Строка, возвращаемая методом *GetFullName*, должна содержать разделённые одним пробелом
    #  имя и фамилию человека по состоянию на конец данного года.
    # Если к данному году не случилось ни одного изменения фамилии и имени, верните строку "Incognito".
    # Если к данному году случилось изменение фамилии,
    # но не было ни одного изменения имени, верните "last_name with unknown first name".
    # Если к данному году случилось изменение имени,
    # но не было ни одного изменения фамилии, верните "first_name with unknown last name".
    # '''
    def __init__(self, f=str, l=str):
        self.name = [f, l]
        self.years_Fname = {}
        self.years_Lname = {}

    def ChangeFirstName(self, year, first_name):
        if year not in self.years_Fname:
            self.years_Fname[year] = first_name
            self.name[0] = first_name

    def ChangeLastName(self, year, last_name):
        if year not in self.years_Lname:
            self.years_Lname[year] = last_name
            self.name[1] = last_name

    def GetFullName(self, year):
        if year in self.years_Lname and year in self.years_Fname:
            return f'{self.years_Fname[year]} {self.years_Lname[year]} ({year})'
        if year in self.years_Lname and year not in self.years_Fname:
            return f'{self.years_Lname[year]} with unknown first name'
        if year in self.years_Fname and year not in self.years_Lname:
            return f'{self.years_Fname[year]} with unknown last name'
        if year not in self.years_Fname and year not in self.years_Lname:
            return 'Incognito'


#
# Vova = Person('Владимир', 'Петров')
#
# while True:
#     print(' 1 - сменить имя', '\n',
#           '2 - сменить фамилию', '\n',
#           '3 - полное имя', '\n',
#           '0 - Выход', '\n',)
#     command = int(input())
#     if command == 1:
#         Vova.ChangeFirstName(int(input('В каком году меняется имя? ')), input('Введите имя '))
#         print("Имя изменено")
#     if command == 2:
#         Vova.ChangeLastName(int(input('В каком году меняется фамилия? ')), input('Введите фамилию '))
#         print("Фамилия изменена")
#     if command == 3:
#         Vova.GetFullName(int(input('Введите год для получения данных ')))
#     if command == 0:
#         break



