# AR1_enigma
## 1. Descripció del Projecte
Recuperació realitzada per:
* Anna Gual Poblet
* Lena Boajram Makarem
* Andrea Olivas Vazquez
Data Bunker es una solució per la protecció de dades. Permet xifrar arxius, gestionar copies de seguretat (backups) y analitzar la composició de carpetes para auditar la informació.

## 2. Arquitectura del Codi
El projecte s'ha organitzat de la següent forma:
* **main.py**: Validador inicial del sistema.
* **menu.py / interfaz.py**: Interacció amb l'usuari (Consola y GUI).
* **crypto_utils.py**: Lógica de xifrat i desxifrat.
* **key_manager.py**: Gestió de claus de seguretat.
* **backup_manager.py**: Gestió d'arxius comprimits i logs.
* **analizar_archivos.py**: (NOU) Analisis estadistico de archivos y extensiones.

## 3. Requisits
Es necesari instalar la llibreria de criptografia perquè el sistema funcioni:
* pip install cryptography
