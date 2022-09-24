# Welcome to Monitax 

## Monitax

Monitax adalah aplikasi untuk monitoring pajak secara online. Pajak yang dimaksud disini adalah pajak pendapatan daerah yang berasal dari dunia usaha kategori hiburan, parkir, dan hotel. 
Mekanisme monitoring dapat terlaksana dengan adanya alat berupa *tapping box* yang dipasang di setiap outlet dari pelaku usaha. Alat akan merekam transaksi yg berasal dari aplikasi Point of Sales dan alat akan mengirimkan setiap *record* transaksi tersebut ke *backend server* yang dimiliki oleh Badan Pendapatan Daerah atau BAPENDA. 

## Command line interface (mon-cli)

Monitax CLI (mon-cli) adalah *command line interface* untuk berinteraksi dengan backend server
Dengan mon-cli Anda bisa melakukan pengelolaan User, Device dan Invoice seperti *create user*, *list user*,
*login*, *device list* dan lain sebagainya.

Monitax cli dibangun dengan menggunakan modul Python *Typer* yang merupakan sister project dari [FastApi](https://fastapi.tiangolo.com/)

