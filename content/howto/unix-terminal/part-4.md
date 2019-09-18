Title: HOWTO Unix Terminal (Część pierwsza)
Date: 2019-08-19
Slug: howto/unix-terminal/part-4
Lang: pl

W tej części umówimy komendy proste, podstawowe oraz zaawansowane.

[TOC]

# 5. Podstawowe komendy do pracy z plikami/folderami ## {: #commands}

## ls

ls = **L**is**T** Wyświetla pliki w folderze. Po prostu.

```bash
$ ls  # wyswietla aktualny listę plików w folderze w którym się znajduje
 2019-07-29.jpg                    krs-hackerspace.pdf
 2019-09-25.jpg                    lecture.pdf
$ ls gimp  # wyswietla folder gimp
IMG_20180408_234932.dng  IMG_20180411_191031.dng  VID_20180317_155713.mp4
IMG_20180411_190933.dng  IMG_20180414_160945.dng  VID_20180317_163447.mp4
$ ls -la # wyświetla wszystkie pliki (również ukryte) `-a jako --all` w postaci długiej listy `-l`
total 3977296
drwxr-xr-x  167 firemark firemark     139264 paź  3 22:50  .
drwxr-xr-x    4 root     root           4096 kwi 24  2018  ..
-rw-rw-r--    1 firemark firemark    1343287 lip 29 22:57  2019-07-29.jpg
-rw-rw-r--    1 firemark firemark      26029 wrz 25 21:31  2019-09-25.jpg
$ ls -thor
# w postaci długiej listy bez grup `-o`
# posortowane po czasie w odwrotnej kolejnosci
# `-tr` oraz ludzkie formaty wielkości plików `-h jako --human-readable`
total 3,8G
-rw-r--r--  1 firemark 3,8G lis 26  2014  win7.ova
drwxr-xr-x  6 firemark 4,0K cze 17  2015  Slic3r
drwx------  3 firemark 4,0K paź 30  2015  Library

```

## pwd

wyświetla w którym aktualnie folderze jesteśmy.

```bash
$ pwd
/home/user/
```

## cd

cd = **C**hange **D**irectory przeskaskuje do danego folderu w terminalu. Brak argumentu przeskakuje do folderu domowego

```bash
$ cd folder
$ pwd
/home/user/folder
```

## touch

"Dotyka" plik, zmieniając mu czas na "teraz". Jeżeli pliku nie ma to tworzy pusty.

```bash
$ touch plik  # tworzy plik
```

## mkdir

mkdir = **M**a**K**e **DIR**ectory

Tworzy folder. Po prostu. Naprawdę.

```bash
$ mkdir folder  # tworzy folder
```

## cat

Wyświetla podany plik - N argumentów wyświetla N plików.

## rm

rm = **R**e**M**ove. Kasuje plik/foldery

```bash
$ rm plik
$ rm *.png -f  # kasuje N plików bez pytania się o każdy plik
$ rm folder -rf  # rekurencyjnie kasuje pliki z folderu oraz sam folder
```

## mv

mv = **M**o**V**e. Przesuwa folder/plik

```bash
$ mv x y  # przesuwa plik/folder x do y (zmienia nazwę)
$ mv plik folder/  # przesuwa plik do folderu folder
# mv *.png folder/  # przesuwa wszystkie pliki do folderu folder
```

## cp

cp = **C**o**P**y. Kopiuje pliki oraz foldery

```bash
$ cp x y  # kopiuje plik x do y
$ cp plik folder/  # kopiuje plik x do folderu folder
$ cp *.png folder/  # kopiuje pliki do folderu folder
# cp folder1 folder2 -r  # kopiuje folder folder1 do folder2 rekurencyjnie (z całą zawartością)
```

## wc

wc = **W**ord **C**ount. Wyświetla statystyki pliku - linijki, znaki etc.

```bash
$ wc -l duzy_plik maly_deszcz # wyswietla ile lin posiadają pliki
300 duzy_plik
  5 maly_deszcz
```

## find

wyszukuje pliki oraz foldery rekurencyjnie. Find ma swój syntax co do argumentów - warto przejrzeć jego manual.

```bash
$ find folder  # znajduje wszystkie pliki w tym folderze i kolejnych
$ find folder -type f  # znajduje tylko pliki, bez folderów
$ find folder -type d  # znajduje tylko foldery
$ find -iname 'name.txt'  # szuka czy istnieja pliki o nazwie name.txt
$ find -iname 'name*'  # szuka czy istnieją pliki o nazwie 'name' na początku
```

Możemy łączyć kilka zapytań w jedno:

```bash
$ find -iname '*.txt' -or -iname '*.png'  # wyszukaj pliki txt lub png
$ find -iname 'sebastian' -and -type d  # wyszukaj foldery o nazwie sebastian
```

Pozwala też kasować pliki:
```bash
$ find -iname '*.js' -delete
```

Dla każdego wyszukanego pliku możemy uruchomić jakąś komendę przy użyciu xargs:

```bash
$ find -iname '*.py'
./foo.py
./bar.py
./foo/foo.py
$ find -iname '*.py' | xargs wc -l  # uruchamia wc -l ./foo.py; wc -l ./bar.py; etc
100 ./foo.py
200 ./bar.py
300 ./foo/foo.py
```

## du

du = **D**isk **U**sage. Sprawdza wielkość plików w danym folderze lub zaznaczoe pliki.

```bash
$ du Desktop   # sprawdza wielkosc folderu
758980  Desktop
$ du -h Desktop  # sprawdza wielkosc folderu i podaje "ludzkie" jednostki (-h = human)
742M    Desktop
$ du -cha Library/VirtualBox  # -c = count; -a = all
8.0K    Library/VirtualBox/VDI/.DS_Store
1.6G    Library/VirtualBox/VDI/xubuntu-6.06.1-x86.vdi
1.6G    Library/VirtualBox/VDI
4.0K    Library/VirtualBox/Machines/xubuntu-6.06.1-x86/xubuntu-6.06.1-x86.xml
8.0K    Library/VirtualBox/Machines/xubuntu-6.06.1-x86
12K     Library/VirtualBox/Machines
1.6G    Library/VirtualBox
1.6G    total
```

## dd

dd = **C**opy **C**opy bo na `cc` już brakło miejsca dlatego przesuneli się na kolejną literkę. Porąbane co nie?

Kopiuje zawartość pliku A (wirtualnego lub zwykłego) do pliku B. Przypommina ze plikami może być pendrive, dysk, partycja, płyta cd. Kopię systemu możemy zapisać do 1 pliku, to jest kurde fajne!

```bash
$ dd if=PLIK_A of=PLIK_B  # skopiowanie całego pliku PLIK_A do pliku PLIK_B
$ dd if=PLIK_A of=PLIK_B bs=N count=M  # skopiowanie M chunków (chunk = "Kawałek" czy grupa bajtów) wielkości N bajtów (czyli N*M bajtów)
$ dd if=PLIK_A of=PLIK_B bs=1K count=100  # skopiowanie 100kB danych
$ dd if=PLIK_A of=PLIK_B status=progress  # wyswietla ile skopiowal danych i z jaka predkoscia caly czas
```

## mc

Taki total commander w terminalu ale nie jesteś hakerem po to by korzystać z takich narzędzi ;-)

# 6. Podstawowe ekrany do pracy z terminalem

## history

Wyświetla historię komend. Fajna sprawa.

## watch

Często się przydaje gdy dany proces działa w tle i coś wykonuje - watch uruchamia co N sekund podaną przez nas komendę.

```bash
$ watch -n2 ls
# co 2 sekundy będzie uruchamiał komendę ls i będzie wyświetlał jakie są aktualne pliki w tym folderze
# przydaje się bardzo gdy mamy skrypt który generuje masę plikóww dłuższym czasie
```

## reset

"Resetuje" ekran - czasami po otwarciu pliki zdarza się, że na ekranie zostają śmieci które psują nawet pisanie. `reset` rozwiązuje problem

## clear

Czyści ekran - pokaże się tylko PROMPT po jej wpisaniu.

## ps

Pokazuje działające procesy w systemie.

```bash
$ ps u  # procesy włączone tylko przez usera
$ ps x  # procesy włączone poza aktualnym terminalem
$ ps a  # procesy innych userów (np. root czy www-data)
$ ps aux  # wszystko naraz!!!
```

## htop

zarządza procesami w systemie - nie jest to domyślna aplikacja ale bardzo wspomaga życie.

# 7. Podstawowe komendy do pracy z tekstem

## echo

Wyświetla tekst z argumentu na ekranie. Często stosowane by wyświetlić stringa z zmiennymi:

```bash
$ echo test
test
$ echo elo $PWD
elo /home/user
```

## more

Fajna komenda - jak masz dużo tekstu z wyniku komendy (np. 300 linijek) i chcesz wszystko przejrzeć to możesz to przyda ci sie komenda more (pozwala na przewijanie linii krok po kroku)

* Enter - przewija linijkę
* Spacja - przewija cały tekst

```bash
$ cat duzy_plik | more
```

## less

Świetna komenda do czytania logów czy dużych plików - wczytuje tyle ile powinnien (a nie jak inne edytory, wczytują cały plik), co się bardzo przydaje gdy plik ma kilka GB.

Poza tym posiada wyszukiwarkę (uaktywnia się klawiszem `/` oraz  `?` jak chcemy szukać w drugą stronę) oraz pozwala na wyświetlanie tylko linijek które pasują do wyrażenia (znak `&`)

Obie funkcje przyjmują wyrażenia regularne (sam sobie poszukaj dokumentacji!)

## head

Pokazuje 10 (domyślnie) linijek z wyniku/pliku. Przydaje się gdy chcesz zobaczyć początek. Komenda też przerywa program z którego odczytuje (no bo i tak wiecej nie wyświetli)

```bash
$ cat duzy_plik | head  # pokazuje 10 linijek
$ cat duzy_plik | head -n20  # pokazuje 20 linijek
$ head -n20 duzy_plik  # to samo co wyzej bez pipe
```

## tail

To samo co head tylko na odwrót - pokazuje ostatnie linijki.

```bash
$ cat duzy_plik | tail  # pokazuje 10 ostatnich linijek
$ cat duzy_plik | tail -n20  # pokazuje 20 ostatnich linijek
```

można też "nasłuchiwać" w tak zwanym trybie follow:

```bash
$ tail -f 2018-01-01.log  #  nasluchuje zmiany w pliku - jak dojdą nowe linijki, tail je wyświetli
$ dlugo_dzialajacy_program_naprawde | tail -f  # nasluchuje ostatnie zmiany z komendy
```

## wc

Bardzo pomaga policzyć ilośc linijek z STDOUT.

```bash
$ ls folder | wc -l  # wyswietla ile było plików (linijek w STDOUT)
```

## cut

Wycina odpowiednie kawałki w linijce. Super narzędzionko

```bash
$ head -n5 /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
$ head -n5 /etc/passwd | cut -d: -f7   # dla podziału znaku ':' wybiera 7 słowo
/bin/bash
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin
/bin/sync
```

## sort

Sortuje wyniki. Bardzo fajny program.

```bash
# rozszerzony przykład z cut
$ head -n5 /etc/passwd | cut -d: -f7 | sort
/bin/bash
/bin/sync
/usr/sbin/nologin
/usr/sbin/nologin
/usr/sbin/nologin

# mozemy też sortować wyniki z du
$ du -h Library/* | sort -hr  # -h = human; -r = reverse
1.6G    Library/VirtualBox/VDI
1.6G    Library/VirtualBox
12K     Library/VirtualBox/Machines
8.0K    Library/VirtualBox/Machines/xubuntu-6.06.1-x86
```

## uniq

Zlicza takie same linijki. Tylko pamiętaj - linijki muszą być obok siebie!

```bash
# rozszerzony przykład z cut
$ head -n10 /etc/passwd | cut -d: -f7 | uniq
/bin/bash
/usr/sbin/nologin
/bin/sync
/usr/sbin/nologin

# sprobójmy posortować
$ head -n10 /etc/passwd | cut -d: -f7 | sort | uniq
/bin/bash
/bin/sync
/usr/sbin/nologin

# możemy też zliczać wystąpienia
$ cat /etc/passwd | cut -d: -f7 | sort | uniq -c
      2 /bin/bash
      5 /bin/false
      1 /bin/sync
      1 /sbin/nologin
     33 /usr/sbin/nologin

# ... oraz posortować ponownie
$ cat /etc/passwd | cut -d: -f7 | sort | uniq -c | sort -n  # -n = numeric
      1 /bin/sync
      1 /sbin/nologin
      2 /bin/bash
      5 /bin/false
     33 /usr/sbin/nologin
```

## grep

najfajniejsza komenda - filtruje linijki z pliku/wyjścia.

```bash
$ grep bash /etc/passwd   # pokaz linijki ktore maja w sobie slowo bash
root:x:0:0:root:/root:/bin/bash
user:x:1000:1000:user,,,:/home/user:/bin/bash
$ grep -v bash /etc/passwd  | wc -l  # zlicz ile jest linijek NIE posiadaja slowa bash
40
$ lspci | grep -i audio  # -i = incase
00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller (rev 06)
00:1b.0 Audio device: Intel Corporation 8 Series/C220 Series Chipset High Definition Audio Controller (rev 05)
01:00.1 Audio device: NVIDIA Corporation GK107 HDMI Audio Controller (rev ff)
```

!!! info ""
    wyrazenie grep jako argument przyjmuje wyrazenia regularne, więcej na [https://www.cyberciti.biz/faq/grep-regular-expressions/](https://www.cyberciti.biz/faq/grep-regular-expressions/)

# 8. Komendy związane z siecią

## wget

Ściąga podany plik i zapisuje go w aktualnym folderze.

```bash
$ wget https://file-examples.com/wp-content/uploads/2017/02/zip_2MB.zip
# zapisuje w folderze aktualnym plik zip_2MB.zip
```

## ssh

W skrócie - pozwala na łączenie się z innymi maszynami które mają dostęp do protokołu ssh

```bash
ssh user@host.pl
# loguje sie do innej maszyny
```

## curl

Robi requesty HTTP na aktualną stronę. Warto przejrzeć jego manual

## httpie

Curl na sterydach - gorąco polecam.

# 9. Konkluzja

W tym artykule zamierzałem pokazać podstawowe elementy poruszania się po terminalu w linuxie oraz podstawowe użycie komend. Często doświadczam u osób początkujących w IT brak wiedzy o terminalu gdzie korzystają go w ostateczności lub unikają go jak ognia korzystając z GUI czy IDE. Zamierzałem też pokazać że terminale nie gryzą i wraz z zrozumieniem jak to wszystko działa daje bardzo potężne narzędzie do pracy z kodem czy "hakowaniem"
