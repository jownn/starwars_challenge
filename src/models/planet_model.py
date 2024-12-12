from db import mongo


class Planet:
    @staticmethod
    def get_all():
        return list(mongo.db.planets.find())

    @staticmethod
    def get_by_id(planet_id):
        return mongo.db.planets.find_one({"_id": planet_id})

    @staticmethod
    def add(data):
        result = mongo.db.planets.insert_one(data)
        return result.inserted_id

    @staticmethod
    def update(planet_id, data):
        result = mongo.db.planets.update_one(
            {"_id": planet_id}, {"$set": data}
        )
        return result.modified_count

    @staticmethod
    def delete(planet_id):
        result = mongo.db.planets.delete_one({"_id": planet_id})
        return result.deleted_count