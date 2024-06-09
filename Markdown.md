# Proyek AKhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan Lembaga Academic yang telah berdiri dari tahun 2000 dan telah menjadi salah satu lembaga academic yang memiliki reputasi sangat baik. saat ini Jaya Jaya Institut memiliki lebih dari 4000 mahasiswa yang tersebar di berbagai course. Namun, saat ini Jaya Jaya Institu mengalami permasalahan academic yang tentunya akan berpengaruh dengan kualitas pendidiakan di lembaga tersebut hingga akan menurunkan reputasi Jaya Jaya Intitiut sendiri. Oleh karena itu, lembaga academic tersebut meminta saya sebagai seorang data scientist untuk mengidentifikasi permasalahan tersebut hingga menemukan solusi agar Jaya Jaya Institut secepat mungkin dapat membenahinya. Adapun masalah yang dihadapi akan dituliskan pada permasalahan bisnis.

## Permasahalan Bisnis
Saat ini Jaya Jaya Institut memiliki pernmasalahan yaitu tingginya angka mahasiswa yang berstatus Dropout. Tentu hal ini akan menjadi masalah besar dikemudian hari jika tidak dibenahi sesegera mungkin seperti kualitas pendidikan hingga ketertarikan lulusan baru untuk mendaftar di Jaya Jaya institut menurun. Selain itu, dampak negatif yang diterima oleh academic adalah berkurangnya modal aset sehingga academic kesulitan dalam mengembangkan academic seperti membuat infrastruktur baru untuk lingkungan academic, fasilitas pendukung proses belajar mahasiswa hingga menurunnya penyerapan tenaga kerja baru seperti dosen, staff academic dan lain-lain.

## Cakupan proyek
Di dalam proyek ini cakupan proyek yang akan saya buat adalah sebagai berikut:
1. Menggunakan bahasa python
2. menggunakan visual code untuk bingkai kerja
3. menyiapkan environment menggunakan anaconda dan menginstall library-library yang dibutuhkan
4. Membuat visualisasi data untuk mempermudah dalam menemukan informasi lebih dalam 
6. Membuat model machine learning dengan menguji berbagai model algoritma dan menggunakan model algoritma terbaik untuk proses prediction
7. Membuat prototype 
8. Membuat proses deployment menggunakan streamnlit
9. Membuat business dashboard menggunakan Tableau

## Persiapan
1. Sumber data : 'https://raw.github.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv'
2. Setup Environment
### Setup Environment - Anaconda
```
conda create --name base python=3.11.7
conda activate base
pip install -r requirements.txt
```

## Business Dashboard
link Tableau : https://public.tableau.com/views/BusinessDashboard_17176476133220/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link
Adapun untuk memantau perkembangan masalah attrition di dalam perusahaan Jaya Jaya Institut, hal tersebut menggunakan Dashboard yang di mana untuk memantau perkembangan masalah tersebut. berikut penjelasan mengenai isi Dashboard tersebut:
1. Grafik Total Mahasiswa di Setiap Course
   Grafik ini merupakan grafik sebaran seluruh mahasiswa di setiap course. Grafik ini menjadi grafik dasar untuk melihat kondisi sebaran mahasiswa. Jika di dalam informasi jumlah dropout didominasi pada sebaran jumlah mahasiswa paling banyak di satu course, maka hal tersebut wajar dan berbanding lurus dengan antara jumlah dropout dengan jumlah mahasiswa. begitu juga sebaliknya. Dari grafik yang dihasilkan bahwa sebaran mahasiswa paling banyak ada di course Nurse dengan total mahasiswa yaitu 766 mahasiswa. sedangkan paling rendah yaitu di course Biofuel Production Technologies sebesar 12 mahasiswa.
2. Grafik Total Mahasiswa berstatus Dropout di Setiap Course
   Dari hasil grafik tersebut, bahwa mahasiswa yang memiliki angka dropout paling tinggi ada di course Management (evening attendance) dengan total yaitu 136 mahasiswa Dropout. dan paling rendah yaitu ada di course Biofuel Production Technologies sebanyak 8 mahasiswa yang dropout. Hal ini tentu menjadi pertanyaan besar karena course management bukanlah course yang mendominasi jumlah sebaran mahasiswa yang paling banyak.
3. Grafik Mahasiswa Berdasarkan GDP percentile 50 di setiap Course
   Grafik ini akan menggali informasi lebih dalam untuk poin sebelumnya. Grafik ini dibuat atas pertanyaan secara tidak langsung merepresentasikan pendapatan perkapita keluarga walaupun GDP merupakan gross domestic product sebuah parameter untuk mengukur hasil produksi barang dan jasa di dalam negara. Dari hasil ghrafik yang didapat bahwa mahasiswa yang mengambil course di Management (evening attendance) memiliki GDP quartil 50 sebesar 0.320 sama seperti mahasiswa yang mengambil course Nurse.
4. Grafik Mahasiswa Dropout Berdasarkan Sebaran Beasiswa di setiap Course
   Grafik ini akan menggali informasi sedikit lebih dalam mengenai kondisi mahasiswa dropout berdasarkan sebaran beasiswa. Dari hasil grafik yang didapat bahwa mahasiswa yang memiliki angka dropout paling tinggi yaitu di course Management (evening attendance) memiliki sebaran beasiswa yang rendah dibandingkan dengan course lainnya dengan kondisi GDP yang sama secara quartile 50.

## Menjalankan Sistem Machine Learning
1. Link : https://projectjayajayainstitut-hs6aaatu2wgdkssbsvvp4x.streamlit.app/
2. Silahkan buka link di atas pada browser anda
3. jika anda ingin mengakses model secara lokal pada komputer yaitu dengan cara
4. buka berkas model lalu copy path berkas tersebut
5. selanjutnya buka cmd pada komputer anda, lalu ketik cd (isikan copy path) dan run
6. kemudian tulis streamlit run students_performance_app.py lalu klik localhost dan model prototype siap untuk digunakan
7. Silahkan isi data mahasiswa atau calon mahasisiswa yang akan di prediction
8. pada kolom units 1st sem grade dan units 2nd sem grade anda dapat memasukkan nilai type float atau bilangan berkoma
9. setelah anda memasukkan semua nilai pada kolom, klik tombol evaluate lalu anda akan diminta untuk mengevaluasi atau check kembali nilai yang sebelumnya telah anda masukkan
10. terakhir, anda dapat klik tombol prediction untuk melihat hasil prediction

## Conclusion
Dari hasil analisis yang didapat ada beberapa conclusion yang dapat diberikan yaitu:
1. Jumlah dropout yang tinggi diakibatkan oleh biaya hidup dan ketidakmampuan mahasiswa dalam membayar biaya kuliah.
2. Sebaran beasiswa yang masih belum efektif sehingga secara langsung berdampak pada perkembangan dropout.
3. Penetapan jumlah biaya kuliah yang belum efektif akan berdampak buruk untuk mahasiswa.

## Action Recomendation
1. Institut harus membuat kebijakan yang bertujuan untuk meringankan biaya kuliah mahasiswa seperti biaya kuliah yang dapat diangsur, mahasiswa yang berprestasi atau memiliki IPK datas 3.50 akan diberikan potongan biaya kuliah.
2. Institut harus meningkatkan sebaran beasiswa untuk di setiap course terutama course  Management (evening attendance) yang memiliki angka dropout paling tinggi. Institut dapat memberikan 40 hingga 50 persen sebaran beasiswa berdasarkan jumlah keseluruhan mahasiswa pada setiap course dan disesuaikan dengan pendapatan perkapita keluarga mahasiswa agar beasiswa bersifat on target.
3. Penetapan biaya kuliah harus disesuaikan dengan kondisi GDP nasional. Agar sesuai dengan kemampuan keluarga mahasiswa dalam membayar biaya kuliah.
4. Institut dapat membuka kesempatan pembiayaan untuk mahasiswa yang memiliki ide bisnis agar ide yang didapatkan dapat direalisasikan dengan baik sehingga dapat meningkatkan ekonomi dan membuka lapangan kerja untuk mahasiswa lain.
