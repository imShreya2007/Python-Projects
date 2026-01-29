# Weather Logger (API + CSV)

A **Python console-based Weather Logger** that fetches **real-time weather data** using the **OpenWeather API** and stores daily weather records persistently in a **CSV file**.  
The application securely loads API keys using **environment variables (`.env`)**, prevents duplicate daily logs for the same city, and handles API/network errors gracefully.

---

## Table of Contents
- [Features](#features)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [API Integration](#api-integration)
- [Data Storage](#data-storage)
- [Concepts Covered](#concepts-covered)

---

## Features

- Fetches **real-time weather data** using OpenWeather API  
- Logs weather details including:
  - Date
  - Time
  - City
  - Temperature (°C)
  - Weather description
- Automatically creates a CSV file on first run
- Prevents duplicate entries for the **same city on the same day**
- Secure API key management using `.env` file
- Handles:
  - Invalid city names
  - Network errors
  - API failures
- Clean and interactive console-based interface
- Allows logging multiple cities in one session

---

## Environment Setup
### Method 1:
Set your OpenWeather API key: 
Before running the program, set the API key as an environment variable:
<br>
**Windows (PowerShell):**
```bash
setx OPENWEATHER_API_KEY "your_api_key_here"
```
**Linux / macOS:**
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

### Method 2 (Recommended):
Using .env File:
This project uses python-dotenv to securely load the API key.
1. Install dependencies
```bash
pip install requests python-dotenv
```
2. Create a .env file and paste the below line
```bash
OPENWEATHER_API_KEY=your_api_key_here
```
⚠️ Do not commit .env to GitHub. Add it to .gitignore.

---

## Usage
2. Run the program
```bash
python weather_logger.py
```
3. Follow the prompts
* Enter a city name
* Weather data is fetched and logged
* Choose whether to log another city or exit

---

## How It Works
The program:
1. Loads environment variables using dotenv
2. Reads the OpenWeather API key securely
3. Takes a city name from the user
4. Checks if today’s weather for that city is already logged
5. Sends a request to the OpenWeather API
6. Extracts:
* Temperature
* Weather description
7. Saves the data with date and time into a CSV file
8. Allows repeated logging until the user exits

---

## API Integration
1. API Used: OpenWeather Current Weather API
2. Endpoint:
```bash
https://api.openweathermap.org/data/2.5/weather
```
3. Parameters:
* q → City name
* appid → API key
* units=metric → Temperature in Celsius

---

## Data Storage
* File name: weather_log.csv
* Format:
```
Date,Time,City,Temperature (°C),Weather

2026-01-27,09:15:10,Delhi,25.4,clear sky
```
* Data persists across program runs

---

## Concepts Covered
* REST API integration
* Secure API key handling using .env
* Environment variables for security
* HTTP requests using requests
* JSON parsing
* CSV file handling
* Date and time manipulation
* Duplicate data prevention
* Exception handling
* Modular and reusable function program
* Console-based user interaction

---