# ⚡ EV INSIGHTS — EV Market Performance

### Exploring the Future of Electric Mobility

EV INSIGHTS is a data-driven web platform designed to explore and understand the electric vehicle (EV) market. It presents market trends, performance indicators, and interactive visualizations through Tableau dashboards and data stories.

The project combines an interactive frontend, a Python Flask backend, and Tableau Public visualizations to make EV market insights accessible and easy to understand.

## 🌐 Live Website

**Website:** https://ev-market-performance-tableau-1.onrender.com

## 📊 Project Visualizations

### 1. EV Market Performance Dashboard

An interactive Tableau dashboard that presents EV market performance and key insights.

[Open Interactive Dashboard](https://public.tableau.com/views/Dashboard1_17937007105250/Dashboard1)

### 2. EV Market Data Story

A visual data story exploring electric vehicle market trends and insights.

[Explore Data Story](https://public.tableau.com/views/EVMARKET-STORY_17937005218180/Story1)

## ✨ Features

- Modern and responsive EV INSIGHTS website.
- Interactive Tableau dashboard integration.
- Tableau data story integration.
- Dedicated Home, About, Dashboard, and Data Story sections.
- Python Flask backend.
- REST API endpoint for project information.
- Health-check endpoint for deployment monitoring.
- Deployment support through Render.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Website structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |
| Python | Backend programming |
| Flask | Backend web framework |
| Tableau Public | Data visualization |
| Gunicorn | Production WSGI server |
| GitHub | Source code management |
| Render | Website hosting and deployment |

## 📁 Project Structure

```text
EV-Market-Performance-Tableau/
│
├── app.py
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Backend API

The Flask backend provides the following routes:

| Endpoint | Description |
|---|---|
| `/` | Serves the main website |
| `/health` | Checks backend service health |
| `/api/project` | Returns project information and visualization links |

## 🚀 Deployment

The project is configured for deployment on Render.

**Deployment configuration:**

- Runtime: Python
- Build command:

```bash
pip install -r requirements.txt
```

- Start command:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120
```

The `render.yaml`
