from abc import abstractmethod
import re
import sys
import mysql.connector
import os
import texttable

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'salaryin'
)

cursor = db.cursor()

if db.is_connected():
    print('Berhasil terhubung ke database\n')


class divisi:

    def __init__(self, namaDivisi):

        self.__namaDivisi = namaDivisi

    def tambahDivisi(self, menu=False):

        val = ('',self.__namaDivisi)
        query = 'INSERT INTO divisi (noDivisi, namaDivisi) VALUES (%s, %s)'
        cursor.execute(query, val)
        db.commit()
        print('\nData berhasil disimpan\n')

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelDivisi()

        else:
            pass

    def lihatDivisi(menu=False):

        query = 'SELECT * FROM divisi'
        cursor.execute(query)
        hasil = cursor.fetchall()

        if cursor.rowcount <= 0:
            print('Tidak ada data')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelDivisi()

        else:
            tabel = texttable.Texttable(0)
            tabel.set_cols_align(['l', 'l'])
            tabel.set_cols_dtype(['a', 'a'])
            tabel.set_cols_valign(['m', 'm'])
            tabel.add_rows([['noDivisi', 'namaDivisi']])
            for data in hasil:
                tabel.add_row([data[0], data[1]])
            print(tabel.draw())

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelDivisi()

        else:
            pass
                

    def hapusDivisi(menu=False):

        divisi.lihatDivisi()
        try:
            noDivisi = input('\nPilih no divisi (Tekan 0 untuk kembali): ')
            if noDivisi == '0':
                os.system('cls')
                return main.tabelDivisi()
            else:
                query = 'DELETE FROM divisi WHERE noDivisi = %s'
                val = (noDivisi,)
                cursor.execute(query, val)
                db.commit()
                #reset AUTO_INCREMENT
                #query = 'ALTER TABLE divisi DROP noDivisi'
                #cursor.execute(query)
                #db.commit()
                #query = 'ALTER TABLE divisi ADD noDivisi INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST'
                #cursor.execute(query)
                #db.commit()
                print('\nData berhasil dihapus')
                
        except:
            print('Error')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelDivisi()

        else:
            pass
        
    def ubahNamaDivisi(menu=False):

        divisi.lihatDivisi()
        try:
            noDivisi = int(input('\nPilih no divisi: '))
            if cursor.rowcount < noDivisi:
                print('Data tidak ada')
                passing = input('\nTekan apapun untuk lanjut\n\n')
                os.system('cls')
                return main.tabelDivisi()

            else:
                namaDivisi = input('Nama divisi baru: ')
                query = 'UPDATE divisi SET namaDivisi = %s WHERE noDivisi = %s'
                val = (namaDivisi, noDivisi)
                cursor.execute(query, val)
                db.commit()
                print('\ndata berhasil diubah')

                if menu == True:
                    passing = input('Tekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelDivisi()

                else:
                    pass

        except:
            print('Error')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelDivisi()

class karyawan:
    
    def __init__(self, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal):

        self._nama = nama
        self._jenisKelamin = jenisKelamin
        self._tanggalLahir = tanggalLahir
        self._gajiBersih = gajiBersih
        self._tunjangan = tunjangan
        self._gajiTotal = gajiTotal

    @abstractmethod
    def tambahKaryawan():
        pass
    
    @abstractmethod
    def hapusKaryawan():
        pass

    @abstractmethod
    def lihatKaryawan():
        pass

    @abstractmethod
    def ubahNama():
        pass

    @abstractmethod
    def ubahJenisKelamin():
        pass

    @abstractmethod
    def ubahTanggalLahir():
        pass

    @abstractmethod
    def ubahGajiBersih():
        pass

    @abstractmethod
    def ubahTunjangan():
        pass

    @abstractmethod
    def hitungGajiTotal():
        pass

class managerDivisi(karyawan):

    def __init__(self, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, noDivisi, bonusPerforma):
        karyawan.__init__(self, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal)
        self.__noDivisi = noDivisi
        self.__bonusPerforma = bonusPerforma

    def tambahKaryawan(self, menu=False):
        
        managerDivisi.hitungGajiTotal(self)
        query = 'INSERT INTO managerdivisi (noPegawaiManager, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, noDivisi, bonusPerforma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = ('', self._nama, self._jenisKelamin, self._tanggalLahir, self._gajiBersih, self._tunjangan, self._gajiTotal, self.__noDivisi, self.__bonusPerforma)
        cursor.execute(query, val)
        db.commit()
        print('\nData berhasil disimpan')

        if menu == True:
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def hapusKaryawan(menu=False):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (Tekan 0 untuk kembali): '))
            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelManagerDivisi()

            else:

                if cursor.rowcount < noPegawaiManager:
                    print('\nData tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi()
                
                else:
                    query = 'DELETE FROM managerdivisi WHERE noPegawaiManager = %s'
                    val = (noPegawaiManager, )
                    cursor.execute(query, val)
                    db.commit()
                    print('\nData berhasil dihapus')
        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        if menu == True:
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def lihatKaryawan(menu=False):

        query = 'SELECT * FROM managerdivisi'
        cursor.execute(query)
        hasil = cursor.fetchall()

        if cursor.rowcount <= 0:
            print('Tidak ada data')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            tabel = texttable.Texttable(0)
            tabel.set_cols_align(['l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'])
            tabel.set_cols_dtype(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
            tabel.set_cols_valign(['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm'])
            tabel.add_rows([['noPegawaiManager', 'nama', 'jenisKelamin', 'tanggalLahir', 'gajiBersih', 'tunjangan', 'gajiTotal', 'noDivisi', 'bonusPerforma']])
            for data in hasil:
                if data[2] == 0:
                    tabel.add_row([data[0], data[1], 'Perempuan', data[3], data[4], data[5], data[6], data[7], data[8]])
                else:
                    tabel.add_row([data[0], data[1], 'Laki - Laki', data[3], data[4], data[5], data[6], data[7], data[8]])
            print(tabel.draw())

            if menu == True:
                passing = input('\nTekan apapun untuk lanjut\n\n')
                os.system('cls')
                return main.tabelManagerDivisi()

            else:
                pass

    def ubahNama(menu=False):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (0 Untuk kembali): '))
            
            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelManagerDivisi()

            else:
                if cursor.rowcount < noPegawaiManager:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi()
                
                else:    
                    nama = input('\nNama baru: ')
                    query = 'UPDATE managerdivisi SET nama = %s WHERE noPegawaiManager = %s'
                    val = (nama, noPegawaiManager)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()   

        if menu == True:
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def ubahJenisKelamin(menu=False):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (0 untuk kembali): '))
            
            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:
                if cursor.rowcount < noPegawaiManager:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi()
                
                else:    
                    jenisKelamin = int(input('Jenis kelamin baru (0 Untuk Perempuan/1 Untuk Laki - Laki): '))
                    if jenisKelamin >= 2:
                        print('Input data dengan benar')
                        passing = input('\nTekan apapun untuk lanjut\n\n')
                        os.system('cls')
                        return main.tabelManagerDivisi()

                    else:
                        query = 'UPDATE managerdivisi SET jenisKelamin = %s WHERE noPegawaiManager = %s'
                        val = (jenisKelamin, noPegawaiManager)
                        cursor.execute(query, val)
                        db.commit()
                        print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        if menu == True:
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def ubahTanggalLahir(menu=True):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (0 untuk kembali): '))
            
            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelManagerDivisi()

            else:

                if cursor.rowcount < noPegawaiManager:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi()
                
                else:    
                    tanggalLahir = input('Tanggal lahir baru (YYYYMMDD): ')
                    query = 'UPDATE managerdivisi SET tanggalLahir = %s WHERE noPegawaiManager = %s'
                    val = (tanggalLahir, noPegawaiManager)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        if menu == True:
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def ubahGajiBersih(menu=False):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (0 untuk kembali): '))

            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelManagerDivisi()

            else:
                if cursor.rowcount < noPegawaiManager:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi()
                
                else:    
                    gajiBersih = int(input('Gaji bersih baru: '))
                    query = 'UPDATE managerdivisi SET gajiBersih = %s WHERE noPegawaiManager = %s'
                    val = (gajiBersih, noPegawaiManager)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM managerdivisi'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiManager:
                            gajiBersih = gajiBersih
                            tunjangan = data[5]
                            gajiTotal = data[6]
                            bonusPerforma = data[8]
                            gajiTotal = gajiBersih + tunjangan + bonusPerforma
                            query = 'UPDATE managerdivisi SET gajiTotal = %s WHERE noPegawaiManager = %s'
                            val = (gajiTotal, noPegawaiManager)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        if menu == True:
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def ubahTunjangan(menu=False):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (0 untuk kembali): '))
            
            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelManagerDivisi()

            else:
                if cursor.rowcount < noPegawaiManager:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi
                
                else:    
                    tunjangan = int(input('Tunjangan baru: '))
                    query = 'UPDATE managerdivisi SET tunjangan = %s WHERE noPegawaiManager = %s'
                    val = (tunjangan, noPegawaiManager)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM managerdivisi'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiManager:
                            gajiBersih = data[4]
                            tunjangan = tunjangan
                            gajiTotal = data[6]
                            bonusPerforma = data[8]
                            gajiTotal = gajiBersih + tunjangan + bonusPerforma
                            query = 'UPDATE managerdivisi SET gajiTotal = %s WHERE noPegawaiManager = %s'
                            val = (gajiTotal, noPegawaiManager)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def hitungGajiTotal(self):
        self._gajiTotal = self._gajiBersih + self._tunjangan + self.__bonusPerforma

    def ubahNoDivisi(menu=False):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (0 untuk kembali): '))
            
            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelManagerDivisi()

            else:
            
                if cursor.rowcount < noPegawaiManager:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi()
                
                else:    
                    noDivisi = int(input('no divisi baru: '))
                    query = 'UPDATE managerdivisi SET noDivisi = %s WHERE noPegawaiManager = %s'
                    val = (noDivisi, noPegawaiManager)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

    def ubahBonusPerforma(menu=False):

        managerDivisi.lihatKaryawan()

        try:
            noPegawaiManager = int(input('\nPilih no pegawai manager (0 untuk kembali): '))
            
            if noPegawaiManager == 0:
                os.system('cls')
                return main.tabelManagerDivisi()

            else:
                if cursor.rowcount < noPegawaiManager:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelManagerDivisi()
                
                else:    
                    bonusPerforma = int(input('Bonus performa baru: '))
                    query = 'UPDATE managerdivisi SET bonusPerforma = %s WHERE noPegawaiManager = %s'
                    val = (bonusPerforma, noPegawaiManager)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM managerdivisi'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiManager:
                            gajiBersih = data[4]
                            tunjangan = data[5]
                            gajiTotal = data[6]
                            bonusPerforma = bonusPerforma
                            gajiTotal = gajiBersih + tunjangan + bonusPerforma
                            query = 'UPDATE managerdivisi SET gajiTotal = %s WHERE noPegawaiManager = %s'
                            val = (gajiTotal, noPegawaiManager)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

        else:
            pass

class anggotaDivisi(karyawan):

    def __init__(self, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, noDivisi, bonusTugas):
        karyawan.__init__(self, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal)
        self.__noDivisi = noDivisi
        self.__bonusTugas = bonusTugas

    def tambahKaryawan(self, menu=False):
        
        anggotaDivisi.hitungGajiTotal(self)
        query = 'INSERT INTO anggotadivisi (noPegawaiAnggota, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, noDivisi, bonusTugas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = ('', self._nama, self._jenisKelamin, self._tanggalLahir, self._gajiBersih, self._tunjangan, self._gajiTotal, self.__noDivisi, self.__bonusTugas)
        cursor.execute(query, val)
        db.commit()
        print('Data berhasil disimpan')

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

    def hapusKaryawan(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai anggota (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:

                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()

                else:
                    query = 'DELETE FROM anggotadivisi WHERE noPegawaiAnggota = %s'
                    val = (noPegawaiAnggota, )
                    cursor.execute(query, val)
                    db.commit()
                    print('\nData berhasil dihapus')
        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

    def lihatKaryawan(menu=False):

        query = 'SELECT * FROM anggotadivisi'
        cursor.execute(query)
        hasil = cursor.fetchall()

        if cursor.rowcount <= 0:
            print('Tidak ada data')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()
        else:
            tabel = texttable.Texttable(0)
            tabel.set_cols_align(['l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'])
            tabel.set_cols_dtype(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
            tabel.set_cols_valign(['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm'])
            tabel.add_rows([['noPegawaiAnggota', 'nama', 'jenisKelamin', 'tanggalLahir', 'gajiBersih', 'tunjangan', 'gajiTotal', 'noDivisi', 'bonusTugas']])
            for data in hasil:
                if data[2] == 0:
                    tabel.add_row([data[0], data[1], 'Perempuan', data[3], data[4], data[5], data[6], data[7], data[8]])
                else:
                    tabel.add_row([data[0], data[1], 'Laki - Laki', data[3], data[4], data[5], data[6], data[7], data[8]])
            print(tabel.draw())

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

    def ubahNama(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai anggota (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:

                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()
                
                else:    
                    nama = input('Nama baru: ')
                    query = 'UPDATE anggotadivisi SET nama = %s WHERE noPegawaiAnggota = %s'
                    val = (nama, noPegawaiAnggota)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()  

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

    def ubahJenisKelamin(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai anggota (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:
                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()
                
                else:    
                    jenisKelamin = int(input('Jenis kelamin baru (0 Untuk Perempuan/1 Untuk Laki - Laki): '))
                    if jenisKelamin >= 2:
                        print('Input data dengan benar')
                        passing = input('\nTekan apapun untuk lanjut\n\n')
                        os.system('cls')
                        return main.tabelAnggotaDivisi()

                    else:
                        query = 'UPDATE anggotadivisi SET jenisKelamin = %s WHERE noPegawaiAnggota = %s'
                        val = (jenisKelamin, noPegawaiAnggota)
                        cursor.execute(query, val)
                        db.commit()
                        print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

    def ubahTanggalLahir(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai anggota (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:
                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()
                
                else:    
                    tanggalLahir = input('Tanggal lahir baru (YYYYMMDD): ')
                    query = 'UPDATE anggotadivisi SET tanggalLahir = %s WHERE noPegawaiAnggota = %s'
                    val = (tanggalLahir, noPegawaiAnggota)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass
        

    def ubahGajiBersih(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai anggota (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:
                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()
                
                else:    
                    gajiBersih = int(input('Gaji bersih baru: '))
                    query = 'UPDATE anggotadivisi SET gajiBersih = %s WHERE noPegawaiAnggota = %s'
                    val = (gajiBersih, noPegawaiAnggota)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM anggotadivisi'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiAnggota:
                            gajiBersih = gajiBersih
                            tunjangan = data[5]
                            gajiTotal = data[6]
                            bonusTugas = data[8]
                            gajiTotal = gajiBersih + tunjangan + bonusTugas
                            query = 'UPDATE anggotadivisi SET gajiTotal = %s WHERE noPegawaiAnggota = %s'
                            val = (gajiTotal, noPegawaiAnggota)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

    def ubahTunjangan(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai anggota (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:
                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()
                
                else:    
                    tunjangan = int(input('Tunjangan baru: '))
                    query = 'UPDATE anggotadivisi SET tunjangan = %s WHERE noPegawaiAnggota = %s'
                    val = (tunjangan, noPegawaiAnggota)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM anggotadivisi'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiAnggota:
                            gajiBersih = data[4]
                            tunjangan = tunjangan
                            gajiTotal = data[6]
                            bonusTugas = data[8]
                            gajiTotal = gajiBersih + tunjangan + bonusTugas
                            query = 'UPDATE anggotadivisi SET gajiTotal = %s WHERE noPegawaiAnggota = %s'
                            val = (gajiTotal, noPegawaiAnggota)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass 


    def hitungGajiTotal(self):
        self._gajiTotal = self._gajiBersih + self._tunjangan + self.__bonusTugas

    def ubahNoDivisi(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai manager (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:
                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()
                
                else:    
                    noDivisi = int(input('no divisi baru: '))
                    query = 'UPDATE anggotadivisi SET noDivisi = %s WHERE noPegawaiAnggota = %s'
                    val = (noDivisi, noPegawaiAnggota)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

    def ubahBonusTugas(menu=False):

        anggotaDivisi.lihatKaryawan()

        try:
            noPegawaiAnggota = int(input('\nPilih no pegawai anggota (0 untuk kembali): '))
            
            if noPegawaiAnggota == 0:
                os.system('cls')
                return main.tabelAnggotaDivisi()

            else:
                if cursor.rowcount < noPegawaiAnggota:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelAnggotaDivisi()
                
                else:    
                    bonusTugas = int(input('Bonus tugas baru: '))
                    query = 'UPDATE anggotadivisi SET bonusTugas = %s WHERE noPegawaiAnggota = %s'
                    val = (bonusTugas, noPegawaiAnggota)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM anggotadivisi'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiAnggota:
                            gajiBersih = data[4]
                            tunjangan = data[5]
                            gajiTotal = data[6]
                            bonusTugas = bonusTugas
                            gajiTotal = gajiBersih + tunjangan + bonusTugas
                            query = 'UPDATE anggotadivisi SET gajiTotal = %s WHERE noPegawaiAnggota = %s'
                            val = (gajiTotal, noPegawaiAnggota)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

        else:
            pass

class ob(karyawan):

    def __init__(self, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, bonusHadir):
        karyawan.__init__(self, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal)
        self.__bonusHadir = bonusHadir

    def tambahKaryawan(self, menu=True):
        
        ob.hitungGajiTotal(self)
        query = 'INSERT INTO ob (noPegawaiOB, nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, bonusHadir) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        val = ('', self._nama, self._jenisKelamin, self._tanggalLahir, self._gajiBersih, self._tunjangan, self._gajiTotal, self.__bonusHadir)
        cursor.execute(query, val)
        db.commit()
        print('Data berhasil disimpan')

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass


    def hapusKaryawan(menu=True):

        ob.lihatKaryawan()

        try:
            noPegawaiOB = int(input('\nPilih no pegawai ob (0 untuk kembali): '))
            
            if noPegawaiOB == 0:
                os.system('cls')
                return main.tabelOB()

            else:
                if cursor.rowcount < noPegawaiOB:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelOB()

                else:
                    query = 'DELETE FROM ob WHERE noPegawaiOB = %s'
                    val = (noPegawaiOB, )
                    cursor.execute(query, val)
                    db.commit()
                    print('\nData berhasil dihapus')
        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

    def lihatKaryawan(menu=False):

        query = 'SELECT * FROM ob'
        cursor.execute(query)
        hasil = cursor.fetchall()

        if cursor.rowcount <= 0:
            print('Tidak ada data')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()
        else:
            tabel = texttable.Texttable(0)
            tabel.set_cols_align(['l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'])
            tabel.set_cols_dtype(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
            tabel.set_cols_valign(['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm'])
            tabel.add_rows([['noPegawaiOB', 'nama', 'jenisKelamin', 'tanggalLahir', 'gajiBersih', 'tunjangan', 'gajiTotal', 'bonusHadir']])
            for data in hasil:
                if data[2] == 0:
                    tabel.add_row([data[0], data[1], 'Perempuan', data[3], data[4], data[5], data[6], data[7]])
                else:
                    tabel.add_row([data[0], data[1], 'Laki - Laki', data[3], data[4], data[5], data[6], data[7]])
            print(tabel.draw())

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

    def ubahNama(menu=False):

        ob.lihatKaryawan()

        try:
            noPegawaiOB = int(input('\nPilih no pegawai ob (0 untuk kembali): '))
            
            if noPegawaiOB == 0:
                os.system('cls')
                return main.tabelOB()

            else:
                if cursor.rowcount < noPegawaiOB:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelOB()
                
                else:    
                    nama = input('Nama baru: ')
                    query = 'UPDATE ob SET nama = %s WHERE noPegawaiOB = %s'
                    val = (nama, noPegawaiOB)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

    def ubahJenisKelamin(menu=True):

        ob.lihatKaryawan()

        try:
            noPegawaiOB = int(input('\nPilih no pegawai ob (0 untuk kembali): '))
            
            if noPegawaiOB == 0:
                os.system('cls')
                return main.tabelOB()

            else:
                if cursor.rowcount < noPegawaiOB:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelOB()
                
                else:    
                    jenisKelamin = int(input('Jenis kelamin baru (0 Untuk Perempuan/1 Untuk Laki - Laki): '))
                    if jenisKelamin >= 2:
                        print('Input data dengan benar')
                        passing = input('\nTekan apapun untuk lanjut\n\n')
                        os.system('cls')
                        return main.tabelOB()

                    else:
                        query = 'UPDATE ob SET jenisKelamin = %s WHERE noPegawaiOB = %s'
                        val = (jenisKelamin, noPegawaiOB)
                        cursor.execute(query, val)
                        db.commit()
                        print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

    def ubahTanggalLahir(menu=True):

        ob.lihatKaryawan()

        try:
            noPegawaiOB = int(input('\nPilih no pegawai ob (0 untuk kembali): '))

            if noPegawaiOB == 0:
                os.system('cls')
                return main.tabelOB()

            else:
                if cursor.rowcount < noPegawaiOB:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelOB()
                
                else:    
                    tanggalLahir = input('Tanggal lahir baru (YYYYMMDD): ')
                    query = 'UPDATE ob SET tanggalLahir = %s WHERE noPegawaiOB = %s'
                    val = (tanggalLahir, noPegawaiOB)
                    cursor.execute(query, val)
                    db.commit()
                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

    def ubahGajiBersih(menu=True):

        ob.lihatKaryawan()

        try:
            noPegawaiOB = int(input('\nPilih no pegawai ob (0 untuk kembali): '))
            
            if noPegawaiOB == 0:
                os.system('cls')
                return main.tabelOB()

            else:
                if cursor.rowcount < noPegawaiOB:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelOB()
                
                else:    
                    gajiBersih = int(input('Gaji bersih baru: '))
                    query = 'UPDATE ob SET gajiBersih = %s WHERE noPegawaiOB = %s'
                    val = (gajiBersih, noPegawaiOB)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM ob'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiOB:
                            gajiBersih = gajiBersih
                            tunjangan = data[5]
                            gajiTotal = data[6]
                            bonusHadir = data[7]
                            gajiTotal = gajiBersih + tunjangan + bonusHadir
                            query = 'UPDATE ob SET gajiTotal = %s WHERE noPegawaiOB = %s'
                            val = (gajiTotal, noPegawaiOB)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

    def hitungGajiTotal(self):
        self._gajiTotal = self._gajiBersih + self._tunjangan + self.__bonusHadir

    def ubahTunjangan(menu=True):

        ob.lihatKaryawan()

        try:
            noPegawaiOB = int(input('\nPilih no pegawai ob (0 untuk kembaali): '))
            
            if noPegawaiOB == 0:
                os.system('cls')
                return main.tabelOB()

            else:
                if cursor.rowcount < noPegawaiOB:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelOB()
                
                else:    
                    tunjangan = int(input('Tunjangan baru: '))
                    query = 'UPDATE ob SET tunjangan = %s WHERE noPegawaiOB = %s'
                    val = (tunjangan, noPegawaiOB)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM ob'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiOB:
                            gajiBersih = data[4]
                            tunjangan = tunjangan
                            gajiTotal = data[6]
                            bonusHadir = data[7]
                            gajiTotal = gajiBersih + tunjangan + bonusHadir
                            query = 'UPDATE ob SET gajiTotal = %s WHERE noPegawaiOB = %s'
                            val = (gajiTotal, noPegawaiOB)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

    def ubahBonusHadir(menu=True):

        ob.lihatKaryawan()

        try:
            noPegawaiOB = int(input('\nPilih no pegawai ob: '))
            
            if noPegawaiOB == 0:
                os.system('cls')
                return main.tabelOB()

            else:
                if cursor.rowcount < noPegawaiOB:
                    print('Data tidak ada')
                    passing = input('\nTekan apapun untuk lanjut\n\n')
                    os.system('cls')
                    return main.tabelOB()
                
                else:    
                    bonusHadir = int(input('Bonus hadir baru: '))
                    query = 'UPDATE ob SET bonusHadir = %s WHERE noPegawaiOB = %s'
                    val = (bonusHadir, noPegawaiOB)
                    cursor.execute(query, val)
                    db.commit()

                    query = 'SELECT * FROM ob'
                    cursor.execute(query)
                    hasil = cursor.fetchall()
                    for data in hasil:
                        if data[0] == noPegawaiOB:
                            gajiBersih = data[4]
                            tunjangan = data[5]
                            gajiTotal = data[6]
                            bonusHadir = bonusHadir
                            gajiTotal = gajiBersih + tunjangan + bonusHadir
                            query = 'UPDATE ob SET gajiTotal = %s WHERE noPegawaiOB = %s'
                            val = (gajiTotal, noPegawaiOB)
                            cursor.execute(query, val)
                            db.commit()

                        else:
                            pass

                    print('\ndata berhasil diubah')

        except:
            print('Error')
            passing = input('\nTekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        if menu == True:
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB()

        else:
            pass

class main:

    def list():

        print('=' * 3 , "APLIKASI SALARY.IN", '=' * 3)
        print('1. Pilih Tabel')
        print('2. Keluar')
        
        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':

            os.system('cls')
            return main.tabel()

        elif pilihan == '2':

            exit

        else:

            print('\nInputan anda salah')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.list()

    def tabel():

        print('=' * 3 , "APLIKASI SALARY.IN", '=' * 3)
        print('1. Divisi')
        print('2. Manager Divisi')
        print('3. Anggota Divisi')
        print('4. OB')
        print('5. Kembali')

        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':

            os.system('cls')
            return main.tabelDivisi()

        elif pilihan == '2':

            os.system('cls')
            return main.tabelManagerDivisi()

        elif pilihan == '3':

            os.system('cls')
            return main.tabelAnggotaDivisi()

        elif pilihan == '4':

            os.system('cls')
            return main.tabelOB()

        elif pilihan == '5':

            os.system('cls')
            return main.list()

        else:

            print('\nInputan anda salah')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabel()      

    def tabelDivisi():
        print('=' * 3 , "APLIKASI SALARY.IN", '=' * 3)
        print('\nTABEL : DIVISI\n')
        print('1. Lihat Divisi')
        print('2. Tambah Divisi')
        print('3. Hapus Divisi')
        print('4. Ubah Nama Divisi')
        print('5. Kembali')
        print('6. Kembali ke menu utama')

        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':

            os.system('cls')
            return divisi.lihatDivisi(menu=True)

        elif pilihan == '2':

            os.system('cls')
            print('TAMBAH DIVISI')

            try:
                namaDivisi = input('Masukkan nama divisi: ')
                divisi(namaDivisi).tambahDivisi(menu=True)


            except:
                print('Error')
                return main.tabelDivisi()

        elif pilihan == '3':

            os.system('cls')
            print('HAPUS DIVISI')
            divisi.hapusDivisi(menu=True)

        elif pilihan == '4':
            
            os.system('cls')
            print('UBAH NAMA DIVISI')
            divisi.ubahNamaDivisi(menu=True)

        elif pilihan == '5':

            os.system('cls')
            return main.tabel()

        elif pilihan == '6':

            os.system('cls')
            return main.list()

        else:

            print('\nInputan anda salah')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelDivisi()  

    def tabelManagerDivisi():
        print('=' * 3 , "APLIKASI SALARY.IN", '=' * 3)
        print('\nTABEL : MANAGER DIVISI\n')
        print('1. Lihat Karyawan Manager Divisi')
        print('2. Tambah Karyawan Manager Divisi')
        print('3. Hapus Karyawan Manager Divisi')
        print('4. Ubah Nama Karyawan Manager Divisi')
        print('5. Ubah Jenis Kelamin Karyawan Manager Divisi')
        print('6. Ubah Tanggal Lahir Karyawan Manager Divisi')
        print('7. Ubah Gaji Bersih Karyawan Manager Divisi')
        print('8. Ubah Tunjangan Karyawan Manager Divisi')
        print('9. Ubah no Divisi Karyawan Manager Divisi')
        print('10. Ubah Bonus Performa Karyawan Manager Divisi')
        print('11. Kembali')
        print('12. Kembali ke menu utama')

        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':

            os.system('cls')
            return managerDivisi.lihatKaryawan(menu=True)

        elif pilihan == '2':

            os.system('cls')
            print('TAMBAH KARYAWAN MANAGER DIVISI')
            
            nama = input('Masukkan nama: ')
            jenisKelamin = int(input('Jenis kelamin (0 untuk Perempuan/1 untuk Laki - Laki): '))
            if jenisKelamin >= 2:
                print('\nMasukkan inputan dengan benar')
                passing = input('\nTekan apapun untuk lanjut\n\n')
                os.system('cls')
                return main.tabelManagerDivisi()
            else:
                pass
            tanggalLahir = input('Masukkan tanggal lahir (YYYY-MM-DD): ')
            gajiBersih = int(input('Masukkan gaji bersih: '))
            tunjangan = int(input('Masukkan tunjangan: '))
            gajiTotal = 0
            noDivisi = int(input('Masukkan no divisi: '))
            bonusPerforma = int(input('Masukkan bonus performa: '))
            managerDivisi(nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, noDivisi, bonusPerforma).tambahKaryawan(menu=True)

        elif pilihan == '3':

            os.system('cls')
            managerDivisi.hapusKaryawan(menu=True)

        elif pilihan == '4':

            os.system('cls')
            managerDivisi.ubahNama(menu=True)

        elif pilihan == '5':

            os.system('cls')
            managerDivisi.ubahJenisKelamin(menu=True)

        elif pilihan == '6':

            os.system('cls')
            managerDivisi.ubahTanggalLahir(menu=True)

        elif pilihan == '7':

            os.system('cls')
            managerDivisi.ubahGajiBersih(menu=True)

        elif pilihan == '8':
            
            os.system('cls')
            managerDivisi.ubahTunjangan(menu=True)

        elif pilihan == '9':

            os.system('cls')
            managerDivisi.ubahNoDivisi(menu=True)

        elif pilihan =='10':

            os.system('cls')
            managerDivisi.ubahBonusPerforma(menu=True)

        elif pilihan == '11':

            os.system('cls')
            return main.tabel()

        elif pilihan == '12':

            os.system('cls')
            return main.list()

        else:

            print('\nInputan anda salah')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelManagerDivisi()

    def tabelAnggotaDivisi():
        print('=' * 3 , "APLIKASI SALARY.IN", '=' * 3)
        print('\nTABEL : ANGGOTA DIVISI\n')
        print('1. Lihat Anggota Divisi')
        print('2. Tambah Anggota Divisi')
        print('3. Hapus Anggota Divisi')
        print('4. Ubah Nama Anggota Divisi')
        print('5. Ubah Jenis Kelamin Anggota Divisi')
        print('6. Ubah Tanggal Lahir Anggota Divisi')
        print('7. Ubah Gaji Bersih Anggota Divisi')
        print('8. Ubah Tunjangan Anggota Divisi')
        print('9. Ubah no Divisi Anggota Divisi')
        print('10. Ubah Bonus Tugas Anggota Divisi')
        print('11. Kembali')
        print('12. Kembali ke menu utama')

        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':

            os.system('cls')
            return anggotaDivisi.lihatKaryawan(menu=True)

        elif pilihan == '2':

            os.system('cls')
            print('TAMBAH KARYAWAN ANGGOTA DIVISI')
            
            nama = input('Masukkan nama: ')
            jenisKelamin = int(input('Jenis kelamin (0 untuk Perempuan/1 untuk Laki - Laki): '))
            if jenisKelamin >= 2:
                print('\nMasukkan inputan dengan benar')
                passing = input('\nTekan apapun untuk lanjut\n\n')
                os.system('cls')
                return main.tabelAnggotaDivisi()
            else:
                pass
            tanggalLahir = input('Masukkan tanggal lahir (YYYY-MM-DD): ')
            gajiBersih = int(input('Masukkan gaji bersih: '))
            tunjangan = int(input('Masukkan tunjangan: '))
            gajiTotal = 0
            noDivisi = int(input('Masukkan no divisi: '))
            bonusTugas = int(input('Masukkan bonus tugas: '))
            anggotaDivisi(nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, noDivisi, bonusTugas).tambahKaryawan(menu=True)

        elif pilihan == '3':

            os.system('cls')
            anggotaDivisi.hapusKaryawan(menu=True)

        elif pilihan == '4':

            os.system('cls')
            anggotaDivisi.ubahNama(menu=True)

        elif pilihan == '5':

            os.system('cls')
            anggotaDivisi.ubahJenisKelamin(menu=True)

        elif pilihan == '6':

            os.system('cls')
            anggotaDivisi.ubahTanggalLahir(menu=True)

        elif pilihan == '7':

            os.system('cls')
            anggotaDivisi.ubahGajiBersih(menu=True)

        elif pilihan == '8':
            
            os.system('cls')
            anggotaDivisi.ubahTunjangan(menu=True)

        elif pilihan == '9':

            os.system('cls')
            anggotaDivisi.ubahNoDivisi(menu=True)

        elif pilihan =='10':

            os.system('cls')
            anggotaDivisi.ubahBonusTugas(menu=True)

        elif pilihan == '11':

            os.system('cls')
            return main.tabel()

        elif pilihan == '12':

            os.system('cls')
            return main.list()

        else:

            print('\nInputan anda salah')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelAnggotaDivisi()

    def tabelOB():
        print('=' * 3 , "APLIKASI SALARY.IN", '=' * 3)
        print('\nTABEL : ANGGOTA DIVISI\n')
        print('1. Lihat OB')
        print('2. Tambah OB')
        print('3. Hapus OB')
        print('4. Ubah Nama OB')
        print('5. Ubah Jenis Kelamin OB')
        print('6. Ubah Tanggal Lahir OB')
        print('7. Ubah Gaji Bersih OB')
        print('8. Ubah Tunjangan OB')
        print('9. Ubah Bonus Hadir OB')
        print('10. Kembali')
        print('11. Kembali ke menu utama')

        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':

            os.system('cls')
            return ob.lihatKaryawan(menu=True)

        elif pilihan == '2':

            os.system('cls')
            print('TAMBAH KARYAWAN OB')
            
            nama = input('Masukkan nama: ')
            jenisKelamin = int(input('Jenis kelamin (0 untuk Perempuan/1 untuk Laki - Laki): '))
            if jenisKelamin >= 2:
                print('\nMasukkan inputan dengan benar')
                passing = input('\nTekan apapun untuk lanjut\n\n')
                os.system('cls')
                return main.tabelOB()
            else:
                pass
            tanggalLahir = input('Masukkan tanggal lahir (YYYY-MM-DD): ')
            gajiBersih = int(input('Masukkan gaji bersih: '))
            tunjangan = int(input('Masukkan tunjangan: '))
            gajiTotal = 0
            bonusHadir = int(input('Masukkan bonus tugas: '))
            ob(nama, jenisKelamin, tanggalLahir, gajiBersih, tunjangan, gajiTotal, bonusHadir).tambahKaryawan(menu=True)

        elif pilihan == '3':

            os.system('cls')
            ob.hapusKaryawan(menu=True)

        elif pilihan == '4':

            os.system('cls')
            ob.ubahNama(menu=True)

        elif pilihan == '5':

            os.system('cls')
            ob.ubahJenisKelamin(menu=True)

        elif pilihan == '6':

            os.system('cls')
            ob.ubahTanggalLahir(menu=True)

        elif pilihan == '7':

            os.system('cls')
            ob.ubahGajiBersih(menu=True)

        elif pilihan == '8':
            
            os.system('cls')
            ob.ubahTunjangan(menu=True)

        elif pilihan =='9':

            os.system('cls')
            ob.ubahBonusHadir(menu=True)

        elif pilihan == '10':

            os.system('cls')
            return main.tabel()

        elif pilihan == '11':

            os.system('cls')
            return main.list()

        else:

            print('\nInputan anda salah')
            passing = input('Tekan apapun untuk lanjut\n\n')
            os.system('cls')
            return main.tabelOB() 

main.list()