command to run script
`uvicorn main:app `



###  POINTS 

get : `/points` # returns all points

get : `/points/<id>` # return point with id = 1
```
 {
    "name": "Point A",
    "latitude": 40.7128,
    "longitude": -74.0060
}
```

post : `/points`
```
body : {
    "name": "Point A",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "description": "random place"
}
```
put : `/points/<id>`
```
body : {
    "name": "Point A new",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "description": "random place 2"
}
```

###  POLYGONS
get : `/polygons` # returns all polygons 

get : `/polygons/<id>`  # return polygon with id = 1

post : `/polygons`
```
body : {
    "name": "Polygon A",
    "coordinates": [
        [-74.0060, 40.7128],
        [-73.9352, 40.7306],
        [-73.9000, 40.7800],
        [-74.0060, 40.7128]
    ],
    "info":{
        "population" : 321
    }
}
```

put : `/polygons/<id>`
```
body : {
    "name": "Polygon A new",
    "coordinates": [
        [-74.0060, 40.7128],
        [-73.9352, 40.7306],
        [-73.9000, 40.7800],
        [-74.0060, 40.7128]
    ],
    "info":{
        "population" : 321
    }
}
```

