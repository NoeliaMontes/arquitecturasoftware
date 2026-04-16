from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos
class Usuarios(BaseModel):
    nombre: str
    email: str
    password: str
    

# GET
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "mensaje": "Mostrando información del usuario"}

# POST
@app.post("/users/")
def create_user(user: Usuarios):
    return {"mensaje": "Usuario creado exitosamente", "user": user}

# PUT
@app.put("/users/{user_id}")
def update_user(user_id: int, user: Usuarios):
    return {"mensaje": f"Usuario {user_id} actualizado", "user": user}

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"mensaje": f"Usuario {user_id} eliminado"}