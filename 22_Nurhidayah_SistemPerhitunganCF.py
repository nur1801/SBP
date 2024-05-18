# Definisikan kode penyakit, nama penyakit, kode gejala, dan nama variabel gejala
kode_penyakit = {
    "P01": "Tuberkolosis",
    "P02": "Bronkitis",
    "P03": "Asma",
    "P04": "Pneumonia",
    "P05": "Penyakit Paru Obstruktif Kronis"
}

kode_gejala = {
    "G01": "Batuk yang berkepanjangan",
    "G02": "Dahak disertai darah",
    "G03": "Nafsu makan menurun",
    "G04": "Demam dan menggigil",
    "G05": "Penurunan berat badan",
    "G06": "Sesak napas",
    "G07": "Napas berbunyi",
    "G08": "Pusing dan sakit tenggorokan",
    "G09": "Nyeri dada ketika batuk",
    "G10": "Susah bernapas",
    "G11": "Dada terasa sesak, nyeri",
    "G12": "Batuk",
    "G13": "Batuk kering/berdahak",
    "G14": "Detak jantung meningkat",
    "G15": "Bau mulut",
    "G16": "Berkeringat",
    "G17": "Batuk berdahak yang berkepanjangan",
    "G18": "Mudah terkena batuk pilek/ISPA",
    "G19": "Tubuh terasa lemas / tidak bertenaga",
    "G20": "Kaki maupun pergelangan kaki membengkak",
    "G21": "Kulit dan bibir kebiruan",
    "G22": "Berkeringat dimalam hari"
}

# Aturan direpresentasikan dalam format yang sama seperti sebelumnya
aturan = {
    "P01": ["G01", "G02", "G03", "G04", "G05", "G06", "G22"],
    "P02": ["G04", "G06", "G07", "G08", "G09"],
    "P03": ["G10", "G11", "G12"],
    "P04": ["G03", "G04", "G06", "G09", "G13", "G14", "G15", "G16"],
    "P05": ["G05", "G06", "G17", "G18", "G19", "G20", "G21"]
}

# Definisi Term CF
term_cf = {
    "Tidak": 0,
    "Mungkin": 0.4,
    "Kemungkinan Besar": 0.6,
    "Hampir Pasti": 0.8,
    "Pasti": 1
}

# Input pengguna dan input pakar direpresentasikan dalam format yang sama
input_pengguna = {
    "G01": ["Batuk yang berkepanjangan", "Kemungkinan Besar", 0.6],
    "G02": ["Dahak disertai darah\t", "Mungkin\t\t", 0.4],
    "G03": ["Nafsu makan menurun\t", "Tidak\t\t", 0],
    "G04": ["Demam dan menggigil\t", "Tidak\t\t", 0],
    "G05": ["Penurunan berat badan\t", "Tidak\t\t", 0],
    "G06": ["Sesak napas\t\t", "Mungkin\t\t", 0.4],
    "G07": ["Napas berbunyi\t\t", "Mungkin\t\t", 0.4],
    "G08": ["Pusing dan sakit tenggorokan", "Kemungkinan Besar", 0.6],
    "G09": ["Nyeri dada ketika batuk\t", "Tidak\t\t", 0],
    "G10": ["Susah bernapas\t\t", "Kemungkinan Besar", 0.6],
    "G11": ["Dada terasa sesak, nyeri", "Mungkin\t\t", 0.4],
    "G12": ["Batuk\t\t\t", "Mungkin\t\t", 0.4],
    "G13": ["Batuk kering/berdahak\t", "Mungkin\t\t", 0.4],
    "G14": ["Detak jantung meningkat\t", "Kemungkinan Besar", 0.6],
    "G15": ["Bau mulut\t\t", "Tidak\t\t", 0],
    "G16": ["Berkeringat\t\t", "Mungkin\t\t", 0.4],
    "G17": ["Batuk berdahak yang berkepanjangan", "Mungkin\t", 0.4],
    "G18": ["Mudah terkena batuk pilek/ISPA", "Pasti\t\t", 1],
    "G19": ["Tubuh terasa lemas / tidak bertenaga", "Tidak\t", 0],
    "G20": ["Kaki maupun pergelangan kaki membengkak", "Tidak\t", 0],
    "G21": ["Kulit dan bibir kebiruan", "Tidak\t\t", 0],
    "G22": ["Berkeringat dimalam hari", "Tidak\t\t", 0]
}

input_pakar = {
    "P01\t": [
        ["G01", "Batuk yang berkepanjangan", 1.0],
        ["G02", "Dahak disertai darah\t", 1.0],
        ["G03", "Nafsu makan menurun\t", 0.4],
        ["G04", "Demam dan menggigil\t", 0.6],
        ["G05", "Penurunan berat badan\t", 0.4],
        ["G06", "Sesak napas\t\t", 0.6],
        ["G22", "Berkeringat dimalam hari", 0.4]
    ],
    "P02\t": [
        ["G04", "Demam dan menggigil\t", 0.6],
        ["G06", "Sesak napas\t\t", 0.6],
        ["G07", "Napas berbunyi\t\t", 1.0],
        ["G08", "Pusing dan sakit tenggorokan", 0.4],
        ["G09", "Nyeri dada ketika batuk\t", 0.6]
    ],
    "P03\t": [
        ["G10", "Susah bernapas\t\t", 1.0],
        ["G11", "Dada terasa sesak, nyeri", 0.6],
        ["G12", "Batuk\t\t\t", 0.4]
    ],
    "P04\t": [
        ["G03", "Nafsu makan menurun\t", 0.4],
        ["G04", "Demam dan menggigil\t", 0.6],
        ["G06", "Sesak napas\t\t", 0.6],
        ["G09", "Nyeri dada ketika batuk\t", 0.6],
        ["G13", "Batuk kering/berdahak\t", 1.0],
        ["G14", "Detak jantung meningkat\t", 0.6],
        ["G15", "Bau mulut\t\t", 0.6],
        ["G16", "Berkeringat\t\t", 0.4]
    ],
    "P05\t": [
        ["G05", "Penurunan berat badan\t", 0.4],
        ["G06", "Sesak napas\t\t", 0.6],
        ["G17", "Batuk berdahak yang berkepanjangan", 0.6],
        ["G18", "Mudah terkena batuk pilek/ISPA", 0.6],
        ["G19", "Tubuh terasa lemas / tidak bertenaga", 1.0],
        ["G20", "Kaki maupun pergelangan kaki membengkak", 0.6],
        ["G21", "Kulit dan bibir kebiruan", 0.6]
    ]
}

def show_kb(kode_penyakit):
    print("\nKnowledge Base:")
    print("Kode Penyakit\t|\tNama Penyakit")
    print("-----------------------------------------")
    for kode, penyakit in kode_penyakit.items():
        print(f"{kode}\t\t|\t{penyakit}")

    print("\nKode Gejala\t|\tNama Variabel Gejala")
    print("-----------------------------------------")
    for kode, gejala in kode_gejala.items():
        print(f"{kode}\t\t|\t{gejala}")

    print("\nRules:")
    for kode_penyakit, gejala_list in aturan.items():
        penyakit = kode_penyakit  # Perbaikan di sini
        print(f"\n{penyakit}:")
        for gejala in gejala_list:
            print(f" - {gejala}: {kode_gejala[gejala]}")

    print("\nTerm CF:")
    for term, cf_value in term_cf.items():
        print(f"{term}: {cf_value}")

def show_user_input(input_data):
    print("\nUser Input:")
    print("Kode Gejala\t|\tNama Variabel Gejala\t\t\t|\tMB\t\t\t|\tNilai MB")
    print("----------------------------------------------------------------------------------------------------------------------")
    for kode, data in input_data.items():
        print(f"{kode}\t\t|\t{data[0]}\t\t|\t{data[1]}\t|\t{data[2]}")

def show_expert_input(input_data):
    print("\nExpert Input:")
    print("Kode Penyakit\t|\tKode Gejala\t|\tNama Variabel Gejala\t\t\t|\tMD")
    print("----------------------------------------------------------------------------------------------------------")
    for kode_penyakit, gejala_list in input_data.items():
        nama_penyakit = kode_penyakit  # Perbaikan di sini
        for data in gejala_list:
            print(f"{nama_penyakit}\t|\t{data[0]}\t\t|\t{data[1]}\t\t|\t{data[2]}")

# Input pakar berupa dictionary dengan kode menu sebagai kunci dan kategori serta nilai MD sebagai nilai
hitung_cf = {
    "P01": [
        ["G01", "Batuk yang berkepanjangan", 0.6, 1.0],
        ["G02", "Dahak disertai darah\t", 0.4, 1.0],
        ["G03", "Nafsu makan menurun\t", 0, 0.4],
        ["G04", "Demam dan menggigil\t", 0, 0.6],
        ["G05", "Penurunan berat badan\t", 0, 0.4],
        ["G06", "Sesak napas\t\t", 0.4, 0.6],
        ["G22", "Berkeringat dimalam hari", 0, 0.4]
    ],
    "P02": [
        ["G04", "Demam dan menggigil\t", 0, 0.6],
        ["G06", "Sesak napas\t\t", 0.4, 0.6],
        ["G07", "Napas berbunyi\t\t", 0.4, 1.0],
        ["G08", "Pusing dan sakit tenggorokan", 0.6, 0.4],
        ["G09", "Nyeri dada ketika batuk\t", 0, 0.6]
    ],
    "P03": [
        ["G10", "Susah bernapas\t\t", 0.6, 1.0],
        ["G11", "Dada terasa sesak, nyeri", 0.4, 0.6],
        ["G12", "Batuk\t\t\t", 0.4, 0.4]
    ],
    "P04": [
        ["G03", "Nafsu makan menurun\t", 0, 0.4],
        ["G04", "Demam dan menggigil\t", 0, 0.6],
        ["G06", "Sesak napas\t\t", 0.4, 0.6],
        ["G13", "Batuk kering/berdahak\t", 0.4, 0.6],
        ["G14", "Detak jantung meningkat\t", 0.6, 1],
        ["G15", "Bau mulut\t\t", 0, 0.6],
        ["G16", "Berkeringat\t\t", 0.4, 0.4]
    ],
    "P05": [
        ["G05", "Penurunan berat badan\t", 0, 0.4],
        ["G06", "Sesak napas\t\t", 0.4, 0.4],
        ["G17", "Batuk berdahak yang berkepanjangan", 0.4, 0.6],
        ["G18", "Mudah terkena batuk pilek/ISPA", 1.0, 0.6],
        ["G19", "Tubuh terasa lemas / tidak bertenaga", 0, 0.6],
        ["G20", "Kaki maupun pergelangan kaki membengkak", 0, 1.0],
        ["G21", "Kulit dan bibir kebiruan", 0, 0.6]
    ]
}

def calculate_combination_cf(penyakit):
    cf_combination = 1
    for gejala in input_pengguna.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combination *= data[2] * data[3]
                break
    return cf_combination

def calculate_aggregated_cf(penyakit):
    cf_combinations = []
    for gejala in input_pengguna.keys():
        for data in hitung_cf[penyakit]:
            if gejala == data[0]:
                cf_combinations.append(data[2] * data[3])
                break

    cf_aggregated = cf_combinations[0]
    for cf in cf_combinations[1:]:
        cf_aggregated = cf_aggregated + cf - (cf_aggregated * cf)

    return cf_aggregated

def calculate_percentage(cf_combination, cf_aggregated):
    return cf_aggregated * 100

def calculate_cf(penyakit):
    cf_combination = calculate_combination_cf(penyakit)
    cf_aggregated = calculate_aggregated_cf(penyakit)
    percentage = calculate_percentage(cf_combination, cf_aggregated)
    
    # Menambahkan langkah-langkah perhitungan CF
    print("\nLangkah-langkah perhitungan CF:")
    print(f"1. Menghitung kombinasi CF: {cf_combination:.2f}")
    print(f"2. Menghitung aggregated CF: {cf_aggregated:.2f}")
    print(f"3. Menghitung presentase CF: {percentage:.2f}%")
    
    return percentage


def main():
    while True:
        print("\n========================Menu:======================")
        print("1. Knowledge Base")
        print("2. Input Pengguna")
        print("3. Input Pakar")
        print("4. Hitung CF")
        print("5. Exit")

        choice = input("Masukkan pilihan (1-5): ")

        if choice == "1":
            show_kb(kode_penyakit)
        elif choice == "2":
            show_user_input(input_pengguna)
        elif choice == "3":
            show_expert_input(input_pakar)
        elif choice == "4":
            kode_penyakit_input = input("Masukkan kode penyakit yang ingin dihitung CF-nya: ")
            if kode_penyakit_input in aturan.keys():
                cf_percentage = calculate_cf(kode_penyakit_input)
                print(f"\nHasil presentase CF untuk {kode_penyakit[kode_penyakit_input]}: {cf_percentage:.2f}%")
            else:
                print("Kode penyakit tidak valid.")
        elif choice == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")


if __name__ == "__main__":
    main()