# MISP Connector Networking Test Scenarios

```
MISP_URL: http://localhost:9999
MISP_KEY: fake_key_here
MISP_SSL_VERIFY: false
```

## What Each Scenario Tests

| Scenario | Init | Search | What You're Testing |
|----------|------|--------|---------------------|
| `no_answer_on_search` | ✅ passes | hangs forever | Read timeout / no timeout handling |
| `slow_answer` | ✅ passes | responds after N seconds | Slow server behavior |
| `partial_response` | ✅ passes | sends headers, body never finishes | Broken connection mid-transfer |
| `empty_events` | ✅ passes | returns `[]` | Normal operation, no data |
| `error_500` | ✅ passes | returns 500 error | Server error handling |
| `no_answer_on_init` | hangs forever | never reached | Connect/init timeout handling |

## What You'll See in the Logs

When the connector starts and hits the fake server:

```sh
2026-02-11 10:00:01 - Fake MISP server running on port 9999
2026-02-11 10:00:01 - Scenario: no_answer_on_search
2026-02-11 10:00:03 - GET /servers/getVersion.json
2026-02-11 10:00:03 - GET /users/view/me.json
2026-02-11 10:00:05 - POST /events/restSearch
2026-02-11 10:00:05 -   Headers: Authorization=fake_key_here
2026-02-11 10:00:05 -   Body: {"returnFormat": "json", "page": 1, "limit": 10...}
2026-02-11 10:00:05 - Simulating no answer on search (hanging)...
```