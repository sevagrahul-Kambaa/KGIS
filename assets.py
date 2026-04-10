import asyncio
from fastapi import FastAPI, HTTPException
import uvicorn

# Employee Email -> Assigned Printer Mapping
EMPLOYEE_ASSETS = {
    "karthicanand@kgis.co": "511902-PR04",
    "eric.brown@kgis.co": "18203-PR01",
    "govind@kgis.co": "511902-PR07",
    "sembharuthi.i@kgis.co": "411104-PR09",
    "chandru.cm@kgis.co": "411112-PR15",
    "aakash.a@kgis.co": "17106-PR30",
    "arbaaz.t@kgis.co": "17102-PRK65",
    "sakthi.s@kgis.co": "411113-PRK68",
    "buvanesan.r@kgis.co": "17103-PRK106",
    "hariharan@kgis.co": "18241-PR18"
}

app = FastAPI(title="Asset Management Service")

async def get_employee_assets(email: str) -> str:
    """Simulates an asynchronous database lookup for employee assets."""
    await asyncio.sleep(0.1)  # Simulate network latency
    return EMPLOYEE_ASSETS.get(email.lower().strip())

@app.get("/assets")
async def list_assets():
    """Returns all employee-to-printer asset mappings."""
    return EMPLOYEE_ASSETS

@app.get("/assets/{email}")
async def get_asset(email: str):
    """Returns the assigned printer for a specific employee email."""
    printer = await get_employee_assets(email)
    if not printer:
        raise HTTPException(status_code=404, detail="Employee email not found in asset records")
    return {"email": email, "printer_label": printer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
