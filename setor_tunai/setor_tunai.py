import csv


def setorTunai(filename, no_rek, pin):
    print()
    print("* SETOR TUNAI *")
    nasabah = []
    with open(filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            nasabah.append(row)
    SALDOAKHIR = 0
    # indeks = 0
    for data in nasabah:
        if data['Rek'] == no_rek and data['Pin'] == pin:
            try:
                setor = int(
                    input("Masukkan Jumlah Saldo Yang Akan di Setor Tunai : "))
                SALDOAKHIR = int(data['Saldo']) + int(setor)
                # nasabah[indeks]['Saldo'] = SALDOAKHIR
                data['Saldo'] = SALDOAKHIR
                with open(filename, mode="w") as csv_file:
                    fieldnames = ['Rek', 'Nama', 'Saldo', 'Pin']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in nasabah:
                        writer.writerow(
                            {'Rek': new_data['Rek'], 'Nama': new_data['Nama'], 'Saldo': new_data['Saldo'], 'Pin': new_data['Pin']})
                    for data in nasabah:
                        if data['Rek'] == no_rek:
                            print("No. Rekening anda : " + data['Rek'] + "\n" +
                                  "Jumlah saldo yang anda Setor Tunai : " + str(setor) + "\n" +
                                  "Jumlah saldo anda sekarang : " + str(data['Saldo']))
                print("Terimakasih atas kunjungan anda ...")
            except ValueError:
                print("Inputan harus berupa angka")
                setorTunai(filename, no_rek, pin)
        # indeks = indeks + 1


# no_rek = "REK311"
# pin = "252525"
# filename = "nasabah.txt"
# setorTunai(filename, no_rek, pin)
