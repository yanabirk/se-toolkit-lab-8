import httpx

url = "http://victorialogs:9428/select/logsql/query"
params = {"query": "_time:1h", "limit": 3}
r = httpx.get(url, params=params, timeout=30.0)
print(f"Status: {r.status_code}")
print(f"Content length: {len(r.text)}")
if r.text.strip():
    print(f"Content: {r.text[:300]}")
else:
    print("Empty response")
