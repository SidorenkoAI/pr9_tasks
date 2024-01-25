class Person:
    '''
    Реализуйте класс для человека, поддерживающий историю изменений человеком своих фамилии и имени.
    Считайте, что в каждый год может произойти не более одного изменения
    фамилии и не более одного изменения имени.
    При этом с течением времени могут открываться всё новые факты из прошлого человека,
    поэтому года́ в последовательных вызовах методов *ChangeLastName* и *ChangeFirstName*
    не обязаны возрастать.
    Строка, возвращаемая методом *GetFullName*, должна содержать разделённые одним пробелом
     имя и фамилию человека по состоянию на конец данного года.
    Если к данному году не случилось ни одного изменения фамилии и имени, верните строку "Incognito".
    Если к данному году случилось изменение фамилии,
    но не было ни одного изменения имени, верните "last_name with unknown first name".
    Если к данному году случилось изменение имени,
    но не было ни одного изменения фамилии, верните " first_name with unknown last name".
    '''
    def __init__(self):
      self.history = dict()

    def ChangeFirstName(self, year, first_name):
      if int(year) not in self.history.keys():
        self.history[int(year)] = {'first_name': first_name}
      else:
        self.history[int(year)]['first_name'] = first_name

    def ChangeLastName(self, year, last_name):
      if int(year) not in self.history.keys():
        self.history[int(year)] = {'last_name': last_name}
      else:
        self.history[int(year)]['last_name'] = last_name
    
    def GetFullName(self, year):
      if int(year) in self.history.keys():
         if list(self.history[int(year)].keys()) == ['first_name', 'last_name']:
            return f'{self.history[int(year)]["first_name"]} {self.history[int(year)]["last_name"]}'
         elif list(self.history[int(year)].keys()) == ['first_name']:
            return f'{self.history[int(year)]["first_name"]} with unknown last name'
         elif list(self.history[int(year)].keys()) == ['last_name']:
            return f'{self.history[int(year)]["last_name"]} with unknown first name'
      elif min(list(self.history.keys())) > year:
        return 'Incognito'
      else:
         return 'в этот год записи нет, но есть в предыдущих годах. не успел реализовать :('