# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Maila Andira Putri
**NIM:** 2225250126
**Kelas:** 3A

---

## Tujuan

Praktikum ini bertujuan untuk memahami penggunaan **list Python** dalam menyimpan dan mengolah kumpulan data numerik.

Melalui praktikum ini, dipelajari penggunaan indeks, slicing, manipulasi list, perulangan, fungsi, serta pengolahan data numerik seperti menghitung jumlah, rata-rata, nilai minimum, nilai maksimum, dan menentukan nilai yang lulus berdasarkan batas tertentu.

---

## Struktur Program

Struktur folder pada praktikum ini adalah sebagai berikut:

```text
pertemuan-09-list-2225250126/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
│
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

### Penjelasan File

| File                          | Keterangan                                               |
| ----------------------------- | -------------------------------------------------------- |
| `01_buat_list.py`             | Membuat list dan menampilkan jumlah data                 |
| `02_indeks_slicing.py`        | Menggunakan indeks dan slicing pada list                 |
| `03_manipulasi_list.py`       | Melakukan perubahan dan manipulasi data pada list        |
| `04_agregasi_nilai.py`        | Menghitung total, rata-rata, nilai minimum, dan maksimum |
| `05_filter_kelulusan.py`      | Menyeleksi nilai berdasarkan batas kelulusan             |
| `06_fungsi_statistik.py`      | Membuat fungsi untuk menghitung rata-rata                |
| `analisis_nilai_mahasiswa.py` | Program utama untuk menganalisis data nilai mahasiswa    |

---

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code menggunakan perintah berikut:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

Untuk menjalankan file latihan, contohnya:

```bash
python3 latihan/01_buat_list.py
```

Nama file dapat diganti sesuai dengan latihan yang ingin dijalankan.

---

## Test Case

### Test Case 1 - Menghitung Rata-rata

**Data:**

```python
[60, 70, 80]
```

**Hasil yang diharapkan:**

```text
70.00
```

**Hasil aktual:**

```text
70.00
```

**Status:** ✅ Berhasil

---

### Test Case 2 - Menentukan Nilai Minimum dan Maksimum

**Data:**

```python
[60, 70, 80]
```

**Hasil yang diharapkan:**

```text
Minimum = 60
Maksimum = 80
```

**Hasil aktual:**

```text
Minimum = 60
Maksimum = 80
```

**Status:** ✅ Berhasil

---

### Test Case 3 - Menghitung Jumlah Nilai Lulus

**Data:**

```python
[60, 70, 80]
```

**Batas kelulusan:** `60`

**Hasil yang diharapkan:**

```text
Jumlah lulus = 3
```

**Hasil aktual:**

```text
Jumlah lulus = 3
```

**Status:** ✅ Berhasil

---

### Test Case 4 - Menguji Batas Kelulusan

**Data:**

```python
[59, 60, 61]
```

**Batas kelulusan:** `60`

**Hasil yang diharapkan:**

```text
Jumlah lulus = 2
```

**Hasil aktual:**

```text
Jumlah lulus = 2
```

**Status:** ✅ Berhasil

---

### Test Case 5 - Menguji List Kosong

**Data:**

```python
[]
```

**Hasil yang diharapkan:**

```text
Rata-rata = 0.00
```

**Hasil aktual:**

```text
Rata-rata = 0.00
```

**Status:** ✅ Berhasil

---

## Hasil Program Utama

Data yang digunakan dalam program utama:

```python
[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
```

Hasil yang diperoleh:

```text
Data           : [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
Banyak data    : 10
Total          : 695
Rata-rata      : 69.50
Minimum        : 45
Maksimum       : 90
Nilai lulus    : [78, 90, 67, 60, 82, 71, 88]
Jumlah lulus   : 7
Belum lulus    : 3
```

---

## Refleksi

Pada praktikum ini saya memahami bahwa **list** digunakan untuk menyimpan beberapa data dalam satu variabel sehingga data lebih mudah diolah. Saya juga memahami bahwa indeks pada list Python dimulai dari angka `0`, sehingga elemen pertama berada pada indeks `0`.

Kesalahan yang berhasil diperbaiki adalah ketika menghitung rata-rata pada list kosong. Jika list kosong langsung dihitung menggunakan pembagian dengan jumlah data, dapat terjadi pembagian dengan nol. Oleh karena itu, fungsi `rata_rata()` dibuat dengan pengecekan terlebih dahulu agar program tidak mengalami error ketika data yang diberikan kosong.

---

## Kesimpulan

Praktikum ini membantu memahami penggunaan list Python untuk menyimpan dan mengolah data numerik. Dengan menggunakan fungsi, perulangan, indeks, dan operasi list, data nilai mahasiswa dapat diolah untuk mendapatkan informasi seperti total, rata-rata, nilai minimum, nilai maksimum, serta jumlah mahasiswa yang lulus dan belum lulus.
