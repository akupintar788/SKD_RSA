from PyPDF2 import PdfFileWriter, PdfFileReader

# buat objek pdf writer
out = PdfFileWriter()

# buka file pdf asli
file = PdfFileReader("C:\Tugas kuliah\Smter 3\Praktik sistem keamanan data\sistem keamanan\enkripsi PDF\V3922032_Muhammad Abidin_TIE_ERD.pdf")

# identifikasi total halaman file
num = file.numPages

#program membaca setiap halaman file sesuai halaman yg diidentifikasi
for idx in range(num):
    

    page = file.getPage(idx)


    out.addPage(page)


# masukkan password enkripsi
password = "pass"

# enkripsi masing-masing halaman
out.encrypt(password)

# buka file enkripsi "myfile_encrypted.pdf"
with open("C:\Tugas kuliah\Smter 3\Praktik sistem keamanan data\sistem keamanan\enkripsi PDF\V3922032_Muhammad Abidin_TIE_ERD.pdf", "wb") as f:
    
    # simpan pdf
    out.write(f)