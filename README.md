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

# License
The MIT License

Copyright (c) 2017 Michał Wąsowicz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

