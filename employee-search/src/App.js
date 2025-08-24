import React, { useState } from 'react';
import "./App.css";

function App() {
  const [filters, setFilters] = useState({
    FirstName: "",
    LastName: "",
    Department: "",
    VehiclePlate: "",
    VehicleDescription: "",
    VehicoleColour: "",
    VehicleMake: "",
    VehicleModel: "",
    StallNumber: "",
    NumberOfVehicles: "",
  });
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
}
