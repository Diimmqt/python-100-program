def fibonacci_iteratif(n):
    fibo = []
    a, b = 0, 1
    for _ in range(n):
        fibo.append(a)
        a, b = b, a + b
    return fibo

# Input dari pengguna
angka = int(input("Masukkan jumlah bilangan Fibonacci: "))
if angka <= 0:
    print("Masukkan bilangan positif!")
else:
    print(f"Deret Fibonacci: {fibonacci_iteratif(angka)}")
