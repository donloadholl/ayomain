import requests

# ====================================================================
# BOT GENERATOR CATALOG IMAGES AI V1.1 - FOCUS: ABSTRACT & ISOMETRIC 3D
# ====================================================================

html_grid_gambar = ""
kunci_api = "43874312-d04b90be8800ba83fe1f4e135"

kategori_target = [
    {"nama": "Abstract Fluid", "query": "abstract+liquid+background"},
    {"nama": "3D Isometric", "query": "ai+generated+3d+isometric"}
]

try:
    print("-> Sedang mengorek 2 tren gambar AI terbesar (Abstract & 3D Isometric)...")
    
    for kat in kategori_target:
        url_api = f"https://pixabay.com/api/?key={kunci_api}&q={kat['query']}&image_type=photo&per_page=6"
        respon = requests.get(url_api, timeout=10)
        data = respon.json()
        
        if data.get('hits'):
            for item in data['hits']:
                img_url = item['webformatURL']
                tags = item['tags'].split(',')[0].title()
                
                html_grid_gambar += f'''
                <div class="ai-card">
                    <div class="image-box">
                        <img src="{img_url}" alt="{tags}">
                        <span class="category-badge">{kat['nama'].upper()}</span>
                    </div>
                    <div class="ai-info">
                        <div class="ai-title">{tags} Art Style</div>
                        <button class="btn-action">COPY PROMPT TEXT</button>
                    </div>
                </div>
                '''
except Exception as e:
    print(f"Gagal mengambil tren live, mengaktifkan database cadangan: {e}")

if not html_grid_gambar:
    gambar_backup = [
        {"t": "Abstract Liquid Gold Wave", "url": "https://images.unsplash.com/photo-1618005198143-e5283b519a7f?w=400", "k": "ABSTRACT"},
        {"t": "Isometric Cute 3D Room", "url": "https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=400", "k": "3D ISOMETRIC"}
    ]
    for g in gambar_backup:
        html_grid_gambar += f'''
        <div class="ai-card">
            <div class="image-box">
                <img src="{g['url']}" alt="{g['t']}">
                <span class="category-badge">{g['k']}</span>
            </div>
            <div class="ai-info">
                <div class="ai-title">{g['t']}</div>
                <button class="btn-action">COPY PROMPT TEXT</button>
            </div>
        </div>
        '''

# LINK UTAMA ADSTERRA KAMU
link_tujuan = "https://www.effectivecpmnetwork.com/u3rqmqpr?key=502be02a558974252ae25de6c2459482"

isi_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Studio 21 - Top Premium Prompts & Visual Assets</title>
    <style>
        body {{ background-color: #0b0f19; color: #f3f4f6; font-family: sans-serif; margin: 0; padding: 0; }}
        .header {{ background: linear-gradient(135deg, #0f172a, #1e1b4b); padding: 35px 15px; text-align: center; border-bottom: 2px solid #3b82f6; }}
        .header h1 {{ margin: 0; font-size: 26px; color: #38bdf8; }}
        .header p {{ margin: 8px 0 0 0; font-size: 13px; color: #9ca3af; }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 20px; }}
        .grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; }}
        @media(min-width: 600px) {{ .grid {{ grid-template-columns: repeat(4, 1fr); }} }}
        .ai-card {{ background: #111827; border-radius: 8px; overflow: hidden; border: 1px solid #1f2937; }}
        .image-box {{ position: relative; width: 100%; padding-top: 100%; background: #000; }}
        .image-box img {{ position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; }}
        .category-badge {{ position: absolute; top: 8px; right: 8px; background: #2563eb; color: white; padding: 3px 8px; font-size: 9px; font-weight: bold; border-radius: 4px; }}
        .ai-info {{ padding: 12px 10px; text-align: center; }}
        .ai-title {{ font-size: 13px; font-weight: bold; margin-bottom: 8px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: #e5e7eb; }}
        .btn-action {{ background: #2563eb; color: white; border: none; width: 100%; padding: 9px; font-size: 11px; font-weight: bold; border-radius: 4px; cursor: pointer; }}
        .click-layer {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999; cursor: pointer; }}
    </style>
</head>
<body>
    <a href="{link_tujuan}" target="_blank" class="click-layer"></a>
    <div class="header">
        <h1>AI STUDIO 21</h1>
        <p>Eksplorasi Ide Prompt Terlaris: Abstract Background & 3D Isometric Design</p>
    </div>
    <div class="container"><div class="grid">{html_grid_gambar}</div></div>
</body>
</html>
'''

with open("index.html", "w") as f:
    f.write(isi_html)

print("-> BERHASIL: File index.html prompt AI super fokus telah dicetak!")
