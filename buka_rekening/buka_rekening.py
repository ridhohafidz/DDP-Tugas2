import random
import string


def buka_rekening(filename):
    print()
    print("* BUKA REKENING *")
    name_rek = input(" Masukkan nama: ")
    try:
        saldo_rek = int(input(" Masukkan setoran awal: "))
        while True:
            pin_rek = int(input(" Masukkan nomor pin: "))
            if (len(str(pin_rek)) == 6):
                break
            else:
                print(" Masukkan 6 digit PIN")
        no_rek = "REK" + ''.join(random.choice(string.digits)
                                 for _ in range(3))
        print(" Pembukaan rekening dengan nomor " + no_rek + " atas nama " +
              name_rek + " dengan pin " + str(pin_rek) + " berhasil")
        print(" note : jangan bagikan pin anda kepada orang lain")
        file = open(filename, 'a+')
        data = [no_rek + "," + name_rek + "," +
                str(saldo_rek) + "," + str(pin_rek)]
        for list_data in data:
            file.write(str(list_data))
        file.write("\n\n")
        file.close()
    except ValueError:
        print("Inputan harus berupa angka")
        buka_rekening(filename)
