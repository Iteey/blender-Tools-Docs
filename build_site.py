#!/usr/bin/env python3
"""Build the bilingual UE5 Tools documentation for GitHub Pages.

Run: python build_site.py
Requires Python 3.10+ and mistune >= 3.
HTML output: docs/ (select /docs or use the included Pages workflow).
"""
from pathlib import Path
from html import escape
import json, re
import mistune

ROOT=Path(__file__).resolve().parent
CONTENT=ROOT/'content'; OUT=ROOT/'docs'
MANIFEST=json.loads((CONTENT/'manifest.json').read_text(encoding='utf8'))
DATA={p.stem:json.loads(p.read_text(encoding='utf8')) for p in CONTENT.glob('*.json') if p.stem!='manifest'}
assert len(DATA)==36
MARKDOWN=mistune.create_markdown(escape=True, plugins=['table','strikethrough'])

I18N={
'ru': {
 'home':'Главная','checks':'Проверки','all':'Все проверки','search':'Поиск проверок…','title':'Документация UE5 Tools','subtitle':'Подготовка игровых моделей к экспорту в Unreal Engine 5',
 'hero':'Каждая проверка — простыми словами','lead':'Что обнаруживает аддон, почему это важно для UE5 и как исправить проблему. 36 проверок, понятные инструкции и иллюстрации.',
 'start':'Смотреть проверки','version':'Основано на коде UE5 Tools v0.4.2','lang':'English','language':'Язык','theme':'Тема','mode':'Режим','priority':'Серьёзность','element':'Выделяемый элемент',
 'quick':'Quick + Advanced','advanced':'Только Advanced','ERROR':'Ошибка','WARN':'Предупреждение','INFO':'Информация',
 'OBJECT':'Объект','FACE':'Грани','EDGE':'Рёбра','VERT':'Вершины','categories':'Категории проверок',
 'read':'Подробнее','contents':'В этой статье','warn':'Не каждое предупреждение означает ошибку. Учитывай назначение ассета и требования проекта.',
 'note':'Документация описывает поведение версии v0.4.2, а не гарантирует корректность экспорта или производительность в UE5.',
 'quicktitle':'Quick vs Advanced','quicktext':'Quick запускает основные проверки. Advanced добавляет дорогие UV-проверки, поиск близких вершин, Texel Density, Pivot и Lightmap. Некоторые проверки могут завершиться SKIP, если данные отсутствуют или превышен безопасный лимит.',
 'status':'Статусы: PASS — всё проверено; WARN/ERROR — обнаружены потенциальные проблемы; INFO — подсказка; SKIP — не проверено; NA — не применимо.',
 'homefooter':'Открывай отдельную страницу проверки через меню или поиск. Примеры схематические, а не скриншоты реального анализа.',
 'noresults':'Ничего не найдено','view':'Все категории','tip':'Инструкция в Blender: нажми на название обнаруженной проблемы, чтобы выделить соответствующие элементы; исправления выполняются вручную.',
 'disclaimer':'Не путай рекомендации Nanite/LOD с измерениями производительности: решение нужно проверять в Unreal Engine.',
 'next':'Следующая','previous':'Предыдущая','modehint':'Quick запускается также в Advanced.',
 },
'en': {
 'home':'Home','checks':'Checks','all':'All checks','search':'Search checks…','title':'UE5 Tools Documentation','subtitle':'Prepare game-ready assets for Unreal Engine 5',
 'hero':'Every check, clearly explained','lead':'What the add-on detects, why it matters for UE5, and how to fix it. 36 checks with practical guidance and diagrams.',
 'start':'Browse checks','version':'Based on UE5 Tools v0.4.2 source','lang':'Русский','language':'Language','theme':'Theme','mode':'Mode','priority':'Severity','element':'Selects',
 'quick':'Quick + Advanced','advanced':'Advanced only','ERROR':'Error','WARN':'Warning','INFO':'Info',
 'OBJECT':'Object','FACE':'Faces','EDGE':'Edges','VERT':'Vertices','categories':'Check categories',
 'read':'Read guide','contents':'On this page','warn':'Not every warning indicates an error. Consider the asset purpose and project requirements.',
 'note':'The documentation describes v0.4.2 behavior; it does not guarantee correct export or UE5 performance.',
 'quicktitle':'Quick vs Advanced','quicktext':'Quick runs core checks. Advanced adds bounded UV analysis, close-vertex detection, Texel Density, Pivot, and Lightmap. A check may report SKIP if required data is absent or a safety limit is reached.',
 'status':'Status meanings: PASS — checked; WARN/ERROR — potential issue found; INFO — advisory; SKIP — not checked; NA — not applicable.',
 'homefooter':'Open any check from navigation or search. Diagrams are illustrative, not captured scan results.',
 'noresults':'No matches','view':'All categories','tip':'In Blender, click the detected issue label to select the affected elements. The scan never fixes the mesh automatically.',
 'disclaimer':'Do not confuse Nanite/LOD advice with a performance benchmark: compare in Unreal Engine.',
 'next':'Next','previous':'Previous','modehint':'Quick checks are also included in Advanced.',
 },
}

SLUGS={key:key.replace('_','-') for key in DATA}

# Source pages kept in GitHub-editable Markdown.
def ensure_markdown_sources():
 for lang in ('ru','en'):
  pdir=CONTENT/lang/'checks';pdir.mkdir(parents=True,exist_ok=True)
  for key,d in DATA.items():
   file=pdir/f'{SLUGS[key]}.md'
   if file.exists():continue
   info=d[lang]
   names=(('Что проверяет','Как работает проверка','Почему важно для UE5','Как исправить','Важные нюансы')
          if lang=='ru' else ('What it checks','How detection works','Why it matters for UE5','How to fix','Important exceptions'))
   sections=[(names[0],info['what']),(names[1],info['mechanism']),(names[2],info['why']),(names[3],info['fix'])]
   if info['exceptions']:sections.append((names[4],info['exceptions']))
   body='# '+info['title']+'\n\n'+ '\n\n'.join(f'## {title}\n\n{text}' for title,text in sections)+'\n'
   file.write_text(body,encoding='utf8')


def rel_root(kind):return '' if kind=='home' else '../'
def asset_root(kind):return '../' if kind=='home' else '../../'

def link(lang,key):return f'checks/{SLUGS[key]}.html'

def nav_links(lang,kind,current):
 r=rel_root(kind);t=I18N[lang]
 sections=[f'<a href="{r}index.html" class="nav-home {"selected" if kind=="home" else ""}">⌂ &nbsp;{escape(t["home"])}</a>',
 f'<a class="nav-home" href="{r}guides/getting-started.html">◈ &nbsp;{"Как пользоваться" if lang=="ru" else "Getting started"}</a>',
 f'<a class="nav-home" href="{r}guides/nanite-vs-lod.html">△ &nbsp;Nanite / LOD Advisor</a>']
 for c in MANIFEST['categories']:
  title=c[lang];active=(current==c['key'] if kind=='category' else DATA.get(current,{}).get('category')==c['key'])
  sections.append(f'<div class="nav-category"><a class="nav-heading {"active" if active else ""}" href="{r}categories/{c["key"]}.html">{escape(title)}<span>{len(c["keys"])}</span></a>')
  for key in c['keys']:
   d=DATA[key]
   href=r+f'checks/{SLUGS[key]}.html'
   current_class='selected' if kind=='check' and current==key else ''
   s=escape((d['label']+' '+d['ru']['what']+' '+d['en']['what']).lower(),quote=True)
   sections.append(f'<a class="nav-check {current_class}" href="{href}" data-search="{s}">{escape(d["label"])}</a>')
  sections.append('</div>')
 return '\n'.join(sections)

def switch_lang(lang,kind,current):
 other='en' if lang=='ru' else 'ru'
 rr='../'+other+'/' if kind=='home' else '../../'+other+'/'
 if kind=='guide':rr+=f'guides/{current}.html'
 elif kind=='check':rr+=f'checks/{SLUGS[current]}.html'
 elif kind=='category':rr+=f'categories/{current}.html'
 else:rr+='index.html'
 return rr

def page(lang,kind,current,page_title,body,description):
 t=I18N[lang]; r=rel_root(kind);ar=asset_root(kind);other=switch_lang(lang,kind,current)
 nav=nav_links(lang,kind,current)
 title_esc=escape(page_title)
 html=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(description[:160],quote=True)}"><meta name="color-scheme" content="dark light">
<title>{title_esc} · UE5 Tools</title><link rel="stylesheet" href="{ar}assets/style.css">
<link rel="icon" type="image/svg+xml" href="{ar}assets/logo.svg"></head>
<body data-language="{lang}">
<div class="mobile-overlay" id="overlay"></div>
<aside class="sidebar" id="sidebar"><a class="brand" href="{r}index.html"><span class="brand-mark">U<span>5</span></span><span><strong>UE5 Tools</strong><small>Documentation · v0.4.2</small></span></a>
<div class="sidebar-controls"><label class="search-field"><span class="magnifier">⌕</span><input type="search" id="search" autocomplete="off" placeholder="{escape(t['search'])}" aria-label="{escape(t['search'])}"></label><div id="search-empty" class="search-empty" hidden>{t['noresults']}</div></div>
<nav class="navigation" aria-label="Documentation navigation">{nav}</nav>
<div class="sidebar-foot"><span class="live-dot"></span> {escape(t['version'])}</div></aside>
<div class="app-shell"><header class="topbar"><button class="mobile-menu" id="menu-button" aria-label="Menu">☰</button>
<a class="topbar-home" href="{r}index.html">UE5 Tools <span>/ Docs</span></a><div class="top-actions">
<a class="action" href="{other}" lang="{'en' if lang=='ru' else 'ru'}" title="{escape(t['language'])}">◎ {t['lang']}</a>
<button id="theme-button" class="action" title="{escape(t['theme'])}" aria-label="{escape(t['theme'])}">◐</button>
</div></header>
<main class="content">{body}</main><footer class="page-footer"><span>{escape(t['version'])}</span><span>© UE5 Tools · Community documentation</span></footer></div>
<script defer src="{ar}assets/app.js"></script></body></html>'''
 return html

def article_page(lang,key):
 d=DATA[key];t=I18N[lang];name=d['label']
 c=next(c for c in MANIFEST['categories'] if c['key']==d['category'])
 src=(CONTENT/lang/'checks'/f'{SLUGS[key]}.md').read_text(encoding='utf8')
 rendered=MARKDOWN(src)
 # Source markdown content has its own H1; use the page heading above instead.
 rendered=re.sub(r'^\s*<h1>.*?</h1>\s*','',rendered,count=1,flags=re.S)
 content=f'''<div class="breadcrumbs"><a href="../index.html">{escape(t['home'])}</a><span>/</span><a href="../categories/{c['key']}.html">{escape(c[lang])}</a><span>/</span><span>{escape(name)}</span></div>
<div class="article-head"><div class="eyebrow">CHECK / {escape(key.upper())}</div><h1>{escape(name)}</h1>
<p class="subline">{escape(d[lang]['what'])}</p>
<div class="meta"><span class="pill {'pill-red' if d['severity']=='ERROR' else 'pill-amber' if d['severity']=='WARN' else 'pill-neutral'}">{escape(t[d['severity']])}</span>
<span class="pill">{escape(t['advanced'] if d['mode']=='advanced' else t['quick'])}</span><span class="pill">{escape(t[d['kind']])}</span></div></div>
<figure class="diagram"><img src="../../assets/diagrams/{escape(d['illustration'])}" alt="{escape(name,quote=True)}" loading="lazy"/><figcaption>{'Схема для объяснения концепции; не скриншот найденной ошибки.' if lang=='ru' else 'Concept illustration, not a screenshot of a detected issue.'}</figcaption></figure>
<div class="article-grid"><article class="prose">{rendered}
<div class="callout"><strong>✦ {'Как использовать результат' if lang=='ru' else 'How to use this result'}</strong><p>{escape(t['tip'])}</p></div>
</article><aside class="article-aside"><div class="aside-sticky"><h3>{escape(t['contents'])}</h3>
<a href="#what">{'Что проверяет' if lang=='ru' else 'What it checks'}</a>
<a href="#mechanism">{'Как работает проверка' if lang=='ru' else 'How detection works'}</a>
<a href="#why">{'Почему важно' if lang=='ru' else 'Why it matters'}</a>
<a href="#fix">{'Как исправить' if lang=='ru' else 'How to fix'}</a>
<p>{escape(t['warn'])}</p></div></aside></div>
<div class="source-note">{escape(t['note'])}</div>'''
 # Stable heading anchors independent of languages, applied in order to h2 tags.
 ids=['what','mechanism','why','fix','exceptions']
 idx=0
 def add_id(m):
  nonlocal idx
  rid=ids[idx] if idx<len(ids) else 'extra';idx+=1
  return f'<h2 id="{rid}">{m.group(1)}</h2>'
 content=re.sub(r'<h2>(.*?)</h2>',add_id,content)
 keys=[k for c in MANIFEST['categories'] for k in c['keys']]
 pos=keys.index(key)
 links=[]
 if pos>0:links.append(f'<a class="pager-link" href="{SLUGS[keys[pos-1]]}.html"><small>← {t["previous"]}</small><strong>{escape(DATA[keys[pos-1]]["label"])}</strong></a>')
 if pos<len(keys)-1:links.append(f'<a class="pager-link right" href="{SLUGS[keys[pos+1]]}.html"><small>{t["next"]} →</small><strong>{escape(DATA[keys[pos+1]]["label"])}</strong></a>')
 content+='<div class="pager">'+''.join(links)+'</div>'
 return page(lang,'check',key,name,content,d[lang]['what'])

def category_page(lang,c):
 t=I18N[lang];cards=[]
 for key in c['keys']:
  d=DATA[key]
  badge='pill-red' if d['severity']=='ERROR' else 'pill-amber' if d['severity']=='WARN' else 'pill-neutral'
  cards.append(f'''<a class="check-card" href="../checks/{SLUGS[key]}.html"><div class="check-card-inner"><span class="pill {badge}">{t[d['severity']]}</span><span class="mode-label">{t['advanced'] if d['mode']=='advanced' else t['quick']}</span></div>
<h3>{escape(d['label'])}</h3><p>{escape(d[lang]['what'])}</p><span class="read-more">{t['read']} →</span></a>''')
 body=f'''<div class="breadcrumbs"><a href="../index.html">{t['home']}</a><span>/</span>{t['checks']}</div>
<div class="article-head"><div class="eyebrow">CATEGORY / {c['key'].upper()}</div><h1>{escape(c[lang])}</h1>
<p class="subline">{len(c['keys'])} {'проверок' if lang=='ru' else 'checks'} · {t['version']}</p></div><div class="check-grid">{''.join(cards)}</div>'''
 return page(lang,'category',c['key'],c[lang],body,c[lang])

def home_page(lang):
 t=I18N[lang]
 cats=[]
 for c in MANIFEST['categories']:
  cats.append(f'''<a class="category-card" href="categories/{c['key']}.html"><span class="category-symbol">{ {'geometry':'◇','transform':'⊞','normals':'↗','uv':'▦','materials':'◈','textures':'▧','polycount':'△','texel':'▩','pivot':'⊙','lightmap':'◫'}[c['key']] }</span><strong>{escape(c[lang])}</strong><small>{len(c['keys'])} {'проверок' if lang=='ru' else 'checks'}</small><span class="category-arrow">↗</span></a>''')
 body=f'''<section class="hero"><div class="hero-lines"></div><div class="eyebrow"><span class="live-dot"></span> UE5 TOOLS / ASSET QUALITY</div>
<h1>{t['hero']}</h1><p>{t['lead']}</p><a href="#categories" class="primary-link">{t['start']} <span>↗</span></a>
<div class="hero-stats"><div><strong>36</strong><span>{t['checks']}</span></div><div><strong>10</strong><span>{t['categories']}</span></div><div><strong>RU / EN</strong><span>{t['language']}</span></div></div></section>
<div class="section-top" id="categories"><div><div class="eyebrow">REFERENCE LIBRARY</div><h2>{t['categories']}</h2></div></div>
<div class="category-grid">{''.join(cats)}</div>
<section class="home-info"><div><div class="eyebrow">WORKFLOW</div><h2>{t['quicktitle']}</h2><p>{t['quicktext']}</p><p>{t['status']}</p></div>
<div class="visual-tile"><img src="../assets/diagrams/normals.svg" alt="Normals explanation diagram" loading="lazy" /></div></section>
<div class="source-note">{escape(t['homefooter'])} {escape(t['note'])}</div>'''
 return page(lang,'home',None,t['title'],body,t['lead'])


def guide_page(lang,slug):
 t=I18N[lang]
 source=(CONTENT/lang/'guides'/f'{slug}.md').read_text(encoding='utf8')
 rendered=MARKDOWN(source)
 heading=BeautifulTitle(source)
 rendered=re.sub(r'^\s*<h1>.*?</h1>\s*','',rendered,count=1,flags=re.S)
 body=f'<div class="breadcrumbs"><a href="../index.html">{t["home"]}</a><span>/</span>{"Руководства" if lang=="ru" else "Guides"}</div><div class="article-head"><div class="eyebrow">GUIDE / UE5 TOOLS</div><h1>{escape(heading)}</h1></div><figure class="diagram"><img src="../../assets/diagrams/{"lod.svg" if slug=="nanite-vs-lod" else "topology.svg"}" alt="Guide illustration"></figure><article class="prose guide-article">{rendered}</article><div class="source-note">{t["note"]}</div>'
 return page(lang,'guide',slug,heading,body,heading)

def BeautifulTitle(source):
 return source.splitlines()[0].removeprefix('# ').strip()

def main():
 ensure_markdown_sources()
 for lang in ('ru','en'):
  (OUT/lang/'checks').mkdir(parents=True,exist_ok=True)
  (OUT/lang/'categories').mkdir(parents=True,exist_ok=True)
  (OUT/lang/'guides').mkdir(parents=True,exist_ok=True)
  for slug in ('getting-started','nanite-vs-lod'):
   (OUT/lang/'guides'/f'{slug}.html').write_text(guide_page(lang,slug),encoding='utf8')
  (OUT/lang/'index.html').write_text(home_page(lang),encoding='utf8')
  for c in MANIFEST['categories']:
   (OUT/lang/'categories'/f'{c["key"]}.html').write_text(category_page(lang,c),encoding='utf8')
  for key in DATA:
   (OUT/lang/'checks'/f'{SLUGS[key]}.html').write_text(article_page(lang,key),encoding='utf8')
 (OUT/'index.html').write_text('''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=ru/index.html"><title>UE5 Tools Docs</title></head><body><p><a href="ru/index.html">Русский</a> · <a href="en/index.html">English</a></p></body></html>''',encoding='utf8')
 (OUT/'.nojekyll').touch()
 print('Built',len(list(OUT.rglob('*.html'))),'HTML pages')

if __name__=='__main__':main()
