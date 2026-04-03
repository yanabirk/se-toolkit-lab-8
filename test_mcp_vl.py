import httpx

# Test from within the MCP server context
url = "http://victorialogs:9428/select/logsql/query"
params = {"query": "_time:10m", "limit": 3}
try:
    with httpx.Client() as client:
        r = client.get(url, params=params, timeout=30.0)
        print(f"Status: {r.status_code}")
        print(f"Content length: {len(r.text)}")
        if r.text.strip():
            print(f"Content: {r.text[:200]}...")
        else:
            print("No logs found")
except Exception as e:
    print(f"Error: {e}")
