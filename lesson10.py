class CalculatorOperation:
    def add(self, a, b):
        return a+b
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        return a/b

calc = CalculatorOperation()

while True:
    print("1: Jumlah [+]")
    print("2: Kurang [-]")
    print("3. Kali [x]")
    print("4. Bagi [/]")

opt=int(input("Pilih operasi(1/2/3/4):"))
