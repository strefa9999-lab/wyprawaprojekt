Mission 
Twoim zadaniem jest dotarcie do wyznaczonego celu na siatce współrzędnych, zarządzanie energią pojazdu i unikanie marsjańskich pułapek. Na koniec misji generowany jest raport, a trasa przejazdu rysuje się w oknie graficznym.
Wymagania i Uruchomienie
Gra nie wymaga instalowania żadnych dodatkowych paczek (np. przez `pip`). Używa tylko standardowej biblioteki Pythona (m.in. `math`, `random`, `json`, `turtle`).
Aby zagrać, otwórz terminal (wiersz poleceń) w folderze z grą i wpisz:
```bash
python main.py
Sterowanie w terminalu:
w - jedź do przodu (kosztuje energię)
a - skręć w lewo (zmiana kąta o 90 stopni)
d - skręć w prawo (zmiana kąta o 90 stopni)
q - przerwij misję i wyjdź
Przed startem misji wybierasz poziom trudności, który wpływa na limit kroków, kary za przeszkody oraz bonusy:
Łatwy (Spacer): Dużo stacji solarnych, mało skał, wysoki limit kroków (80), małe kary za zderzenia.
Średni (Normalny): Standardowy balans, limit 50 kroków.
Trudny (Piekło): Mało czasu (30 kroków), bardzo dużo skał i kraterów, stacje solarne to rzadkość, a zderzenia surowo karzą utratą energii.
Uważaj też na losowe zdarzenia (np. burze piaskowe czy znalezienie minerałów), które aktywują się podczas jazdy!!
