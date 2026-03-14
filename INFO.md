# Instrukcja obsługi środowiska testowego

## Korzystając z Github Actions
1. Upewnij się, że wersja kodu ktrórą chcesz wykorzystać do testowania znajduje się na [repozytorium GitHub](https://github.com/DanielMierzwa/OOB_Tests-ImageIO).
2. Przejdź do sekcji [*Actions*](https://github.com/DanielMierzwa/OOB_Tests-ImageIO/actions)
3. Wybierz odpowiedni pipeline. (W tym przypadku [*OOB Testing Pipeline*](https://github.com/DanielMierzwa/OOB_Tests-ImageIO/actions/workflows/oob_pipeline.yml))
4. Kliknij przycisk *Run workflow*, wybierz branch na którym uruchomi sie pipeline i kliknij zielony przycisk *Run workflow*.
5. Po uruchomienu zostaniesz przeniesiony na strone tego konkretnego workflow. Po zakończeniu testów wyświetli się tam podsumowanie w postaci pliku `raport.md`, oraz możliwość pobrania artefaktów testu. Artefakty to pliki: `raport.md` z raportem testów, `coverage.xml` z statystykami wykorzystania kodu biblioteki oraz `results.xml` z danymi o przeprowadzonych testach. Artefakty przechowywane są przez 7 dni od wykonania testów.

## Lokalnie (na swoim komputerze)
1. Upewnij się, że masz zainstalowane wszystkie potrzebne biblioteki python oraz interpreter pythona.

    ```pip install imageio pytest pytest-cov```
2. Będąc w folderze projektu użyj komendy

    ```pytest tests/ --cov=imageio --cov-report=xml:coverage.xml --junitxml=results.xml```
3. Aby wygenerować raport użyj komendy

    ```python ./scripts/report_generator.py```