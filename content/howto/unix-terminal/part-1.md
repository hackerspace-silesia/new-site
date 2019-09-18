Title: HOWTO Unix Terminal (Część pierwsza)
Date: 2019-08-19
Slug: howto/unix-terminal/part-1
Lang: pl

[TOC]

Często zauważam że dużo początkujących nie ma żadnego pojęcia jak się poruszać po konsoli w linuxie. Uważam, że konsola w linuxie jest tak potężnym narzędziem że każdy __haker__ powinnien znać w jakimś tam minimalnym stopniu.

Zacznijmy od podstaw podstaw które mogą nam pomóc w zrozumieniu co się dzieje w konsoli:

# 1. (Prawie) wszystko jest plikiem

W linuxie prawie wszystko można potraktować coś jako plik. Czy to jest połączenie, czy to jest dysk twardy, czy to jest partycja, obrazek, sterowanie jasnością monitora to można go odczytać lub do niego zapisać (pod warunkiem że plik jest read oraz/lub write). Pozwala to na bardzo szybkie podłączenie się z swoim skryptem czy użycie prostych komend by zobaczyć co siedzi w jakimś sprzęcie. Możemy nawet zrobić 'dump' dysku przy pomocy jednej linijki w konsoli.

# 2. Procesy

!!! info ""
    Jeżeli brakuje ci przykładów, to możesz przejść do komend [tutaj](/howto/unix-terminal/part-4#commands) - w razie problemów możesz wrócić tutaj

Programy w linuxie działają przez procesy, mogą sobie pracować w tle, mogą być uruchomione w konsoli (do czasu zakończenia), mamy też demony (programy uruchomione podczas startu systemu, nie widać ich ale pracują i knują jak ci zepsuć system, dlatego są demonami).
Każde uruchomienie komendy w konsoli tworzy nowy proces. A co proces może zawierać?

* `STDOUT` - strumień wyjścia, czyli to co program wyświetli/zwróci to się pojawi. Standardowo pokaże się to na ekranie konsoli.
* `STDIN` - strumień wejścia, czyli to co zostanie wprowadzone do procesu w trakcie wykonywania. Standardowo pokazuje się gdy klepiemy literki w odpowiedzi
* `STDERR` - dodatkowy strumień na błędy/warningi/informacje. Bardzo fajne gdy program generuje coś np. obrazek i wyświetli błąd na strumieniu błędów nie uszkadzając już po części wygenerowanego obrazka. wyjasnię to bardziej w przykładach później
* Argumenty - każda komenda może przyjąć argumenty. Narazie to tyle - więcej będzie w rozdziale [argumenty](/howto/unix-terminal/part-2#arguments) (czyli już za chwilę, naprawdę)
* Zmienne Środowiskowe - przy skomplikowanych programach (jak serwery baz danych) nie wystarczy podać wszystko jako argumenty - stosuje się do tego dodatkowe zmienne które można albo przekazać tylko programowi albo wyexportować w terminalu (wyjaśnię to w późniejszych działach)
* Exitcode - każdy proces jak się zakończy zwraca małą (0-255) liczbę. Jak jest 0 to oznacza że nie ma żadnego błędu, jak jest inna liczba tzn że jest program nie skończył się poprawnie.

Więcej o procesach w linuxie możesz doczytać tutaj (ENG): [https://peteris.rocks/blog/htop/](https://peteris.rocks/blog/htop/)

W tej części to na tyle, zapraszam do kolejnej [tutaj](/howto/unix-terminal/part-2).
