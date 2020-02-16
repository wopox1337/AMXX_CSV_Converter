 ![AMXX_CSV_Converter](https://img.icons8.com/officel/2x/export-csv.png)
 # AMXX_CSV_Converter
Tool for convert AMXX language files to CSV (.INI &lt;-> .CSV) (also supports .txt)

### Usage:
```
AMXX_CSV_Converter.py <inputfile> <outputfile> -e <encoding>
  Examples:
    AMXX_CSV_Converter.py file.csv file.ini (Converts .csv -> .ini)
    AMXX_CSV_Converter.py file.ini file.csv (Converts .ini -> .csv)
    AMXX_CSV_Converter.py file.ini (Converts file.ini -> file.csv)
    AMXX_CSV_Converter.py file.csv (Converts file.csv -> file.ini)
```
Drag & Drop - supports.

### Build exe file
- [Install PyInstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html) (pip install pyinstaller)
- Run `exe_build.bat`

`AMXX_CSV_Converter.exe` will be placed at /dist directory. 

### Example:
`amxmodx/data/lang/imessage.txt`
```
[en]
CHO_FIN_EXT = Choosing finished. Current map will be extended to next %.0f minutes
CHO_FIN_NEXT = Choosing finished. The nextmap will be %s
CHOSE_EXT = %s chose map extending
X_CHOSE_X = %s chose %s
CHOOSE_NEXTM = AMX Choose nextmap
EXTED_MAP = Extend map %s
TIME_CHOOSE = It's time to choose the nextmap...

[de]
CHO_FIN_EXT = Auswahl beendet. Laufende Map wird um %.0f Minuten verlängert.
CHO_FIN_NEXT = Auswahl beendet. Nächste Map ist %s
CHOSE_EXT = %s wählte Map-Verlängerung
X_CHOSE_X = %s wählte %s
CHOOSE_NEXTM = [AMXX] Wählt die nächste Map
EXTED_MAP = Verlängere Map %s
TIME_CHOOSE = Es ist an der Zeit, die nächste Map zu wählen...

[sr]
CHO_FIN_EXT = Biranje zavrseno. Sadasnja mapa ce biti produzena za %.0f minuta
CHO_FIN_NEXT = Biranje zavrseno. Sledeca mapa ce biti %s
CHOSE_EXT = %s biraj mapu sa produzivanjem
 // etc
```
Converts to:
```
 ,en,de,sr,tr,fr,sv,da,pl,nl,es,bp,cz,fi,bg,ro,hu,lt,sk,mk,hr,bs,ru,cn
CHO_FIN_EXT,Choosing finished. Current map will be extended to next %.0f minutes,Auswahl beendet. Laufende Map wird um %.0f Minuten verlängert.,Biranje zavrseno. Sadasnja mapa ce biti produzena za %.0f minuta,Oylama bitmisdir. Su anki map %.0f dakika uzatilacakdir,Les choix sont termines. La carte est prolongee de %.0f minutes,Val avslutat. Aktuell karta kommer att vara ytterligare %.0f minuter,Valg afsluttet. Nuvaerende bane bliver forlaenget til naeste %.0f minutter,Wybor zakonczony. aktualna mapa zostanie przedluzona o %.0f minut,Kiezen voltooid. Huidige map wordt verlengd met %.0f minuten,Eleccion finalizada. El mapa actual se extendera durante %.0f minutos mas,Escolha terminada. O mapa atual sera extendido pelos proximos %.0f minutos,Volba ukoncena. Nynejsi mapa zde bude na dalsich %.0f minut,Valinta suoritettu. nykyista mappia jatketaan %.0f minuuttia,Izbiraneto prikluchi. Nastoqshtata karta shte e udaljena za ushte %.0f minuti,Votarea s-a incheiat. Harta actuala va fi prelungita %.0f minute,A választás véget ért. A mostani pálya még %.0f percig lesz.,Pasirinkimai baigti. Sis zemelapis dar bus %.0f minutes,Volba ukoncena. Tato mapa bude este dalsych %.0f minut,Izborot e zavrshen. Segashnata mapa kje bide prodolzhena za %.0f minuti,Biranje zavrseno. Trenutna mapa ce biti produzena za %.0f minuta,Biranje zavrseno. Sadasnja mapa ce biti produzena za %.0f minuta,Голосование завершено. Карта продлена на %.0f минут,选择结束. 当前地图将被延长 %.0f 分钟
CHO_FIN_NEXT,Choosing finished. The nextmap will be %s,Auswahl beendet. Nächste Map ist %s,Biranje zavrseno. Sledeca mapa ce biti %s,Oylama bitmisdir. Secilen map ise %s,Les choix sont termines. La prochaine carte sera %s,Val avslutat. Kommande karta kommer att vara %s,Valg afsluttet. Naeste bane bliver %s,Wybor zakonczony. Nastepna mapa to %s,Kiezen voltooid. De volgende map is %s,Eleccion finalizada. El proximo mapa sera %s,Escolha terminada. O proximo mapa sera %s,Volba ukoncena. Dalsi mapa bude %s,Valinta suoritettu. Seuraava mappi on %s,Izbiraneto prikluchi. Sledvashtata karta shte e %s,Votarea s-a incheiat. Urmatoarea harta va fi %s,A választás véget ért. A következő pálya a %s lesz.,Pasirinkimtas baigtas. Kitas zemelapis %s,Volba ukoncena. Dalsia mapa bude %s,Izborot e zavrshen. Slednata mapa kje bide %s,Biranje zavrseno. Sljedeca mapa ce biti %s,Biranje zavrseno. Slijedeca mapa ce biti %s,Голосование завершено. Следующая карта %s,选择结束. 下一张地图为 %s
CHOSE_EXT,%s chose map extending,%s wählte Map-Verlängerung,%s biraj mapu sa produzivanjem,%s Map uzatilmasini secin,%s a choisi de prolonger la carte.,%s valde f'o'rlangning pa aktuell karta,%s valgte bane forlaengelse,%s wybral przedluzenie mapy,%s koos voor verlenging,%s ha elegido extender el mapa,%s escolheu extender o mapa,%s volil prodlouzeni soucasne mapy,%s valitsi nykyisen mapin,%s izbra udaljenie na nastoqshtata karta,%s a votat pentru prelungirea hartii actuale,%s még maradni szeretne,%s Pasirinko zemelapio pratesima,%s zvolil predlzenie sucasnej mapy,%s izbra prodolzjuvanje na mapata,%s je izabrao produzivanje mape,%s biraj mapu sa produzivanjem,%s выбрал продление карты,%s 选择延长当前地图
X_CHOSE_X,%s chose %s,%s wählte %s,%s izabrao %s,%s Secin %s,%s a choisi la carte %s,%s valde %s,%s valgte %s,%s wybral %s,%s koos %s,%s ha elegido %s,%s escolheu %s,%s volil %s,%s valitsi %s,%s izbra %s,%s a votat pentru %s,%s a %s pályára szavazott,%s pasirinko %s,%s zvolil %s,%s ja izbra mapata %s,%s je izabrao %s,%s izabrao %s,%s выбрал %s,%s 选择了 %s
CHOOSE_NEXTM,AMX Choose nextmap,[AMXX] Wählt die nächste Map,AMX izaberi sledecu mapu,AMX diger map secimi,AMX Choisir la prochaine carte,AMX valde kommande karta,AMX vaelg naeste bane,AMX wybral nastepna mape,AMX Kies volgende map,AMX Elegir proximo mapa,AMX Escolher proximo mapa,Zvol si dalsi mapu,Valitse seuraava mappi,AMX Izberete sledvashta karta,AMX Alege harta urmatoare,Válaszd ki a következő pályát.,AMX Issirink sekanti zemelapi,Zvol si dalsiu mapu,AMX Izberete sledna mapa,AMX Izbor sljedece mape,AMX izaberi slijedecu mapu,AMX Выбор следующей карты,AMX 选择下一张地图
EXTED_MAP,Extend map %s,Verlängere Map %s,Produzi mapu %s,%s Map surecini uzat,Prolonger la carte %s,Fortsatt karta %s,Forlaeng bane %s,Przedluz mape %s,Verleng map %s,Extender el mapa %s,Extender o mapa %s,Prodluzuje mapu %s,Jatka mappia %s,Udalji kartata %s,Prelungirea hartii actuale %s,Maradjunk a %s pályán!,Pratestas zemelapis %s,Predlzuje mapu %s,Prodolzhi ja mapata %s,Produzi mapu %s,Produzi mapu %s,Продление карты на %s,延长地图 %s
TIME_CHOOSE,It's time to choose the nextmap...,"Es ist an der Zeit, die nächste Map zu wählen...",Vreme je da se izabere sledeca map...,Yeni map secimi baslamisdir...,Il est temps de choisir la prochaine carte...,Dags att utse kommande karta...,Det er tid til at vaelge naeste bane...,Wybierz ktora mape chcesz grac,Het is tijd om de volgende map te kiezen...,Es hora de elegir el proximo mapa...,E a hora de escolher o proximo mapa...,Je cas pro volbu dalsi mapy...,On aika valita seruaava mappi...,Vreme e da se izbere sledvashtata karta...,E timpul sa alegeti harta urmatoare...,Itt az idő hogy kiválaszd a következő pályát.,Laikas issirinkti kita zemelapi..,Je cas pre volbu dalsej mapy...,Vreme e da se izbere sledna mapa...,Vrijeme je za izbor nove mape...,Vrijeme je da se izabere slijedeca mapa...,Пора выбирать следующую карту...,是该选择下一张地图了...

```
Then we can import CSV to Excel table:
![Table](https://i.imgur.com/UzbD61U.png)
