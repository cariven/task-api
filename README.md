# Task Management API

## Deskripsi
API sederhana untuk mengelola task (create, read, update).

## Cara Menjalankan
Install dependency:
pip install -r requirements.txt

Jalankan server:
uvicorn src.main:app --reload

Buka di browser:
http://127.0.0.1:8000/docs

## Cara Testing
pytest --cov=src


## Strategi Testing
- Unit test untuk logic service
- Integration test untuk endpoint API

## CI
Menggunakan GitHub Actions untuk:
- install dependencies
- run test
- generate coverage