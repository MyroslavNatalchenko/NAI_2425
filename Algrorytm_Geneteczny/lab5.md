# Lab 5 - Algorytm Genetyczny

Uruchom przykład i zobacz co on robi
## 0 Zadanie

Przygotuj większy przykład problemu plecakowego - ma być 15 elementów. Upewnij się, że nie wszystkie się zmieszczą, ale co najmnie 3 wejdą do plecaka. Uruchom dla populacji rozmiaru 100 oraz 50 iteracji. Zanotuj wyiki dla 5 uruchomień w tej wersji w arkuszu kalkulacyjnym.

## 1 Krzyżowanie

Zaimplementuj krzyżowanie dwupunktowe. Zobacz opis na https://www.mathworks.com/help/gads/genetic-algorithm-options.html. Oaimplementuj. Sugeruję użyć operatorów na tablicach w języku Python.

Podmień wywołanie funkcji krzyżowania i przetestuj czy działa.

Zanotuj wynik pięciu uruchomień. Dopisz do tabeli z wynikami.

## 2 Mutacja

Zobacz, jakie mogą być operatory mutacji (poszukaj). Zaimplementuj mutację probabilistyczną. Tu zadanie dla Ciebie - wyszukaj.

Zanotuj wynik pięciu uruchomień. Dopisz do tabeli z wynikami.

## 3 Prawdopodobieństwa krzyżowania i mutacji.

Dodaj możliwość podania prawdopodobieństwa zajścia mutacji i krzyżowania (p_mutation, p_crossover). Dodaj te parametry do funkcji algorytmu genetycznego. Test na krzyżowanie powinien pozwalać na to, aby w zależności od wyniku losowania, zastosować krzyżowanie lub skopiować osobniki bez zmian. Podobnie z krzyżowaniem, z tym, że prawdopodobieństwo krzyżowania możan zaaplikować albo dla decyzji, czy wywoływać funkcję mutacji, czy też już jako parametr mutacji.

Aby wykonać losowanie z zadanym prawdopodobieństwem, trzeba zrobić tak:
Niech ```u``` będzie zmienną losową z zakresu od 0 to 1. Niech ```p``` będzie prawdopodobieństwem. Warunek jest taki, że jeżeli ```u < p``` wtedy wykounjemy coś z prawdopodobieństwem ```p```.

Zanotuj wynik pięciu uruchomień. Dopisz do tabeli z wynikami.

## 4 Porównanie wyników

Uśrednij wyniki poszczególnych wersji i zobacz jak się zmieniały.

## Zadanie domowe

Niech zadanie do rozwiązania będzie ładowane z pliku. Format dowolny (json, csv, txt, ...). Rozmiar zadania ma być dowolny. Program powinien wypisać wynik. Nazwa pliku zadania powinna być podana z CLI.

## Zadanie dodatkowe

Zaimplementuj po swojemu to samo w C++ i porównaj czasy obliczeń dla zadania plecakowego o rozmiarze 2000. Tu trzeba jakoś to zadanie wygenerować i przetestować obie wersje w sposób taki jak poprzednio. Dodaj jeszcze mierzenie czasu. Niech rozmiary populacji będą po 2000 osobnikóœ, a iteracji będzie 500.

