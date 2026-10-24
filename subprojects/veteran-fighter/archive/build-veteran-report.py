from pathlib import Path
from html import escape
import re, json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).parent
SRC=ROOT/'Veteran_Level_3_Combat_Identity_2026-09-30.md'
OUT=ROOT/'output/pdf/Veteran_Level_3_Combat_Identity_2026-09-30.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
fontbase=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('DV','DejaVuSans.ttf'),('DV-Bold','DejaVuSans-Bold.ttf'),('DV-Italic','DejaVuSans.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(fontbase/file)))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DV-Bold',italic='DV-Italic',boldItalic='DV-Bold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Text',fontName='DV',fontSize=9.8,leading=14.4,spaceAfter=8,textColor=colors.HexColor('#202a35')))
styles.add(ParagraphStyle(name='SmallCell',parent=styles['Text'],fontSize=8,leading=11,spaceAfter=0))
styles.add(ParagraphStyle(name='CellHeader',parent=styles['SmallCell'],fontName='DV-Bold',textColor=colors.white))
styles.add(ParagraphStyle(name='TitleV',parent=styles['Text'],fontName='DV-Bold',fontSize=24,leading=29,spaceAfter=16,textColor=colors.HexColor('#15334c')))
styles.add(ParagraphStyle(name='H2V',parent=styles['Text'],fontName='DV-Bold',fontSize=16,leading=21,spaceBefore=17,spaceAfter=11,keepWithNext=True,textColor=colors.HexColor('#15334c')))
styles.add(ParagraphStyle(name='H3V',parent=styles['Text'],fontName='DV-Bold',fontSize=12,leading=17,spaceBefore=12,spaceAfter=8,keepWithNext=True))
styles.add(ParagraphStyle(name='BulletV',parent=styles['Text'],leftIndent=12,firstLineIndent=-8))

def inline(t):
    t=t.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
    t=escape(t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',t)
    # URL paragraphs retain clickable source links with safe wrapping.
    t=re.sub(r'(https://[^\s<]+)',lambda m:'<link href="'+m.group(1)+'" color="#1b567d">'+m.group(1)+'</link>',t)
    return t

lines=SRC.read_text().splitlines(); story=[]; idx=0
while idx<len(lines):
    line=lines[idx].strip()
    if not line: idx+=1;continue
    if line.startswith('|'):
        raw=[]
        while idx<len(lines) and lines[idx].strip().startswith('|'):
            cells=[x.strip() for x in lines[idx].strip().strip('|').split('|')]
            if not all(re.fullmatch(r'[-: ]+',x) for x in cells): raw.append(cells)
            idx+=1
        cols=len(raw[0]); width=498
        if cols==5: weights=[.14,.24,.25,.22,.15]
        elif cols==4: weights=[.18,.28,.28,.26]
        elif cols==3: weights=[.2,.4,.4]
        elif cols==6: weights=[.13,.19,.18,.18,.16,.16]
        else: weights=[1/cols]*cols
        data=[[Paragraph(inline(x),styles['CellHeader'] if r==0 else styles['SmallCell']) for x in row] for r,row in enumerate(raw)]
        tab=Table(data,colWidths=[width*w for w in weights],repeatRows=1,hAlign='LEFT')
        tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#15334c')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f0f4f7'),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#15334c')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#d5dce3'))]))
        story.extend([tab,Spacer(1,10)]);continue
    if line.startswith('# '): story.append(Paragraph(inline(line[2:]),styles['TitleV']))
    elif line.startswith('## '):
        if line.startswith('## J.'):
            story.append(PageBreak())
        story.append(Paragraph(inline(line[3:]),styles['H2V']))
    elif line.startswith('### '):
        if line.startswith('### Prototype 2:'): story.append(PageBreak())
        story.append(Paragraph(inline(line[4:]),styles['H3V']))
    elif line.startswith('- '): story.append(Paragraph('&#8226; '+inline(line[2:]),styles['BulletV']))
    else:
        para=[line]
        while idx+1<len(lines) and lines[idx+1].strip() and not lines[idx+1].startswith(('#','|','- ')):
            idx+=1;para.append(lines[idx].strip())
        story.append(Paragraph(inline(' '.join(para)),styles['Text']))
    idx+=1

def footer(c,doc):
    c.saveState(); c.setStrokeColor(colors.HexColor('#b5c2ce'));c.line(57,43,555,43)
    c.setFont('DV',7);c.setFillColor(colors.HexColor('#5c6b78'))
    c.drawString(57,30,'VETERAN / LEVEL-3 COMBAT IDENTITY / ADVISORY PROTOTYPES')
    c.drawRightString(555,30,str(doc.page));c.restoreState()
class ReportDoc(SimpleDocTemplate):
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='H2V' and re.match(r'[A-M]\. ',f.getPlainText()):
            label=f.getPlainText();key='section-'+label[0]
            self.canv.bookmarkPage(key);self.canv.addOutlineEntry(label,key,level=0,closed=False)
doc=ReportDoc(str(OUT),pagesize=(612,792),rightMargin=57,leftMargin=57,topMargin=48,bottomMargin=58,title='Veteran Fighter: Level-3 Combat Identity',author='Design research - September 30, 2026')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)

# Reproducible illustrative calculations; no simulation randomness.
def studied(n,W,U=None):
    # state = next attack has advantage, fallback already used
    state={(False,False):1.0}; total=0
    for _ in range(n):
        nxt={}
        for (adv,used),mass in state.items():
            p=.8775 if adv else .65
            total+=mass*p*W
            nxt[(False,used)]=nxt.get((False,used),0)+mass*p
            fail=mass*(1-p)
            if U is not None and not used:
                total+=fail*.8775*U
                nxt[(False,True)]=nxt.get((False,True),0)+fail*.8775
                nxt[(True,True)]=nxt.get((True,True),0)+fail*(1-.8775)
            else: nxt[(True,used)]=nxt.get((True,used),0)+fail
        state=nxt
    return total,sum(m for (adv,_),m in state.items() if adv)
results={'assumptions':{'p':.65,'advantage_p':.8775,'weapon_hit_damage':12,'current_punch_hit_damage':6,'no_crit_mastery':True},'baselines':[], 'studied':{}}
for level,n,s in [(3,1,3),(5,2,4),(11,3,5),(13,3,5),(20,4,5)]:
    rows=[]
    for p in [.5,.65,.8]:
        F=1-p**n
        rows.append({'p':p,'miss_probability':F,'current_punch':F*p*(1+s),'practical_contact':p*(3.5+s),'d8_fallback':F*p*(4.5+s)})
    results['baselines'].append({'level':level,'n':n,'ability_modifier':s,'results':rows})
for n in [3,4]:
    base,last_adv=studied(n,12)
    current,_=studied(n,12,6)
    results['studied'][n]={'weapon_only':base,'current_with_punch':current,'current_net':current-base,'practical_late_contact':8.5*(.65+last_adv*(.8775-.65)),'carried_advantage_probability':last_adv}
(ROOT/'Veteran_Level_3_Model_2026-09-30.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results['studied'],indent=2))
