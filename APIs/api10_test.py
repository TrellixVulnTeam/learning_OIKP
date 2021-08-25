import requests
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description="Ioi, Item of interest")
parser.add_argument("-c","--category", type=str, help="Category in which your Ioi is")
parser.add_argument("-i","--item", type=str, help="Your Ioi")
args = parser.parse_args()


def get_info(category,item):
    BASE = "http://127.0.0.1:5000"

    response = requests.post(BASE + "/payment_info/list")

    response2 = requests.put(BASE + "/payment_info/user",{"interest":f"{category} {item}"})


    pprint(response2.json())
    pprint(response.json())


if __name__ == '__main__':
    get_info(args.category,args.item)