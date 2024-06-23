# Data Analyzer Python

## Struktura projektu

- **commands/**: Główne katalogi z komendami, które zawierają podkatalogi dla analizy, aplikacji oraz wizualizacji
  danych.
    - **analysis/**: Skrypty odpowiedzialne za analizę danych.
        - **average_medals_per_participant.py**: Oblicza średnią liczbę medali na uczestnika.
        - **countries_with_most_participations.py**: Wyświetla kraje z największą liczbą udziałów.
        - **explore_data.py**: Eksploracja danych.
        - **filter_data.py**: Filtruje dane według określonych kryteriów.
        - **medals_by_country.py**: Liczy medale zdobyte przez poszczególne kraje.
        - **sort_data.py**: Sortuje dane według określonych kryteriów.
    - **app/**: Skrypty związane z aplikacją.
        - **exit.py**: Obsługuje zamknięcie aplikacji.
    - **visualization/**: Skrypty odpowiedzialne za wizualizację danych.
        - **plot_medal_comparison.py**: Tworzy wykres porównawczy medali.
        - **plot_medal_ratio_pie.py**: Tworzy wykres kołowy przedstawiający proporcje medali.
        - **plot_medals_per_country.py**: Tworzy wykres medali na kraj.
        - **plot_medals_per_country_pie.py**: Tworzy wykres kołowy medali na kraj.
- **data/**: Katalog z danymi wejściowymi.
    - **olympic_committee_2022.csv**: Plik CSV z danymi komitetu olimpijskiego z 2022 roku.
- **helpers/**: Klasy pomocnicze dla komend.
    - **columns_info.py**: Informacje o kolumnach danych.
- **loaders/**: Obsługa ładowania plików.
    - **file_loader.py**: Skrypt do ładowania plików.
- **resolvers/**: Obsługa pobierania odpowiedniej klasy po typie.
    - **command_resolver.py**: Skrypt do rozwiązywania komend.

## O progrmaie

Program implementuje podstawowe algorytmy analizy danych takie jak:

- **Filtracja**
- **Sortowanie**

Projekt generuje też kilka wykresów danych:

- **Porównanie medali**
- **Proporcje medali**
- **Medale na kraj**
- **Medale na kraj (wykres kołowy)**

Kod projektu wykorzystuje kilka zasad organizacji i wzorców projektowych:

- **Mapowanie komend**: Wybór użytkownika jest mapowany do odpowiednich klas komend, co pozwala na odseparowanie żądania
  od jego wykonania.

- **Fabryka obiektów**: Tworzenie instancji klas komendy z użyciem fabryki abstrakcyjnej, co umożliwia elastyczne
  zarządzanie obiektami aplikacji.

Te wzorce projektowe pomagają w utrzymaniu czytelności kodu, separacji odpowiedzialności oraz ułatwiają rozwój i
rozszerzanie funkcjonalności aplikacji.

