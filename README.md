# Trade Opportunity API

A FastAPI-based backend service that analyzes global trade opportunities for different sectors using AI.

The API collects simulated market data, analyzes it using Google Gemini AI, and generates a structured markdown report.

---

## Features

* Sector-based trade opportunity analysis
* AI-powered insights using Gemini
* Markdown report generation
* API Key Authentication
* Rate Limiting (5 requests/minute)
* Session tracking for API usage
* Modular FastAPI architecture

---

## Tech Stack

* FastAPI
* Python
* Google Gemini API
* SlowAPI (Rate Limiting)
* Uvicorn
* REST API Architecture

---

## Project Structure

```
TradeOpportunityAPI
│
├── app
│   ├── main.py
│   │
│   ├── routes
│   │   └── analyze.py
│   │
│   ├── services
│   │   ├── data_collector.py
│   │   ├── gemini_service.py
│   │   └── report_generator.py
│   │
│   └── security
│       ├── auth.py
│       ├── rate_limit.py
│       └── session_tracker.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone <repo-url>
cd TradeOpportunityAPI
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the API

Start the server:

```
uvicorn app.main:app --reload
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Analyze Trade Opportunities

```
GET /analyze/{sector}
```

Example:

```
/analyze/technology
```

Header required:

```
x-api-key: test123
```

---

## Example Response

```
{
  "sector": "technology",
  "report": "## Market Analysis...",
  "session_requests": 2
}
```

---

## Security Features

* API Key authentication
* Rate limiting
* Session tracking

---

## Future Improvements

* Real-time trade data integration
* Database logging
* Caching
* Multi-user authentication
* Production deployment

---

## Author

Built as part of a backend engineering assignment.
