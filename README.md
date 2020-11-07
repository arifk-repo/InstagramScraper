# InstagramScraper
This repo is useful for scraping Instagram posts

silahkan clone repo ini dengan menjalankan perintah pada terminal:

git clone https://github.com/codeby-arifk/InstagramScraper.git

untuk menggunakan program ini silahkan install semua library pada requirements.txt

selanjutnya silahkan download chrome driver (alternatif lain geckodriver untuk mozila) pada link berikut https://chromedriver.chromium.org/downloads
sesuaikan versi chrome driver anda, untuk mengecek versi chrome anda dapat memasukan chrome://version/ pada chrome anda

selanjutnya extrack file driver yang anda download dan masukan kedalam folder driver

silahkan ganti baris pada file otomate.py:
jika anda menggunakan linux : basepath = os.path.join("driver", "chromedriver")
jika anda menggunakan windows : basepath = os.path.join("driver", "chromedriver.exe")

untuk menjalankan program, anda dapat melalui app.py atau dengan perintah terminal: python app.py

silahkan masukan url,username dan password anda
username dan assword digunakan untuk proses otomatisasi login
