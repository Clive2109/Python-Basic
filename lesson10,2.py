from lesson10cal import Calculator

print("==============================")
print("Operasi Matematika")
print("1. Jumlah [+]")
print("2. Kurang [-]")
print("3. Kali   [*]")
print("4. Bagi   [/]")
print("==============================")
operasi=input("Pilih Operasi (1/2/3/4) ")
a=int(input("Masukkan bilangan pertama:"))
b=int(input("Masukkan bilangan kedua:"))
print("==============================")

calculator = Calculator()
if operasi == "1":
    calculator.add(a,b)
if operasi == "2":
    calculator.subtract(a,b)
if operasi == "3":
    calculator.multiply(a,b)
if operasi == "4":
    calculator.divide(a,b)