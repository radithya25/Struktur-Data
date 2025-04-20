import pandas as pd

def baca_data(C:"/Users/DELL/Downloads/Struktur_Data_Dataset_Kelas_A_B_C.xlsx"):
    data = pd.read_excel(r"C:/Users/DELL/Downloads/Struktur_Data_Dataset_Kelas_A_B_C.xlsx")
    data.columns = data.columns.str.strip().str.lower()
    return data

def linear_search(data, column, keyword):
    result = []
    for index, row in data.iterrows():
        if str(keyword).lower() in str(row[column]).lower():
            result.append(row)
    return result

def cari_biner(df, kolom, kata_kunci):
    df_sorted = df.sort_values(by=kolom).reset_index(drop=True)
    hasil = []
    kiri, kanan = 0, len(df_sorted) - 1
    kata_kunci = kata_kunci.lower()

    if kolom == "tahun terbit":
        try:
            kata_kunci = int(kata_kunci)
            df_sorted[kolom] = pd.to_numeric(df_sorted[kolom], errors='coerce').fillna(0).astype(int)
        except:
            print("Masukkan tahun dalam angka!")
            return []

    else:
        df_sorted[kolom] = df_sorted[kolom].astype(str).str.lower()

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        nilai = df_sorted.loc[tengah, kolom]

        if nilai == kata_kunci:
            hasil.append(df_sorted.loc[tengah])

            # Cek ke kiri
            i = tengah - 1
            while i >= 0 and df_sorted.loc[i, kolom] == kata_kunci:
                hasil.insert(0, df_sorted.loc[i])
                i -= 1

            # Cek ke kanan
            i = tengah + 1
            while i < len(df_sorted) and df_sorted.loc[i, kolom] == kata_kunci:
                hasil.append(df_sorted.loc[i])
                i += 1
            break
        elif kata_kunci < nilai:
            kanan = tengah - 1
        else:
            kiri = tengah + 1
    return hasil

# Menampilkan hasil
def tampilkan(hasil):
    if not hasil:
        print("Tidak ditemukan.")
    else:
        for i, row in enumerate(hasil, 1):
            print(f"\n[{i}] Judul   : {row.get('judul paper')}")
            print(f"     Tahun   : {row.get('tahun terbit')}")
            print(f"     Penulis : {row.get('nama penulis')}")
            print(f"     Mahasiswa: {row.get('nama mahasiswa')}")
            print(f"     Link    : {row.get('link paper')}")

# Program utama
def main():
    C:"/Users/DELL/Downloads/Struktur_Data_Dataset_Kelas_A_B_C.xlsx" = r"C:/Users/DELL/Downloads/Struktur_Data_Dataset_Kelas_A_B_C.xlsx"
    data = baca_data(r"C:/Users/DELL/Downloads/Struktur_Data_Dataset_Kelas_A_B_C.xlsx")


    print("=== Cari Paper ===")
    print("1. Judul\n2. Tahun\n3. Penulis\n4. Mahasiswa")
    opsi = input("Pilih (1/2/3/4): ")
    metode = input("Metode (linier/biner): ").lower()
    kata = input("Masukkan kata kunci: ")

    kolom = "judul paper"
    if opsi == "2":
        kolom = "tahun terbit"
    elif opsi == "3":
        kolom = "nama penulis"
    elif opsi == "4":
        kolom = "nama mahasiswa"

    if metode == "linier":
        hasil = linear_search(data, kolom, kata)
    elif metode == "biner":
        hasil = cari_biner(data, kolom, kata)
    else:
        print("Metode tidak dikenali.")
        return

    tampilkan(hasil)

if __name__ == "__main__":
    main()
