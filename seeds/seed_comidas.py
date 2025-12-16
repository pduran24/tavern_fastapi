from app.database import SessionLocal, engine
from app import models
from app.models import ProductType

models.Base.metadata.create_all(bind=engine)

def seed_comidas():
    db = SessionLocal()

    comidas = [
        ("Pan de Lembas Élfico", "Un bocado basta para seguir caminando.", 8.0, 200),
        ("Estofado Hobbit Tradicional", "Contundente y reconfortante.", 7.5, 40),
        ("Conejo con Buenas Patatas", "Receta secreta de Sam.", 8.5, 25),
        ("Tarta de Manzana de la Comarca", "Dulce y crujiente.", 6.0, 30),
        ("Pan Negro del Norte", "Denso y nutritivo.", 4.0, 50),
        ("Queso Curado de Bree", "Fuerte aroma, gran sabor.", 5.5, 35),
        ("Sopa Caliente del Dragón Verde", "Perfecta tras un largo viaje.", 6.5, 45),
        ("Pastel de Carne Enano", "Pesado como un martillo.", 9.0, 20),
        ("Salchichas Ahumadas", "Crujientes por fuera, jugosas por dentro.", 6.0, 40),
        ("Pescado del Brandivino", "Fresco del día.", 7.0, 25),
        ("Miel Silvestre de la Comarca", "Dorada y aromática.", 6.5, 30),
        ("Galletas de Avena Hobbit", "Ideales para el segundo desayuno.", 4.5, 60),
        ("Jamón Asado de Bree", "Lento y jugoso.", 10.0, 15),
        ("Setas Salteadas del Bosque", "Recogidas al amanecer.", 5.0, 20),
        ("Pastel Dulce de Frutos Rojos", "Ligero y festivo.", 6.8, 25),
    ]

    for name, desc, price, stock in comidas:
        if not db.query(models.Product).filter_by(name=name).first():
            db.add(models.Product(
                name=name,
                description=desc,
                price=price,
                stock=stock,
                category=ProductType.COMIDA
            ))

    db.commit()
    db.close()
    print("🥘 Comidas sembradas correctamente.")

if __name__ == "__main__":
    seed_comidas()
