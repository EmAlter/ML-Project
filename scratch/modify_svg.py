import xml.etree.ElementTree as ET
import re
import math

svg_file = r'c:\Users\dimag\Desktop\Modello di Dominio - Stage.svg'

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
tree = ET.parse(svg_file)
root = tree.getroot()
ns = {'svg': 'http://www.w3.org/2000/svg'}

def parse_translate(transform_str):
    if not transform_str: return 0, 0
    m = re.search(r'translate\(([\d.-]+),([\d.-]+)\)', transform_str)
    if m:
        return float(m.group(1)), float(m.group(2))
    return 0, 0

nodes = []

# Find all nodes. A node seems to be a <g> with a <rect> and <text>
for g in root.findall('.//svg:g', ns):
    texts = g.findall('svg:text', ns)
    rect = g.find('svg:rect', ns)
    if texts and rect is not None:
        name = texts[0].text.strip().lower()
        if ':' in name or name in ['1', '0..1', '0..n', '1..n'] or '►' in name or '◄' in name or '▼' in name or '▲' in name:
            continue
        if 'testo' in name:
            continue
        if name in ['pre', 'post']:
            continue
        
        # Modify the g tag for nodes
        g.set('id', name.replace(' ', '-'))
        g.set('class', 'uml-class')
        
        tx, ty = parse_translate(g.get('transform', ''))
        width = float(rect.get('width', 0))
        height = float(rect.get('height', 0))
        x = float(rect.get('x', 0))
        y = float(rect.get('y', 0))
        
        nodes.append({
            'name': name.replace(' ', '-'),
            'x1': tx + x,
            'y1': ty + y,
            'x2': tx + x + width,
            'y2': ty + y + height
        })

print(f'Found {len(nodes)} nodes')
for n in nodes:
    print(n['name'])

def dist(px, py, node):
    dx = max(node['x1'] - px, 0, px - node['x2'])
    dy = max(node['y1'] - py, 0, py - node['y2'])
    return math.sqrt(dx*dx + dy*dy)

def get_closest_node(px, py):
    min_d = float('inf')
    closest = None
    for n in nodes:
        d = dist(px, py, n)
        if d < min_d:
            min_d = d
            closest = n
    return closest, min_d

# Paths usually have a 'd' attribute like 'M x y L x y'
for g in root.findall('.//svg:g', ns):
    paths = g.findall('svg:path', ns)
    if not paths: continue
    
    # Exclude nodes that we already processed (they have id)
    if g.get('id'): continue
    
    # Exclude <g> that are just bounding boxes or clip paths?
    # Some <g> elements just wrap paths. Let's see if this <g> has rect
    rect = g.find('svg:rect', ns)
    if rect is not None: continue
    
    # Also some paths are inside clipPath definitions, avoid those
    # We are searching starting from root, but let's avoid <defs>
    
    # Get all points from paths
    d = ''
    for p in paths:
        d_attr = p.get('d', '')
        # Only consider paths that look like connections
        if 'M' in d_attr or 'L' in d_attr:
            d += d_attr + ' '
    
    points = re.findall(r'[ML]\s*([\d.-]+)\s+([\d.-]+)', d)
    if not points or len(points) < 2: continue
    
    tx, ty = parse_translate(g.get('transform', ''))
    
    px1 = float(points[0][0]) + tx
    py1 = float(points[0][1]) + ty
    
    px2 = float(points[-1][0]) + tx
    py2 = float(points[-1][1]) + ty
    
    n1, d1 = get_closest_node(px1, py1)
    n2, d2 = get_closest_node(px2, py2)
    
    # For a connection, the start and end should be somewhat close to nodes
    if n1 and n2 and d1 < 50 and d2 < 50:
        for p in paths:
            if p.get('fill') == 'white' or p.get('stroke') == 'none':
                # Possibly part of arrow head or fill, let's just add the class to all paths representing the connection.
                # The instructions said "tutti i tag <path> che rappresentano i collegamenti"
                pass
            p.set('class', 'uml-link')
            p.set('data-connects', f"{n1['name']} {n2['name']}")

# Now also need to remove the first xml declaration if ET.write adds it and it's already there
tree.write(svg_file, encoding='UTF-8', xml_declaration=True)
print('Done writing modified file')

