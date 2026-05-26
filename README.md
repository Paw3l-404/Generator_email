# 🚀 Generator Odpowiedzi E-mail

Aplikacja webowa oparta na frameworku Flask, automatyzująca proces tworzenia odpowiedzi na wiadomości e-mail (takie jak zapytania ofertowe, propozycje współpracy) przy wykorzystaniu sztucznej inteligencji **Google Gemini 1.5 Flash**. 

Projekt został zrealizowany w 2025 roku w ramach zajęć na Wydziale Matematyki i Fizyki Stosowanej Politechniki Rzeszowskiej.

---

## 📖 O projekcie

Głównym celem projektu było stworzenie narzędzia automatyzującego zarządzanie komunikacją elektroniczną, co jest odpowiedzią na rosnącą liczbę wiadomości w życiu zawodowym. Aplikacja pozwala na szybkie wygenerowanie logicznej, kontekstowej odpowiedzi na otrzymanego e-maila. Użytkownik decyduje, czy propozycja zostaje zaakceptowana czy odrzucona, oraz określa docelowy ton wiadomości (formalny lub nieformalny).

### 💡 Rozwiązane problemy technologiczne
Początkowo projekt zakładał stworzenie rozszerzenia (MailExtension) do klienta poczty Mozilla Thunderbird opartego na API ChatGPT. W toku prac napotkaliśmy jednak na problemy z walidacją plików w Thunderbirdzie, blokady protokołu CORS oraz wyczerpanie darmowych limitów w OpenAI. Wymusiło to zmianę architektury. 

Ostatecznie zaimplementowaliśmy pełnoprawną aplikację webową o architekturze klient-serwer. Ewentualne problemy z mechanizmem CORS rozwiązano stosując bibliotekę Flask-CORS, a silnik generatywny zmieniono na bardziej przystępny model od Google.

---

## ✨ Główne funkcjonalności

* **Generowanie kontekstowych odpowiedzi:** Algorytm czyta oryginalną treść e-maila i na jej podstawie tworzy spójną odpowiedź.
* **Pełna kontrola nad decyzją:** Możliwość wyboru odpowiedzi pozytywnej (akceptacja) lub negatywnej (odmowa).
* **Dostosowanie tonu:** Dwa tryby generowania tekstu – formalny (biznesowy) oraz nieformalny.
* **Responsywny interfejs:** Przyjazny dla użytkownika frontend z dynamicznie skalującym się polem tekstowym i płynnymi animacjami (GSAP).

---

## 🛠 Technologie

**Backend:**
* Python 3
* Flask & Flask-CORS
* Google Generative AI (`google-generativeai`)
* `python-dotenv` 

**Frontend:**
* HTML5 / CSS3 / Vanilla JavaScript
* GSAP (animacje UI)
* FontAwesome (ikony)

---

# 🚀 Instalacja i Uruchomienie Projektu

## 1. Instalacja zależności środowiskowych

Upewnij się, że posiadasz zainstalowane środowisko **Python 3**.

Uruchom w terminalu:

```bash
pip install flask flask-cors google-generativeai python-dotenv
```

## 2. Konfiguracja bezpieczeństwa (.env)

W głównym katalogu projektu utwórz plik o nazwie .env i umieść w nim swój prywatny klucz API Google AI:
```bash
API_KEY=TWÓJ_KLUCZ_API_GEMINI
```

## 3. Uruchomienie backendu (Flask)

Uruchom serwer aplikacji:

```bash
python app.py
```
Po poprawnym uruchomieniu aplikacja będzie nasłuchiwać na porcie 5000.

## 4. Uruchomienie frontendu
Otwórz plik index.html bezpośrednio w przeglądarce
lub uruchom projekt przy użyciu serwera statycznego, np.: Live Server w Visual Studio Code

# ⚠️ Zastrzeżenie / Disclaimer

Projekt został stworzony wyłącznie w celach edukacyjnych oraz demonstracyjnych.

Autorzy nie ponoszą odpowiedzialności za:
- niewłaściwe wykorzystanie aplikacji,
- utratę danych,
- błędy wynikające z działania zewnętrznych usług API,
- szkody powstałe wskutek modyfikacji kodu przez użytkownika,
- przerwy w działaniu systemu lub niepoprawne generowanie treści przez modele AI.

Użytkownik korzysta z aplikacji na własną odpowiedzialność.

Wszelkie klucze API, dane dostępowe oraz konfiguracje bezpieczeństwa powinny być przechowywane wyłącznie lokalnie i nigdy nie powinny być publikowane w publicznych repozytoriach.

