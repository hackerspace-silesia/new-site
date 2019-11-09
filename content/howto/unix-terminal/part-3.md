Title: HOWTO Unix Terminal (Część trzecia)
Date: 2019-08-19
Slug: howto/unix-terminal/part-3
Lang: pl

[TOC]

# 3b. Bash (zaawansowane rzeczy)

## Cudzysłowia

Nauczmy się nowej komendy `cat` - służy do otwierania zawartości plików (binarnych też, ale to niebezpieczne!).

```bash
$ cat dojo
Coding dojo to jest spotkanie, gdzie spotyka się masa programistów (lub potocznie, nerdów), gdzie w grupach (...)
```

Fajne tak? spróbujmy otworzyć plik `file name.txt`

```bash
$ cat file name.txt
cat: file: No such file or directory
cat: name.txt: No such file or directory
```

A co tu się stanęło? Komenda przyjęła nie 1 argument tylko 2, więc cat próbówał wyświetlić dwa pliki o nazwach które nie istnieją. Ale możemy zrobić tak:

```bash
$ cat 'file name.txt'
```

Możemy skorzystać z pojedyncznego cudzysłowia (podwójny ma inne, ukryte zachowanie, do którego zaraz dojdziemy) by bash ogarnął, że to jest 1 argument z spacją.

Inny przykład, co jeśli chcemy wyświetlić cudzysłowia? to musimy zrobić tak:

```bash
$ echo 'SIEMA'
SIEMA
$ echo \'SIEMA\'
'SIEMA'
```

Jak widać, skorzystaliśmy z znaku 'escape char' - żargonowo w Polsce nazywają to `eskejpowaniem`.
Tutaj inny przykład escape char - tutaj zamiast cudzysłowia użyliśmy escape char `\ `:

```bash
$ cat file\ name.txt
```

korzystając z znaku `\` kolejny znak został zignorowany jako specjalny i został zinterpretowany jako zwykły znak. Możemy oczywiście `eskejpować` takie znaki jak `*` `\` `?` `$` etc.

### Cudzysłów pojedynczy a podwójny

Z początku używanie pojedyncznego czy podwójnego nie robi różnicy, ale można się przejechać:

```bash
$ echo 'foobar-$PWD'
foobar-$PWD
$ echo "foobar-$PWD"
foobar-/home/user
```

1. Wyświetlił stringa jakiego chcieliśmy
2. Wyświetlił stringa wrzucając tam zmienną $PWD czyli aktualną ściężkę w której się znajduje

## Zmienne środowiskowe

W procesach w linuxie by nie wysyłać wszystkiego parametrami komendy (60 parametrów w 1 linijce, no jakaś masakra), niektóre programy pozwalają na użycie zmiennych środowiskowych.

```bash
# brak spacji przy = jest bardzo ważny!!
$ LANG=pl_PL.UTF-8 ls -  # zmienna $LANG będzie tylko w tej linijce
ls: nie ma dostępu do '-': Nie ma takiego pliku ani katalogu
$ LANG=en_US.UTF-8 ls -
ls: cannot access '-': No such file or directory
$ export LANG=pl_PL.UTF-8  # jest zapisana teraz globalnie i będzie stosowana w każdym uruchomionym programie w tym terminalu
$ ls -
ls: nie ma dostępu do '-': Nie ma takiego pliku ani katalogu
```

Możemy skorzystać z funkcji env która wyświetla wszystkie zmienne:
```bash
$ env
COLORFGBG=15;0
COLORTERM=truecolor
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
…
```

zmienne możemy wykorzystywać w terminalu (co jest bardzo fajne!)
```bash
$ echo folder w którym jestem to $PWD
folder w którym jestem to /home/user
```


## Pomoc

Często nie wiemy / nie pamiętamy wszystkich argumentów do komend. Jeżeli utkniemy to najczęściej są dwa sposoby:

1. `komenda --help` wyświetli na ekranie całą pomoc
2. `man komenda` uruchomi osobny program do wyświetlania dokumentacji. Klawisz `Q` by wyjść, klawisz `/` by wyszukać słowo kluczowe

Jeżeli oba sposoby zawodzą to zostaje tylko stack overflow albo modlitwa.

## Skróty klawiszowe

Często w dokumentacjach `CTRL+<KLAWISZ>` zapisuje się jako `^KLAWISZ` (`CTRL+` jest zamieniany na `^`).

Opiszę tutaj najczęściej stosowane przeze mnie skróty klawiszowe.
Więcej klawiszy tutaj: https://www.ostechnix.com/list-useful-bash-keyboard-shortcuts/

### CTRL+C

**C** Jak **C**ancel - Przerywa wykonania komendy / sekwencji (ale nie koniecznie wyłącza program)

* W bashu (lub innym programie do wpisywania komend jak np. klient SQL) gdy mamy uruchomiony program i chcemy go przerwać to przyciskamy `^C`.
* Jeżeli pomylimy się przy wpisywaniu komendy to możemy też przycisnąć `^C` i linijka się zresetuje.

### CTRL+L

**L** jak c**L**ear (Bo `C` jest już zajęte) - czyści ekran (czyli dla niekumatych - kasuje wyświetlaną treść z ekranu)

### CTRL+D

**D** Jak **D**etach - z ang. "odłączać" - wyłącza uruchomiony program. Można to uznać za "brutalniejsze" `^C` - jeżeli `^C` jest niewystarczające to `^D` powinno w większości rozwiązać sprawę (licz się z konsekwencjami, że może zostać przerwany program w połowie wykonaniego zadania).

### CTRL+R

**R** jako **R**everse Search - na podstawie historii komend i to co będziecie wpisywać próbuje wyszukać komendę którą wpisaliście wcześniej.

### CTRL+\

jak `^C` oraz `^D` nie działa to można jeszcze kliknąć `^\` - bardzo brutalnie wyłącza uruchomiony program, stosować w ostateczności.

### CTRL+W

Kasuje słowo (słowo = znaki bez spacji) przed kursorem.

### CTRL+H

Kasuje znak przed kursorem - tak jak backspace. Jedyną przewagą `^H` jest to, że jest bliżej od backspace dla palców. Jest to generalnie zaleciałość historyczna dla klawiatur których nie miały klawisza backspace (tak, to jest dziwne)

### CTRL+Q

Kasuje całą linijkę. Po prostu.

## Wildcard

Możemy też wykorzystać tzn `wildcard` do budowania wzorców które pomogą nam wybierać pliki. Np.

```bash
$ cat *.txt
```

Wyświetli zawartość wszystkich plików w danym folderze które kończą na `.txt`

Oczywiście nic nie stoi na przeszkodzie by korzystać z `*` w innych kombinacjach np.

```bash
$ ls 2018*.csv
2018-01.csv  2018-03.csv  2018-05.csv  2018-07.csv  2018-09.csv  2018-11.csv
2018-02.csv  2018-04.csv  2018-06.csv  2018-08.csv  2018-10.csv  2018-12.csv

$ ls 201*-01.csv
2015-01.csv  2016-01.csv  2018-01.csv  2019-01.csv

$ ls 201*-1*.csv
2015-10.csv  2015-12.csv  2016-11.csv  2018-10.csv  2018-12.csv
2015-11.csv  2016-10.csv  2017-12.csv  2018-11.csv
```

Jedna uwaga - korzystanie z znaku specjalnego `*` jak i innych tak naprawdę "rozwijają"
o wszystkie możliwe pliki znalezione wyrażeniem i wrzucają jako argumenty oddzielone spacją.

Jeżeli zrobisz:

```bash
$ *.csv
bash: command not found: 2015-01.csv
```

Wyświetli się error, że nie znalazł komendy `2015-01.csv` tylko dlatego, że to był pierwszy znaleziony plik,
a pierwsze słowo w bashu to jest komenda którą ma uruchomić.

Są też inne `wildcard` - jak np. `?`, w przeciwienstwie do `*`, `?` wyszukuje po jednym znaku, a nie ile znajdzie. np.

```bash
$ ls
a123.txt  ab123.txt  b123.txt

$ ls *123.txt
a123.txt  ab123.txt  b123.txt

$ ls ?123.txt
a123.txt  b123.txt
```

Mamy też nawiasy kwadratowe jeżeli chcemy wybrać zakres znaków (tylko jednego w danym miejscu)

```bash
$ ls ?123.txt
a123.txt  b123.txt  c123.txt  d123.txt  e123.txt  f123.txt  g123.txt

$ ls [c-f]123.txt
c123.txt  d123.txt  e123.txt  f123.txt
```

Przyznam szczerze że `?` oraz `[]` korzystam relatywnie rzadko, w większości przypadków `*` wystarcza.

!!! info ""
    W tym momencie jak już poznaliśmy tyle z basha jesteśmy w stanie poznawać bardziej zaawansowane rzeczy albo więcej komend.

    * Jezeli chcesz więcej komend to kliknij [tutaj](/howto/unix-terminal/part-4#commands)
    * Jeżeli chcesz więcej funkcji bashowych - czytaj po prostu dalej

## Uruchamianie wiele komend

Możemy uruchomić wiele komend naraz w jeden linijce, użyjemy do tego średnika:

```bash
$ cd folder; cat foo.csv
```

Wykona po kolei - najpierw komendę `cd folder` a później `cat foo.csv` -
obojętnie czy komenda pierwsza się wykona lub nie. Jeżeli folder nie istnieje to wyrzuci nam dwa błędy:

```bash
$ cd folder; cat foo.csv
cd: no such file or directory: folder
cat: foo.csv: No such file or directory
```

Nie jest to zbyt dobre rozwiązanie - dlatego częściej się stosuje z operatora `&&`:

```bash
$ cd folder && cat foo.csv
cd: no such file or directory: folder
```

W tym wykonaniu jak pierwsza komenda nie wykona się poprawnie (czyli wynik będzie inny niż 0)
to kolejne komendy się nie wykonają, łańcuch wykonań zostanie przerwany.

## Eval

Bardzo potężnym 'ficzerem' w shellu jest eval - pozwala zmienić wynik komendy (STDOUT, pamiętasz?)
na argument do komendy nadrzędnej (przykład wyjaśni to bardziej obrazowo).
Załóżmy że mamy plik który zawiera listę ważnych plików i chcemy sprawdzić
ile linijek kazdy z tych plików w tej liście posiada.

Musimy najpierw zaznajomić się z komendą `wc` - wbrew pozorom nie chodzi o toaletę tylko o skrót do `word count`.

```bash
$ cat important-files.txt
a123.txt
b123.txt
c123.txt

$ wc important-files.txt
 3  3 27 important-files.txt

$ wc -l important-files.txt
3
```

* Pierwsza komenda jak wyżej poznaliśmy - wyświetla zawartość pliku
* Druga komenda sprawdza w kolejności: ilość linijek, ilość słów, ilość znaków w pliku
* Trzecia komenda sprawdza tylko ilość linijek w pliku

Jak zauważyliśmy - jest to lista "ważnych plików" - tak jak obiecaliśmy, policzmy teraz ile linijek się znajduje w każdym pliku z tej listy:

```bash
$ wc -l $(cat important-files.txt)
  1 a123.txt
 22 b123.txt
  4 c123.txt
 27 total
```

Co tu się stało?

1. Wykonaliśmy najpierw komendę cat important-files.txt
2. Wynik komendy `cat` został wrzucony jako argumenty dla komendy `wc`
3. Ostatecznie nasza komenda rozwinęła się do `wc -l a123.txt b123.txt c123.txt`
4. Dostaliśmy listę linijek z podsumowaniem

Oczywiście - zamiast `cat` możemy skorzystać z obojętnie jakiej komendy - może to być program generujący jakiś wynik etc.

!!! danger ""
    Potocznie uważa sie że „eval is evil” i słusznie - argumenty podane dla eval
    przy błędnej konfiguracji mogą być destrukcyjnym narzędziem. Pamiętaj o tym!

## zapisywanie wyniku STDOUT do pliku i vice versa

OK - poznaliśmy całkiem sporo, czas poznać jak zapisywać do pliku.

Chcielibyśmy żeby wynik który jest wypluwany na ekranie (czyli STDOUT) został przekierowany do pliku.
Powiedzmy, że chcemy wyświetlić wszystkie pliki oraz zapisać wynik. Zrobimy to tak:

```bash
$ ls -la /bin > file.txt
$ wc -l file.txt
168 file.txt
```

1. Wykonaliśmy komendę `ls -la /bin`
2. Wynik zapisaliśmy do pliku `file.txt`
3. wyświetliliśmy ile jest linijek w pliku `file.txt`

A co jeśli wyskoczy nam błąd?

```bash
$ ls folder > file.txt
ls: cannot access 'folder': No such file or directory

$ cat file.txt
# nic nie wyswietla
```

Możecie zauważyć, że pomimo iż przekazujemy wynik do pliku to jednak błąd się pojawił. Pojawił się dlatego, że nie został przekazany przez strumień STDOUT tylko przez strumień STDERR

Jeżeli chcemy przekazać STDERR do innego pliku to możemy zrobić tak:

```bash
$ ls folder > file.txt 2> errors
$ cat errors
ls: cannot access 'folder': No such file or directory
```

zapis `2>` wskazuje, że mamy przekazywać do strumienia nr 2 którym domyślnie jest STDERR. Nie jest to zbyt oczywiste, ale taki bash już niestety jest.

znak `>` nadpisuje plik. Jeżeli chcemy dodawać nowy content do pliku możemy skorzystać z `>>`:

```bash
$ echo 111 >> file.txt
$ echo 222 >> file.txt
$ echo 333 >> file.txt
$ cat file.txt
111
222
333
```

Możemy też w drugą stronę - przekazywać strumień z innego pliku do programu (STDIN) np.

```bash
$ cat < file.txt
111
222
333
```

Osobiście z operatora `<` rzadko stosuję bo programy zwykle mają odczyt z plików w postaci parametrów.

### Wirtualne pliki

W systemie linux mamy kilka wirtualnych plików:

* `/dev/null` - pustka, wysłanie do niego źródeł kasuje je bezpowrotnie. Stosuje się gdy chcesz by nie drukowało na ekranie
* `/dev/random` - wysyła losowe wartości, dobre do nadpisania plików (skasowany plik tak naprawdę nie kasuje wartośći, tylko oznacza ją do ponownego zapisu)
* `/dev/urandom` - to samo co `/dev/random` ale robi to szybciej ale mniej bezpieczniej (szczegóły [https://www.2uo.de/myths-about-urandom](https://www.2uo.de/myths-about-urandom))
* `/dev/zero` - wysyła same zera (w sense liczbowym, a nie znakiem 0 który ma wartość 48, tablica ascii)

## Pipe

Jak już poznaliśmy jak wrzucać strumień z ekranu do pliku to możemy poznać pipe czyli po polsku rury.
Operator `|` (nazywanym operatorem pipe) pozwala nam na uruchamianie serię komend
gdzie kolejna komenda pobiera z strumienia poprzedniej komendy dane. Brzmi dość obco? To może przykładzik:

```bash
$ ls folder | wc -l
94
```

1. Wyswietlamy wszystkie pliki w folderze `folder`
2. Strumień z komendy `ls` jest pobierany przez komendę `wc -l` jako wejście

Możemy robić ciekawsze rzeczy jak np. sprawdzenie binarnego pliku PNG. Do tego potrzebujemy dwóch nowych komend:

* `head` - wyświetla kilka pierwszych linii z wejścia.
* `hexdump` - wyświetla binarne dane w postaci hex - każdy bajt jest pokazany jako dwa liczby 16-tkowe.

Jedziem z przykładem:

```bash
$ cat plik.png | hexdump -C | head -n4
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
00000010  00 00 01 e4 00 00 03 5c  08 02 00 00 00 01 ca 4b  |.......\.......K|
00000020  9f 00 00 00 03 73 42 49  54 08 08 08 db e1 4f e0  |.....sBIT.....O.|
00000030  00 00 20 00 49 44 41 54  78 9c ec dd 77 58 14 c7  |.. .IDATx...wX..|
```

1. wyświetliliśmy plik binarny
2. `hexdump -C` pokazał formę 16-tkową oraz znaki ASCII po prawej stronie
3. `head -n4` pokazał 4 linijki wyścia z komendy `hexdump -C`

To by było na tyle z podstaw i zaawansowanych rzeczy - jest oczywiście sporo innych rzeczy
ale to wystarczy by spokojnie się poruszać i wykorzystywac pełną moc shella w linuxie :)

# 4. Co zamiast basha?

## zsh + ohmyzsh

Sam codziennie korzystam z zsh oraz nakladki z pluginami oh my zsh - posiada masę pluginów które przyśpieszą bardzo skutecznie pracę oraz posiada 50 theme terminali :)

## fishshell

Nie używam, ale z screenshotów wygląda fajnie - już przy samym wpisywaniu komend próbuje podpowiedzieć jak jej użyć oraz sporo innych eyecandy gadżetów

## powershell

To żart. Proszę odejdź.

W tej części to na tyle, zapraszam do kolejnej [tutaj](/howto/unix-terminal/part-4).
