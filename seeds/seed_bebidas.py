from app.database import SessionLocal, engine
from app import models
from app.models import ProductType

models.Base.metadata.create_all(bind=engine)

def seed_bebidas():
    db = SessionLocal()

    bebidas = [
        ("Pinta Dorada de la Comarca", "Suave y espumosa, orgullo hobbit.", 3.5, 120),
        ("Cerveza Negra de Erebor", "Oscura y potente, elaborada por enanos.", 5.5, 60),
        ("Hidromiel del Anduin", "Dulce y traicionera como un río crecido.", 6.0, 40),
        ("Vino Blanco de Rivendel", "Ligero y aromático, casi canta.", 11.0, 15),
        ("Vino Tinto de Gondor", "Robusto, digno de la mesa del Rey.", 13.5, 18),
        ("Sidra del Brandivino", "Refrescante y afrutada.", 4.0, 70),
        ("Licor de Moras de Bree", "Dulce con un golpe inesperado.", 7.0, 35),
        ("Cerveza Ahumada del Norte", "Con notas de roble y fuego.", 5.0, 50),
        ("Aguardiente de los Dúnedain", "Fuerte y serio como sus guardianes.", 9.0, 20),
        ("Hidromiel Especiada de Rohan", "Calienta como una carga de los Rohirrim.", 6.5, 30),
        ("Vino Rosado de Dorwinion", "Exótico y fragante.", 12.0, 12),
        ("Cerveza Clara de los Puertos Grises", "Suave, con sabor a despedida.", 4.5, 40),
        ("Elixir Dulce de Lórien", "Ligero, floral y casi mágico.", 14.0, 10),
        ("Cerveza Roja de la Marca del Este", "Intensa y con carácter.", 5.8, 45),
        ("Sidra Especiada de Otoño", "Ideal para noches frías.", 4.8, 55),
    ]

    for name, desc, price, stock in bebidas:
        if not db.query(models.Product).filter_by(name=name).first():
            db.add(models.Product(
                name=name,
                description=desc,
                price=price,
                stock=stock,
                category=ProductType.BEBIDA
            ))

    db.commit()
    db.close()
    print("🍺 Bebidas sembradas correctamente.")

if __name__ == "__main__":
    seed_bebidas()
