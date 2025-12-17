class Product:
    def __init__(self, id, name, description, price, stock, category):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category

    # Método helper para convertir el json en objeto
    @staticmethod
    def from_json(data):
        return Product(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            stock=data.get('stock'),
            category=data.get('category')
        )