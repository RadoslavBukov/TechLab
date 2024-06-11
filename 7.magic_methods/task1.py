'''
Създайте клас Fibs, реализиращ протокола за итериране. Следният код трябва да може работи с вашия клас, но да НЕ СЕ съдържа в качения от вас файл.
fibs = Fibs()
for f in fibs:
   if f > 1000:
      print(f)
      break
'''


class Fibs:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib


fibs = Fibs()
for f in fibs:
    if f > 1000:
      print(f)
      break

# for i in range(0, 10):
#     print(fibs.__next__())