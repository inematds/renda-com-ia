#!/usr/bin/env python3
"""Atualiza apenas os quatro diagramas do guia, preservando vídeo e traduções existentes."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,html
R=Path(__file__).resolve().parent.parent
e=lambda s:html.escape(s,quote=True)
CSS="""
.diagram{margin:30px 0;padding:28px;background:var(--bg2);border:1px solid var(--line);border-radius:16px}
.diagram figcaption{font-size:.9rem;color:var(--mut);margin-top:20px;max-width:74ch}
.diagram h3{font-size:1.25rem;line-height:1.3;margin-bottom:22px}
.role-route,.case-route{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:36px}
.role-node,.case-node{position:relative;min-width:0}
.role-node:not(:last-child):after,.case-node:not(:last-child):after{content:'→';position:absolute;right:-28px;top:22px;color:var(--amb);font-size:25px}
.role-icon{width:52px;height:52px;border-radius:50%;background:var(--card);border:1px solid var(--line);display:grid;place-items:center;color:var(--amb);margin-bottom:16px}
.diagram svg{width:28px;height:28px;display:block}
.role-node strong,.case-node strong{display:block;font:600 1.02rem/1.4 Sora,sans-serif;margin-bottom:8px}
.role-node p,.case-node p{font-size:1rem;line-height:1.55;margin:0;color:var(--txt)}
.diagram .diagram-note{margin:20px 0 0;padding-top:18px;border-top:1px solid var(--line);font-size:.95rem;color:var(--mut)}
.case-node small{display:block;color:var(--mut);font-size:.8rem;margin:8px 0 14px}
.case-node blockquote{margin:0;min-height:108px;padding:20px;background:var(--card);border:1px solid var(--line);border-radius:12px;font-size:1.08rem;line-height:1.55}
.check-strip{display:flex;flex-wrap:wrap;gap:12px 24px;padding:22px 0 0}
.check-strip span{display:flex;align-items:center;gap:8px;font-size:.93rem}
.check-strip svg{color:var(--amb);width:20px;height:20px;flex-shrink:0}
.roadline{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin:0;padding:0;list-style:none}
.roadline:before{content:'';position:absolute;top:20px;left:20px;right:20px;height:1px;background:var(--amb)}
.roadline li{position:relative;min-width:0}
.road-marker{position:relative;width:42px;height:42px;border-radius:50%;background:var(--bg2);border:2px solid var(--amb);display:grid;place-items:center;font:600 1rem Sora,sans-serif;color:var(--amb);margin-bottom:20px}
.roadline time{display:block;font-size:.84rem;color:var(--mut);margin-bottom:8px}
.roadline strong{display:block;font:600 1.1rem Sora,sans-serif;margin-bottom:12px}
.roadline p{font-size:.95rem;line-height:1.55;margin:0 0 18px}
.road-output{padding-top:14px;border-top:1px solid var(--line);font-size:.87rem;color:var(--amb)}
.road-output small{display:block;color:var(--mut);margin-bottom:5px;font-size:.76rem}
.energy-heading{margin:0 0 26px;font-size:1rem;color:var(--mut)}
.energy-row{display:grid;grid-template-columns:230px minmax(0,1fr) 90px;gap:20px;align-items:center;margin:24px 0}
.energy-row label{font-size:.95rem}
.energy-row b{font:600 1.1rem Sora,sans-serif;text-align:right;white-space:nowrap}
.energy-track{position:relative;height:34px;border-bottom:1px solid var(--line);background:var(--card)}
.energy-fill{height:100%;background:var(--amb);width:36.666667%;border-radius:3px}
.energy-range{position:absolute;left:55.833333%;right:0;height:100%;background:color-mix(in srgb,var(--amb) 22%,var(--bg2));border:2px dashed var(--amb);border-radius:3px}
.energy-scale{margin:8px 110px 0 250px;display:flex;justify-content:space-between;font-size:.8rem;color:var(--mut)}
.energy-legend{display:flex;align-items:center;gap:10px;font-size:.85rem;color:var(--mut);margin-top:22px}
.range-key{display:inline-block;width:30px;height:16px;background:color-mix(in srgb,var(--amb) 22%,var(--bg2));border:2px dashed var(--amb)}
@media(max-width:760px){
 .diagram{padding:22px;margin:24px 0}
 .role-route,.case-route{grid-template-columns:1fr;gap:38px}
 .role-node{padding-left:70px;min-height:60px}
 .role-icon{position:absolute;left:0;top:0;margin:0}
 .role-node:not(:last-child):after{content:'↓';left:17px;right:auto;top:auto;bottom:-32px}
 .case-node:not(:last-child):after{content:'↓';right:auto;left:50%;top:auto;bottom:-32px}
 .case-node blockquote{min-height:0}
 .roadline{grid-template-columns:1fr;gap:26px}
 .roadline:before{top:20px;bottom:20px;left:20px;right:auto;width:1px;height:auto}
 .roadline li{padding-left:64px}
 .road-marker{position:absolute;left:0;top:0;margin:0}
 .roadline p{margin-bottom:12px}
 .energy-row{grid-template-columns:minmax(0,1fr) auto;gap:10px;margin:26px 0}
 .energy-track{grid-column:1/-1;grid-row:2}
 .energy-row b{grid-column:2;grid-row:1}
 .energy-scale{margin:0}
}
"""
icons={
'in': '<path d="M4 5h16v14H4z"/><path d="M4 12h5l2 3h2l2-3h5M8 8h8"/>',
'ai':'<rect x="6" y="6" width="12" height="12" rx="3"/><path d="M9 1v5m6-5v5M9 18v5m6-5v5M1 9h5m-5 6h5m12-6h5m-5 6h5M9 12h6"/>',
'user':'<circle cx="12" cy="7" r="4"/><path d="M4 22v-3a8 8 0 0 1 16 0v3"/>',
'check':'<path d="m4 12 5 5L20 5"/>'
}
def icon(name):
 return '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'+icons[name]+'</svg>'
def fragment(s):return BeautifulSoup(s,'html.parser')
def replace_figure(wrap,name,markup,before=None):
 old=wrap.find(id=name)
 if old:old.decompose()
 new=fragment(markup)
 if before:before.insert_before(new)
 else:wrap.append(new)
for lang,path in [('pt','guia/index.html'),('en','guia/en/index.html'),('es','guia/es/index.html')]:
 p=R/path;doc=BeautifulSoup(p.read_text(),'html.parser');d=json.loads((R/f'i18n/diagramas/{lang}.json').read_text())
 old=doc.find('style',id='diagramas-css')
 if old:old.decompose()
 tag=doc.new_tag('style',id='diagramas-css');tag.string=CSS;doc.head.append(tag)
 wrap=doc.select_one('#mudanca .wrap')
 # Replace redundant prose, retain the explicit 2028 qualification.
 paras=wrap.find_all('p',recursive=False)
 caution=next(x for x in paras if '2028' in x.get_text())
 for x in paras:
  if x is not caution:x.decompose()
 intro=doc.new_tag('p');intro.string=d['intro'];caution.insert_before(intro)
 nodes=''.join('<div class="role-node"><div class="role-icon">'+icon(ico)+'</div><strong>'+e(title)+'</strong><p>'+e(text)+'</p></div>' for ico,(title,text) in zip(['in','ai','user'],d['roles']))
 markup='<figure class="diagram" id="diagrama-papeis"><h3>'+e(d['roles_title'])+'</h3><div class="role-route">'+nodes+'</div><p class="diagram-note">'+e(d['bottleneck'])+'</p><figcaption>'+e(d['roles_note'])+' '+e(d['agent'])+'</figcaption></figure>'
 replace_figure(wrap,'diagrama-papeis',markup,before=caution)
 wrap=doc.select_one('#exemplo .wrap')
 for x in list(wrap.children):
  if getattr(x,'name',None) and x.name!='h2':x.decompose()
 nodes=''.join('<div class="case-node"><strong>'+e(title)+'</strong><small>'+e(label)+'</small><blockquote>'+e(text)+'</blockquote></div>' for title,text,label in d['case'])
 checks=''.join('<span>'+icon('check')+e(text)+'</span>' for text in d['compare'])
 wrap.append(fragment('<figure class="diagram" id="diagrama-pedido"><h3>'+e(d['case_title'])+'</h3><div class="case-route">'+nodes+'</div><p class="diagram-note">'+e(d['compare_title'])+'</p><div class="check-strip">'+checks+'</div><figcaption>'+e(d['compare_note'])+' '+e(d['case_note'])+'</figcaption></figure>'))
 wrap=doc.select_one('#plano .wrap')
 for x in list(wrap.children):
  if getattr(x,'name',None) and x.name!='h2':x.decompose()
 nodes=''.join('<li><span class="road-marker" aria-hidden="true">'+str(i)+'</span><time>'+e(days)+'</time><strong>'+e(title)+'</strong><p>'+e(text)+'</p><div class="road-output"><small>'+e(d['output'])+'</small>'+e(output)+'</div></li>' for i,(days,title,text,output) in enumerate(d['road'],1))
 wrap.append(fragment('<figure class="diagram" id="diagrama-plano"><h3>'+e(d['road_title'])+'</h3><ol class="roadline">'+nodes+'</ol><figcaption>'+e(d['road_note'])+'</figcaption></figure>'))
 wrap=doc.select_one('#fontes .wrap')
 target=wrap.find(id='grafico-energia') or next(x for x in wrap.find_all('p',recursive=False) if 'DOE/LBNL' in x.get_text())
 # data labels and scale remain text, accessible without color.
 markup='<figure class="diagram" id="grafico-energia"><h3>'+e(d['energy_title'])+'</h3><p class="energy-heading">'+e(d['energy_sub'])+'</p><div class="energy-row"><label>'+e(d['energy_actual'])+'</label><div class="energy-track" aria-hidden="true"><div class="energy-fill"></div></div><b>'+e(d['energy_value'])+'</b></div><div class="energy-row"><label>'+e(d['energy_future'])+'</label><div class="energy-track" aria-hidden="true"><div class="energy-range"></div></div><b>'+e(d['energy_low'])+'–'+e(d['energy_high'])+'</b></div><div class="energy-scale" aria-label="'+e(d['energy_scale'])+'"><span>0%</span><span>12%</span></div><div class="energy-legend"><span class="range-key" aria-hidden="true"></span>'+e(d['forecast_key'])+'</div><figcaption>'+e(d['energy_note'])+' <a href="https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers">'+e(d['energy_link'])+'</a>.</figcaption></figure>'
 target.replace_with(fragment(markup))
 for text in doc.footer.find_all(string=True):
  if 'v1.0.0' in str(text):text.replace_with(str(text).replace('v1.0.0','v1.0.1'))
 p.write_text(str(doc))
 print(lang,': 4 diagramas')
(R/'VERSION').write_text('1.0.1\n')
