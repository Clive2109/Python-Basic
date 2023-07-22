class Calculator:
    @staticmethod
    def add(a,b):
        hasil=a+b
        print("Hasil operasi dari", a, "+", b, "adalah", hasil)
    @staticmethod
    def subtract(a,b):
        hasil=a-b
        print("Hasil operasi dari", a, "-", b, "adalah", hasil)
    @staticmethod
    def multiply(a,b):
        hasil=a*b
        print("Hasil operasi dari", a, "x", b, "adalah", hasil)
    @staticmethod
    def divide(a,b):
        hasil=a/b
        print("Hasil operasi dari", a, "/", b, "adalah", hasil)