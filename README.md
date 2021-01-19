# probes

## What this app is about ?

This app is simple python app for testing Liveness and Readiness probes on K8s.

## API

You should defining probes:
 - /ready/check
 - /live/check

You could enable/disable probes using simple api calls:
Live probe:
- GET /live/start
- GET /live/stop
Ready probe:
- GET /ready/start
- GET /ready/stop

At begining both endpoints (live and ready) are returning 200 http code.
When you make req to /ready/stop, ready endpoint (/ready/check) will start failing.
After req to /ready/start, ready endpoint will start returning 200 http code again.

