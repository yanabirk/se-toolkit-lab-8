---
name: observability
description: Use observability tools to investigate errors and trace failures
always: true
---

# Observability Skill

Use VictoriaLogs and VictoriaTraces MCP tools to investigate system health and debug failures.

## Available Tools

- `obs_logs_search` — Search VictoriaLogs using LogsQL query
- `obs_logs_error_count` — Count errors for a service over a time window
- `obs_traces_list` — List recent traces for a service
- `obs_traces_get` — Fetch a specific trace by ID

## Strategy

### When the user asks about errors or failures:
1. Start with `obs_logs_error_count` to check if there are recent errors for the relevant service
2. If errors exist, use `obs_logs_search` to find the specific error logs
3. Extract any `trace_id` from the error logs
4. Use `obs_traces_get` to fetch the full trace and understand the failure path
5. Summarize findings concisely — don't dump raw JSON

### When the user asks about system health:
1. Check error counts for key services (e.g., "Learning Management Service")
2. Report whether the system is healthy or if there are recent errors
3. If there are errors, provide a brief summary of what went wrong

### Query tips:
- Use narrow time windows for fresh data: `_time:10m` for last 10 minutes
- Filter by service: `service.name:"Learning Management Service"`
- Filter by severity: `severity:ERROR`
- Example query: `_time:10m service.name:"Learning Management Service" severity:ERROR`

### Response style:
- Summarize findings in plain language
- Don't dump raw JSON unless explicitly asked
- If you find a trace, explain what went wrong in the request flow
- If no errors found, say so clearly

## Example reasoning flow

User: "Any LMS backend errors in the last 10 minutes?"

1. Call `obs_logs_error_count` with service="Learning Management Service", minutes=10
2. If count > 0:
   - Call `obs_logs_search` with query=`_time:10m service.name:"Learning Management Service" severity:ERROR`
   - Look for `trace_id` in the results
   - If trace_id found, call `obs_traces_get` to inspect the failure
   - Summarize: what failed, where, and why
3. If count = 0:
   - Report: "No errors found in the last 10 minutes"
