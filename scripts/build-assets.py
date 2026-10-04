from pathlib import Path
from html import escape
from PIL import Image,ImageEnhance

ROOT=Path(__file__).resolve().parents[1]
portrait=Image.open(ROOT/'assets/portrait.webp').convert('L')
portrait=ImageEnhance.Contrast(portrait).enhance(1.35).resize((74,55))
chars=' .:-=+*#%@'
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="480" viewBox="0 0 1000 480" role="img" aria-labelledby="title desc">',
'<title id="title">Bhavesh Jain — research, made useful</title>',
'<desc id="desc">An ASCII portrait of Bhavesh alongside his current role, AI research focus, learning areas, and contact links. Data Scientist and Team Lead Data and Development at Joint Innovation Hub, Fraunhofer ISI, Heilbronn.</desc>',
'<style>text{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}.cursor{animation:blink 1.2s steps(1) 8}.intro{animation:appear .65s ease-out}@keyframes blink{50%{opacity:0}}@keyframes appear{from{opacity:.4;transform:translateY(3px)}to{opacity:1;transform:translateY(0)}}@media(prefers-reduced-motion:reduce){.cursor,.intro{animation:none}}</style>',
'<rect width="1000" height="480" rx="14" fill="#0d1117"/>',
'<path d="M0 44H1000M450 44V480" fill="none" stroke="#27323e"/>',
'<circle cx="26" cy="22" r="4" fill="#79cdb8"/><circle cx="42" cy="22" r="4" fill="#5c6977"/><circle cx="58" cy="22" r="4" fill="#5c6977"/>',
'<text x="92" y="27" font-size="12" fill="#a6b3c2">bhav1212@github</text>',
'<text x="968" y="27" text-anchor="end" font-size="12" fill="#79cdb8">research, made useful</text>',
'<text x="28" y="78" fill="#79cdb8" font-size="12">$ ./portrait</text>']
for row in range(55):
    line=''.join(chars[min(9,int((255-portrait.getpixel((col,row)))/256*10))] for col in range(74))
    svg.append(f'<text x="35" y="{102+row*5.8:.1f}" xml:space="preserve" textLength="380" lengthAdjust="spacing" font-size="6.6" fill="#ced7df">{escape(line)}</text>')
svg+=['<text x="28" y="450" font-size="11" fill="#a6b3c2">Heilbronn, Germany · CET/CEST</text>',
'<g class="intro">',
'<text x="485" y="82" font-size="12" fill="#79cdb8">$ whoami</text>',
'<text x="485" y="121" font-size="26" font-weight="700" fill="#e6edf3">Bhavesh Jain</text>',
'<text x="485" y="149" font-size="16" fill="#e6edf3">Data Scientist</text>',
'<text x="485" y="178" font-size="13" fill="#a6b3c2">Team Lead Data &amp; Development</text>',
'<text x="485" y="199" font-size="13" fill="#a6b3c2">Joint Innovation Hub · Fraunhofer ISI</text>',
'<path d="M485 220H965" stroke="#27323e"/>',
'<text x="485" y="251" font-size="12" fill="#79cdb8">$ focus --current</text>',
'<text x="485" y="279" font-size="15" fill="#e6edf3">GenAI · Multi-agent systems</text>',
'<text x="485" y="303" font-size="15" fill="#e6edf3">Strategic foresight · AI evaluation</text>',
'<text x="485" y="338" font-size="12" fill="#79cdb8">$ learning</text>',
'<text x="485" y="364" font-size="13" fill="#a6b3c2">Agentic systems · AI product management</text>',
'<text x="485" y="385" font-size="13" fill="#a6b3c2">AI project management · Context engineering</text>',
'<path d="M485 406H965" stroke="#27323e"/>',
'<text x="485" y="435" font-size="13" fill="#e6edf3">bhaveshjain.com</text>',
'<text x="485" y="459" font-size="13" fill="#79cdb8">hello@bhaveshjain.com</text>',
'<rect class="cursor" x="684" y="449" width="7" height="12" fill="#79cdb8"/>','</g>','</svg>']
(ROOT/'assets/profile-terminal.svg').write_text('\n'.join(svg)+'\n')
print('Original terminal portrait and profile facts generated.')

# A compact layout keeps identity and role legible on narrow profile pages.
mobile=['<svg xmlns="http://www.w3.org/2000/svg" width="600" height="620" viewBox="0 0 600 620" role="img" aria-labelledby="title desc">',
'<title id="title">Bhavesh Jain — Data Scientist</title>',
'<desc id="desc">ASCII portrait of Bhavesh. Team Lead Data and Development, Joint Innovation Hub, Fraunhofer ISI. GenAI, multi-agent systems, and strategic foresight. Heilbronn, Germany.</desc>',
'<rect width="600" height="620" rx="14" fill="#0d1117"/><style>text{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}</style>',
'<path d="M0 44H600" stroke="#27323e"/><text x="26" y="28" font-size="17" fill="#79cdb8">bhav1212@github: ~$ whoami</text>']
for row in range(55):
    line=''.join(chars[min(9,int((255-portrait.getpixel((col,row)))/256*10))] for col in range(74))
    mobile.append(f'<text x="120" y="{70+row*5.3:.1f}" xml:space="preserve" textLength="360" lengthAdjust="spacing" font-size="6.3" fill="#ced7df">{escape(line)}</text>')
mobile+=['<path d="M26 378H574" stroke="#27323e"/>',
'<text x="28" y="423" font-size="36" font-weight="700" fill="#e6edf3">Bhavesh Jain</text>',
'<text x="28" y="457" font-size="24" fill="#e6edf3">Data Scientist</text>',
'<text x="28" y="490" font-size="19" fill="#a6b3c2">Team Lead Data &amp; Development</text>',
'<text x="28" y="519" font-size="18" fill="#a6b3c2">Joint Innovation Hub · Fraunhofer ISI</text>',
'<text x="28" y="556" font-size="19" fill="#79cdb8">GenAI · Agents · Strategic foresight</text>',
'<text x="28" y="593" font-size="18" fill="#a6b3c2">bhaveshjain.com · Heilbronn, Germany</text>','</svg>']
(ROOT/'assets/profile-terminal-mobile.svg').write_text('\n'.join(mobile)+'\n')
print('Mobile terminal asset generated.')
