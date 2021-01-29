class Transaksi:
    def __init__(self):
        print('*** Menu Transaksi ***')
        print('[1] Setoran tunai')
        print('[2] Tarik tunai')
        print('[3] Transfer')
        print('[4] Lihat daftar transfer')
        inp = int(input('Masukan pilihan menu'))
        self.pilihMenu(inp)

    def pilihMenu(self, inp):
        if inp == 1:
            self.setoranTunai()
        elif inp == 2:
            self.tarikTunai()
        elif inp == 3:
            self.transfer()
        elif inp == 4:
            self.lihatDaftarTransfer()
        else:
            print('menu tidak tersedia')
            Transaksi()

    def setoranTunai(self):
        print('Setoran tunai disini')


if __name__ == "__main__":
    Transaksi()


def main():
    nomor_rekening = input("Masukkan Nomor Rekening = ")
    file = open("Nasabah.txt")
    for check in file:
        check = check.split()
        print(check)
        if nomor_rekening == check[0]:
            pin_rekening = input("Masukkan Pin Rekening = ")
            if pin_rekening == check[3]:
                print('*** Menu Transaksi ***')
                print('[1] Setoran tunai')
                print('[2] Tarik tunai')
                print('[3] Transfer')
                print('[4] Lihat daftar transfer')
                inp = int(input('Masukan pilihan menu: '))
                pilihMenu(inp)
            else:
                pass
        else:
            pass
    file.close()


def pilihMenu(inp):
    if inp == 1:
        setoranTunai()
    elif inp == 2:
        tarikTunai()
    elif inp == 3:
        transfer()
    elif inp == 4:
        lihatDaftarTransfer()
    else:
        print('menu tidak tersedia')
        main()


def setoranTunai():
    print('Setoran tunai disini')


if __name__ == "__main__":
    main()
