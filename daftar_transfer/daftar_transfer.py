import csv


def daftarTransfer(filename, no_rek, pin):
    nasabah = ""
    with open(filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Rek_sumber'] == no_rek or row['Rek_tujuan'] == no_rek:
                nasabah += row['Kode_transfer'] + " " + row['Rek_sumber'] + \
                    " " + row['Rek_tujuan'] + " " + \
                    row['Nominal_transfer'] + "\n"
        if nasabah == "":
            print("Tidak dapat menampilkan data")
        else:
            print(nasabah)


# daftarTransfer("transfer.txt", "REK829", "252525")
