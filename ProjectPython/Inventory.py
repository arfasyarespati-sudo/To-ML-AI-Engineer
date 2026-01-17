import time
import os
inventory_items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
inventory_prices = [15000000, 250000, 500000, 2000000]

def clear_screen():
   \
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration):
    """Membuat efek visual teks loading selama durasi tertentu"""
    print("\nMenyiapkan data", end="")
    for _ in range(duration):
        for dot in [".  ", ".. ", "..."]:
            print(f"\rMenyiapkan data {dot}", end="", flush=True)
            time.sleep(0.33)
    print("\n")

def tampilkan_menu():
    print("="*30)
    print("   SISTEM INVENTARIS TOKO")
    print("="*30)
    print("1. Lihat Semua Barang")
    print("2. Tambah Barang Baru")
    print("3. Hapus Barang Terakhir")
    print("4. Cari Harga Barang")
    print("5. Urutkan Barang (A-Z)")
    print("6. Keluar")
    print("-"*30)

def main():
    while True:
        clear_screen()
        loading_animation(2) # Menjalankan animasi selama ~2 siklus (sekitar 2-3 detik)
        
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            print("\nDAFTAR BARANG:")
            if not inventory_items:
                print("Gudang kosong!")
            else:
                for i in range(len(inventory_items)):
                    print(f"{i+1}. {inventory_items[i]:<15} | Rp{inventory_prices[i]:>10,}")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == '2':
            nama = input("\nMasukkan nama barang baru: ")
            try:
                harga = int(input("Masukkan harga barang: "))
                inventory_items.append(nama)
                inventory_prices.append(harga)
                print(f"Sukses! {nama} telah ditambahkan.")
            except ValueError:
                print("Gagal! Harga harus berupa angka.")
            time.sleep(1.5)

        elif pilihan == '3':
            if inventory_items:
                item_dihapus = inventory_items.pop()
                harga_dihapus = inventory_prices.pop()
                print(f"\nBarang '{item_dihapus}' telah dihapus dari sistem.")
            else:
                print("\nTidak ada barang untuk dihapus.")