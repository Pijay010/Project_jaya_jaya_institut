# Proyek AKhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan Lembaga Academic yang telah berdiri dari tahun 2000 dan telah menjadi salah satu lembaga academic yang memiliki reputasi sangat baik. saat ini Jaya Jaya Institut memiliki lebih dari 4000 mahasiswa yang tersebar di berbagai course. Namun, saat ini Jaya Jaya Institu mengalami permasalahan academic yang tentunya akan berpengaruh dengan kualitas pendidiakan di lembaga tersebut hingga akan menurunkan reputasi Jaya Jaya Intitiut sendiri. Oleh karena itu, lembaga academic tersebut meminta saya sebagai seorang data scientist untuk mengidentifikasi permasalahan tersebut hingga menemukan solusi agar Jaya Jaya Institut secepat mungkin dapat membenahinya. Adapun masalah yang dihadapi akan dituliskan pada permasalahan bisnis.

## Permasahalan Bisnis
Saat ini Jaya Jaya Institut memiliki pernmasalahan yaitu tingginya angka mahasiswa yang berstatus Dropout. Tentu hal ini akan menjadi masalah besar dikemudian hari jika tidak dibenahi sesegera mungkin seperti kualitas pendidikan hingga ketertarikan lulusan baru untuk mendaftar di Jaya Jaya institut menurun. Selain itu, dampak negatif yang diterima oleh academic adalah berkurangnya modal aset sehingga academic kesulitan dalam mengembangkan academic seperti membuat infrastruktur baru untuk lingkungan academic, fasilitas pendukung proses belajar mahasiswa hingga menurunnya penyerapan tenaga kerja baru seperti dosen, staff academic dan lain-lain.

## Cakupan proyek
Di dalam proyek ini cakupan proyek yang akan saya buat adalah sebagai berikut:
1. Menggunakan bahasa python
2. menggunakan google colab untuk proses analisis hingga membuat model machine learning
3. Menggunakan library otomatis yang disediakan oleh google colab. sedangkan untuk library yanag tidak disediakan oleh google colab seperti library XGBoost, saya menginstallnya secara manual dengan scrpt code !pip install xgboost
4. Membuat visualisasi data untuk mempermudah dalam menemukan informasi lebih dalam 
5. Membuat model machine learning dengan menguji berbagai model algoritma dan menggunakan model algoritma terbaik untuk proses prediction
6. Membuat protoype 
7. Membuat proses deployment menggunakan streamnlit
9. Membuat business dashboard menggunakan Tableau

## Persiapan
1. Sumber data
   Sumber data yang digunakan merupakan data yang diunduh secara manual dari dicoding dan diupload secara manual ke google colab melalui storage local komputer. Adapun file data akan dilampirkan di path berkas ('file_final_project.zip'/'file_final_project'/'Notebook'/'data.csv').
2. Setup Environment
  Saya menggunakan dua bingkai kerja yang berbeda untuk proses mengerjakan project. bingkai kerja pertama adalah Google colab untuk mengerjakan file 'Project_Jaya_Jaya_institut.IPYNB', dalam hal ini setup environment yang digunakan sudah terpasang secara otomatis oleh goole colab. Adapun untuk menjalankannya yaitu buka google colab -> upload file 'Project_Jaya_Jaya_institut.IPYNB' -> upload 'data.csv'. Install library yang tidak secara otomatis disediakan oleh google colab dengan cara >> pip install 'library'. Bingkai kerja kedua adalah VScode yang digunakan untuk mengerjakan prototype dan deployment. Setup Environment yang digunakan adalah: 
