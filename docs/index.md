# Welcome to Monitax 

## Monitax

### Gambaran umum

Monitax adalah aplikasi untuk monitoring pajak secara online. Pajak yang dimaksud disini adalah pajak pendapatan daerah yang berasal dari dunia usaha kategori hiburan, parkir, dan hotel. 
Mekanisme monitoring dapat terlaksana dengan adanya alat berupa *tapping box* yang dipasang di setiap outlet dari pelaku usaha. Alat akan merekam transaksi yg berasal dari aplikasi Point of Sales (PoS) dan alat akan mengirimkan setiap *record* transaksi tersebut ke *backend server* yang dimiliki oleh Badan Pendapatan Daerah atau BAPENDA. 

Monitax terdiri dari:
1. Aplikasi frontend. Tugas2 administrasi seperti *create user*, *add device*, *assign device*, dashboard dan lain-lain dapat dilakukan di aplikasi frontend
2. Aplikasi mobile android/iOS untuk digunakan oleh wajib pajak dalam hal ini pelaku usaha. Pelaku usaha bisa memonitoring transaksi per device, misalnya saja penjualan harian/mingguan, total pajak harian/mingguan dan lain-lain
3. Backend server. Server yang berfungsi untuk mencatat setiap transaksi dari usaha milik wajib pajak yang dicapture oleh tapping box.    
4. Dan tentu saja device yang disebut sebagai tapping box. Sesuai dengan namanya, device ini melakukan tap atau intercept terhadap data order atau transaksi dari aplikasi Point os Sales. Selanjutnya data order atau transaksi dikirim ke backend server. Data dapat berupa text atau image. Backend server akan melakukan parsing data order atau transaksi untuk mengekstrak data-data yang diperlukan seperti tanggal transaksi, nomor invoice/struk/receipt, nilai total sales atau penjualan, nilai pajak dan lain-lain. 

### Gambaran Teknis

<p style="text-align: center;">
``` mermaid
graph TD
  A[Customer] --> |place| B[Order];
  B --> |recorded| C[PoS];
  C --> |captured| D[Tapping box] 
  C --> |print| E[Receipt printer]
  D --> |send| F[Backend server];
  F --> G[(DB)]
```
</p>
