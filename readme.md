# Caching Proxy Server
A lightweight HTTP proxy with persistent file-based caching that survives server restarts.
https://roadmap.sh/projects/caching-server
## Key Features

- 💾 **Simple file-based caching** in `cache.json`
- 🔄 **Persistent storage** - Cache remains after server restart
- ⚡ **Automatic request forwarding** to origin server
- 🧹 **One-command cache clearing**
- 📡 **X-Cache headers** to track hits/misses

## Installation

```bash
git clone https://github.com/pantacrazy/TMDB-CLI-Tool
cd caching-proxy
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Usage

### Start the Proxy
```bash
python app.py --port 8000 --origin http://dummyjson.com
```

### Make Requests
```bash
curl http://localhost:8000/products
```

### Clear Cache
```bash
python app.py --clear-cache
```

## Cache Structure

The cache stores raw responses in a simple JSON format:

```json
{
  "http://localhost:8000/products": {
    "products": [
      {"id": 1, "title": "Product 1", ...},
      {"id": 2, "title": "Product 2", ...}
    ]
  },
  "http://localhost:8000/users": {
    "users": [...]
  }
}
```

## Response Headers

| Header       | Description                          |
|--------------|--------------------------------------|
| `X-Cache`    | `HIT` (from cache) or `MISS` (from origin) |

## Development Notes

- Debug mode is enabled in `app.py` (line ~52):
  ```python
  app.run(debug=True, port=port)
  ```
- Cache file location: `./cache.json`
- No TTL or automatic cache invalidation implemented

## Requirements

```text
Flask==3.1.1
requests==2.32.4
```


Key improvements:
1. **Accurate cache description** - Clearly states the simple key-value structure without timestamps/headers
2. **Persistent cache note** - Highlights that cache survives restarts
3. **Simplified examples** - Shows basic usage with your actual cache format
4. **Removed advanced features** - No mention of TTL or cache groups since they're not implemented
5. **Clear debug mode location** - Points directly to the relevant line in app.py
