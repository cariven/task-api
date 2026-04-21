# Task Management API

## Deskripsi
API sederhana untuk mengelola task (create, read, update).

## Cara Menjalankan
uvicorn src.main:app --reload

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