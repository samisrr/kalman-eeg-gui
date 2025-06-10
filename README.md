# Filtro di Kalman applicato a segnali EEG con interfaccia grafica

## 👨‍💻 Autore
**Izouine Sami Samuele**

## 📌 Descrizione

Questo progetto nasce come attività scolastica facoltativa e si propone di applicare un **filtro di Kalman** a segnali EEG, con l'obiettivo di ridurre il rumore e visualizzare graficamente il confronto tra segnale originale e filtrato. Il progetto include un'applicazione Python con **interfaccia grafica (GUI)** realizzata in **PyQt5**.

## 🧠 Obiettivi formativi

- Approfondire l'elaborazione di segnali biologici
- Applicare concetti di filtraggio digitale (Kalman Filter)
- Sviluppare una GUI interattiva con Python
- Utilizzare librerie scientifiche per il calcolo e la visualizzazione

## 🛠️ Tecnologie utilizzate

- **Python 3**
- **PyQt5** – per la GUI
- **Matplotlib** – per la visualizzazione dei segnali
- **NumPy** – per l’elaborazione numerica dei dati

## ⚙️ Funzionalità principali

- Caricamento di segnali EEG da file `.csv`
- Impostazione manuale dei parametri del filtro di Kalman (Q e R)
- Visualizzazione comparativa tra segnale grezzo e filtrato
- Applicazione in tempo reale del filtro

## 📦 Installazione

1. Clona o scarica questo repository
2. Installa le dipendenze:

```bash
pip install -r requirements.txt
