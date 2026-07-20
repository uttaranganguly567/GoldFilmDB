import urllib.request
import sys

print("Sending request to http://127.0.0.1:8000/ ...")
try:
    with urllib.request.urlopen("http://127.0.0.1:8000/", timeout=5) as response:
        html = response.read().decode('utf-8')
        print("SUCCESS! Server responded.")
        print(f"Status Code: {response.status}")
        print("First 200 characters of HTML response:")
        print(html[:200])
except Exception as e:
    print(f"\nERROR: Failed to connect to local server.", file=sys.stderr)
    print(f"Details: {e}", file=sys.stderr)
    sys.exit(1)
