# Задача 1. Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок
class FlatIterator():
  def __init__(self, list_of_list):
    self.list_of_list = (list_of_list)

  def __iter__(self):
    self.li = []
    for item in self.list_of_list:
      self.li += item
    return self

  def __next__(self):
    li = self.li
    if li == []:
      raise StopIteration
    for l in li:
      li.remove(l)
      return (l)
  
# Задача 2. Доработать функцию flat_generator, Должен получиться генератор, который принимает список списков и возвращает их плоское представление. Функция test в коде ниже также должна отработать без ошибок.
def flat_generator(lists):
    lists = iter(lists)
    li = []
    for item in lists:
      li += item

    for l in li:
      if li == []:
        exit()
      yield (l)


