# Instrukcja obsługi środowiska testowego

## Korzystając z Github Actions
1. Upewnij się, że wersja kodu ktrórą chcesz wykorzystać do testowania znajduje się na [repozytorium GitHub](https://github.com/DanielMierzwa/OOB_Tests-ImageIO).
2. Przejdź do sekcji [*Actions*](https://github.com/DanielMierzwa/OOB_Tests-ImageIO/actions)
3. Wybierz odpowiedni pipeline. (W tym przypadku [*OOB Testing Pipeline*](https://github.com/DanielMierzwa/OOB_Tests-ImageIO/actions/workflows/oob_pipeline.yml))
4. Kliknij przycisk *Run workflow*, wybierz branch na którym uruchomi sie pipeline i kliknij zielony przycisk *Run workflow*.
5. Po uruchomienu zostaniesz przeniesiony na strone tego konkretnego workflow. Po zakończeniu testów wyświetli się tam podsumowanie w postaci pliku `raport.md`, oraz możliwość pobrania artefaktów testu. Artefakty to pliki: `raport.md` z raportem testów, `coverage.xml` z statystykami wykorzystania kodu biblioteki, `results.xml` z danymi o przeprowadzonych testach oraz `imageio_build_info.json` z metadanymi builda ImageIO. Artefakty przechowywane są przez 7 dni od wykonania testów.

> **Uwaga:** Pipeline nie instaluje ImageIO z PyPI. Zamiast tego buduje paczkę
> z oficjalnego repozytorium GitHub ([imageio/imageio](https://github.com/imageio/imageio))
> z commita `971b83e` (v2.37.3). Szczegóły tego procesu opisano w pliku
> [Doc/Build_from_commit.md](./Doc/Build_from_commit.md).

## Lokalnie (na swoim komputerze)

### Korzystając z konsoli
1. Upewnij się, że masz zainstalowane wszystkie potrzebne biblioteki python oraz interpreter pythona.

    ```python -m pip install -r requirements.txt```

2. Zbuduj i zainstaluj ImageIO z wybranego commita:

    ```python scripts/build_imageio_from_commit.py```

3. Będąc w folderze projektu użyj komendy

    ```python -m pytest```

4. Aby wygenerować raport użyj komendy

    ```python ./scripts/report_generator.py```

### Korzystając z pliku `run_tests.py`
1. Upewnij się, że masz zainstalowane wszystkie potrzebne biblioteki python oraz interpreter pythona.

    ```python -m pip install -r requirements.txt```

2. Zbuduj i zainstaluj ImageIO z wybranego commita:

    ```python scripts/build_imageio_from_commit.py```

3. Uruchom plik `run_tests.py`

    ```python ./run_tests.py``` lub poprzez np. Visual Studio Code