# Legends Vote

Günde bir kez, belirlenen saatte Legends Online oy sayfasını açar ve 4 oy sitesini
sekme olarak hazırlar. Sen kutucukları tıklayıp oyları verirsin.

## \## Gereksinimler

## 

## \- Windows 10/11

## \- Python 3.11+

## \- \[uv](https://docs.astral.sh/uv/getting-started/installation/)

## \- Google Chrome

## 

## \## Kurulum (kullanicilar icin)

## 

## 1\. Bu repoyu indir (Code -> Download ZIP) ve bir klasore cikar.

## 2\. `.env.example` dosyasini `.env` olarak kopyala.

## 3\. `.env` icine \*\*kendi\*\* Legends Online kullanici adi ve sifreni yaz.

## 4\. PowerShell ac, klasore gel:

## &#x20;  ```powershell

## &#x20;  cd legends-vote

## &#x20;  uv sync

## &#x20;  uv run playwright install chrome

## &#x20;  powershell -ExecutionPolicy Bypass -File .\\build\_exe.ps1

## &#x20;  powershell -ExecutionPolicy Bypass -File .\\install\_startup.ps1

