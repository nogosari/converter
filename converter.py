# A11.2019.11745
# Harits Jauza F
# Konversi Bilangan Sederhana

from tabulate import tabulate    #module tabulate
import itertools as it           #module itertools/perulangan

#Fungsi Untuk Konversi Bilangan
def libConverter(angka, pembilang, ref_output):
    result = []
    loop = True
    while loop:
        if angka >= pembilang:
            result.append(angka)
            sisa = angka % pembilang
            angka = angka // pembilang
            if sisa > 9:
                sisa = libChar(sisa)      
            divid = "{0} ================> {1}".format(pembilang, sisa)
            result.append(divid)
            ref_output.append(str(sisa))
        else:
            if angka > 9:
                angka = libChar(angka)
            result.append(angka)
            loop = False
            break
        result.append("")
    ref_output.append(str(angka))
    return result

#Fungsi Untuk Bilangan Hexa diatas 9
def libChar(angka):
    if angka == 10:
        return "A"
    elif angka == 11:
        return "B"
    elif angka == 12:
        return "C"
    elif angka == 13:
        return "D"
    elif angka == 14:
        return "E"
    elif angka == 15:
        return "F"

def listToString(s):
    list.reverse(s)
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  

def start():
    angka = int(input("Masukkan bilangan desimal untuk dikonversi : "))
    print("==================================================================")
    result_bin = []
    result_oct = []
    result_hex = []

    biner = libConverter(angka, 2, result_bin)
    octal = libConverter(angka, 8, result_oct)
    hexa = libConverter(angka, 16, result_hex)

    combine = list(it.izip_longest(biner, octal, hexa))
    header = ("Biner", "Octal", "Hexadecimal")
    print(tabulate(combine, header))
    print("==================================================================")
    print("Biner={}                Octal = {}               Hexa = {}".format(listToString(result_bin),listToString(result_oct),listToString(result_hex)))

    choose = input("Apakah Anda Ingin mengulangi? 1.Ya || 2.Tidak ====> ")
    if int(choose) == 2:
        return True
    else:
        start()
        return False
    while True:
        break

if __name__ == "__main__": 
    start()
