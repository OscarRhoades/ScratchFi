
import json 

def then_json(arg1, arg2):
    then = {
        "type": "then",
        "arg1": arg1,
        "arg2": arg2
    }
    return then

def ticker_json(tkr_str):
    ticker = {
        "type": "ticker",
        "ticker_name": tkr_str,
    }
    return ticker

def moving_average_json(arg1, window):
    moving_average = {
        "type": "moving_average",
        "arg1": arg1,
        "window": window
        
    }
    return moving_average



def compair_filter_json(arg1, arg2, direction):
    compair_filter = {
        "type": "compair_filter",
        "arg1": arg1,
        "arg2": arg2,
        "direction": direction
    }
    return compair_filter

def oversold_json(arg1, window, percentile):
    oversold = {
        "type": "oversold",
        "arg1": arg1,
        "window": window,
        "percentile": percentile
    }
    return oversold

def derivative_json(arg1):
    print("derivative")

    

# object_program = then_json(compair_filter_json(ticker_json("AMZN"),moving_average_json(ticker_json("AMZN"), 30), False), compair_filter_json(ticker_json("GLD"),moving_average_json(ticker_json("GLD"), 30), False))


# json_object = json.dumps(object_program, indent = 4) 
# print(json_object)

# with open("sample.json", "w") as outfile:
#     json.dump(object_program, outfile)
