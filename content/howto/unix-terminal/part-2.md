Title: HOWTO Unix Terminal (Część druga)
Date: 2019-08-19
Slug: howto/unix-terminal/part-2
Lang: pl

[TOC]

# 3a. Bash (podstawy)

Najpopularniejszą domyślną powłoką w systemach linuxowych jest bash (aczkolwiek nie najlepszą, ja preferuję zsh, inni fish shell etc) i jak na początek nam to wystarczy. Składnia bash jest bardzo pomocna do uruchomienia komend w linuxie oraz samych operacji na plikach oraz folderach.

## Podstawowe komendy

Żeby łatwiej zrozumieć podstawy powłoki (shella) uznałem że potrzebujemy wiedzieć o 4 podstawowych komendach:

* `cd FOLDER` zmienia aktualny folder na FOLDER.
* `echo TEKST` wyświetla podany TEKST na ekranie.
* `ls` wyświetla wszystkie (prawie) pliki w aktualnym folderze.
* `cat PLIK` wyświetla zawartość pliku (nawet binarnego co najczęściej psuje ekran).

## Podstawy

!!! info ""
    Dobry protip - bash oraz inne shella posiadają tab completion - nie musicie wpisywać całą nazwę komendy/pliku tylko wystarczy wpisać część początku słowa i kliknąć w *tab* - bash powinnien sam podpowiedzieć (o ile zdoła) i uzupełnić za nas

Jeżeli chcemy uruchomić jakąś komendę wystarczy że ją wpiszemy np. komendę do wyświetlania plików:

```bash
$ ls  # Komentarz
2019-07-29.jpg                    legacy_code.png
Arduino                           Library
```

* Pierwsze słowo to tak zwany prompt - służy tylko do zasugerowania że to jest miejsce gdzie user może wpisywać komendy.
* Komentarze zaczynają się od `#` - po `#` wszystko jest ignorowane do końca linii
* Kolejne słowo to wpisana przez nas komenda - tutaj mamy `ls`
* Komenda znalazła pliki oraz foldery w folderze w którym się znajduje w tej chwili program
* Znalezione pliki oraz foldery zostały 'wyrzucone' do strumienia `STDOUT`, który domyślnie wyświetla na ekran wynik

### Kod wyniku
a co z exit code o którym wspominaliśmy?

```bash
$ echo $?
0
```

w Bashu komenda `$?` zwraca wynik ostatniej wykonanej komendy - taki kod jest bardzo pomocny w skryptach by zweryfikować poprawność wykonania komendy

!!! info ""
    Rzadko się korzysta z `$?` w samym shellu - wspomniałem tutaj o tym byś miał świadomość,
    że wyniki wykonanej komendy istnieją i że są wykorzystywane - przyda się to na później :)


## Argumenty/Parametry ## {: #arguments}
Komenda `ls` może też korzystać z argumentów, które wpisujemy jako kolejne słowa

```bash
$ ls Arduino
accelerometer_MMA8653  alkomi  libraries  noemi  sketch_mar10a  sketch_may12a
```

Ta Komenda otwiera dany folder i wyświetla w nim pliki/foldery. Argumenty mogą zawierać różne opcje:

```bash
$ ls --all -l
total 3976972
drwxr-xr-x  165 firemark firemark     139264 wrz 19 23:55  .
drwxr-xr-x    4 root     root           4096 kwi 24  2018  ..
-rw-rw-r--    1 firemark firemark    1343287 lip 29 22:57  2019-07-29.jpg
drwx------    5 firemark users          4096 maj 25  2017  .adobe
drwx------    2 firemark users          4096 paź 14  2018  .alsaplayer
drwxr-xr-x    3 firemark users          4096 sty 13  2018  .altera.quartus
```

Użyliśmy opcję `--all` oraz `-l`:

* `--all` wyświetla wszystko włącznie z `.` (folder aktualny) oraz `..` (folder poprzedni) oraz ukrytymi plikami (zaczynającymi się na `.`)
* `-l` wyświetla pliki/foldery w postaci listy w każdej linijce z dodatkowymi informacjami jak user, grupa, uprawnienia etc

Pewnie zauważyłeś/aś, że `--all` zawiera podwójny myślnik, a `-l` posiada tylko jeden. Dlaczego?
Ponieważ przyjęło się (nie jest to reguła dla każdego programu!), że jednoliterkowa opcja posiada tylko jeden myślnik, a dłuższa opcja zawiera podwójny.
Z takie odróżnienia, które są jednoznakowe a które wieloznakowe opcje, pozwala to nam lączyć jednozakowe.
Wiele opcji ma aliasy w postaci jednoznakowych literek, np. w komendzie `ls` opcja `--all` można zapisać jako `-a` czyli:

```bash
$ ls -l --all
$ ls -l -a
$ ls -la
```

Wykonają takie same akcje. Kolejność jednolinijkowych opcji nie jest ważna,
więc można odpalić komendę ls która zamienia wielkość w bajtach na 'ludzki'
rozmiar oraz posortuje względem day:

```
$ ls -thor  # o ls będzie więcej w innym rozdziale - w tej chwili sie nie przejmuj co to za literki
total 3,8G
-rw-rw-r--  1 firemark 590K wrz  7 20:49  iso.png
-rw-rw-r--  1 firemark 145K wrz  8 16:17  oblique.png
drwx------  6 firemark  12K wrz 17 22:20  Downloads
-rw-rw-r--  1 firemark  82K wrz 17 22:26  x.png
-rw-rw-r--  1 firemark 2,1K wrz 18 23:24  howto-bash
```

Opcje mogą zawierać dodatkowe parametry np. `ls` posiada opcję `--ignore` który pozwala ignorować pliki względem wzorca np.

```bash
$ ls --ignore='*.jpg'
$ ls -I '*.jpg'
```

Obie komendy wykonują to samo (tzn wyświetlają wszystko poza plikami jpg). Przyjęło sie, że dla długich nazw opcji parametr jest podawany z znakiem `=`, a dla jednoznakowych oddziela się spacją.

!!! danger ""
    To że komenda i sporo innych komend ma taką konwecję argumentów
    wynika tylko z dobroczynności programisty - nie każda komenda będzie się trzymać tej konwencji
    przykładem jest komenda find, która zostanie opisane w kolejnych działach

## Foldery specjalnie

odróżniamy w zasadzie 4 specjalne foldery:

* `.` - folder w którym aktualnie się znajdujemy
* `..` - folder rodzica - np. jak jesteśmy w `/foo/bar/` to rodzicem jest `/foo/`
* `~` - folder domowy użytkownika. Najczęściej to jest `/home/<USERNAME>/`
* `/` - folder "root" - początek filesystemu w linuxie. Jeżeli w nazwie pliku/folderu zaczyna się od `/` to oznacza że adres jest stały, a nie względny

### Przykłady

```bash
$ cd ~  # załóżmy że to jest /home/firemark/
$ cd magic  # załóżmy że jest taki folder
$ cat plik  # wyświetla /home/firemark/magic/plik
$ cat folder/plik  # wyświetla /home/firemark/magic/folder/plik
$ cat ./plik  # wyświetla /home/firemark/magic/plik  - tak samo jak poprzednie przyklady
$ cat ../plik  # wyświetla /home/firemark/plik  - szuka w folderze poprzednim
$ cat ~/folder/plik  # wyświetla /home/firemark/folder/plik  - szuka w folderze domowym
$ cat /plik  # wyświetla /plik
```

W tej części to na tyle, zapraszam do kolejnej [tutaj](/howto/unix-terminal/part-3).
