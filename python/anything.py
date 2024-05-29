class asdf():
    def __init__(self):
        self.jan = 0
    def plus(self, ina):
        self.ina = ina
        self.jan+=self.jan+ina
        print(self.jan)
    def minus(self,aut):
        self.aut = aut
        print([self.jan-aut if self.jan>=aut else "잔액이 부족합니다."][0])
asd = asdf()
asd.plus(10)
asd.minus(5)
asd.minus(55)