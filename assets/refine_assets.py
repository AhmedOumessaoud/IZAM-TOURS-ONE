"""Maintain the reference layout while replacing raster-only UI with SVG/HTML."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
page = root / 'index.html'
html = page.read_text(encoding='utf-8')
symbols = '''<symbol id="quad" viewBox="0 0 48 40"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="30" r="7"/><circle cx="38" cy="30" r="7"/><path d="m10 30 8-15h12l8 15H10l13-11m-4-8 3-7h7m1 11 4-6h6M16 15H9"/></g></symbol>
<symbol id="camel" viewBox="0 0 48 40"><path d="m5 22 3-9q3-6 9 0 5-10 12-1l4 7 4-9V4l6 2 2 7-5 2-3 13-5 1-2 10h-3l-2-11H14l-3 11H8L7 25 3 23Z" fill="currentColor"/></symbol>
<symbol id="dinner" viewBox="0 0 48 40"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M5 31h38M2 36h44M8 29a16 16 0 0 1 32 0M21 9q3-6 6 0M24 4V2"/></g></symbol>
<symbol id="people" viewBox="0 0 48 40"><g fill="none" stroke="currentColor" stroke-width="2.7"><circle cx="24" cy="10" r="6"/><circle cx="8" cy="15" r="4"/><circle cx="40" cy="15" r="4"/><path d="M12 36v-6q0-12 12-12t12 12v6M2 34v-7q0-7 9-7m26 0q9 0 9 7v7"/></g></symbol>
<symbol id="sliders" viewBox="0 0 40 40"><g fill="none" stroke="currentColor" stroke-width="3"><path d="M3 10h9m8 0h17M3 29h20m8 0h6"/><circle cx="16" cy="10" r="4"/><circle cx="27" cy="29" r="4"/></g></symbol>
<symbol id="badge" viewBox="0 0 40 40"><path d="m20 2 5 4 6 1 1 6 4 5-3 6-1 6-7 1-5 4-5-4-7-1-1-6-3-6 4-5 1-6 6-1Zm0 7 3 6 6 1-5 4 1 6-5-3-5 3 1-6-5-4 6-1Z" fill="none" stroke="currentColor" stroke-width="2"/></symbol>
<symbol id="phone" viewBox="0 0 32 32"><path d="M9 3 4 7q-2 12 13 21 6 3 10-3l2-4-8-5-4 4q-5-3-6-7l4-3Z" fill="currentColor"/></symbol>'''
if 'id="quad"' not in html:
 html = html.replace('</defs>', symbols + '</defs>')
html=html.replace('src="assets/images/hero.webp"','src="assets/images/hero-generated.webp" srcset="assets/images/hero-generated-768.webp 768w, assets/images/hero-generated.webp 1536w" sizes="(max-width: 900px) 100vw, 900px"')
html=html.replace('content="assets/images/hero.webp"','content="assets/images/hero-generated.webp"')
html=html.replace('data-label="call">☎</a>','data-label="call"><svg aria-hidden="true"><use href="#phone"/></svg></a>')
html=html.replace('<div class="mountain-decoration">△</div>','')
html=html.replace('<span data-i18n="nights"></span><span data-i18n="camp"></span><span data-i18n="camel"></span>','<span><svg aria-hidden="true"><use href="#calendar"/></svg><b data-i18n="nights"></b></span><span><svg aria-hidden="true"><use href="#mountain"/></svg><b data-i18n="camp"></b></span><span><svg aria-hidden="true"><use href="#camel"/></svg><b data-i18n="camel"></b></span>')
html=html.replace('<b class="google">G</b>','<svg class="google" aria-label="Google" viewBox="0 0 48 48"><path fill="#4285f4" d="M43.6 24.5c0-1.5-.1-3-.4-4.5H24v8.5h11a9.4 9.4 0 0 1-4.1 6.2v5.2h6.7c3.9-3.6 6-8.9 6-15.4Z"/><path fill="#34a853" d="M24 44c5.5 0 10.1-1.8 13.6-5l-6.7-5.2c-1.8 1.2-4.1 2-6.9 2-5.3 0-9.8-3.6-11.4-8.5H5.7v5.3A20.5 20.5 0 0 0 24 44Z"/><path fill="#fbbc05" d="M12.6 27.3a12.3 12.3 0 0 1 0-7.8v-5.3H5.7a20.4 20.4 0 0 0 0 18.4Z"/><path fill="#ea4335" d="M24 11.2c3 0 5.5 1 7.6 3l5.7-5.7A19.2 19.2 0 0 0 24 3 20.5 20.5 0 0 0 5.7 14.2l6.9 5.3c1.6-4.9 6.1-8.3 11.4-8.3Z"/></svg>')
page.write_text(html,encoding='utf-8')
jsfile=root/'js/app.js';js=jsfile.read_text(encoding='utf-8')
js=js.replace("icon(k==='evening'?'glass':'mountain')", "icon(k==='evening'?'dinner':k)")
js=js.replace("['shield','shield','pin','mountain'][i]", "['badge','shield','people','sliders'][i]")
jsfile.write_text(js,encoding='utf-8')
