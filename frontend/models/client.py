class Client:
    def __init__(self, id, name, cash, is_active):
        self.id = id
        self.name = name
        self.cash = cash
        self.is_active = is_active

    @staticmethod
    def from_json(data):
        return Client(
            id=data.get('id'),
            name=data.get('name'),
            cash=data.get('cash'),
            is_active=data.get('is_active')
        )
        