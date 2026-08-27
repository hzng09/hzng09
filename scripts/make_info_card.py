def make_info_card():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 370" width="490" height="370">
  <style>
    .bg { fill: #0d1117; rx: 10px; stroke: #30363d; stroke-width: 1px; }
    .header { fill: #8b949e; font-family: monospace; font-size: 12px; }
    .label { fill: #58a6ff; font-family: monospace; font-size: 13px; font-weight: bold; }
    .value { fill: #c9d1d9; font-family: monospace; font-size: 13px; }
    .accent { fill: #79c0ff; font-family: monospace; font-size: 13px; }
  </style>
  <rect width="100%" height="100%" class="bg" />
  <text x="20" y="30" class="header">user@github ~ $ neofetch</text>
  <line x1="20" y1="42" x2="470" y2="42" stroke="#30363d" stroke-width="1" />
  
  <text x="20" y="75" class="label">OS:<tspan class="value"> macOS / Linux</tspan></text>
  <text x="20" y="110" class="label">Host:<tspan class="value"> GitHub Actions Cloud</tspan></text>
  <text x="20" y="145" class="label">Role:<tspan class="value"> Software Developer</tspan></text>
  <text x="20" y="180" class="label">Stack:<tspan class="value"> Python, TypeScript, React, Docker</tspan></text>
  <text x="20" y="215" class="label">Focus:<tspan class="value"> Building High-Performance Web &amp; Cloud Systems</tspan></text>
  <text x="20" y="250" class="label">Status:<tspan class="accent"> 🚀 Open to Collaborations &amp; Projects</tspan></text>
</svg>'''
    with open("info-card.svg", "w") as f:
        f.write(svg_content)
    print("Generated info-card.svg")

if __name__ == "__main__":
    make_info_card()
