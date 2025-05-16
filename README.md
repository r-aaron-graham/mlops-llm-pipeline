# MLOps LLM Pipeline

## Overview
An end-to-end demonstration of deploying a lightweight LLM inference service with CI/CD, monitoring, and a retraining workflow.

## Prerequisites
- Python 3.8+
- Docker installed
- GitHub repository with Actions enabled
- Access to a cloud container registry or deployment target (e.g., Render)

## Setup
1. **Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
