# CLI

Monitax CLI (mon-cli) adalah *command line interface* untuk berinteraksi dengan backend server Monitax
Dengan mon-cli Anda bisa melakukan pengelolaan User, Device dan Invoice seperti *create user*, *list user*,
*login*, *device list* dan lain sebagainya.

Monitax cli dibangun dengan menggunakan modul Python [Typer](https://typer.tiangolo.com/)  yang merupakan *sister project* dari [FastApi](https://fastapi.tiangolo.com/)

## Configure
### Init
Langah pertama yang harus dilakukan sebelum berinteraksi dengan backend server, terlebih dahulu dilakukan configurasi koneksi ke backend server. Misalkan DNS dari backend server adalah raspigeek.online, maka perintahkan yang harus diketikkan di terminal shell adalah sebagai berikut:
```bash
$ mon-cli configure init
```
Contoh response
```bash
$ mon-cli configure init
Host: raspigeek.online
Ssl [y/n]: y
Initializing done 👍👍

```


## User
### Login
```bash
$ mon-cli user login 
```
Contoh response 

```bash
Username: admin@example.com
Password: 
{
  "token_type": "Bearer",
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NjQxMTI4NTIsImV4cCI6MTY2NDExNDY1Miwic3ViIjoiYWYwMjExMTktNzk3Ny00Y2U4LWFkY2ItOTMyYjg4MTc0MWM5Iiwicm9sZSI6IkFkbWluaXN0cmF0b3IiLCJuYW1lIjoiYWRtaW5AZXhhbXBsZS5jb20iLCJyZWZyZXNoIjpmYWxzZX0.L1VkTKznuVwyVJ2kGGlfEg1Wwm1R1kSQbJpuv9UMudE",
  "exp": 1664114652,
  "iat": 1664112852,
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NjQxMTI4NTIsImV4cCI6MTY2NDExNjQ1Miwic3ViIjoiYWYwMjExMTktNzk3Ny00Y2U4LWFkY2ItOTMyYjg4MTc0MWM5Iiwicm9sZSI6IkFkbWluaXN0cmF0b3IiLCJuYW1lIjoiYWRtaW5AZXhhbXBsZS5jb20iLCJyZWZyZXNoIjp0cnVlfQ.KnylMwbM8qnBLV79GDVxaZUEdbCiRYejtOkzPKYR4aI",
  "refresh_token_expires_at": 1664116452,
  "refresh_token_issued_at": 1664112852
}
```
