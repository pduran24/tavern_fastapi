from app.database import SessionLocal, engine
from app import models
from app.models import ProductType

models.Base.metadata.create_all(bind=engine)

def seed_otros():
    db = SessionLocal()

    otros = [
        ("Hierba Viejo Toby", "La mejor hierba para pipa de la Comarca.", 15.0, 60),
        ("Mapa Detallado de la Tierra Media", "Con rutas y anotaciones antiguas.", 5.0, 12),
        ("Pipa Enana Tallada", "Pesada y resistente.", 18.0, 8),
        ("Pipa Élfica de Madera Blanca", "Ligera y elegante.", 22.0, 6),
        ("Amuleto de la Suerte de Bree", "Dicen que protege a los viajeros.", 10.0, 15),
        ("Pergamino con Runas Antiguas", "Nadie sabe leerlas del todo.", 25.0, 4),
        ("Dado Tallado en Hueso", "Perfecto para apuestas nocturnas.", 6.0, 20),
        ("Cuchillo Decorativo Élfico", "No apto para combate, pero hermoso.", 30.0, 3),
        ("Cantimplora del Montaraz", "Resistente y práctica.", 14.0, 10),
        ("Bolsa de Viaje Hobbit", "Más grande por dentro de lo que parece.", 12.0, 9),
    ]

    for name, desc, price, stock in otros:
        if not db.query(models.Product).filter_by(name=name).first():
            db.add(models.Product(
                name=name,
                description=desc,
                price=price,
                stock=stock,
                category=ProductType.OTROS
            ))

    db.commit()
    db.close()
    print("🗺️ Objetos sembrados correctamente.")

if __name__ == "__main__":
    seed_otros()
