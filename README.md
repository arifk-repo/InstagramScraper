# Instagram Comment Scraper
## _Using selenium and beautifull soup_

[![N|Solid](https://ml7a1cnkmo5m.i.optimole.com/6IH-QXI-zCN84owO/w:650/h:433/q:auto/https://www.dev-cafe.org/wp-content/uploads/2018/08/python-logo-3.6.gif)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Pertama, kalo buka program ini masuk ke branch master, dan clone isinya, saya jelaskan secara singkat mengenai proses instalasinya.
Bahan-bahan yang diperlukan:
- install semua library di requirements.txt
- kemudian install browser driver sesuai yang kalian pake, kalo chrome pake chromedriver, firefox pake geckodriver, kalo kamu pakai selain itu? Cari sendiri lah wkwk

## Fitur 

- Scraping data di kolom komentar sebuah post instagram 
- datanya berbentuk excel
- kalau mau diganti jenisnya bisa, tinggal ubah dalam program saja :)

## Installation

Untuk menjalankan program ini pertama clone dulu repo ini dengan cara 
```sh
git clone https://github.com/codeby-arifk/InstagramScraper.git
```

Setelah diclone, kemudian buka terminal dan install library yang dibutuhkan dengan cara

```sh
pip install -r requirements.txt
```

Setelah itu extrack file browser driver dan masukan kedalam folder driver
untuk kamu yang pake windows, pada file otomate.py tuliskan _basepath_ seperti ini
```sh
basepath = os.path.join("driver", "chromedriver.exe")
```
sedangkan yang pake windows, pada file otomate.py tuliskan _basepath_ seperti ini
```sh
basepath = os.path.join("driver", "chromedriver")
```
Sesuaikan juga drivernya dengan browser yang kamu gunakan, setelah proses itu selesai tinggal jalankan programnya

## NOTE :
- kalau jumlah data yang kamu dapatkan sedikit, kamu bisa memodivikasinya pada file otomate.py pada baris ke 63, _time.sleep(0.2)_ ganti angka dalam kurung ke angka yang lebih besar, namun saya sarankan 0.5-0.7 saja sudah cukup, karena kalau terlalu tinggi waktunya juga lama _hehehe_
