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

1. conda create --name base python 3.11.8
2. conda activate base
3. streamlit run students_performance_app.py

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

## Link Prototype dan cara menggunakan Prototype
1. Link : https://projectjayajayainstitut-hs6aaatu2wgdkssbsvvp4x.streamlit.app/
2. Cara menggunakan Prototype yaitu:
1. Silahkan buka link di browser anda
2. Silahkan isi data mahasiswa atau calon mahasisiswa yang akan di prediction
3. pada kolom units 1st sem grade dan units 2nd sem grade anda dapat memasukkan nilai type float atau bilangan berkoma
4. setelah anda memasukkan semua nilai pada kolom, klik tombol evaluate lalu anda akan diminta untuk mengevaluasi atau check kembali nilai yang sebelumnya telah anda masukkan
5. terakhir, anda dapat klik tombol prediction untuk melihat hasil prediction

