# 🏘️ WardMonitor

**WardMonitor** is a lightweight FastAPI + SQLAlchemy server designed to receive, store, and visualize housing data from Final Fantasy XIV residential wards. It accepts structured data (Region → Wards → Plots), stores it in a relational database, and offers a toggleable web dashboard for real-time monitoring.

---

## ✨ Features

- 📡 Receives housing data via `/ward-update` POST endpoint
- 💾 Persists regions, wards, and plots in a relational database (SQLAlchemy)
- 🖥️ Web-based dashboard with toggle to show only available plots
- 🏠 Structured and extensible data model (Region → Ward → Plot)
- 📄 Rotating human-readable logs saved to `logs/wardmonitor.log`
- 🔁 Automatically recreates DB schema on startup
- 🔌 Easy to extend with WebSocket/live data, alerts, etc.

---

## 📦 Requirements

- Python 3.9+
- `fastapi~=0.116.1`
- `uvicorn`
- `pydantic~=2.11.7`
- `sqlalchemy`
- `jinja2`

Install with:

```bash
pip install -r requirements.txt
```

---

## 🏁 Running the Server

```bash
uvicorn app.main:app --reload
```

Then visit:

- **API:** [http://localhost:8000/ward-update](http://localhost:8000/ward-update)
- **Dashboard:** [http://localhost:8000/](http://localhost:8000/)

---

## 📤 Example Request

POST to `/ward-update` with JSON body:

```json
{
  "region_name": "The Mist",
  "wards": [
    {
      "ward_id": 1,
      "plots": [
        {"plot_number": 4, "price": 1800000, "size": "S", "available": true},
        {"plot_number": 2, "price": 3975000, "size": "M", "available": false}
      ]
    },
    {
      "ward_id": 2,
      "plots": [
        {"plot_number": 1, "price": 2000000, "size": "S", "available": true},
        {"plot_number": 2, "price": 4005000, "size": "L", "available": true}
      ]
    }
  ]
}
```

---

## 🧠 Data Model

### Region
- `region_name`: Name of the residential region (e.g., "The Goblet")
- `wards`: List of wards in the region

### Ward
- `ward_id`: Integer (1–30)
- `plots`: List of up to 60 plots

### Plot
- `plot_number`: Integer (1–60)
- `price`: Integer (gil)
- `size`: `"S"` | `"M"` | `"L"`
- `available`: Boolean

---

## 🖥️ Web Dashboard

Access the dashboard at `/`. Features include:

- View all regions, wards, and plots
- Toggle visibility of unavailable plots using a checkbox at the top

---

## 📂 Project Structure

```
WardMonitor/
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── models.py      # Pydantic models (input validation)
│   ├── models_db.py   # SQLAlchemy ORM models
│   ├── database.py    # Session and engine setup
│   ├── logger.py      # Rotating file logger
│   └── templates/
│       └── dashboard.html  # Jinja2 template
├── logs/              # Log output directory
├── requirements.txt   # Dependencies
└── README.md          # You're here
```

---

## 🛡️ Logging

Logs are saved to `logs/wardmonitor.log` and rotate at 1MB with 5 backups.  
Example:

```log
[2025-07-29 22:51:41,004] [INFO] Received data for region: The Goblet
[2025-07-29 22:51:41,004] [INFO]   Ward 1 with 2 plots
[2025-07-29 22:51:41,004] [INFO]     Plot 01: L - 3,750,000 gil
[2025-07-29 22:51:41,004] [INFO]     Plot 02: M - 1,875,000 gil
```

---

## 🚧 Roadmap

- [x] Persist data to SQLite
- [x] Create dashboard with plot filtering
- [ ] WebSocket support for live updates
- [ ] CSV or JSON export of available plots

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, submit issues, or open PRs.  
Please follow best practices and keep the code clean and documented.

---

## 📜 License

MIT License – do what you want, but be kind and credit the project.

---

## 🎮 Acknowledgements

This project is inspired by the housing wars of Eorzea and the unsung heroes who refresh ward signs at 4AM.
