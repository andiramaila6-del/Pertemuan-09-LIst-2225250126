def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

lulus = nilai_lulus(nilai)

print(f"Data           : {nilai}")
print(f"Banyak data    : {len(nilai)}")
print(f"Total          : {sum(nilai)}")
print(f"Rata-rata      : {rata_rata(nilai):.2f}")
print(f"Minimum        : {min(nilai)}")
print(f"Maksimum       : {max(nilai)}")
print(f"Nilai lulus    : {lulus}")
print(f"Jumlah lulus   : {len(lulus)}")
print(f"Belum lulus    : {len(nilai) - len(lulus)}")


# TEST CASE
print("\n=== TEST CASE ===")

data1 = [60, 70, 80]
print(f"Test 1 - Rata-rata: {rata_rata(data1):.2f}")

print(f"Test 2 - Minimum: {min(data1)}, Maksimum: {max(data1)}")

print(f"Test 3 - Jumlah lulus: {len(nilai_lulus(data1))}")

data2 = [59, 60, 61]
print(f"Test 4 - Jumlah lulus: {len(nilai_lulus(data2))}")

data3 = []
print(f"Test 5 - Rata-rata list kosong: {rata_rata(data3):.2f}")