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

if operasi == "1":
    hasil=a+b
    print("Hasil operasi dari",a,"+",b,"adalah",hasil)
elif operasi == "2":
    hasil=a-b
    print("Hasil operasi dari",a,"-",b,"adalah",hasil)
elif operasi == "3":
    hasil=a*b
    print("Hasil operasi dari",a,"x",b,"adalah",hasil)
elif operasi == "4":
    hasil=a/b
    print("Hasil operasi dari",a,"/",b,"adalah",hasil)
print("==============================")