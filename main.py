# Create a FastAPI instance
from fastapi import FastAPI, Query
import mysql.connector


app = FastAPI(title="Employee Search API", description="API for searching employee details in a database")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jackal0309!",
        database="nesthealthcentre"
    )

# Search Endpoints

@app.get("/search")

def search_employees(
    FirstName: str | None = Query(None, description="Search by First Name"),
    LastName: str | None = Query(None, description="Search by Last Name"),
    Department: str | None = Query(None, description="Search by Department"),
    VehiclePlate: str | None = Query(None, description="Search by Vehicle Plate"),
    VehicleDescription: str | None = Query(None, description="Search by Vehicle Description"),
    VehicleColour: str | None = Query(None, description="Search by Vehicle Colour"),
    VehicleMake: str | None = Query(None, description="Search by Vehicle Make"),
    VehicleModel: str | None = Query(None, description="Search by Vehicle Model"),
    StallNumber: str | None = Query(None, description="Search by Stall Number"),
    NumberOfVehicles: int | None = Query(None, description="Search by Number of Vehicles")
):
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Base Queries
    query = "SELECT * FROM Employees WHERE 1=1"
    params = []

    # Filters based on provided parameters
    if FirstName:
        query += " AND FirstName LIKE %s"
        params.append(f"%{FirstName}%")
    if LastName:
        query += " AND LastName LIKE %s"
        params.append(f"%{LastName}%")
    if Department:
        query += " AND Department LIKE %s"
        params.append(f"%{Department}%")
    if VehiclePlate:
        query += " AND VehiclePlate LIKE %s"
        params.append(f"%{VehiclePlate}%")
    if VehicleDescription:
        query += " AND VehicleDescription LIKE %s"
        params.append(f"%{VehicleDescription}%")
    if VehicleColour:
        query += " AND VehicleColour LIKE %s"
        params.append(f"%{VehicleColour}%")
    if VehicleMake:
        query += " AND VehicleMake LIKE %s"
        params.append(f"%{VehicleMake}%")
    if VehicleModel:
        query += " AND VehicleModel LIKE %s"
        params.append(f"%{VehicleModel}%")
    if StallNumber:
        query += " AND StallNumber LIKE %s"
        params.append(f"%{StallNumber}%")
    if NumberOfVehicles is not None:
        query += " AND NumberOfVehicles = %s"
        params.append(NumberOfVehicles)

    cursor.execute(query, params)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"employees": results}