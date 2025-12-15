from app.database import SessionLocal, engine
from app import models
from app.models import ProductType

# Nos aseguramos de que las tablas existan
models.Base.metadata.create_all(bind=engine)

def seed_db():
    db = SessionLocal()

    # --- LISTA DE PRODUCTOS DE LA COMARCA ---
    products_data = [
        # BEBIDAS
        {
            "name": "Pinta de Cerveza 1420",
            "description": "La especialidad de la casa. Elaborada con cebada dorada de la Cuaderna del Sur.",
            "price": 3.50,
            "stock": 100,
            "category": ProductType.BEBIDA
        },
        {
            "name": "Hidromiel Vieja",
            "description": "Dulce y fuerte. Cuidado, que pega más fuerte que un Troll de las cavernas.",
            "price": 5.00,
            "stock": 50,
            "category": ProductType.BEBIDA
        },
        {
            "name": "Vino de los Elfos",
            "description": "Importado directamente de Rivendel (o eso dice el mercader).",
            "price": 12.00,
            "stock": 10,
            "category": ProductType.BEBIDA
        },
        
        # COMIDA
        {
            "name": "Pan de Lembas",
            "description": "Un solo bocado llena el estómago de un hombre adulto (o de 4 Hobbits).",
            "price": 8.00,
            "stock": 200,
            "category": ProductType.COMIDA
        },
        {
            "name": "Estofado de Conejo",
            "description": "Con buenas patatas. Receta especial de Sam.",
            "price": 7.50,
            "stock": 20,
            "category": ProductType.COMIDA
        },
        {
            "name": "Segundo Desayuno Completo",
            "description": "Huevos, bacon, tostadas, salchichas y tomates asados.",
            "price": 10.00,
            "stock": 40,
            "category": ProductType.COMIDA
        },
        {
            "name": "Setas Salteadas",
            "description": "Recogidas (robadas) de los campos del granjero Maggot.",
            "price": 4.50,
            "stock": 15,
            "category": ProductType.COMIDA
        },

        # OTROS
        {
            "name": "Hierba para Pipa (Viejo Toby)",
            "description": "La mejor hierba de la Comarca. Relajante y aromática.",
            "price": 15.00,
            "stock": 60,
            "category": ProductType.OTROS
        },
        {
            "name": "Mapa de la Tierra Media",
            "description": "Un poco arrugado y con manchas de cerveza, pero legible.",
            "price": 2.00,
            "stock": 5,
            "category": ProductType.OTROS
        }
    ]

    print("🌱 Sembrando la base de datos del Dragón Verde...")
    
    count = 0
    for item in products_data:
        # Verificamos si ya existe para no duplicarlo (por nombre)
        exists = db.query(models.Product).filter(models.Product.name == item["name"]).first()
        if not exists:
            # Magia de Python: **item desempaqueta el diccionario en los argumentos
            new_product = models.Product(**item)
            db.add(new_product)
            count += 1
            print(f"   -> Añadido: {item['name']}")
        else:
            print(f"   -> Ya existe: {item['name']}")

    db.commit()
    db.close()
    print(f"✅ Proceso terminado. Se han añadido {count} productos nuevos.")

if __name__ == "__main__":
    seed_db()