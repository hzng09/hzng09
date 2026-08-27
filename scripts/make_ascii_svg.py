import sys
import os
from PIL import Image

RAMP = " .`:-=+*cs#%@"  # Bright (sparse/spaces) -> Dark (dense chars)

def image_to_ascii_svg(image_path="source-prepped.png", output_svg="avi-ascii.svg", target_width=100):
    if not os.path.exists(image_path):
        print(f"Error: Prepped image '{image_path}' not found. Run prep_photo.py first!")
        sys.exit(1)
        
    img = Image.open(image_path).convert("L")
    
    aspect_ratio = img.height / img.width
    target_height = int(target_width * aspect_ratio * 0.55)
    
    resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    font_size = 7
    line_height = 8.5
    char_width = 4.2
    
    svg_w = int(target_width * char_width + 20)
    svg_h = int(target_height * line_height + 20)
    
    text_lines = []
    ramp_len = len(RAMP)
    
    for y in range(target_height):
        line_chars = []
        for x in range(target_width):
            pixel = resized.getpixel((x, y))
            char_idx = int((255 - pixel) / 255 * (ramp_len - 1))
            char = RAMP[char_idx]
            if char == '<': char = '&lt;'
            elif char == '>': char = '&gt;'
            elif char == '&': char = '&amp;'
            line_chars.append(char)
            
        line_text = "".join(line_chars)
        row_y = 20 + y * line_height
        delay = y * 0.04
        text_lines.append(
            f'<text x="10" y="{row_y:.1f}" class="ascii-row">'
            f'{line_text}'
            f'<animate attributeName="opacity" from="0" to="1" dur="0.2s" begin="{delay:.2f}s" fill="freeze" />'
            f'</text>'
        )

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="370" height="370">
  <style>
    .bg {{ fill: #0d1117; rx: 10px; stroke: #30363d; stroke-width: 1px; }}
    .ascii-row {{ font-family: monospace; font-size: {font_size}px; fill: #8b949e; white-space: pre; }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  <g>
    {"".join(text_lines)}
  </g>
</svg>'''

    with open(output_svg, "w") as f:
        f.write(svg_content)
    print(f"Generated self-typing ASCII SVG '{output_svg}' successfully!")

if __name__ == "__main__":
    img_path = sys.argv[1] if len(sys.argv) > 1 else "source-prepped.png"
    image_to_ascii_svg(img_path)
