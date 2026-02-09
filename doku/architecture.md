# PandaSpa - Project Conception

## 1. Project Idea
Kurzbeschreibung der Idee:
Ein Panda betreibt ein gemütliches Spa für Waldtiere. Die Python-Anwendung hilft, Services, Kunden, Buchungen, Finanzen und Statistiken zu verwalten.

---

## 2. Purpose
- Unterstützung des Spa-Betriebs
- Organisation von Terminen und Einnahmen
- Automatisierte Vorschläge für Kundenpräferenzen
- Lernziel: Python OOP, GUI, Datenverwaltung

---

## 3. Software Requirements

| ID        | Type           | Description                                                      | Priority |
|-----------|----------------|------------------------------------------------------------------|----------|
| FR-01     | Functional     | The system shall allow the user to create and view Services.     | Must     |
| FR-02     | Functional     | The system shall allow the user to create and view Customers.    | Must     |
| FR-03     | Functional     | The system shall allow the user to book a Service for a Customer.| Must     |
| FR-04     | Functional     | The system shall automatically calculate total revenue from bookings.| Must  |
| FR-05     | Functional     | The system shall allow the user to enter Expenses.               | Should   |
| FR-06     | Functional     | The system shall display a Statistics view with most popular Services.| Should|
| NFR-01    | Non-functional | The system shall persist data in JSON files.                     | Can      |
| NFR-02    | Non-functional | The GUI shall be intuitive and user-friendly.                    | Should   |

---

## 4. Architecture / Design

### 4.1. File Structure

PandaSpa/
├─ main.py
├─ README.md
└─ data/
   └─ spa_data.json_
└─ doku/
   └─ architecture.md
└─ src/
	└─ spa/
	   ├─ __init__.py
	   ├─ service.py
	   ├─ customer.py	   
	   ├─ data_manager_.py
	   ├─ finance.py
	   └─ booking.py
	└─ gui/
	   ├─ __init__.py
	   ├─ app.py
	   ├─ service_view.py
	   ├─ customer_view.py
	   ├─ booking_view.py
	   ├─ expenses_view.py
	   ├─ finances_view.py
	   └─ statistics_view.py


### 4.2. UML / Use-Case Diagram

**Akteur:** Panda (Spa-Betreiber)  
**Use Cases:**
- Create Service
- Create Customer
- Book Service
- Add Expense
- View Financial Overview
- View Statistics
- Exit Application

[Panda] --> (Create Service)
[Panda] --> (Create Customer)
[Panda] --> (Book Service)
[Panda] --> (Add Expense)
[Panda] --> (View Financial Overview)
[Panda] --> (View Statistics)

---

## 5. Data Flow / GUI Flow

- Service → Customer → Booking → Financial Overview → Statistics  
- JSON files persist all data  
- `matplotlib` visualizes statistics charts  
- User can add expenses directly in the GUI

---

## 6. Example Data

### Services
- Thermal Bath (60 min, €25)  
- Bamboo Massage (45 min, €30)  
- Tea Therapy (30 min, €15)  

### Customers
- Fuzzy (Fox)  
- Hazel (Deer)  
- Rocky (Raccoon)  

### Bookings
- Fuzzy → Thermal Bath → 2026-02-10 10:00  
- Hazel → Bamboo Massage → 2026-02-10 11:30  
- Rocky → Tea Therapy → 2026-02-10 12:00  

### Expenses
- Tea → €15  
- Massage Oil → €20  
- Bamboo Bath → €10  

---

## 7. Challenges / Notes

- Terminal → GUI refactor with `tkinter`  
- JSON persistence with proper error handling  
- Statistics chart using `matplotlib`  
- Future improvements:  
  - Revenue per service diagram  
  - Date filtering for bookings
