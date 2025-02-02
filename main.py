from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from shapely.geometry import Point, Polygon
from geoalchemy2.shape import to_shape
from shapely import wkb
from database import SessionLocal, init_db,engine
import models, schemas

app = FastAPI()

# Initialize database tables
init_db()

models.Base.metadata.create_all(bind=engine)
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/points/", response_model=dict)
def create_point(data: schemas.PointCreate, db: Session = Depends(get_db)):
    point_wkt = f"POINT({data.longitude} {data.latitude})"
    db_point = models.PointData(name=data.name, location=point_wkt, description = data.description)
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return {"message": "Point created successfully"}

@app.get("/points/")
def get_points(db: Session = Depends(get_db)):
    points = db.query(models.PointData).all()
    return [
        {"id": p.id, "name": p.name, "location": to_shape(p.location).wkt}
        for p in points
    ]

@app.get("/points/{id}")
def get_point(id: int, db: Session = Depends(get_db)):
    point = db.get(models.PointData, id)    
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return {"id": point.id, "name": point.name, "location": to_shape(point.location).wkt}

@app.put("/points/{id}", response_model=dict)
def update_point(id: int, data: schemas.PointCreate, db: Session = Depends(get_db)):
    point = db.get(models.PointData, id)
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    
    point_wkt = f"POINT({data.longitude} {data.latitude})"
    point.name = data.name
    point.location = point_wkt
    point.description = data.description
    
    db.commit()
    db.refresh(point)
    return {"message": "Point updated successfully"}

@app.post("/polygons/", response_model=dict)
def create_polygon(data: schemas.PolygonCreate, db: Session = Depends(get_db)):
    coordinates_str = ", ".join(f"{lon} {lat}" for lon, lat in data.coordinates)
    polygon_wkt = f"POLYGON(({coordinates_str}))"
    db_polygon = models.PolygonData(name=data.name, boundary=polygon_wkt,info = data.info )
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return {"message": "Polygon created successfully"}




@app.get("/polygons/")
def get_polygons(db: Session = Depends(get_db)):
    polygons = db.query(models.PolygonData).all()
    return [
        {"id": p.id, "name": p.name, "boundary": to_shape(p.boundary).wkt}
        for p in polygons
    ]

@app.get("/polygons/{id}")
def get_polygons(db: Session = Depends(get_db)):
    polygons = db.get(models.PolygonData, id)
    return [
        {"id": p.id, "name": p.name, "boundary": to_shape(p.boundary).wkt}
        for p in polygons
    ]

@app.put("/polygons/{id}", response_model=dict)
def update_polygon(id: int, data: schemas.PolygonCreate, db: Session = Depends(get_db)):
    polygon = db.get(models.PolygonData, id)
    if polygon is None:
        raise HTTPException(status_code=404, detail="Polygon not found")
    
    coordinates_str = ", ".join(f"{lon} {lat}" for lon, lat in data.coordinates)
    polygon_wkt = f"POLYGON(({coordinates_str}))"
    polygon.name = data.name
    polygon.boundary = polygon_wkt
    polygon.info = data.info
    
    db.commit()
    db.refresh(polygon)
    return {"message": "Polygon updated successfully"}
