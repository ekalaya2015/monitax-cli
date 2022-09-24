# Welcome to Monitax 

## Monitax

### Gambaran umum

Monitax adalah aplikasi untuk monitoring pajak secara online. Pajak yang dimaksud disini adalah pajak pendapatan daerah yang berasal dari dunia usaha kategori hiburan, parkir, dan hotel. 
Mekanisme monitoring dapat terlaksana dengan adanya alat berupa *tapping box* yang dipasang di setiap outlet dari pelaku usaha. Alat akan merekam transaksi yg berasal dari aplikasi Point of Sales (PoS) dan alat akan mengirimkan setiap *record* transaksi tersebut ke *backend server* yang dimiliki oleh Badan Pendapatan Daerah atau BAPENDA. 

### Gambaran Teknis

``` mermaid
graph TD
  A[Customer] --> |place| B[Order];
  B --> |recorded| C[PoS];
  C --> |captured| D[Tapping box];
  D --> |send| E[Backend server];
  E --> F[(DB)]
```

