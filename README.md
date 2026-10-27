# Smart Parking Space Allocation

A simple Flask web app that allocates a parking slot to a vehicle.

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Deploy with GitHub + Render
1. Create a GitHub repository and upload all files/folders in this project.
2. In Render, choose **New +** → **Web Service** and connect the repository.
3. Select Python as the runtime.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Click **Create Web Service** and wait for deployment to finish.
7. Open the live URL Render provides.

Note: parking occupancy is currently stored in memory, so it resets when the app restarts or redeploys.
