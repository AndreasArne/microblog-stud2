# Technical study: Grafana Loki for Microblog logs

## What it is
Loki stores and queries log lines. It indexes only labels (container, service), not the text, so it is cheap to run.
Promtail reads the logs from the Docker containers and sends them to Loki. You query with LogQL, for example
`{service="prod"} |= "GET"`.

## How it is used in Microblog
`logging/docker-compose.yml` and `logging/promtail.yml`. Microblog writes its gunicorn access log to stdout
(see `boot.sh`), Docker keeps it, and Promtail finds the containers through the Docker socket.

```
docker compose up -d prod
docker compose -f logging/docker-compose.yml up -d
curl -G localhost:3100/loki/api/v1/query_range --data-urlencode 'query={service="prod"} |= "GET"'
```

Tested result (terminal output, see report): the `GET /version` (200) and `GET /nope` (404) lines came back with the
labels `container=microblog-stud-prod-1, service=prod`.

## DevOps
Logs from many containers on many servers (our two app servers and the load balancer) end up in one place, so you
see an error without SSH to each server. It is the "monitor and learn" part of the DevOps loop and it pairs with
the Prometheus metrics of kmom04. Alerts on log lines are possible. Cost: it needs storage and care so secrets
are not logged.

## Screenshots
NOT INCLUDED: the test run had no browser or Grafana (Grafana is not allowed in this kmom). The query output above
is the evidence.
