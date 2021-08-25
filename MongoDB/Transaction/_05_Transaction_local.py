from pymongo import MongoClient,read_concern,write_concern,ReadPreference
from faker import Faker
from bson import ObjectId
from pprint import pprint
import random


class MongoTrans:
    client = MongoClient("localhost",27017)
    my_wc_concern = write_concern.WriteConcern("majority",wtimeout=1000)


    def callback(self,session,user_id,payment,category,item):
        inventory = session.client.trans.inventory
        user = session.client.trans.users
        # for i in user.find():
        #     print(i)
        #print(user.find_one({"_id":user_id}))
        if user.find_one({"_id":user_id})['savings'] >=payment:
            if inventory.find_one({f"{category}.{item}.stock":{"$gte":1}}) :
                inventory.update_one({f"{category}.{item}": {"$exists": True}}, {"$inc": {f"{category}.$.{item}.stock": -1}})
                user.update_one({"_id":user_id},{"$push":{"ordered":item},"$inc":{"savings":-payment}})


                user_name = user.find_one({"_id": user_id})['name']
                things_ordered_so_far = user.find_one({"_id": user_id})['ordered']
                savings = user.find_one({"_id": user_id})['savings']
                print("Transaction succeeded!")
                print("-User: {}\n-What they have bought: {}\n-Savings_left :{}".format(user_name,things_ordered_so_far,savings))
            else:
                print(f"{item} is not available at the moment")
        else:
            print("비싸서 살수가 없어요")

    def list_items(self):
        hash = {}
        for i in self.client.trans.inventory.find():
            hash = i
        return hash

    def transaction(self,interest):

        item = interest.split()
        category = item[0]
        item = item[1]

        payment = list(self.client.trans.inventory.aggregate([{"$project":{"price":f"${category}.{item}.price"}}]))[0]['price'][0]
        user_id = self.client.trans.users.find_one({"savings":{"$gte":payment}})['_id']
        with self.client.start_session() as session:
            session.with_transaction(lambda s :self.callback(s,user_id,payment,category,item),
                                 read_concern=read_concern.ReadConcern('local'),
                                 write_concern=self.my_wc_concern,
                                 read_preference=ReadPreference.PRIMARY)



if __name__ == '__main__':

    #create Fake info
    fake = Faker()
    a = MongoTrans()
    for i in range(100):
        a = fake.profile()
        a.pop('current_location')
        a.pop('birthdate')
        a.update({"ordered":[],"savings" : i*random.randint(500,50000)})
        a.client.trans.users.insert_one(a)

    lst_of_item=["shoes","almond","coffee","bag","computer","piano","smartphone"]
    a.client.trans.inventory.insert_one({"grocery":[{"coffee":{"stock":1000,"price":2200}},
                                                    {"almond": {"stock":1500,"price":17000}}],
                                       "musical_instrument":[{"piano":{"stock":2,"price":10000000}}],
                                        "fashion":[{"bag":{"stock":5,"price":100000}},
                                                   {"shoes":{"stock":7,"price":28000}}],
                                       "electronic" :[{"smartphone":{"stock":10,"price":290000}},
                                                      {"computer":{"stock":3,"price":1500000}}]})




