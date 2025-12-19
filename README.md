# Overview

This repository contains the source code and supporting materials for the **Amazon Recommender System** project.

> [**Project Report**](docs/AR_Report.pdf)

> [**Presentation Slides**](docs/AR_Presentation.pdf)

> [**Data Source**](https://amazon-reviews-2023.github.io/)



# Set Up

Install relevant dependencies.
```bash
pip install -r requirements.txt
```

Start the application.
```bash
cd flask_app
python app.py
```

Once running, the application will be available at:
```
http://localhost:5000
```

## Cloudflare Tunnel Setup (Optional)

To expose the local application through a public URL, install the `cloudflared` CLI tool.

**Windows**
```bash
winget install Cloudflare.cloudflared
```

**macOS**
```bash
brew install cloudflare/cloudflare/cloudflared
```

**Linux**
```bash
sudo apt install cloudflared
```

Once installed, start the tunnel with:
```bash
cloudflared tunnel --url http://localhost:5000
```

The terminal will display a temporary public HTTPS URL (e.g. `https://*.trycloudflare.com`) that can be accessed from any computer while the app and tunnel are running.

# Implications
This project illustrates how data-driven systems can meaningfully influence user experience, decision-making, and platform efficiency at scale. Thoughtful recommendation design has real implications for discovery, fairness, and trust which ties directly to making system transparency, evaluation, and reproducibility essential.

The techniques explored here form a foundation for building responsible, scalable recommendation systems in real-world environments.









