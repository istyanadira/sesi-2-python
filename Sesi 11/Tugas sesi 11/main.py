from ecommerce.pricing import hitung_harga_diskon, hitung_harga_pajak, hitung_total
from ecommerce.order import buat_id_pesanan

def main():
    harga_asli = 100.0
    diskon = 10.0
    tarif_pajak = 5.0

    harga_setelah_diskon = hitung_harga_diskon(harga_asli, diskon)
    pajak = hitung_harga_pajak(harga_setelah_diskon, tarif_pajak)
    total = hitung_total(harga_setelah_diskon, pajak)
    id_pesanan = buat_id_pesanan()

    print(f"ID Pesanan: {id_pesanan}")
    print(f"Harga Asli: {harga_asli}")
    print(f"Harga Setelah Diskon: {harga_setelah_diskon}")
    print(f"Pajak: {pajak}")
    print(f"Total Belanja: {total:.2f}")

if __name__ == "__main__":
    main()