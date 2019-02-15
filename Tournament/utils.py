from entities import Competitor, Forecaster


def show(s):
    if isinstance(s, Competitor) or isinstance(s, Forecaster):
        return s.show()
    elif isinstance(s, str): 
        return s
    else:
        return None
