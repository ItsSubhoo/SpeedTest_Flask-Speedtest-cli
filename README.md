#UPseepd [SpeedTest_Flask-Speedtest-cli]

This is an Internet Speed Test application built with Flask for the backend and HTML, CSS, and JavaScript for the frontend. It allows users to measure their internet speed in terms of download and upload speeds, with real-time visual feedback using gauges.

## Features

- Real-time download and upload speed measurement.
- 30-second countdown during the speed test.
- Visual representation of speeds using gauges.
- User-friendly interface.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, JustGage, Raphael.js
- **Backend**: Flask, Speedtest-cli
- **Dependencies**: 
  - Flask
  - Speedtest-cli

## Getting Started

### Prerequisites

Make sure you have Python and Flask installed. You can install Flask and the speedtest-cli using pip:

```bash
pip install Flask speedtest-cli
```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/internet-speed-test-app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd internet-speed-test-app
    ```

3. Install dependencies:

    ```bash
    pip install Flask speedtest-cli
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000`.
