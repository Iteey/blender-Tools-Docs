"""Fast, dependency-free validation for a generated GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

DOC=Path(__file__).resolve().parent/'docs'
HTML=list(DOC.rglob('*.html'))
assert len(HTML)==99,f'Expected 99 HTML pages; got {len(HTML)}'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[];self.ids=set();self.h1s=0
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag in ('a','link') and attrs.get('href'):self.links.append(attrs['href'])
        if tag in ('img','script') and attrs.get('src'):self.links.append(attrs['src'])
        if attrs.get('id'):self.ids.add(attrs['id'])
        if tag=='h1':self.h1s+=1

cache={}
def scan(path):
    if path not in cache:
        p=Links();p.feed(path.read_text(encoding='utf8'));cache[path]=p
    return cache[path]

errors=[]
for file in HTML:
    dom=scan(file)
    if file.name!='index.html' or file.parent!=DOC:
        if dom.h1s!=1:errors.append((file,'expected exactly one H1'))
    for href in dom.links:
        if href.startswith(('https:','http:','mailto:','data:')):continue
        parsed=urlsplit(href)
        dest=(file.parent/unquote(parsed.path)).resolve() if parsed.path else file.resolve()
        if not dest.is_file():errors.append((file,href,'missing resource'))
        elif parsed.fragment and dest.suffix=='.html' and unquote(parsed.fragment) not in scan(dest).ids:
            errors.append((file,href,'missing anchor'))
for lang in ('ru','en'):
    checks=list((DOC/lang/'checks').glob('*.html'))
    cats=list((DOC/lang/'categories').glob('*.html'))
    guides=list((DOC/lang/'guides').glob('*.html'))
    assert len(checks)==36,(lang,'checks',len(checks))
    assert len(cats)==10,(lang,'categories',len(cats))
    assert len(guides)==2,(lang,'guides',len(guides))
    for p in checks:
        if not {'what','mechanism','why','fix'}.issubset(scan(p).ids):errors.append((p,'missing explanatory sections'))
if errors:
    for msg in errors[:50]:print('FAIL',*[str(x) for x in msg])
    sys.exit(f'{len(errors)} site validation errors')
diag=len(list((DOC/'assets'/'diagrams').glob('*.svg')))
print(f'PASS: {len(HTML)} pages, 36 checks per language, {diag} SVG diagrams, all local links and headings valid')
