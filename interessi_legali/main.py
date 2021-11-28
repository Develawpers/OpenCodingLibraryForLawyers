__author__ = "Biagio Distefano"
__copyright__ = "Copyright 2021, Law Engineering Systems s.r.l."
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "b.distefano@lawengineeringsystems.com"
__stolen_from__ = "https://github.com/lawengineeringsystems/lawyertools/tree/master/lawyertools/it/interessi_legali"

import datetime

from dateutil.relativedelta import relativedelta

# this defines the interest rates for every time range
# like so: (date_from: date, date_to: date, interest_rate: float)
TABELLA = [
    (datetime.date(1942, 4, 12), datetime.date(1990, 12, 15), 5.0),
    (datetime.date(1990, 12, 16), datetime.date(1996, 12, 31), 10.0),
    (datetime.date(1997, 1, 1), datetime.date(1998, 12, 31), 5.0),
    (datetime.date(1999, 1, 1), datetime.date(2000, 12, 31), 2.5),
    (datetime.date(2001, 1, 1), datetime.date(2001, 12, 31), 3.5),
    (datetime.date(2002, 1, 1), datetime.date(2003, 12, 31), 3.0),
    (datetime.date(2004, 1, 1), datetime.date(2007, 12, 31), 2.5),
    (datetime.date(2008, 1, 1), datetime.date(2009, 12, 31), 3.0),
    (datetime.date(2010, 1, 1), datetime.date(2010, 12, 31), 1.0),
    (datetime.date(2011, 1, 1), datetime.date(2011, 12, 31), 1.5),
    (datetime.date(2012, 1, 1), datetime.date(2013, 12, 31), 2.5),
    (datetime.date(2014, 1, 1), datetime.date(2014, 12, 31), 1.0),
    (datetime.date(2015, 1, 1), datetime.date(2015, 12, 31), 0.5),
    (datetime.date(2016, 1, 1), datetime.date(2016, 12, 31), 0.2),
    (datetime.date(2017, 1, 1), datetime.date(2017, 12, 31), 0.1),
    (datetime.date(2018, 1, 1), datetime.date(2018, 12, 31), 0.3),
    (datetime.date(2019, 1, 1), datetime.date(2019, 12, 31), 0.8),
    (datetime.date(2020, 1, 1), datetime.date(2020, 12, 31), 0.05),
    (datetime.date(2021, 1, 1), None, 0.01),
]


"""
The interest formula is as follows:
I = C * s * t / 36500

Where:
- I -> total interests
- C -> initial capital
- s -> interest rate
- t -> time expressed in days
"""


# this is just a helper to validate compounding units and have them both ita/eng
CAP_UNIT_MAP = dict(giorni="days", mesi="months", anni="years")
# so allowed cap units are gonna be all keys and values of CAP_UNIT_MAP
# we use a set cuz it's more efficient
ALLOWED_CAP_UNITS = set(list(CAP_UNIT_MAP.keys()) + list(CAP_UNIT_MAP.values()))


# here's where the magic happens
def calcola_interessi(
        capitale: float,            # initial capital
        dal: (datetime.date, str),  # from when
        al: (datetime.date, str),   # to when
        capitalizzazione: int = 0,  # how often to compound; no compounding by default
        cap_unit: str = "months"    # compounding unit (days/months/years); months by default
):
    # First we make sure that `from` (dal) and `to` (al) dates are datetime.date objects
    if isinstance(dal, str):
        dal = datetime.datetime.strptime(dal, "%Y-%m-%d").date()
    if isinstance(al, str):
        al = datetime.datetime.strptime(al, "%Y-%m-%d").date()

    # let's validate cap_unit
    cap_unit = CAP_UNIT_MAP.get(cap_unit, cap_unit)
    assert cap_unit in ALLOWED_CAP_UNITS, f"Unità di capitalizzazione non valida: {cap_unit}." \
                                          f"Unità ammesse: {ALLOWED_CAP_UNITS}"

    # we need this to protect our script from little fuckers
    # that might ask to calculate 70 years of interest with 1-day compounding
    # this would crash our machines
    if cap_unit == "days":
        assert capitalizzazione >= 30, f"La capitalizzazione non può essere inferiore a un mese"

    interessi_parziali = []     # we initialise the partial interest list (from, to, partial interest)
    interessi_totali = 0.0      # we initialise the total interest sum

    # let's make sure that the `from` value is not earlier than the first date on our table
    assert (dal >= TABELLA[0][0]), f"Data minima ammessa: {TABELLA[0][0].isoformat()}"

    # if the user wants to have compounding, we need to use recursion
    if capitalizzazione > 0:
        # here we use the dateutil library and a dict trick to get automagically the correct
        # time delta regardless of the user's compounding unit preference
        new_dal, new_al = dal, dal + relativedelta(**{cap_unit: capitalizzazione})
        new_al = min(new_al, al)  # if the `to` value is after the current time range we set it to the latter
        while True:
            # YAY! recursion magic!
            # we call the same function with the compounding-narrowed time range
            # but we call it without compounding
            # (compounding must only happen in the first call of this function)
            res = calcola_interessi(capitale, new_dal, new_al)
            # we add/append the results to the initialised variables
            capitale += res["interessi_totali"]
            interessi_totali += res["interessi_totali"]
            interessi_parziali.extend(res["interessi_parziali"])
            # we set the new `from` to the previous `to` + 1 day
            new_dal = new_al + relativedelta(days=1)
            # we set the new `to` to the new `from` + compounding time delta
            new_al = new_dal + relativedelta(**{cap_unit: capitalizzazione})
            # if the new `from` is later than the original `to` value
            # it means we finished, so we can break the while loop and
            # return the results
            if new_dal > al:
                break
            new_al = min(new_al, al)  # if the new `to` is later than the original, the latter prevails
        # we can return the result
        return dict(interessi_totali=round(interessi_totali, 2), interessi_parziali=interessi_parziali)

    # this is where the calculation happens
    for _dal, _al, saggio in TABELLA:
        # we iter through the tables, unpacking it in `from`, `to`, `interest rate`
        _al = _al or al     # `to` might be None, because it's ongoing. In that case we get the user input
        _al = min(_al, al)  # we have to take into account the interest rate of the given range
        if al < _dal:
            # if the `to` is later than the `from`, we finished our calculation and can break the loop
            break
        if dal > _al:
            # if the user's `from` is later than the current time range `from`, we can skip it
            continue
        _dal = max(_dal, dal)  # we need to take the later value from the user input and the time range
        td = _al - _dal     # calculate time delta in days
        giorni_parziali = td.days
        interessi = round(capitale * saggio * giorni_parziali / 36500, 2)  # apply the formula to get the interests
        # we append the partial range result to our list
        interessi_parziali.append(dict(dal=_dal, al=_al, saggio=saggio, giorni=giorni_parziali, interessi=interessi))
        interessi_totali += interessi  # self-explanatory
    return dict(interessi_totali=round(interessi_totali, 2), interessi_parziali=interessi_parziali)


if __name__ == '__main__':
    _res = calcola_interessi(1000, "1970-01-01", datetime.date.today(),
                            capitalizzazione=3, cap_unit="mesi")
    for __dal, __al, __saggio, __giorni, __interessi in _res["interessi_parziali"]:
        print(
            f"dal {__dal.strftime('%d-%m-%Y')} al {__al.strftime('%d-%m-%Y')}: {__saggio}%, {__giorni} giorni, interessi: {__interessi}")
    print(_res["interessi_totali"])
