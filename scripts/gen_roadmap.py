#!/usr/bin/env python3
"""Generate assets/figures/legal-roadmap.svg (swimlane roadmap, Q4 2025 - Q4 2029). Structure follows the
Spherity Research EBW roadmap; all dates are indicative scenarios except the Commission proposal."""
import os
from xml.sax.saxutils import escape as x
ROOT = os.path.join(os.path.dirname(__file__), "..")
W, H = 1600, 810
LX, GX, GW = 24, 250, 1330          # label x, grid x, grid width
NQ = 17                              # Q4 2025 .. Q4 2029
QW = GW / NQ
def qx(i): return GX + i * QW        # i = quarters since start of Q4 2025 (float ok)
PET, CY, OR, GR = "#023852", "#00B6BD", "#E8730C", "#445260"
out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="tm dm">')
a('<title id="tm">European Business Wallet legal and operational roadmap, Q4 2025 to Q4 2029</title>')
a('<desc id="dm">Swimlane roadmap from Q4 2025 to Q4 2029 with Council presidencies and seven tracks: regulation and policy, standardisation, Architecture Reference Framework, large-scale pilots, Member States, conformity and accreditation, industry adoption. Only the Commission proposal of 19 November 2025 is confirmed; all other milestones are indicative scenarios that depend on adoption and entry into force of the regulation.</desc>')
a('<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:RDF><cc:Work rdf:about=""><dc:title>European Business Wallet legal and operational roadmap 2025-2029</dc:title><dc:description>Swimlane roadmap with indicative legal, standardisation, pilot, conformity and adoption milestones for the European Business Wallet.</dc:description><dc:creator>European Business Wallet Requirements project</dc:creator><dc:subject>European Business Wallet; roadmap; eIDAS 2.0; COM(2025) 838; timeline</dc:subject><dc:language>en</dc:language><dc:format>image/svg+xml</dc:format><dc:rights>CC BY 4.0</dc:rights><cc:license rdf:resource="https://creativecommons.org/licenses/by/4.0/"/></cc:Work></rdf:RDF></metadata>')
a('<style>text{font-family:Archivo,Arial,sans-serif;fill:#253746}.t{font-size:26px;font-weight:700;fill:#023852}.lane{font-size:15px;font-weight:700;fill:#023852}.sub{font-size:12.5px;fill:#445260}.yr{font-size:22px;font-weight:700;fill:#023852}.q{font-size:13px;font-weight:600;fill:#fff}.bx{font-size:13.5px}.pres{font-size:13px;font-weight:600;fill:#023852}.leg{font-size:13px;fill:#445260}.grid{stroke:#C9C7C2;stroke-width:1;stroke-dasharray:4 5}</style>')
a(f'<rect width="{W}" height="{H}" fill="#fff"/>')
a(f'<text x="{LX}" y="40" class="t">European Business Wallet: legal and operational roadmap</text>')
a(f'<text x="{LX}" y="62" class="sub">Indicative scenario; the Commission proposal is the only confirmed milestone. Analysis, not legal advice.</text>')
# year labels and quarter ribbon
years = [(2025, 0, 1), (2026, 1, 5), (2027, 5, 9), (2028, 9, 13), (2029, 13, 17)]
for y, s, e in years:
    a(f'<text x="{(qx(s)+qx(e))/2:.0f}" y="96" class="yr" text-anchor="middle">{y}</text>')
    a(f'<line x1="{qx(s):.0f}" y1="104" x2="{qx(s):.0f}" y2="{H-70}" class="grid"/>')
labels = ["Q4"] + ["Q1", "Q2", "Q3", "Q4"] * 4
for i, l in enumerate(labels):
    col = "#046A5F" if l == "Q4" and i == 0 else PET
    a(f'<rect x="{qx(i)+1:.0f}" y="108" width="{QW-2:.0f}" height="28" rx="14" fill="{col}"/><text x="{qx(i)+QW/2:.0f}" y="127" class="q" text-anchor="middle">{l}</text>')
# presidencies
pres = [("Denmark", 0, 1), ("Cyprus", 1, 3), ("Ireland", 3, 5), ("Lithuania", 5, 7), ("Greece", 7, 9), ("Italy", 9, 11), ("Latvia", 11, 13), ("Luxembourg", 13, 15), ("Netherlands", 15, 17)]
PY = 146
a(f'<text x="{LX}" y="{PY+20}" class="lane">Council presidency</text>')
for n, s, e in pres:
    a(f'<rect x="{qx(s)+2:.0f}" y="{PY}" width="{(e-s)*QW-4:.0f}" height="28" rx="6" fill="#F2F0ED" stroke="#C9C7C2"/><text x="{(qx(s)+qx(e))/2:.0f}" y="{PY+19}" class="pres" text-anchor="middle">{n}</text>')
def diamond(cx, cy, confirmed=False):
    f = OR if confirmed else "#fff"
    a(f'<path d="M{cx:.0f} {cy-9} L{cx+9:.0f} {cy} L{cx:.0f} {cy+9} L{cx-9:.0f} {cy} Z" fill="{f}" stroke="{OR}" stroke-width="2"/>')
def lines(x0, y0, txt, anchor="start", cls="bx", lh=17):
    for k, l in enumerate(txt.split("|")):
        a(f'<text x="{x0:.0f}" y="{y0+k*lh}" class="{cls}" text-anchor="{anchor}">{x(l)}</text>')
def bar(s, e, y, h, label=None, fill="#E6F3F4", stroke=CY):
    a(f'<rect x="{qx(s)+2:.0f}" y="{y}" width="{(e-s)*QW-4:.0f}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    if label: lines(qx(s)+14, y+h/2-(len(label.split('|'))-1)*8.5+5, label)
lanes = [("Regulation / policy", "top milestones", 190, 100), ("Standardisation", "", 306, 44), ("Reference framework", "ARF", 366, 52),
         ("Wallet large-scale pilots", "WE BUILD and others", 434, 52), ("Member States", "EBW acceptance", 502, 64),
         ("Conformity and accreditation", "based on eIDAS", 582, 64), ("Industry adoption", "", 662, 52)]
for n, s, y, h in lanes:
    a(f'<text x="{LX}" y="{y+20}" class="lane">{x(n)}</text>')
    if s: a(f'<text x="{LX}" y="{y+37}" class="sub">{x(s)}</text>')
# lane separators
for yy in (298, 358, 426, 494, 574, 654, 722):
    a(f'<line x1="{LX}" y1="{yy}" x2="{GX+GW}" y2="{yy}" stroke="#E4E2DD"/>')
# regulation / policy
diamond(qx(0.5), 204, True); lines(qx(0.5)+16, 208, "Commission proposal|COM(2025) 838|19 Nov 2025")
diamond(qx(4.9), 204); lines(qx(4.9)-16, 208, "Parliament and Council|provisional agreement|(trilogue), late 2026", "end")
diamond(qx(5.15), 204); lines(qx(5.15)+16, 208, "T0 = publication in the|Official Journal (est. Q1-Q2 2027);|entry into force 20 days later")
diamond(qx(13.15), 204); lines(qx(13.15)+16, 208, "EBW go-live: mandatory acceptance|by public administrations, T0 + 24 months|(2028-2029, subject to adoption)")
diamond(qx(16.2), 268); lines(qx(16.2)-16, 262, "QERDS go-live: mandatory acceptance|by public administrations, T0 + 36 months", "end")
# standardisation
bar(0, 17, 308, 40, None, "#fff", PET); lines(qx(8.5), 333, "Standardisation in ETSI ESI and CEN-CENELEC (ongoing)", "middle")
# ARF
bar(5, 13.7, 372, 40, None, "#fff", PET); lines(qx(5)+14, 397, "EBW specifics added to the ARF")
diamond(qx(8.6), 392); lines(qx(8.6)+16, 397, "Toolbox upgrade for EBW specifics")
# pilots
bar(0, 9, 440, 40, "Pilots for business, supply chain, payments: semantics,|architecture and trust registry, QTSP", "#fff", PET)
diamond(qx(9.1), 460); lines(qx(9.1)+16, 456, "EBW-ready solution|baseline", cls="bx")
# member states
bar(0, 17, 508, 52, None, "#fff", PET)
lines(qx(0)+14, 539, "Trusted pilots B2G")
diamond(qx(5.2), 534); lines(qx(5.2)+16, 530, "Pilot start: EBW acceptance|(public and regulated sectors)")
diamond(qx(9.4), 534); lines(qx(9.4)+16, 523, "Start publishing company credentials|(EAA / QEAA) by authentic sources", lh=17)
diamond(qx(13.3), 534); lines(qx(13.3)+16, 530, "Member States enable acceptance|of EBW use cases")
# conformity
bar(0, 17, 588, 52, None, "#fff", PET)
diamond(qx(5.0), 614); lines(qx(5.0)-16, 610, "CABs operational for QTSPs issuing QEAAs|(per CIR 2024/2981)", "end")
diamond(qx(5.7), 614); lines(qx(5.7)+16, 610, "QTSPs issuing QEAAs start conformity|assessment and accreditation pathway")
# industry
bar(0, 9, 668, 44, "Trusted pilots of EBW-ready solutions (Industry 4.0, supply|chain, data spaces, DPP, cross-border procurement, payment)", "#fff", PET)
bar(9.2, 17, 668, 44, "Widespread industry adoption", "#fff", PET)
# legend
ly = H - 60
a(f'<rect x="0" y="{H-80}" width="{W}" height="80" fill="#F7F6F4"/>')
diamond(LX+10, ly+6, True); a(f'<text x="{LX+26}" y="{ly+11}" class="leg">confirmed</text>')
diamond(LX+130, ly+6); a(f'<text x="{LX+146}" y="{ly+11}" class="leg">indicative (scenario)</text>')
a(f'<text x="{LX+330}" y="{ly+11}" class="leg">CAB conformity assessment body, EAA electronic attestation of attributes, QEAA qualified EAA, QTSP qualified trust service provider, T0 date of entry into force</text>')
a(f'<text x="{LX}" y="{ly+34}" class="leg">Sources: COM(2025) 838 (proposal date); other milestones follow the Spherity Research roadmap scenario (2026-05-18, updated 2026-09-07), not an official timetable. Council presidency order per Council rotation.</text>')
a('</svg>')
open(os.path.join(ROOT, "assets/figures/legal-roadmap.svg"), "w").write("\n".join(out))
