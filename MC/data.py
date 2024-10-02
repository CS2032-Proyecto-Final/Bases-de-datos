import string

import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker('es_MX')

# Configuraciones
num_personas = 1000  # Número de personas
num_tiendas = 1000 # NúMmero de tiendas
saldo_min = 0.0  # Monto mínimo
saldo_max = 10000.0  # Monto máximo

# Generar datos para las tablas
cliente_data = []
persona_data = []
tienda_data = []
cuenta_data = []

for i in range(num_personas):
    
    id = i
    nombre = fake.name()
    saldo = round(random.uniform(saldo_min, saldo_max), 2)
    telefono = str(random.randint(100000000, 999999999))


    cliente_data.append({
        "id": id,
        "nombre": nombre,
    })

    persona_data.append({
        "cliente_id": id,
        "telefono": telefono
    })

    cuenta_data.append({
        "id": id,
        "cliente_id": id,
        "saldo": saldo
    })

for i in range(num_tiendas):

    id = num_personas + i
    nombre = fake.company()
    saldo = round(random.uniform(saldo_min, saldo_max), 2)
    
    # Limpiar el nombre de la compañía eliminando espacios y caracteres especiales
    nombre_limpio = nombre.replace(' ', '').replace(',', '').replace('.', '').lower()

    # Generar un nombre de usuario aleatorio y combinarlo con la compañía
    correo = f"{nombre_limpio}@gmail.com"

    cliente_data.append({
        "id": id,
        "nombre": nombre,
    })

    tienda_data.append({
        "cliente_id": id,
        "correo": correo
    })

    cuenta_data.append({
        "id": id,
        "cliente_id": id,
        "saldo": saldo
    })

cliente_df = pd.DataFrame(cliente_data)
cliente_df.to_csv('clientes.csv', index=False)

persona_df = pd.DataFrame(persona_data)
persona_df.to_csv('personas.csv', index=False)

tienda_df = pd.DataFrame(tienda_data)
tienda_df.to_csv('tiendas.csv', index=False)

cuenta_df = pd.DataFrame(cuenta_data)
cuenta_df.to_csv('cuentas.csv', index=False)

print("Se generaron los CSVs.")
