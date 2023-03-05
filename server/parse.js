function then_json(arg1, arg2) {
    let then = {
        type: "then",
        arg1: arg1,
        arg2: arg2
    };
    return then;
}

function ticker_json(tkr_str) {
    let ticker = {
        type: "ticker",
        ticker_name: tkr_str
    };
    return ticker;
}

function moving_average_json(arg1, window) {
    let moving_average = {
        type: "moving_average",
        arg1: arg1,
        window: window
    };
    return moving_average;
}

function compair_filter_json(arg1, arg2, direction) {
    let compair_filter = {
        type: "compair_filter",
        arg1: arg1,
        arg2: arg2,
        direction: direction
    };
    return compair_filter;
}

function oversold_json(arg1, window, percentile) {
    let oversold = {
        type: "oversold",
        arg1: arg1,
        window: window,
        percentile: percentile
    };
    return oversold;
}