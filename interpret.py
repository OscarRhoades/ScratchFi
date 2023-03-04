import parse
import execute as e
import json
# convert json object into function call

# function

with open('sample.json') as json_file:
    data = json.load(json_file)

def apply(block):
    id = block["type"]

    match id:
        case "then":
            return e.then(apply(block["arg1"]), apply(block["arg2"]))
        case "ticker":
            return e.ticker(block["ticker_name"])
        case "moving_average":
            return e.moving_average(apply(block["arg1"]), int(block["window"]))
        case "compair_filter":
            return e.compair_filter(apply(block["arg1"]), apply(block["arg2"]))


apply(data)