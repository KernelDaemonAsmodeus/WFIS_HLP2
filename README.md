Projekt Webowy przy użyciu Flask (Ruletka)

Projekt można uruchomić lokalnie poprzez:
  1. sklonowanie repozytorium
  2a. w wybranym IDE (np. PyCharm) pobrać zależności
      wymienione w pliku requirements.txt
  3. uruchomić plik:
     app.py
lub
  2b. wpisanie w terminal w katalogu z aplikacją:
     pip install -r requirements.txt
  3. wpisanie w terminal w katalogu z aplikacją:
     flask run

Aby zbudować obraz Dockera należy:
  1. sklonować repozytorium z platformy Github
  2. w folderze ze sklonowanym repozytorium otworzyć terminal i wpisać:
     docker build --tag WFISHLP2 .

Aby uruchomić obraz Dockera należy:
  1a. w programie Docker Desktop w zakładce Images uruchomić zbudowany
      wcześniej obraz WFISHLP2
lub
  1b. wpisać w terminal:
      docker run -p 5000:5000 --name WFISHLP2 WFISHLP2
     
