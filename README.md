# ELK Stack Demo Project

A demonstration of the ELK (Elasticsearch, Logstash, Kibana) stack for centralized logging with a Flask application.

## What This Project Does

This project demonstrates a complete logging pipeline:

1. **Flask App** - A simple web application that generates logs when endpoints are accessed
2. **Logstash** - Collects and parses logs from the Flask app
3. **Elasticsearch** - Stores and indexes the parsed logs
4. **Kibana** - Provides a web interface to visualize and search logs

### Application Endpoints

- `GET /` - Returns "Hello, ELK!" and logs the request
- `GET /error` - Triggers an error log and returns a 500 status

## Prerequisites

- Docker
- Docker Compose

## Setup Instructions

### 1. Build the Flask Application Docker Image

```bash
docker build -t flask-elk-app .
```

### 2. Start the ELK Stack

```bash
docker-compose up
```

Wait for all services to start (this may take 1-2 minutes).

### 3. Access the Services

- **Flask App**: http://localhost:5000
- **Kibana**: http://localhost:5601
- **Elasticsearch**: http://localhost:9200

### 4. Generate Logs

Visit the Flask endpoints to generate logs:

```bash
curl http://localhost:5000/
curl http://localhost:5000/error
```

### 5. View Logs in Kibana

1. Open Kibana at http://localhost:5601
2. Go to **Management** → **Stack Management** → **Index Patterns**
3. Create an index pattern: `flask-logs*`
4. Go to **Discover** to view and search your logs

## Architecture

```
Flask App → Logs to File → Logstash → Elasticsearch → Kibana
```

- Flask writes logs to `/app/logs/app.log`
- Logstash reads the log file, parses it, and sends to Elasticsearch
- Kibana queries Elasticsearch to display logs

## Stopping the Stack

```bash
docker-compose down
```

## Troubleshooting

- If services fail to start, ensure ports 5000, 5044, 5601, 9200, and 9600 are available
- Check logs: `docker-compose logs <service-name>`
- Elasticsearch needs at least 2GB of RAM
