# Tripadvisor-Scraper
Scrap acctractions from Tripadvisor using Beautiful Soup.
Prepare training data for implementing a near real-time recommendations with Amazon Personalize.
## Attraction types
- Points of Interest & Landmarks
- Museums
- Nature & Parks
## Cities
- Toronto
- Vancouver
- New York
- Quebec City
- Washington DC
## Data Structure
```
item = {
    "destinationId": DESTINATIONID,
    "name": name,
    "labels": labels,
    "address": address,
    "description": description,
    "timeCost": timeCost,
    "rate": rate,
    "heat": heat,
    "opentime": opentime,
    "imgUrl": img_url,
}
```