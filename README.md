# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

**Nama:** Nada Syifa Kamilia
**NIM:** 2225250089
**Kelas:** 3B

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai `if-elif-else` untuk mengevaluasi input berdasar banyak kondisi (tipe data, rentang nilai, dan bobot penilaian) yang terstruktur tanpa tumpang tindih.

## Cara Menjalankan
Jalankan program melalui terminal atau *command prompt* dengan mengeksekusi file Python berikut:

```bash
python3 praktik/validasi_klasifikasi_nilai.py
## Tabel Keputusan

| Kategori | Syarat (Kondisi) | Contoh Masukan (Ujian, Tugas, Hadir) |
| :--- | :--- | :--- |
| **Bukan Angka** | Gagal konversi ke `float` (`ValueError`) | `"A"`, `80`, `90` |
| **Rentang Tidak Valid** | Nilai `< 0` ATAU `> 100` | `110`, `80`, `90` |
| **Gagal Kehadiran** | `hadir < 80` (Otomatis Predikat E) | `90`, `90`, `75` |
| **Predikat A** | `nilai_akhir >= 85` dan `hadir >= 80` | `90`, `85`, `100` |
| **Predikat B** | `70 <= nilai_akhir < 85` dan `hadir >= 80` | `75`, `70`, `90` |
| **Predikat C** | `60 <= nilai_akhir < 70` dan `hadir >= 80` | `65`, `60`, `85` |
| **Predikat D** | `50 <= nilai_akhir < 60` dan `hadir >= 80` | `55`, `50`, `90` |
| **Predikat E** | `nilai_akhir < 50` dan `hadir >= 80` | `40`, `45`, `80` |

*Catatan: Nilai Akhir dihitung dari `(0.6 * ujian) + (0.4 * tugas)`.*


## Hasil Pengujian

| Masukan (U, T, H) | Keluaran Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- |
| `85`, `90`, `kosong` | Masukan ditolak: seluruh data harus berupa angka. | Masukan ditolak: seluruh data harus berupa angka. | ✅ Pass |
| `-10`, `80`, `90` | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100. | ✅ Pass |
| `100`, `100`, `70` | Nilai akhir=100.00, Predikat=E, Status=Belum lulus | Nilai akhir=100.00, Predikat=E, Status=Belum lulus | ✅ Pass |
| `90`, `80`, `100` | Nilai akhir=86.00, Predikat=A, Status=Lulus | Nilai akhir=86.00, Predikat=A, Status=Lulus | ✅ Pass |
| `65`, `65`, `80` | Nilai akhir=65.00, Predikat=C, Status=Lulus | Nilai akhir=65.00, Predikat=C, Status=Lulus | ✅ Pass |
| `45`, `50`, `90` | Nilai akhir=47.00, Predikat=E, Status=Belum lulus | Nilai akhir=47.00, Predikat=E, Status=Belum lulus | ✅ Pass |
## Refleksi

Satu masukan tidak valid yang semula terlewat adalah **input berupa huruf, teks kosong, atau spasi tambahan yang tidak disengaja** (misalnya mengetik `"A"`, `" 80 "`, atau sekadar menekan Enter tanpa memasukkan angka).

**Masalah:**
Jika program hanya mengandalkan pengecekan rentang angka (`if nilai < 0 or nilai > 100:`), program akan langsung *crash* (berhenti paksa) dan memunculkan pesan error `ValueError`. Hal ini terjadi karena program tidak bisa mengubah karakter alfabet atau teks kosong menjadi tipe data angka desimal (*float*).

**Cara menanganinya:**
Saya melakukan dua perbaikan pada kode program:
1. Menambahkan fungsi `.strip()` pada perintah input untuk secara otomatis menghapus spasi awal dan akhir yang tidak disengaja.
2. Membungkus proses konversi teks ke angka menggunakan blok **`try-except ValueError`**. 

Dengan metode ini, saat program menerima masukan huruf, program tidak lagi *crash*. Error tersebut berhasil ditangkap oleh `except` dan program merespons dengan menampilkan peringatan *"Masukan ditolak: seluruh data harus berupa angka."* secara elegan.