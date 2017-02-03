# wd-student
Pythonowy skrypt sprawdzający oceny w dziekanacie. Powiadamia mailowo o każdej zmianie w ocenach.

# Instalacja dla leniwych 
1. Za pomocą ssh zalogować się na student.agh.edu.pl
2. git clone https://github.com/vonsowic/wd-student
3. cd wd-student
4. ./install.sh (jak wyskoczą czerwone napisy straszące o braku miejsca na dysku to się nie ma co przejmować)

#Pare słów komentarza na temat instalacji
Na studencie nie ma pythona w wersji 3.x, dlatego install.sh najpierw go pobiera co chwilę zajmuje. Po zakonczeniu budowy interpretera program prosi o podanie danych do logowania,a także o adres mailowy na który będą wysyłane powiadomienia.

# Todo
Program generalnie działa, ale zostało parę rzeczy do poprawy, np. z jakiegoś względu python na studencie woli latin-1 od standardowego utf-8, przez co niektóre polskie znaki w powiadomieniu nie są poprawnie zakodowane. Każda wysłana poprawka będzie mile widziana ;)

