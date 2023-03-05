def parse_labels(block):
    id = block["type"]

    match id:
        case "then":
            return str("(" + parse_labels(block["arg1"]) + ")" + " then " + "(" + parse_labels(block["arg2"]) + ")")
        case "ticker":
            return block["ticker_name"]
        case "moving_average":
            return str("moving average of " + parse_labels(block["arg1"]) + " with a " + str(block["window"]) + " window")
        case "compair_filter":
            if bool(block["direction"]):
                return str(parse_labels(block["arg1"]) + " if greater than " + parse_labels(block["arg2"]))
            else:
                return str(parse_labels(block["arg1"]) + " if less than " + parse_labels(block["arg2"]))

        