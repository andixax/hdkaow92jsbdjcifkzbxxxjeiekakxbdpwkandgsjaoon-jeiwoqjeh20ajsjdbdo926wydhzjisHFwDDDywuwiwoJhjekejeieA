import math

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Pembagian dengan nol tidak diperbolehkan."
    return a / b

def pangkat(a, b):
    return a ** b

def akar(a):
    if a < 0:
        return "Akar kuadrat dari bilangan negatif tidak diperbolehkan."
    return math.sqrt(a)

def logaritma(a, base=10):
    if a <= 0:
        return "Logaritma dari bilangan nol atau negatif tidak diperbolehkan."
    return math.log(a, base)

def faktorial(a):
    if a < 0:
        return "Faktorial dari bilangan negatif tidak diperbolehkan."
    return math.factorial(a)

def modulo(a, b):
    return a % b

def sinus(a):
    return math.sin(math.radians(a))

def kosinus(a):
    return math.cos(math.radians(a))

def tangen(a):
    return math.tan(math.radians(a))

def cotangen(a):
    if tangen(a) == 0:
        return "Cotangen tidak terdefinisi untuk sudut 0 derajat."
    return 1 / tangen(a)

def secan(a):
    if kosinus(a) == 0:
        return "Secan tidak terdefinisi untuk sudut 90 derajat."
    return 1 / kosinus(a)

def kosecan(a):
    if sinus(a) == 0:
        return "Kosecan tidak terdefinisi untuk sudut 0 derajat."
    return 1 / sinus(a)

def arsinus(a):
    if a < -1 or a > 1:
        return "Masukkan harus antara -1 dan 1 untuk arsinus."
    return math.degrees(math.asin(a))

def arkosinus(a):
    if a < -1 or a > 1:
        return "Masukkan harus antara -1 dan 1 untuk arkosinus."
    return math.degrees(math.acos(a))

def artangen(a):
    return math.degrees(math.atan(a))

def logaritma_natural(a):
    if a <= 0:
        return "Logaritma dari bilangan nol atau negatif tidak diperbolehkan."
    return math.log(a)

def main():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Eksponensial (Pangkat)")
    print("6. Akar Kuadrat")
    print("7. Logaritma")
    print("8. Faktorial")
    print("9. Modulo")
    print("10. Sinus")
    print("11. Kosinus")
    print("12. Tangen")
    print("13. Cotangen")
    print("14. Secan")
    print("15. Kosecan")
    print("16. Arsinus")
    print("17. Arkosinus")
    print("18. Artangen")
    print("19. Logaritma Natural")
    print("20. Hiperbola Sinus")

    pilihan = input("Masukkan pilihan (1-20): ")

    if pilihan in [str(i) for i in range(1, 21)]:
        if pilihan in ['1', '2', '3', '4', '5', '9']:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            if pilihan == '1':
                print(f"Hasil: {tambah(a, b)}")
            elif pilihan == '2':
                print(f"Hasil: {kurang(a, b)}")
            elif pilihan == '3':
                print(f"Hasil: {kali(a, b)}")
            elif pilihan == '4':
                print(f"Hasil: {bagi(a, b)}")
            elif pilihan == '5':
                print(f"Hasil: {pangkat(a, b)}")
            elif pilihan == '9':
                print(f"Hasil: {modulo(a, b)}")
        elif pilihan == '6':
            a = float(input("Masukkan angka: "))
            print(f"Hasil: {akar(a)}")
        elif pilihan == '7':
            a = float(input("Masukkan angka: "))
            base = float(input("Masukkan basis logaritma (default 10): ") or 10)
            print(f"Hasil: {logaritma(a, base)}")
        elif pilihan == '8':
            a = int(input("Masukkan angka: "))
            print(f"Hasil: {faktorial(a)}")
        elif pilihan == '10':
            a = float(input("Masukkan sudut dalam derajat: "))
            print(f"Hasil: {sinus(a)}")
        elif pilihan == '11':
            a = float(input("Masukkan sudut dalam derajat: "))
            print(f"Hasil: {kosinus(a)}")
        elif pilihan == '12':
            a = float(input("Masukkan sudut dalam derajat: "))
            print(f"Hasil: {tangen(a)}")
        elif pilihan == '13':
            a = float(input("Masukkan sudut dalam derajat: "))
            print(f"Hasil: {cotangen(a)}")
        elif pilihan == '14':
            a = float(input("Masukkan sudut dalam derajat: "))
            print(f"Hasil: {secan(a)}")
        elif pilihan == '15':
            a = float(input("Masukkan sudut dalam derajat: "))
            print(f"Hasil: {kosecan(a)}")
        elif pilihan == '16':
            a = float(input("Masukkan nilai: "))
            print(f"Hasil: {arsinus(a)}")
        elif pilihan == '17':
            a = float(input("Masukkan nilai: "))
            print(f"Hasil: {arkosinus(a)}")
        elif pilihan == '18':
            a = float(input("Masukkan nilai: "))
            print(f"Hasil: {artangen(a)}")
        elif pilihan == '19':
            a = float(input("Masukkan angka: "))
            print(f"Hasil: {logaritma_natural(a)}")
        elif pilihan == '20':
            a = float(input("Masukkan angka: "))
            print(f"Hasil: {sinh(a)}")

if __name__ == "__main__":
    main()
