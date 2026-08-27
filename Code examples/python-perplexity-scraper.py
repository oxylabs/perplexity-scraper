import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'perplexity',
    'prompt': 'top 3 smartphones in 2025, compare pricing across US marketplaces',
    'geo_location': 'United States',
    'parse': True,
    'callback_url': 'https://your-server.com/oxylabs-callback'
}

# Get a response.
response = requests.post(
    'https://data.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload
)

# Print prettified response to stdout.
pprint(response.json())
