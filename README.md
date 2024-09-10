Here's a detailed README for the weather app project that covers functionality, importance, how it works, and potential future improvements.

---

# Weather App Project

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [How It Works](#how-it-works)
  - [Python Weather Scraper](#python-weather-scraper)
  - [Node.js Backend](#nodejs-backend)
  - [Frontend](#frontend)
- [Why This is Important](#why-this-is-important)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Improvements and Future Iterations](#improvements-and-future-iterations)

## Project Overview

This weather app project is a complete solution that fetches weather data from multiple sources (currently focusing on aviation weather), processes it, and uploads it to cloud storage. It provides a simple Node.js API backend for serving this weather data and a frontend interface for displaying it.

The main components are:
1. **Python Weather Scraper**: Gathers data from an external API and uploads it to Azure Blob Storage.
2. **Node.js Backend**: Serves the data to the frontend from Azure Blob Storage.
3. **Frontend (HTML+JS)**: Displays the weather data fetched from the backend.

This modular structure makes it scalable and flexible, allowing for multiple weather data sources and potential feature expansions.

---

## Features

### 1. **Data Collection**
   - Fetches METAR (Meteorological Aerodrome Reports) from aviationweather.gov.
   - The current implementation fetches data from the "KNKX" weather station in METAR format, with an option to add more sources.

### 2. **Azure Blob Storage Integration**
   - The weather data is uploaded to an Azure Blob Storage container, which can be expanded to store other types of weather data.
   - Using cloud storage ensures that data can be accessed by multiple systems without duplication.

### 3. **REST API (Node.js)**
   - A Node.js Express API is provided to retrieve weather data stored in Azure.
   - Simple and efficient backend design that could be extended with more endpoints or integrated with other data sources.

### 4. **Dynamic Frontend**
   - A basic frontend displays weather data using HTML, JavaScript, and asynchronous data fetching.
   - Lightweight interface designed to be mobile-friendly and can be integrated into larger applications.

---

## Technology Stack

- **Python**: For weather data scraping and uploading to Azure Blob Storage.
- **Node.js (Express)**: For serving the weather data from Azure Blob Storage to the frontend.
- **Azure Blob Storage**: Used to store the weather data.
- **HTML/CSS/JavaScript**: Simple and responsive frontend to display the weather data.

---

## How It Works

### 1. **Python Weather Scraper**

The `weatherdatascraper.py` script:
- Makes a request to the **Aviation Weather API** to retrieve METAR data.
- Stores the response as a JSON object.
- Uploads the JSON data to **Azure Blob Storage** using the Azure SDK for Python.
- Handles errors during API requests or Azure operations, making sure the system doesn't fail silently.

### 2. **Node.js Backend**

The `server.js` in the backend:
- Hosts an Express.js web server that listens on a port (default: 3000).
- Provides a `/weather` route that retrieves the latest weather data from Azure Blob Storage.
- Fetches the stored JSON data, processes it, and sends it as a response to the client.
- Converts the raw blob stream into a readable format using helper functions to stream from Azure.

### 3. **Frontend**

The `index.html` frontend:
- Simple HTML/CSS layout that is mobile-responsive.
- Uses JavaScript's `fetch` API to make an HTTP request to the Node.js backend at `/weather`.
- Dynamically updates the page with the retrieved weather data in JSON format.
- Gracefully handles errors by displaying a user-friendly message if the data can't be loaded.

---

## Why This is Important

### **Real-time Weather Monitoring**
- Accurate and up-to-date weather information is crucial for many applications, such as aviation, agriculture, and even for regular users who want to track weather conditions.
- This project focuses on METAR data, which is used heavily in aviation to provide weather information at airports and aerodromes.

### **Scalability**
- By storing the data in Azure Blob Storage, you ensure scalability and availability. Cloud storage provides a central location for multiple clients and applications to access data without performance bottlenecks.
- The use of REST APIs in the backend ensures the project can be expanded or integrated into other systems, allowing for additional features and increased functionality.

### **Modularity**
- This project is designed to be modular, with a Python backend handling data retrieval, a Node.js backend handling data serving, and a simple frontend.
- Each of these components can be developed or replaced independently, making it easy to add new features like additional data sources, extended functionality in the API, or a more advanced user interface.

---

## Installation

### Prerequisites:
- Python 3.x
- Node.js (v18+)
- Azure account (for Blob Storage)
- Basic familiarity with the terminal or command line

### Steps:
1. Clone the repository.
2. Install dependencies for Python:
   ```bash
   pip install azure-storage-blob requests python-dotenv
   ```
3. Install dependencies for Node.js:
   ```bash
   cd backend/node
   npm install express axios dotenv @azure/storage-blob
   ```

4. Set up your environment variables in both the Python and Node.js `.env` files:
   ```bash
   AZURE_CONNECTION_STRING=your_connection_string_here
   ```

5. Make sure you have a valid container and blob set up in your Azure Blob Storage.

---

## How to Run

### Running the Python Scraper:
1. Navigate to the Python scripts folder:
   ```bash
   cd backend/python-scripts
   ```
2. Run the Python script to scrape the weather data and upload it to Azure:
   ```bash
   python3 weatherdatascraper.py
   ```

### Running the Node.js Backend:
1. Navigate to the Node.js folder:
   ```bash
   cd backend/node
   ```
2. Start the Node.js server:
   ```bash
   node server.js
   ```

### Viewing the Frontend:
1. Open `frontend/index.html` in a browser.
2. The frontend will automatically make a request to the Node.js backend and display the weather data.

---

## Improvements and Future Iterations

While this project is functional, there are several areas for improvement and expansion:

### 1. **Additional Weather Data Sources**
   - Currently, the scraper pulls data from a single API endpoint (aviationweather.gov). Adding more sources such as **OpenWeatherMap**, **NOAA**, or **AccuWeather** would make the app more versatile and useful for different domains.

### 2. **Scheduled Data Updates**
   - Implementing a cron job or task scheduler would allow the Python script to run periodically (e.g., every hour or every day), ensuring the weather data stays up to date without manual intervention.

### 3. **Frontend UI Enhancements**
   - The current frontend is basic. Adding a more polished design with charts, graphs, or even maps to visualize the weather data would make it more engaging.
   - Using a frontend framework like **React** or **Vue.js** could improve scalability and code maintainability.

### 4. **Caching Layer**
   - Add a caching layer (e.g., **Redis**) to store recently fetched weather data on the server to avoid hitting Azure Blob Storage for every request, improving performance.

### 5. **Authentication & Security**
   - Implement user authentication to control access to certain API endpoints, especially if sensitive weather data is integrated in the future.
   - Add HTTPS encryption for secure communication between the frontend, backend, and Azure services.

### 6. **Global Deployment**
   - Deploy the backend using cloud services like **Heroku**, **AWS**, or **Azure App Services** to make the weather app accessible to users globally.

### 7. **Unit Testing & CI/CD**
   - Implement automated tests for both the Python scraper and Node.js backend to ensure the stability of the application.
   - Set up a CI/CD pipeline for automatic deployment of changes to the cloud.

---

By building on these core ideas, this project can evolve into a powerful, scalable weather-tracking application with advanced features and improved performance.

---
