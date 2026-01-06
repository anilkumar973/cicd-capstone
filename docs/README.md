CI/CD Pipeline Project – Docker + GitHub Actions (Staging Deployment)
 Project Overview

This project demonstrates a complete CI/CD pipeline that automatically tests, builds, scans, and deploys a simple 2-tier web application into a staging environment using:

Docker & Docker Compose

GitHub Actions CI

Trivy Security Scanner

PostgreSQL database

The pipeline follows industry best practices including multi-stage Docker builds, non-root containers, environment-based configurations, and automated deployments.

 Architecture Overview
Application Components
Layer	Technology
Frontend	Static HTML served via Nginx
Backend	Flask REST API
Database	PostgreSQL
CI/CD	GitHub Actions
Containerization	Docker & Docker Compose
Request Flow
User → Frontend (Nginx) → Backend (Flask) → PostgreSQL

 Tools & Technologies Used
Tool	Purpose
Git & GitHub	Source control
Docker	Containerization
Docker Compose	Local orchestration
Flask	Backend API
Nginx	Frontend web server
PostgreSQL	Database
GitHub Actions	CI/CD automation
Trivy	Container security scanning
Linux VM	Staging deployment
 Project Structure
cicd-webapp/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── test_app.py
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── Dockerfile
├── docker-compose.yml
├── .github/workflows/ci.yml
├── scripts/
│   ├── deploy.sh
│   └── migrate.sh
├── docs/
│   ├── architecture.md
│   ├── pipeline.md
│   └── runbook.md
└── README.md

 Application Setup
Backend – Flask API

Exposes /health endpoint

Connects to PostgreSQL using environment variables

Includes unit tests using pytest

Frontend – Static Web Page

Simple HTML page

Served using Nginx container

 Docker Implementation
Docker Best Practices Used

 Multi-stage builds
 Non-root users
 Minimal base images
 Layer caching
 Environment variables

Image Size Optimization
Image	Before	After (Multi-Stage)
Backend	~950MB	~120MB
 Local Development (Docker Compose)
Services

frontend

backend

postgres

Features

Custom Docker network

Persistent database volume

Environment variables

Service dependency management

Run Locally
docker compose up --build


Access:

Frontend: http://localhost:8080

Backend: http://localhost:5000/health

 CI/CD Pipeline (GitHub Actions)
Pipeline Stages

Checkout source code

Build Docker images

Run unit tests inside containers

Scan images using Trivy

Tag Docker images

Push images to Docker registry

Deploy to staging environment

Trigger

Automatically runs on every git push

 Security Scanning (Trivy)

Scans Docker images for:

OS vulnerabilities

Dependency vulnerabilities

Fails pipeline if critical issues are found

 Staging Deployment
Deployment Scripts
deploy.sh

Pulls latest images

Stops existing containers

Starts updated containers

migrate.sh

Runs database migrations

Ensures schema consistency

Deployment Flow
./deploy.sh
./migrate.sh

⚙ Environment Configuration
Environment	Purpose
Local	Development & testing
Staging	Pre-production validation

Configuration handled via:

.env files

Docker Compose variables

GitHub Secrets

 Documentation
Included Documents

Architecture Diagram

CI/CD Pipeline Flow

Deployment Runbook

Troubleshooting Guide

Troubleshooting Examples
Issue	Solution
Container not starting	Check logs using docker logs
DB connection error	Verify env variables
CI pipeline failure	Review GitHub Actions logs
 Demo Video Walkthrough

The demo covers:

Code push to GitHub

CI pipeline execution

Trivy security scan

Image push to registry

Automated staging deployment

Live application verification

 Key Deliverables

 Working 2-tier web application
 Optimized Docker images
 PostgreSQL database integration
 GitHub Actions CI/CD pipeline
 Trivy security scanning
 Automated staging deployment
 Shell scripts for operations
 Professional documentation
 End-to-end live demo

 Outcome

This project simulates a real-world DevOps CI/CD workflow and demonstrates skills in:

Containerization

CI/CD automation

Secure deployments

Infrastructure documentation

Production-ready DevOps practices

 Next Steps (Optional Enhancements)

Add production environment

Kubernetes deployment

Helm charts

Monitoring with Prometheus & Grafana

Slack / Email notifications