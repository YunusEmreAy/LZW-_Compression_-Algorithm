# Yunus Emre Ay / E-posta:TR.yunus.emre.ay@gmail.com
import time

baslangic = time.perf_counter()

with open("Main.txt", "r", encoding="utf-8") as file:
    metin = file.read()

sozluk = {"a":1,"b":2,"c":3,"d":4}
sayi = len(sozluk)+1

string_char = ""
cikti = 0
for i in metin:
    string_char += i
    if string_char in sozluk:
        continue
    else:
        cikti += 1
        sozluk[string_char] = sayi
        sayi += 1
        string_char = string_char[len(string_char)-1:len(string_char)]
cikti += 1

bit = 0
sayac = 0
while sayac < (sayi-1):
    bit += 1
    sayac = pow(2,bit)-1

print(sozluk)

bitis = time.perf_counter()

with open("LZW.txt", "w", encoding="utf-8") as file:
    file.write("Dosyanın Sıkıştırılmadan Önceki Boyutu: {} bit\n".format(3*len(metin)))
    file.write("Dosyanın Sıkıştırıldıktan Sonraki Boyutu: {} bit\n".format(bit*cikti))
    file.write("LZW Algoritmasının Çalışma Süresi: {} ms".format(str((bitis-baslangic))))

