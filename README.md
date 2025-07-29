# 🏘️ WardMonitor

**WardMonitor** is a lightweight FastAPI server designed to receive and log housing data from Final Fantasy XIV residential wards. It accepts structured data (Region → Wards → Plots) and provides a foundation for real-time housing status monitoring, data analysis, or plugin integration.

---

## ✨ Features

- 📡 Receives ward updates via a clean `/ward-update` POST endpoint
- 🏠 Structured data model: Region → Ward → Plot
- 📄 Human-readable logs saved to disk (`logs/wardmonitor.log`)
- 🔁 Rotating log handler to manage disk space
- 🧩 Easy to extend with database support, web UI, or alerts

---

## 📦 Requirements

- Python 3.9+
- `fastapi~=0.116.1`
- `uvicorn`
- `pydantic~=2.11.7`

Install with:

```bash
pip install -r requirements.txt
```

---

## 🏁 Running the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:  
[http://localhost:8000/ward-update](http://localhost:8000/ward-update)

---

## 📤 Example Request

POST to `/ward-update` with JSON body:

```json
{
  "region_name": "The Goblet",
  "wards": [
    {
      "ward_id": 1,
      "plots": [
        {"price": 3750000, "size": "L"},
        {"price": 1875000, "size": "M"}
      ]
    }
  ]
}
```

---

## 🧠 Data Model

### Region
- `region_name`: Name of the residential region (e.g., "The Goblet")
- `wards`: List of 30 wards

### Ward
- `ward_id`: Integer (1–30)
- `plots`: List of 60 plots

### Plot
- `price`: Integer (gil)
- `size`: `"S"` | `"M"` | `"L"`

---

## 📂 Project Structure

```
WardMonitor/
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── models.py      # Pydantic data models
│   └── logger.py      # Rotating file logger
├── logs/              # Log output directory
├── requirements.txt   # Dependencies
└── README.md          # You are here
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

- [ ] Persist data to SQLite or PostgreSQL
- [ ] Create a dashboard to display plot availability
- [ ] WebSocket support for live updates

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, submit issues, or open PRs.  
Please follow best practices and keep the code clean and documented.

---

## 📜 License

MIT License – do what you want, but be kind and credit the project.

---

## 🎮 Acknowledgements

This project is inspired by the ongoing housing rushes of Eorzea and those brave enough to camp signs for hours.
