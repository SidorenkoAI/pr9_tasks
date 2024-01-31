'''
Дополните класс Person методом *GetFullNameWithHistory*:
В отличие от метода *GetFullName*, метод *GetFullNameWithHistory* должен вернуть не только последние имя и фамилию к концу данного года, но ещё и все предыдущие имена и фамилии в обратном хронологическом порядке. Если текущие факты говорят о том, что человек два раза подряд изменил фамилию или имя на одно и то же, второе изменение при формировании истории нужно игнорировать.

Для лучшего понимания формата см. примеры.

##### Пример 1 #####
###### Код ######
```objectivec
int main() {
  Person person;

  person.ChangeFirstName(1900, "Eugene");
  person.ChangeLastName(1900, "Sokolov");
  person.ChangeLastName(1910, "Sokolov");
  person.ChangeFirstName(1920, "Evgeny");
  person.ChangeLastName(1930, "Sokolov");
  cout << person.GetFullNameWithHistory(1940) << endl;

  return 0;
}
```

###### Вывод ######
```objectivec
Evgeny (Eugene) Sokolov
```


'''