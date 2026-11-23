"""Build the local, dependency-free icon sprite from attributed original SVG assets."""
from pathlib import Path
import re
from xml.etree import ElementTree as ET

root=Path(__file__).resolve().parent.parent
folder=root/'assets/icons'
symbols=[]
ET.register_namespace('', 'http://www.w3.org/2000/svg')
for key in ['pin','plane','glass','mountain','wa','phone','calendar','shield','badge','people','sliders','quad','camel','dinner','tent','menu','close','chevron','next','star','ellipsis']:
 svg=ET.parse(folder/(key+'.svg')).getroot()
 if key=='camel':
  for child in list(svg):
   if child.get('d')=='M0 0h512v512H0z':svg.remove(child)
 content=''.join(ET.tostring(child,encoding='unicode') for child in svg)
 content=re.sub(r' xmlns="[^"]+"','',content)
 content=re.sub(r'fill="(?:#000(?:000)?|black|#fff(?:fff)?|white)"','fill="currentColor"',content)
 content=re.sub(r'<path ', '<path fill="currentColor" ',content) if 'fill=' not in content else content
 symbols.append('<symbol id="'+key+'" viewBox="'+svg.get('viewBox','0 0 24 24')+'">'+content+'</symbol>')
symbols.append('''<symbol id="route" viewBox="0 0 64 56"><path d="M27 33c18-15 33-7 24 6C43 52 9 48 9 40c0-5 8-8 15-8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-dasharray="4 4" stroke-linecap="round"/><svg x="9" y="1" width="28" height="34" viewBox="0 0 384 512"><use href="#pin"/></svg></symbol>''')
page=root/'index.html';html=page.read_text(encoding='utf-8')
html=re.sub(r'(<svg class="sprite"[^>]*><defs>).*?(</defs></svg>)',lambda m:m[1]+''.join(symbols)+m[2],html,count=1,flags=re.S)
html=html.replace('class="sprite" xmlns=', 'class="sprite" aria-hidden="true" xmlns=')
html=html.replace('<use href="#mountain"/></svg><b data-i18n="camp">','<use href="#tent"/></svg><b data-i18n="camp">')
html=html.replace('20261123-2','20261123-icons')
html=html.replace('<span>⌄</span>','<svg class="dropdown-chevron" aria-hidden="true"><use href="#chevron"/></svg>')
html=html.replace('data-label="menu">☰</button>','data-label="menu"><svg aria-hidden="true"><use href="#menu"/></svg></button>')
html=html.replace('data-label="close">×</button>','data-label="close"><svg aria-hidden="true"><use href="#close"/></svg></button>')
html=html.replace('<b>›</b>','<svg class="cta-chevron" aria-hidden="true"><use href="#next"/></svg>')
html=html.replace('<b>★ ★ ★</b>','<b class="brand-stars">'+''.join('<svg aria-hidden="true"><use href="#star"/></svg>' for _ in range(3))+'</b>')
html=html.replace('<div class="stars">★★★★★</div>','<div class="stars" aria-label="5/5">'+''.join('<svg aria-hidden="true"><use href="#star"/></svg>' for _ in range(5))+'</div>')
html=html.replace('<div class="stars">★★★★<span>★</span></div>','<div class="stars" aria-label="4.5/5">'+''.join('<svg aria-hidden="true"><use href="#star"/></svg>' for _ in range(4))+'<span class="half-star"><svg aria-hidden="true"><use href="#star"/></svg></span></div>')
page.write_text(html,encoding='utf-8')
js=root/'js/app.js';s=js.read_text(encoding='utf-8')
s=s.replace("['plane','pin','glass','mountain'][i]","['plane','route','glass','mountain'][i]")
s=s.replace('const icon=name=>`<svg aria-hidden="true">','const icon=name=>`<svg class="icon icon-${name}" aria-hidden="true" focusable="false">')
js.write_text(s,encoding='utf-8')
