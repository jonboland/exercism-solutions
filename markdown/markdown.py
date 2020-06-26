import re


U_LIST = r"(<li>.*</li>)"
LIST_ITEMS = r"^\* (.*)"
EMPHASIS = "_(.*)_"
STRONG = "__(.*)__"
HEADING_TYPES = ["#" * num for num in range(1, 7)]


def parse(text):
    for heading_type in HEADING_TYPES:
        n = len(heading_type)
        headings = f"^{heading_type} (.*)"
        text = re.sub(headings, fr"<h{n}>\1</h{n}>", text, flags=re.M)
    text = re.sub(STRONG, r"<strong>\1</strong>", text)
    text = re.sub(EMPHASIS, r"<em>\1</em>", text)
    text = re.sub(LIST_ITEMS, r"<li>\1</li>", text, flags=re.M)
    text = re.sub(U_LIST, r"<ul>\1</ul>", text, flags=re.S).splitlines()
    text = [x if "<h" in x or "<l" in x else f"<p>{x}</p>" for x in text]
    return "".join(text)
