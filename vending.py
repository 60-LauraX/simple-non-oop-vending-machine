class Vending:
    fund = 0
    lemon = {'rasa': 'Lemon', 'harga':'10'}
    jeruk = {'rasa': 'Jeruk', 'harga':'12'}
    apel = {'rasa': 'Apel', 'harga':'11'}
    anggur = {'rasa': 'Anggur', 'harga':'8'}
    mangga = {'rasa': 'Mangga', 'harga':'9'}
    sirsak = {'rasa': 'Sirsak', 'harga':'15'}
    jambu = {'rasa': 'Jambu', 'harga':'9'}
    list = [lemon, jeruk, apel, anggur, mangga, sirsak, jambu]
    cont = True

    def main(self):
        print()
        print("Selamat Datang ke Vending Machine!")
        print("----------------------------------")
        print("Fund anda = {}".format(self.fund))
        print("1. Beli barang")
        print("2. Tambah fund")
        print("3. Refund")
        print("4. Exit")
        print("----------------------------------")
        menu = str(input("Pilih menu = "))
        if menu == "1":
            self.beliBarang()
        elif menu == "2":
            self.addFund()
        elif menu == "3":
            self.refund()
        elif menu == "4":
            self.exit()
            print("Terima kasih!")
        else:
            print("Menu tidak tersedia!")
            self.main()

    def beliBarang(self):
        dict = {}
        i = 1
        print()
        print("Selamat Datang ke Vending Machine!")
        print("----------------------------------")
        print("Pilih Barang")
        for rasa in self.list:
            print("{}. {} \t {}".format(i, rasa.get('rasa'), rasa.get('harga')))
            i = i+1
        print("----------------------------------")
        menu = str(input("Pilih barang = "))
        if menu == "1":
            hrg = self.lemon.get('harga')
            if int(self.fund) >= int(hrg):
                self.fund = int(self.fund) - int(hrg)
                print("Transaksi berhasil! Fund anda tersisa = {}".format(self.fund))
            else:
                print("Fund kurang! Silakan isi fund terlebih dahulu")
        elif menu == "2":
            hrg = self.jeruk.get('harga')
            if int(self.fund) >= int(hrg):
                self.fund = int(self.fund) - int(hrg)
                print("Transaksi berhasil! Fund anda tersisa = {}".format(self.fund))
            else:
                print("Fund kurang! Silakan isi fund terlebih dahulu")
        elif menu == "3":
            hrg = self.apel.get('harga')
            if int(self.fund) >= int(hrg):
                self.fund = int(self.fund) - int(hrg)
                print("Transaksi berhasil! Fund anda tersisa = {}".format(self.fund))
            else:
                print("Fund kurang! Silakan isi fund terlebih dahulu")
        elif menu == "4":
            hrg = self.anggur.get('harga')
            if int(self.fund) >= int(hrg):
                self.fund = int(self.fund) - int(hrg)
                print("Transaksi berhasil! Fund anda tersisa = {}".format(self.fund))
            else:
                print("Fund kurang! Silakan isi fund terlebih dahulu")
        elif menu == "5":
            hrg = self.mangga.get('harga')
            if int(self.fund) >= int(hrg):
                self.fund = int(self.fund) - int(hrg)
                print("Transaksi berhasil! Fund anda tersisa = {}".format(self.fund))
            else:
                print("Fund kurang! Silakan isi fund terlebih dahulu")
        elif menu == "6":
            hrg = self.sirsak.get('harga')
            if int(self.fund) >= int(hrg):
                self.fund = int(self.fund) - int(hrg)
                print("Transaksi berhasil! Fund anda tersisa = {}".format(self.fund))
            else:
                print("Fund kurang! Silakan isi fund terlebih dahulu")
        elif menu == "7":
            hrg = self.jambu.get('harga')
            if int(self.fund) >= int(hrg):
                self.fund = int(self.fund) - int(hrg)
                print("Transaksi berhasil! Fund anda tersisa = {}".format(self.fund))
            else:
                print("Fund kurang! Silakan isi fund terlebih dahulu")
        else:
            print("Barang tidak tersedia!")
            self.beliBarang()
    
    def addFund(self):
        print()
        print("Selamat Datang ke Vending Machine!")
        print("----------------------------------")
        self.fund = str(int(self.fund) + int(input("Silakan masukkan fund = ")))
        return self.fund

    def refund(self):
        print()
        print("Selamat Datang ke Vending Machine!")
        print("----------------------------------")
        print("Fund anda sebesar {} telah dikembalikan".format(self.fund))
        self.fund = 0
        print("Fund anda sekarang sebesar = 0")

    def exit(self):
        self.cont = False
        return self.cont

class Run:
    def main(self):
        ven = Vending()
        while ven.cont == True:
            ven.main()

if __name__ == "__main__":
    run = Run()
    run.main()