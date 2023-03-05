import parse as p
import execute as e
import chart_conversion as chart
import parse_labels as pl
import sys



import json
# convert json object into function call

# function

object_program = p.then_json(p.compair_filter_json(p.ticker_json("AMZN"),p.moving_average_json(p.ticker_json("AMZN"), 30), True), p.compair_filter_json(p.ticker_json("GLD"),p.moving_average_json(p.ticker_json("GLD"), 30), False))






# oversold_program = p.then_json(p.oversold_json(p.ticker_json("AMZN"), 30, 0.95), p.oversold_json(p.ticker_json("AAPL"), 30, 0.95))

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
            return e.compair_filter(apply(block["arg1"]), apply(block["arg2"]), bool(block["direction"]))
        case "oversold":
            return e.oversold(apply(block["arg1"]), int(block["window"]), block["percentile"])






def main():
    # print(str(sys.argv[1]))

    program = json.loads(str(sys.argv[1]))

    labels = [pl.parse_labels(program["arg1"]), pl.parse_labels(program["arg2"])]

    
    oversold_program = p.then_json(p.compair_filter_json(p.ticker_json("AMZN"), p.oversold_json(p.ticker_json("AMZN"), 60, 0.95), True), p.compair_filter_json(p.ticker_json("AAPL"), p.oversold_json(p.ticker_json("AAPL"), 60, 0.95), True))
   
    # print(program)
    # print(oversold_program)

    program_output = apply(program)
    print(chart.full_convert(program_output, labels))

main()