curl 'https://data.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "perplexity",
        "prompt": "best supplements for better sleep",
        "geo_location": "United States",
        "parse": true,
        "callback_url": "https://your-server.com/oxylabs-callback"
    }'
