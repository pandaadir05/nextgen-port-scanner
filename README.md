# NextGen Port Scanner

**NextGen Port Scanner** is an advanced, AI-powered port scanning tool designed for cybersecurity professionals and enthusiasts. This project uses asynchronous scanning, machine learning-based vulnerability analysis, and a distributed architecture to deliver fast, accurate results. A modern React dashboard provides real-time visualization, and everything is containerized with Docker for seamless deployment.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Scanner](#command-line-scanner)
  - [API Server](#api-server)
  - [React Dashboard](#react-dashboard)
- [Docker & Deployment](#docker--deployment)
- [CI/CD](#cicd)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

NextGen Port Scanner is built to be:
- **Fast:** Uses Python’s `asyncio` for concurrent port scanning.
- **Smart:** Integrates an AI/ML model to analyze service banners and flag potential vulnerabilities.
- **Scalable:** Supports distributed scanning with Celery and RabbitMQ.
- **User-Friendly:** Features a modern React dashboard for real-time monitoring.
- **Portable:** Fully containerized using Docker and orchestrated with Docker Compose.
- **Reliable:** CI/CD pipelines ensure consistent builds and quality assurance.

---

## Features

- **Asynchronous Scanning:** Scan thousands of ports concurrently.
- **AI-Based Vulnerability Analysis:** Evaluate service banners with a machine learning model.
- **Distributed Scanning:** Scale scanning tasks using Celery workers and RabbitMQ.
- **Real-Time Dashboard:** Visualize scan progress and results using a React interface.
- **Containerized Deployment:** Easy setup with Docker and Docker Compose.
- **CI/CD Integration:** Automated testing and deployment using GitHub Actions.

---

## Architecture

- **Scanner Engine:** Core scanning logic using Python's `asyncio`.
- **AI Analysis Module:** Loads a trained model to predict vulnerabilities from banners.
- **API Server:** FastAPI backend exposes endpoints for scanning.
- **Distributed Worker:** Celery worker distributes scanning tasks via RabbitMQ.
- **Frontend Dashboard:** React app displays real-time scanning results.
- **Containerization:** All components are packaged with Docker.
- **CI/CD Pipeline:** GitHub Actions automates testing and builds.

---

## Installation

### Prerequisites

- Python 3.10 or later
- Docker & Docker Compose (for containerized deployment)
- Node.js and npm (for the React dashboard)

### Local Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/nextgen-port-scanner.git
   cd nextgen-port-scanner
   ```

2. **Set Up Python Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up the React Dashboard:**

   ```bash
   cd frontend
   npm install
   ```

---

## Usage

### Command-Line Scanner

Run a basic scan from the terminal:

```bash
python scanner.py 127.0.0.1 --start 1 --end 1024
```

### API Server

Start the FastAPI server:

```bash
python server.py
```

Then send a POST request to the `/scan` endpoint (using curl or Postman):

```bash
curl -X POST "http://localhost:8000/scan" \
     -H "Content-Type: application/json" \
     -d '{"ip": "127.0.0.1", "start_port": 1, "end_port": 1024}'
```

### React Dashboard

Launch the frontend dashboard:

```bash
cd frontend
npm start
```

Open [http://localhost:3000](http://localhost:3000) in your browser to view the dashboard.

---

## Docker & Deployment

Deploy all components using Docker Compose:

```bash
docker-compose up --build
```

**Services:**
- **API Server:** FastAPI on port 8000.
- **Celery Worker:** Processes distributed scanning tasks.
- **RabbitMQ:** Task broker on ports 5672 and 15672.
- **Frontend:** React dashboard on port 3000.

---

## CI/CD

The project uses GitHub Actions for continuous integration and deployment. The workflow is defined in `.github/workflows/ci.yml` and includes:
- Code checkout
- Python environment setup
- Dependency installation
- Running tests
- Building Docker images

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

For major changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- **FastAPI** for providing a fast and modern web framework.
- **Celery & RabbitMQ** for enabling scalable distributed processing.
- **React** for a dynamic and responsive user interface.
- Thanks to the open-source community for tools and inspiration.

---

*Happy Scanning!*
