try:
    import ujson as json
except ImportError:
    import json


loads = json.loads
dumps = json.dumps
