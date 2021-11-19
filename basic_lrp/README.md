# Basic Legal Reference Parser

## What's this

This is just a super basic demo of what you can do with Regular Expressions (regex)
to find legal references in a text using Python's re library.

This piece of code will take a HTML file as an input, find (some) legal references
and create hyperlinks to the corresponding legal resource on www.normattiva.it

For a more in-depth understanding of regex checkout [this webpage](https://www.regular-expressions.info/) and
[this interactive tool](https://regex101.com/) to test them out.

## Workflow

This is how it works:

- open the HTML file
- find the matches of the references
- resolve the matches into urls
- add `<a>` tags to the HTML file
- write the file

## the basics of Regular Expressions and the re library

Find a quickstart guide [here](https://www.regular-expressions.info/quickstart.html)

Re's library documentation: https://docs.python.org/3/library/re.html

```shell
>>> python
>>> import re
>>> pattern = r"(?P<art>art(icolo|\.)) (?P<num>\d+)"
>>> match = re.search(pattern, "come previsto dall'articolo 10", re.I)
>>> match
<re.Match object; span=(19, 26), match='art. 10'>
>>> match.start()
19
>>> match.end()
26
>>> match.group()
'art. 10'
>>> match.group("art")
'art.'
>>> match.group("num")
'10'
>>> match.groupdict()
{'art': 'articolo', 'num': '10'}
>>> for match in re.finditer(pattern, "blah blah art. 10, blah blah articolo 256, blah blah art. 40", re.I):
...     print(match)
... 
<re.Match object; span=(10, 17), match='art. 10'>
<re.Match object; span=(29, 41), match='articolo 256'>
<re.Match object; span=(53, 60), match='art. 40'>
```


## In depth:

First thigs first

```python
import re
```

### setting up our patterns

We're going to look for patterns such as `art. 844 del codice civile`. We can build this in a modular fashion.

First we crete the general patterns for the `codici` we want to match,
making sure we use named groups `(?P<name>pattern)` and use those names as keys of our `dict`.

```python
PATTERN_CODICI = {
    "cost": r"(?P<cost>(costituzione|cost\.))",
    "cpc": r"(?P<cpc>(codice di procedura civile|cod\. proc\. civ\.|c\.p\.c\.))",
    "cpp": r"(?P<cpc>(codice di procedura penale|cod\. proc\. pen\.|c\.p\.p\.))",
    "cc": r"(?P<cc>(codice civile|cod\. civ\.|c\.c\.))",
    "cp": r"(?P<cp>(codice penale|cod\. pen\.|c\.p\.))",
}
```

Then we write the pattern for `<articolo> <numero>`

```python
PATTERN_ARTICOLO = r"(?P<art>(articolo|art\.) (?P<num>\d{1,4}([ -]?(?P<numerale>(bis|ter|quater)))?))"
```

Then we combine everything dynamically

```python
ALL_PATTERNS = {k: PATTERN_ARTICOLO + "?( del(la)?)? ?" + v for k, v in PATTERN_CODICI.items()}
```

Now we need a BASE_URL and normattiva's `URNs` for our `codici`.
You can find normattiva's documentation on URNs [here (in Italian)](https://www.normattiva.it/staticPage/utilita#1)

```python
BASE_URL = "https://www.normattiva.it/uri-res/N2Ls?"

URN_NIR = {
    "cost": "urn:nir:stato:costituzione",
    "cpc": "urn:nir:stato:regio.decreto:1940-10-28;1443",
    "cpp": "urn:nir:stato:decreto.del.presidente.della.repubblica:1988-09-22;447",
    "cc": "urn:nir:stato:regio.decreto:1942-03-16;262",
    "cp": "urn:nir:stato:regio.decreto:1930-10-19;1398"
}
```

### building the code


This is our main function. First thing we read the file into a string.

```python
def hyperlinker(filepath):
    assert filepath.endswith(".html"), "This only works with html files for now"
    with open(filepath, "r") as f:
        filestring = f.read()
    ...
```

Now we need to get those matches:
```python
def hyperlinker(filepath):
    assert filepath.endswith(".html"), "This only works with html files for now"
        with open(filepath, "r") as f:
            filestring = f.read()
    matches = get_matches(filestring)
    ...
```

In our `get_matches()` function we simply iterate over all of our patterns and use `re.finditer()` with them:

```python
def get_matches(text):
    matches = []
    for k, v in ALL_PATTERNS.items():
        matches.extend(list(re.finditer(v, text, re.IGNORECASE)))
    return purge_overlaps(matches)
```

Since we use many different patterns, we might get overlaps.
E.g. `art. 40 c.p.c.` will match both `art. 40 c.p.` AND `art. 40 c.p.c.`.
Let's purge those nasty bastards.

```python
def purge_overlaps(matches):
    # first we sort them by the their start offset
    matches.sort(key=lambda x: x.start())
    purged = []  # we create a new list
    if len(matches) > 1:  # we only need to do this if we have more than 1 match
        purged.append(matches[0])  # we append the first one to the new list
        for m in matches[1:]:  # and we iter the old one starting from element [1]
            # if the match starts after the end of the previous one, it does not overlap
            if m.start() >= purged[-1].end():
                purged.append(m)  # we can safely append it to the new list
            elif m.end() >= purged[-1].end():  # but if it doesn't and partially overlap...
                # we'll make the longest match prevail
                m_len = m.end() - m.start()
                last_len = purged[-1].end() - purged[-1].start()
                if m_len > last_len:
                    purged.pop()
                    purged.append(m)
    else:
        return matches
    return purged
```

Now we have clean and sexy matches. Let's resolve them into urls.

```python
def hyperlinker(filepath):
    assert filepath.endswith(".html"), "This only works with html files for now"
    with open(filepath, "r") as f:
        filestring = f.read()
    matches = get_matches(filestring)
    references = resolve_matches(*matches)
    ...
```

We'll need to create a list of `references`. A `reference` is going to be
a `tuple` of two elements: another `tuple` containing `start` and `end` offset,
and a `string` that represents the `url`, like in the comment below

```python
def resolve_matches(*matches):
    references = []  # ((offset start, offset end), url)
    for m in matches:
        num = ""
        groupdict = m.groupdict()
        num += groupdict.get("num") or ""
        num += groupdict.get("numerale") or ""
        if num:
            num = f"~art{num}"
        # this is a for-else loop. More info here: https://www.pythontutorial.net/python-basics/python-for-else/
        for k in PATTERN_CODICI.keys():
            if groupdict.get(k) is not None:
                references.append((m.span(), BASE_URL + URN_NIR[k] + num))
                break
        else:
            raise Exception(f"Cannot resolve codice: {m.group()}")
    references.sort(key=lambda x: x[0][0])
    return references
```

Now that we have the references and their offset in the text, we can create the `<a>` tags:

```python
def hyperlinker(filepath):
    ...
    newstring = ""  # we start with an empty string
    prev_start = 0  # declare a prev_start to 0
    for (s, e), url in references:  # iter through the references
        newstring += filestring[prev_start:s]  # add a piece of string slicing from the previous start to the current one
        newstring += f"<a href=\"{url}\">{filestring[s:e]}</a>"  # create an <a> tag with the URL
        prev_start = e  # set the prev_start to the end offset of the current url object
    newstring += filestring[prev_start:]  # finish up building the string with the remaining chars
    # now we write the file
    with open(filepath.replace(".html", ".lrp.html"), "w") as f:
        f.write(newstring)
```

...aaaand our main statement:


```python
if __name__ == '__main__':
    hyperlinker("demo.html")
```