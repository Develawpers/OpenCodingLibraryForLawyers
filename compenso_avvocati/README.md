This piece of software is borrowed from Law Engineering System's `lawyertools`.

It is not meant to be used as a `CLI` but to be integrated into an `API`.


## how this works

* in `data/tabelle.py` a `dict` holds the parameters specified by the DECRETO 10 marzo 2014, n 55, as amended in 2018
    - the dict holds the base parameters for each phase and corresponding value
    - the dict holds the special rules for increasing and decreasing the compensation
    
* in `compenso_avvocati.py` the function `calcola_compenso` will perform the calculations based on the provided input
    - args:
        - `pkey`: `str` --> what parameters to use (as of now, only `"p2018"` is available)
        - `competenza`: `str` --> what court is the case in front of
        - `valore`: `int` --> the value of the controversy
        - `fasi`: `List(Tuple(str, float))` --> a list consisting of `[("name of the phase", <percentage of increase/decrease>), ...]`
        - `cpa`: `bool` --> include lawyer's social sec
        - `iva`: `bool` --> include VAT
        - `**kwargs`: keyword arguments for special increase/decrease
    
* the input arguments are validated against the chosen set of rules
* the calculations are performed
* a dict with a structured result is returned