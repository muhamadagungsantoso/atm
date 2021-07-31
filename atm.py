# import module
from datetime import datetime as dt

# variable
kesempatan = 3
keluar = False
saldoBalance = 500000
validation = 2002

# function
def cekSaldo(saldo):
    print(f"\nSaldo anda sekarang adalah Rp {saldo}")

def tarikUang(saldo):
    print("\nJumlah nominal penarikan:")
    print("1. Rp 50000")
    print("2. Rp 100000")
    print("3. Rp 150000")
    print("4. Rp 200000")
    print("5. lainnya")

    cek = True
    while cek:
        pilihanPenarikan = int(input("Masukkan sesuai angka: "))

        if pilihanPenarikan == 1:
            penarikan = 50000
            break
        elif pilihanPenarikan == 2:
            penarikan = 100000
            break
        elif pilihanPenarikan == 3:
            penarikan = 150000
            break
        elif pilihanPenarikan == 4:
            penarikan = 200000
            break
        elif pilihanPenarikan == 5:
            penarikan = float(input("Masukkan nominal yang ingin ditarik: "))
            break
        else:
            print("Anda memasukkan angka yang salah!")
            cek = True

    if saldo >= penarikan:
        saldo = saldo - penarikan
        sekarang = dt.now()
        tanggalSekarang = sekarang.strftime("%A, %d-%B-%Y")

        print(f"\nPenarikan berhasil pada {tanggalSekarang}")
        print("Silahkan ambil uang dislot!")
        print(f"Saldo anda sekarang adalah Rp {saldo}")
    else:
        print("Saldo anda tidak mencukupi!")

    return saldo

def transfer(saldo):
    cek = True
    while cek:
        kodeRekening = int(input("Masukkan 10 digit kode rekening: "))
        digitKodeRekening = len(str(kodeRekening))

        if digitKodeRekening == 10:
            print("\nRekening yang anda masukkan benar!")
            jumlahTransfer = float(input("Masukkan jumlah transfer: "))

            if saldo >= jumlahTransfer:
                saldo = saldo - jumlahTransfer
                sekarang = dt.now()
                tanggalSekarang = sekarang.strftime("%A, %d-%B-%Y")

                print(f"\nTransfer berhasil pada {tanggalSekarang}")
                print(f"Saldo anda sekarang adalah Rp {saldo}")
                break
            else:
                print("Saldo anda tidak mencukupi!")
                break
        else:
            print("Kode rekening harus 10 digit!")
            cek = True

    return saldo

while kesempatan > 0:
    pin = int(input("Masukkan 4 digit PIN anda: "))
    if pin == validation:
        print("PIN anda benar")
        print("\n===SELAMAT DATANG===")

        while keluar == False:
            print("\nMenu:")
            print("1. Cek Saldo")
            print("2. Tarik Uang")
            print("3. Transfer")
            print("4. Keluar")
            option = int(input("Masukkan pilihan anda: "))

            if option == 1:
                cekSaldo(saldoBalance)
            elif option == 2:
                if saldoBalance <= 0:
                    print("Saldo anda 0 tidak bisa melakukan transaksi!")
                    continue
                else:
                    saldoBalance = tarikUang(saldoBalance)
            elif option == 3:
                if saldoBalance <= 0:
                    print("Saldo anda 0 tidak bisa melakukan transaksi!")
                    continue
                else:
                    saldoBalance = transfer(saldoBalance)
            elif option == 4:
                yakin = input("Apakah anda yakin? y|n: ")
                if yakin == "y" or yakin == "Y":
                    print("Terima Kasih!")
                    kesempatan = 0
                    keluar = True
                elif yakin == "n" or yakin == "N":
                    continue
                else:
                    print("Masukkan pilihan yang sesuai!")
            else:
                print("Masukkan pilihan yang sesuai!")
    else:
        print("PIN anda salah!")
        kesempatan = kesempatan - 1
        if kesempatan == 0:
            print("Kesempatan anda sudah habis!")