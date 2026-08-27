import json
import os

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_svg():
    data_file = "data/contributions.json"
    if not os.path.exists(data_file):
        print(f"{data_file} not found. Run fetch_contributions.py first.")
        return

    with open(data_file) as f:
        data = json.load(f)

    days = data.get("days", [])
    username = data.get("username", "GitHub User")
    
    cell_size = 11
    cell_gap = 3
    margin_x = 20
    margin_y = 30
    
    svg_width = 860
    svg_height = 160
    
    rects = []
    for i, day in enumerate(days):
        col = i // 7
        row = i % 7
        x = margin_x + col * (cell_size + cell_gap)
        y = margin_y + row * (cell_size + cell_gap)
        lvl = min(max(day.get("level", 0), 0), 5)
        color = PALETTE[lvl]
        delay = (col + row) * 0.015
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{color}">'
            f'<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{delay:.3f}s" fill="freeze" />'
            f'</rect>'
        )

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; }}
    .title {{ fill: #58a6ff; font-family: monospace; font-size: 13px; font-weight: bold; }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  <text x="{margin_x}" y="18" class="title">@{username} contribution graph (past year)</text>
  <g>
    {"".join(rects)}
  </g>
</svg>'''

    with open("contrib-heatmap.svg", "w") as f:
        f.write(svg_content)
    print("Generated contrib-heatmap.svg successfully.")

if __name__ == "__main__":
    render_svg()
