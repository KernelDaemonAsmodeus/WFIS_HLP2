Projekt Webowy przy użyciu Flask (Ruletka)

Projekt można uruchomić lokalnie poprzez:
  1. uruchomienie pliku:
     app.py
lub
  2. wpisanie w terminal w katalogu z aplikacją:
     flask run

Aby zbudować obraz Dockera należy:
  1. sklonować repozytorium z platformy Github
  2. w folderze ze sklonowanym repozytorium otworzyć terminal i wpisać:
     docker build --tag WFISHLP2 .

Aby uruchomić obraz Dockera należy:
  1. w programie Docker Desktop w zakładce Images uruchomić zbudowany
     wcześniej obraz WFISHLP2
lub
  2. wpisać w terminal:
     docker run -p 5000:5000 --name WFISHLP2 WFISHLP2
