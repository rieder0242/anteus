# Mivégre?

Ez egy teszt feladat az Anteus Kft részére.

Olyan grafikus alkalmazást, ami egy adatbázis tábláinak tartalmát exportálja CSV fájlokba

# Specifikáció

## Elvárások, igények

- A program kapcsolódjon egy MySQL adatbázishoz. A kapcsolat beállításait egy konfigurációs fájlból
  vegye.
- Az adatbázis tábláit táblázatos/grid-es megjelenítési formában mutassa meg. Annyi sort mutasson,
  ahány tábla van az adatbázisban.
- A táblázat első oszlopa legyen pipálható.
- A második oszlopban jelenítse meg az adatbázis tábla nevét.
- Az ablak alján legyen egy Save gomb, amit ha megnyomunk, akkor a program a munkakönyvtárba
  mentse ki a kipipált táblák tartalmát CSV formátumban. Egy tábla egy CSV fájl, a fájl neve a tábla neve
  legyen, CSV kiterjesztéssel.
- A feladatot lehetőleg Python 3.9 verzió alatt oldja meg
- GUI-t wxPython-ban (jelenlegi stabil verzió wxPython 4.2.1a).

## Projekt struktúra

Úgy készítse el a megoldást, ahogyan az interneten publikusan közzétett projektektől is elvárná. Cél, hogy a
program célja és beüzemelésének módja közérthető, megismételhető legyen.

- A megoldás áttekinthető könyvtár struktúrában készüljön (forrásfájlok helye nem a projekt gyökerében
  van)
- Tartalmazzon egy rövid leÍrást (README.md)
- Futtatás lehetőleg virtualenv-ből történjen. Könyvtár és leírás tartalmazza a környezet felépítéséhez
  szükséges modul és verzióinformációkat is (requirements.txt)
- A kód formázásakor, dokumentálásakor vegye figyelembe a Python ajánlásokat

# Install

```sh
venv\Scripts\pip install pyyaml
venv\Scripts\pip install mysql-connector-python
venv\Scripts\pip install wxPython
```

# Run

```sh
python.exe src\main.py
```

# Működés

A konfig helye a futtatás helyén a `conf.yml`.
Ugyan ide késziti a csv fileokat.
