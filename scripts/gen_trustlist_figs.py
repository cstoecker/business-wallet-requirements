#!/usr/bin/env python3
"""Generate the two Trust list figures (assets/figures/trust-list-*.svg) in the Spherity figure style."""
import os
from xml.sax.saxutils import escape as x
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "figures")
STYLE = '''<defs>
    <marker id="ah" viewBox="0 0 12 12" markerWidth="10" markerHeight="10" refX="10" refY="6" orient="auto"><path d="M1,1 L10,6 L1,11" fill="none" stroke="#023852" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></marker>
    <style>
      text{font-family:Archivo,Arial,sans-serif}
      .bx{fill:#FFFFFE;stroke:#023852;stroke-width:2}
      .sig{fill:#2BFEBB;stroke:#023852;stroke-width:2}
      .big{fill:#023852;stroke:#023852;stroke-width:2}
      .t{font-size:17px;font-weight:600;fill:#023852;text-anchor:middle}
      .tw{font-size:17px;font-weight:600;fill:#F4F2EE;text-anchor:middle}
      .li{font-size:16px;fill:#253746}
      .lab{font-size:16px;fill:#253746;text-anchor:middle}
      .arr{fill:none;stroke:#023852;stroke-width:2.2;stroke-linecap:round}
      .grp{fill:none;stroke:#C9C7C2;stroke-width:2}
      .gt{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:13px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;fill:#445260}
      .wbg{fill:#F4F2EE}
    </style>
  </defs>'''
def head(w, h, tid, title, desc, subj):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t{tid} d{tid}">
  <title id="t{tid}">{x(title)}</title>
  <desc id="d{tid}">{x(desc)}</desc>
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:RDF><cc:Work rdf:about=""><dc:title>{x(title)}</dc:title><dc:description>{x(desc)}</dc:description><dc:creator>European Business Wallet Requirements project</dc:creator><dc:subject>{x(subj)}</dc:subject><dc:language>en</dc:language><dc:format>image/svg+xml</dc:format><dc:rights>CC BY 4.0</dc:rights><cc:license rdf:resource="https://creativecommons.org/licenses/by/4.0/"/></cc:Work></rdf:RDF></metadata>
  {STYLE}
  <rect width="{w}" height="{h}" fill="#F4F2EE"/>
'''
def lines(x0, y0, items, cls="li", lh=24):
    return "".join(f'<text class="{cls}" x="{x0}" y="{y0+i*lh}">{x(s)}</text>' for i, s in enumerate(items))
# ---- Figure 1: anatomy
a = head(1260, 640, "5", "Anatomy of a trusted list and who uses it",
  "A signed trusted list has three parts: scheme information, a list of providers with their services, and a digital signature. Each service carries a type, a digital identity used as trust anchor, a current status with start time and a history. A scheme operator publishes the list; relying parties read it.",
  "trusted list; ETSI TS 119 612; trust anchor; service status; European Business Wallet")
a += '<rect class="grp" x="20" y="70" width="190" height="500" rx="16"/><text class="gt" x="115" y="98" text-anchor="middle">Publisher</text>\n'
a += '<rect class="grp" x="260" y="70" width="740" height="500" rx="16"/><text class="gt" x="630" y="98" text-anchor="middle">Signed trusted list (XML)</text>\n'
a += '<rect class="grp" x="1050" y="70" width="190" height="500" rx="16"/><text class="gt" x="1145" y="98" text-anchor="middle">Relying party</text>\n'
a += '<rect class="bx" x="40" y="200" width="150" height="90" rx="12"/><text class="t" x="115" y="236" >Scheme</text><text class="t" x="115" y="260">operator</text>\n'
a += '<rect class="bx" x="285" y="120" width="690" height="130" rx="12"/><text class="t" x="630" y="148">Scheme information</text>' + lines(310, 178, ["Operator, territory, list type, sequence number", "Issue date and next update", "Pointers to other lists, distribution points"]) + '\n'
a += '<rect class="bx" x="285" y="270" width="690" height="190" rx="12"/><text class="t" x="630" y="298">Providers and their services</text>' + lines(310, 328, ["Provider: name, address", "Service: type identifier, name", "Service digital identity (the trust anchor)", "Current status and status starting time", "Service history: earlier statuses, newest first"]) + '\n'
a += '<rect class="sig" x="285" y="480" width="690" height="64" rx="12"/><text class="t" x="630" y="519">Digital signature of the scheme operator</text>\n'
a += '<rect class="big" x="1070" y="240" width="150" height="110" rx="12"/><text class="tw" x="1145" y="284">Validates</text><text class="tw" x="1145" y="308">signature, status</text><text class="tw" x="1145" y="332">and chain</text>\n'
a += '<path class="arr" d="M190,245 H255" marker-end="url(#ah)"/><text class="lab" x="222" y="232">Signs</text>\n'
a += '<path class="arr" d="M1045,295 H1000" marker-end="url(#ah)"/><text class="lab" x="1022" y="282">Reads</text>\n'
a += '</svg>\n'
open(os.path.join(OUT, "trust-list-anatomy.svg"), "w").write(a)
# ---- Figure 2: validation flow
steps = [("Locate the", "list of lists"), ("Verify its", "signature"), ("Find the", "national list"), ("Verify that", "list's signature"), ("Find service", "and identity"), ("Check status", "and next update")]
f = head(1260, 520, "6", "How a relying party uses a trusted list",
  "Flow in six steps. The relying party locates the Commission list of trusted lists, verifies its signature against the digest published in the Official Journal, finds the pointer to the national list, downloads that list and verifies its signature with the certificate named in the list of lists, finds the service and its digital identity, checks that the status was granted and the list has not expired, and uses the digital identity as trust anchor for certificate path validation.",
  "trusted list; list of trusted lists; relying party validation; trust anchor; ETSI TS 119 612")
f += '<rect class="grp" x="20" y="80" width="785" height="190" rx="16"/><text class="gt" x="40" y="108">Authenticate the lists</text>\n'
f += '<rect class="grp" x="825" y="80" width="415" height="190" rx="16"/><text class="gt" x="845" y="108">Use the list</text>\n'
xs = [40, 235, 430, 625, 845, 1040]
w = 160
for i, (a1, a2) in enumerate(steps):
    cls = "bx"
    f += f'<rect class="{cls}" x="{xs[i]}" y="150" width="{w}" height="84" rx="12"/><text class="t" x="{xs[i]+w//2}" y="186">{x(a1)}</text><text class="t" x="{xs[i]+w//2}" y="210">{x(a2)}</text><text class="gt" x="{xs[i]+10}" y="140">{i+1}</text>\n'
    if i < 5:
        f += f'<path class="arr" d="M{xs[i]+w},192 H{xs[i+1]-4}" marker-end="url(#ah)"/>\n'
f += '<rect class="sig" x="400" y="340" width="460" height="90" rx="12"/><text class="t" x="630" y="376">Trust anchor for certificate</text><text class="t" x="630" y="400">path validation</text>\n'
f += f'<path class="arr" d="M{xs[5]+w//2},234 C{xs[5]+w//2},300 700,300 700,336" marker-end="url(#ah)"/>\n'
f += '<text class="lab" x="630" y="480">If any check fails, the relying party does not trust the result.</text>\n'
f += '</svg>\n'
open(os.path.join(OUT, "trust-list-validation.svg"), "w").write(f)
