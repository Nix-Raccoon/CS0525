# 🛡️ Cybersecurity Bootcamp Portfolio

Benvenuti nella repository ufficiale del mio percorso intensivo in Cybersecurity presso Epicode School. Qui raccolgo i project work pratici, gli script di automazione e le configurazioni di rete sviluppate durante il master.

---

## 🗂️ I Miei Progetti Principali (Buildweeks)

### ✅ 1. Network Infrastructure & Security Hardening (Mese 1)
* **Path:** `/UNIT_1/S4-buildweek` | **Stato:** Completato 🟢
* **Obiettivo:** Progettazione e messa in sicurezza di un'infrastruttura di rete aziendale simulata.
* **Architettura:** Segmentazione di rete (DMZ, LAN) e configurazione regole Firewall su pfSense.
* **Automation:** Sviluppo di tool custom in Python (Port Scanner, Network Sniffer, HTTP Scanner).
* **Testing:** Vulnerability Assessment su target virtualizzati.

---

### 🚧 2. Offensive Security & Web Vulnerabilities (Mese 2)
* **Focus previsto:** Web Application Penetration Testing e sfruttamento vulnerabilità note.
* **Web App Attacks:** Ricerca e sfruttamento di vulnerabilità come SQL Injection, Cross-Site Scripting (XSS) e CSRF.
* **Web Proxy & Testing:** Intercettazione, modifica e analisi del traffico HTTP/S e Fuzzing tramite Burp Suite (Repeater, Intruder, Sequencer).
* **Exploitation & Post-Exploitation:** Utilizzo avanzato di Metasploit Framework (MSFConsole) per la ricerca di vulnerabilità, l'invio di payload (MsfVenom) e l'apertura di sessioni Meterpreter sui target.
* **Social Engineering:** Esecuzione di attacchi di Phishing e Credential Harvesting tramite clonazione di pagine web (es. utilizzo del Social Engineer Toolkit - SET).

---

### 📅 3. SIEM & SOC Operations (Mese 3)
* **Focus previsto:** Log Analysis, Incident Detection & Response e configurazione SIEM.
* **SIEM & Monitoraggio:** Raccolta, normalizzazione e correlazione degli eventi di sicurezza utilizzando Splunk e la suite Security Onion (ELK Stack: Elasticsearch, Logstash, Kibana).
* **Analisi degli Allarmi (Triage):** Valutazione degli alert tramite Sguil, distinguendo minacce reali da falsi positivi, e pivoting su Wireshark e log di Zeek per l'analisi forense dei pacchetti (PCAP).
* **Incident Response:** Applicazione del ciclo di vita della gestione degli incidenti basato sul framework NIST SP 800-61 (Preparazione, Rilevamento & Analisi, Contenimento, Eradicazione, Ripristino e Post-Incidente).
* **Threat Mitigation:** Individuazione di attacchi in corso (es. DoS, Brute Force, movimenti laterali) e definizione delle procedure di contenimento (es. isolamento host).

---

## 📂 Struttura della Repository

La repository è divisa in tre unità principali, corrispondenti ai moduli del master. All'interno di ogni directory troverai sia il progetto finale (Buildweek) che le esercitazioni settimanali e i laboratori.

```text
📦 Cybersecurity-Bootcamp-Portfolio
┣ 📂 UNIT_1
┃ ┣ 📁 S1
┃ ┣ 📁 S2
┃ ┣ 📁 S3
┃ ┣ 📁 S4-buildweek
┃ ┗ 📁 UTILITY/Python
┣ 📂 UNIT_2
┃ ┣ 📁 BlackBox_Vancouver
┃ ┣ 📁 S5
┃ ┣ 📁 S6
┃ ┣ 📁 S7
┃ ┗ 📁 S8-buildweek
┣ 📂 UNIT_3
┃ ┣ 📁 S09
┃ ┣ 📁 S10
┃ ┣ 📁 S11
┃ ┗ 📁 S12-buildweek
┗ 📄 README

🛠️ Tech Stack & Strumenti Utilizzati
Durante il percorso ho avuto modo di operare in laboratori virtuali (VirtualBox) simulando attacchi reali e difese aziendali
.
🛡️ Blue Team / SOC Operations: Splunk, Security Onion (Sguil, ELK Stack: Elasticsearch, Logstash, Kibana), OSSEC (HIDS)
.
⚔️ Red Team / Pentesting: Metasploit Framework (MSFConsole, MsfVenom), Burp Suite, SQLMap
.
🔍 Vulnerability & Network Analysis: Wireshark, Nmap, Nessus, Zeek
.
💻 Scripting & Automazione: Python (creazione di socket, port scanner, HTTP sniffer)
.
🧱 Sistemi & Infrastruttura: Linux (Kali Linux, Ubuntu), Windows Server 2022 (Active Directory), pfSense (Firewall/DMZ)
.
🔬 Competenze Pratiche e Laboratori
Oltre alle Buildweek, in questa repo puoi trovare documentazione e script relativi a:
Gestione degli Incidenti (IR): Redazione di report basati sul ciclo di vita dell'Incident Response secondo il framework NIST SP 800-61 (Preparazione, Rilevamento & Analisi, Contenimento/Eradicazione/Ripristino, Attività Post-Incidente)
.
Analisi Log e Allarmi: Classificazione degli alert (falsi positivi vs veri positivi), pivoting tra Sguil, Kibana e Wireshark per l'analisi forense e indagine su traffico sospetto e log di server web
.
Privilege Escalation & Post-Exploitation: Utilizzo di moduli Metasploit avanzati per movimenti laterali, routing di rete, dumping di hash (SAM) e tecniche di persistenza su macchine compromesse
.
👤 Chi Sono
Sono Nicolò Calì, un Junior Cybersecurity Specialist con l'obiettivo di operare come SOC Analyst L1
. Il mio percorso è caratterizzato da competenze ibride: prima di specializzarmi in Cyber Defense tramite Epicode, ho lavorato come Sviluppatore Software (Python/C#) e come operatore in Sala Controllo per il monitoraggio allarmi
.
Questo mix mi permette di unire una profonda "disciplina operativa" (gestione allarmi in real-time, triage rapido e gestione dello stress) con un mindset analitico orientato alla comprensione profonda delle architetture e all'automazione dei processi di sicurezza.
📫 Mettiamoci in contatto:
LinkedIn: [www.linkedin.com/in/nicolò-calì]
Email: nicolo.cali22@gmail.com

--------------------------------------------------------------------------------
⭐️ Se trovi utili i miei script o la mia documentazione, sentiti libero di lasciare una star a questa repository!
