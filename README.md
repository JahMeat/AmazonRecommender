# Amazon Recommender System

📘 **Project Report**  
👉 [Open the complete project report](docs/AR_Report.pdf)

📊 **Presentation Slides**  
👉 [Open presentation slides](docs/AR_Presentation.pdf)


This repository contains the source code and supporting materials for the **Amazon Recommender System** project.

The full documentation is provided in the PDF linked above.


## How to Run Locally

### Setup
```bash
pip install -r requirements.txt
```

### Start the application
```bash
cd flask_app
python app.py
```

Once running, the application will be available at:
```
http://localhost:5000
```

## Public Demo (Optional)

To expose the local application through a public URL (for demos or sharing), run:

```bash
cloudflared tunnel --url http://localhost:5000
```

The terminal output will display a temporary public HTTPS URL (e.g. `https://*.trycloudflare.com`) that can be accessed from any computer **while the app and tunnel are running**.

> The public URL changes each time the tunnel is started.


## Notes
- Large datasets are downloaded automatically on first run and cached locally.
- The project is designed to run locally for performance and reproducibility.


## License
This project is intended for educational and demonstration purposes.









