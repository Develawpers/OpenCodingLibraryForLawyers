"""
Super basic Legal Reference Parser.

Usage: python main.py <filepath.html>

Q: can this be done with *.docx document?
A: sure, but it's a pain in the ass and ain't nobody got time for that

Q: can this work also with paragraphs, case law and what not?
A: sure, just add whatever pattern you want and adapt the resolver

Q: can this work with very weird and more complex references?
A: technically yes, but good luck with that.

Q: I need to parse a shitload of documents/webpages professionally and very precisely, how can I do this?
A: contact me: b.distefano@lawengineeringsystems.com
"""


import re


PATTERN_CODICI = {
    "cost": r"(?P<cost>(costituzione|cost\.))",
    "cpc": r"(?P<cpc>(codice di procedura civile|cod\. proc\. civ\.|c\.p\.c\.))",
    "cpp": r"(?P<cpc>(codice di procedura penale|cod\. proc\. pen\.|c\.p\.p\.))",
    "cc": r"(?P<cc>(codice civile|cod\. civ\.|c\.c\.))",
    "cp": r"(?P<cp>(codice penale|cod\. pen\.|c\.p\.))",
}

PATTERN_ARTICOLO = r"(?P<art>(articolo|art\.) (?P<num>\d{1,4}([ -]?(?P<numerale>(bis|ter|quater)))?))"


ALL_PATTERNS = {k: PATTERN_ARTICOLO + "?( del(la)?)? ?" + v for k, v in PATTERN_CODICI.items()}

BASE_URL = "https://www.normattiva.it/uri-res/N2Ls?"

URN_NIR = {
    "cost": "urn:nir:stato:costituzione",
    "cpc": "urn:nir:stato:regio.decreto:1940-10-28;1443",
    "cpp": "urn:nir:stato:decreto.del.presidente.della.repubblica:1988-09-22;447",
    "cc": "urn:nir:stato:regio.decreto:1942-03-16;262",
    "cp": "urn:nir:stato:regio.decreto:1930-10-19;1398"
}


# WARNING: Normattiva urn links work whenever the fuck they want, don't trust them


def get_matches(text):
    matches = []
    for k, v in ALL_PATTERNS.items():
        matches.extend(list(re.finditer(v, text, re.IGNORECASE)))
    return purge_overlaps(matches)


def purge_overlaps(matches):
    matches.sort(key=lambda x: x.start())
    purged = []
    if len(matches) > 1:
        purged.append(matches[0])
        for m in matches[1:]:
            if m.start() >= purged[-1].end():
                purged.append(m)
            elif m.end() >= purged[-1].end():
                m_len = m.end() - m.start()
                last_len = purged[-1].end() - purged[-1].start()
                if m_len > last_len:
                    purged.pop()
                    purged.append(m)
    else:
        return matches
    return purged


def resolve_matches(*matches):
    references = []  # ((offset start, offset end), url)
    for m in matches:
        num = ""
        groupdict = m.groupdict()
        num += groupdict.get("num") or ""
        num += groupdict.get("numerale") or ""
        if num:
            num = f"~art{num}"
        for k in PATTERN_CODICI.keys():
            if groupdict.get(k) is not None:
                references.append((m.span(), BASE_URL + URN_NIR[k] + num))
                break
        else:
            raise Exception(f"Cannot resolve codice: {m.group()}")
    references.sort(key=lambda x: x[0][0])
    return references


def hyperlinker(filepath):
    assert filepath.endswith(".html"), "This only works with html files for now"
    with open(filepath, "r") as f:
        filestring = f.read()
    matches = get_matches(filestring)
    references = resolve_matches(*matches)
    newstring = ""
    prev_start = 0
    for (s, e), url in references:
        newstring += filestring[prev_start:s]
        newstring += f"<a href=\"{url}\">{filestring[s:e]}</a>"
        prev_start = e
    newstring += filestring[prev_start:]
    with open(filepath.replace(".html", ".lrp.html"), "w") as f:
        f.write(newstring)


if __name__ == '__main__':
    hyperlinker("demo.html")
