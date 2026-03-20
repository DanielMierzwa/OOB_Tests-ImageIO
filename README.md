# OOB_Tests-ImageIO
![CI Status](https://github.com/DanielMierzwa/OOB_Tests-ImageIO/actions/workflows/oob_pipeline.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)

## 1. Opis projektu
Projekt **OOB_Tests-ImageIO** ma na celu testowanie biblioteki ImageIO, ze szczególnym uwzględnieniem testów **Out-of-Box (OOB)** – czyli testów sprawdzających zachowanie systemu przy dostępie do pamięci poza dozwolonymi granicami.

## 2. Zespół i Podział Ról


### **Szymon Rospondek** [![GitHub](https://img.shields.io/badge/@NiskiSzymus-24292e?style=flat-square&logo=github&logoColor=white)](https://github.com/NiskiSzymus)
**Tech Lead**, **DevOps**, **Developer**<br>Architektura, decyzje technologiczne, utrzymanie CI/CD, konfiguracja środowisk, implementacja testów.


### **Daniel Mierzwa** [![GitHub](https://img.shields.io/badge/@DanielMierzwa-24292e?style=flat-square&logo=github&logoColor=white)](https://github.com/DanielMierzwa)
**Product Owner**, **Developer**<br>Zarządzanie backlogiem, definiowanie celów biznesowych i wymagań, implementacja logiki testów.
### **Filip Walczak** [![GitHub](https://img.shields.io/badge/@FILIPWXD-24292e?style=flat-square&logo=github&logoColor=white)](https://github.com/FILIPWXD)
**Tester**, **Dokumentacja**, **Developer**<br>Projektowanie i wykonywanie przypadków testowych, dbanie o kompletność i przejrzystość dokumentacji, wsparcie w pisaniu kodu.

## 3. Kanał Komunikacji
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)

## 4. Struktura Projektu

Poniżej przedstawiono układ najważniejszych plików i katalogów w repozytorium:

```bash
OOB_Tests-ImageIO/
│
├── .github/workflows/    # Skrypty mechanizmu CI/CD (GitHub Actions)
├── AcceptanceTests/      # Definicje dla testów akceptacyjnych
├── Doc/                  # Dokumentacja poboczna: Harmonogram.md, Strategia_testowania.md, TASK.md
├── Results/              # Folder zawierający logi, raporty i przykładowe rezultaty testów 
├── scripts/              # Narzędzia pomocnicze i skrypty robocze
├── tests/                # Główny katalog z testami podziałem np. na functional/ i performance/
│
├── INFO.md               # Instrukcje uruchamiania testów w GitHub Actions oraz lokalnie
├── README.md             # Główny plik dokumentacji projektu (ten plik)
├── Pipeline.py           # Skrypt wejściowy dla procesów automatycznych
└── .gitignore            # Konfiguracja ignorowanych plików przez Git
```

## 5. Jak zacząć? (Szybki start)

### Lokalnie
1. Zainstaluj wszystkie potrzebne biblioteki oraz instancje:
   ```bash
   pip install imageio pytest pytest-cov
   ```
2. Uruchom testy korzystając z głównego katalogu testów:
   ```bash
   pytest tests/ --cov=imageio --cov-report=xml:coverage.xml --junitxml=results.xml
   ```
3. Zbuduj raport z operacji:
   ```bash
   python ./scripts/report_generator.py
   ```

*Bardziej szczegółowa instrukcja, w tym dla GitHub Actions znajduje się w pliku [INFO.md](./INFO.md)*
