# Multi-Agent Temporal Workflow (Template)

## Architecture Diagram

                 Client

                    │

              POST /run

                    │

               FastAPI API

                    │

         Start Temporal Workflow

                    │

             Temporal Worker

                    │

      Planner → Researcher → Writer → Reviewer

                    │

             Docker Sandbox

                    │

          Structured JSON Trace

          
## Overview
This project is a simple reference implementation Multi-Agent Temporal Workflow.

### Features
- FastAPI REST API
- Temporal workflow (Planner -> Researcher -> Writer -> Reviewer)
- Retry/Timeout handled by Temporal activities
- Docker-based sandbox (placeholder)
- Structured JSON traces
- Ready for GitHub

## Folder Structure

```
api/
workflow/
worker/
agents/
sandbox/
traces/
```

## Run

1. Create virtual environment
2. `pip install -r requirements.txt`
3. `docker compose up -d`
4. Start worker
5. Start FastAPI
6. Call:

POST /run

## Isolation Model
Development:
- Docker sandbox
- --network none
- --read-only
- CPU and memory limits

Production:
- Firecracker microVMs

## Retry Strategy
- Max Attempts: 3
- Exponential Backoff
- Activity Timeout: 30 seconds

## Multi-Tenant Hardening
- Separate workflow IDs
- Per-tenant queues
- Per-tenant secrets
- Audit logs
- Resource quotas
- Authentication
------------------------------------------------

# Multi-Agent Temporal Workflow 

## Overview
This Basic project demonstrates the architecture requested in the assignment.

Flow:
Client -> FastAPI -> Temporal Workflow -> Activities (Planner, Researcher, Writer, Reviewer)
-> Docker Sandbox -> Structured Trace Logs

## Folder Explanation

### api/
Receives HTTP requests.
- POST /run : Starts a workflow
- GET / : Health check

### workflow/
Contains the Temporal workflow and activities.
Workflow only controls execution order.
Activities perform the actual work.

### worker/
Runs the Temporal Worker which executes workflow activities.

### agents/
Simple agent implementations.
Planner -> Creates a plan
Researcher -> Collects information
Writer -> Produces output
Reviewer -> Reviews output

### sandbox/
Placeholder for secure Docker execution.
In production replace with Firecracker microVMs.

### traces/
Produces JSON structured logs similar to Langfuse.

## Execution Steps

1. Install Python 3.12
2. Install Docker Desktop
3. pip install -r requirements.txt
4. docker compose up -d
5. python worker/worker.py
6. uvicorn api.main:app --reload
7. Open http://localhost:8000/docs
8. Execute POST /run

## Design Decisions

- FastAPI exposes REST API.
- Temporal provides durable execution.
- Activities support retry and timeout.
- Docker isolates untrusted execution.
- JSON logs improve observability.

## Future Improvements

- Firecracker microVM
- Authentication
- Kubernetes deployment
- Langfuse integration
