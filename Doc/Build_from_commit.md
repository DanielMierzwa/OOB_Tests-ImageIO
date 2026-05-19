# Budowanie ImageIO z wybranego commita

## Cel

Zamiast instalować `imageio` z rejestru PyPI, projekt buduje paczkę lokalnie
ze źródeł oficjalnego repozytorium [imageio/imageio](https://github.com/imageio/imageio).
Dzięki temu testy działają na dokładnie określonej wersji kodu źródłowego,
niezależnej od aktualnego stanu wydań na PyPI.

## Wybrany commit

| Właściwość | Wartość |
| :--- | :--- |
| **Repozytorium** | `https://github.com/imageio/imageio.git` |
| **Commit (short)** | `971b83e` |
| **Wersja** | `v2.37.3` |
| **Python** | `>= 3.10` |

## Zależności

Plik `requirements.txt` **nie zawiera** `imageio`. Zawiera natomiast:

| Paczka | Rola |
| :--- | :--- |
| `numpy` | Wymagany runtime dependency ImageIO |
| `Pillow` | Plugin Pillow używany przez ImageIO do operacji PNG/JPEG |
| `pytest` | Framework testowy |
| `pytest-cov` | Raportowanie pokrycia kodu |
| `tzdata` | Strefy czasowe dla generatora raportów |
| `build` | Budowanie wheela ImageIO ze źródeł (`python -m build`) |

## Proces builda

Skrypt `scripts/build_imageio_from_commit.py` wykonuje następujące kroki:

1. **Czyszczenie** – usuwa katalog `.build/imageio-src`, jeśli istnieje.
2. **Klonowanie** – `git clone --no-checkout` repozytorium imageio do `.build/imageio-src`.
3. **Checkout** – `git checkout 971b83e` i zapis pełnego SHA.
4. **Budowanie** – `python -m build --wheel` tworzy plik `.whl` w `.build/imageio-src/dist/`.
5. **Instalacja** – `pip install --force-reinstall <wheel>` instaluje zbudowaną paczkę.
6. **Weryfikacja** – importuje `imageio.v3` i wypisuje wersję.
7. **Metadane** – zapisuje `imageio_build_info.json` w katalogu głównym projektu.

## Uruchomienie lokalne

```bash
# 1. Zainstaluj zależności (bez imageio)
python -m pip install -r requirements.txt

# 2. Zbuduj i zainstaluj ImageIO z commita
python scripts/build_imageio_from_commit.py

# 3. Uruchom testy
python -m pytest

# 4. Wygeneruj raport
python scripts/report_generator.py
```

## Pipeline CI/CD

W pliku `.github/workflows/oob_pipeline.yml` dodano krok
**Build ImageIO from selected GitHub commit**, który uruchamia skrypt budowania
po instalacji `requirements.txt`, a przed uruchomieniem `pytest`.

Artefakty pipeline zawierają dodatkowo `imageio_build_info.json`.

## Plik `imageio_build_info.json`

Przykładowa zawartość:

```json
{
  "repository": "https://github.com/imageio/imageio.git",
  "commit_short": "971b83e",
  "commit_full": "971b83e...(pełny SHA)",
  "wheel_file": "imageio-2.37.3-py3-none-any.whl",
  "install_method": "wheel from local build",
  "build_timestamp": "2026-05-18T16:00:00+00:00"
}
```

Generator raportów (`scripts/report_generator.py`) wczytuje ten plik i dodaje
sekcję **Tested ImageIO Build** do `raport.md`. Jeśli plik nie istnieje,
raport nadal działa – wyświetla informację o braku metadanych.