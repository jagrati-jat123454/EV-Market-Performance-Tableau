# EV Market Performance — Render Deployment

A Flask-powered website that presents the EV Market Performance Tableau dashboard and Tableau Story.

## Included visualizations

- Dashboard: https://public.tableau.com/views/Dashboard1_17937007105250/Dashboard1
- Story: https://public.tableau.com/views/EVMARKET-STORY_17937005218180/Story1

The visualizations are embedded from Tableau Public. Tableau hosts the visualization content and interactive controls; this Flask application serves the website and its backend routes.

## Project structure

```text
EV_Market_Performance_Render/
├── app.py
├── requirements.txt
├── Procfile
├── render.yaml
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Deploy directly from GitHub to Render

1. Extract this ZIP file.
2. Create a new GitHub repository.
3. Upload the **contents inside** this folder to the repository root (do not upload only the ZIP).
4. On Render, choose **New + → Web Service**.
5. Connect the GitHub repository.
6. Render should detect `render.yaml`. If it asks for settings, use:
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120`
7. Click **Deploy** and wait for the build to finish.

No VS Code or local run step is required.

## Backend endpoints

- `/` — serves the website
- `/health` — Render health check; returns JSON status
- `/api/project` — returns project and Tableau visualization metadata

## Important

- The Tableau visualizations must be published and accessible on Tableau Public for the embeds to load.
- This project does not copy Tableau's data or recreate Tableau's analytics engine. Tableau Public remains responsible for rendering the dashboard and story.
- If you later want a separate database, user login, or custom analytics API, those are additional backend features and require a defined data source and requirements.
