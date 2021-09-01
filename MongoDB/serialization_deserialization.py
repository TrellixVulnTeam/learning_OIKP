from marshmallow import Schema, fields

class Store:
    def __init__(self, name: str, location: list):
        self.name = name
        self.location = location


class StoreSchema(Schema):
	name = fields.Str()
	location = fields.List(cls_or_instance=fields.Integer())


walmart = Store("Walmart", [1,2])
store_schema = StoreSchema()

print(store_schema.dump(walmart))

store_data = {"name": "dsds", "location":[1,2,3,4] }
print(store_schema.load(store_data))