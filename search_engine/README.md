## Search Engine
This Django project returns k most relevant summaries for each query.

### Dependency Installation
`pip install -r requirements.txt`

### Start Server
`python manage.py runserver 0.0.0.0:8000`

### Test
`python manage.py test`

### Usage
1. Need to call following POST request for search results.
   - URL: http://localhost:8000/search-app/search/
   - Json Body: `{"k": 3, queries: ["is your problems" , "achieve take book"]}`
