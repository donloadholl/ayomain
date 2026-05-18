import random
from datetime import datetime

# ====================================================================
# BOT GENERATOR PROMPT AI V1.7 - DAILY UNIQUE AUTO-GENERATE (ANTI-BLOCK)
# ====================================================================

# Bank Data Dasar Elemen Abstract Fluid
subjek_abstract = ["liquid gold wave", "holographic fluid ripples", "pastel marble acrylic pour", "cyberpunk neon magma", "emerald royal silk", "cosmic nebula splash", "translucent glass ocean", "metallic chrome vortex", "sunset gradient flow", "minimalist monochrome smoke", "amethyst crystal fluid", "iridescent pearl wave"]
gaya_abstract = ["luxury aesthetic", "futuristic synthwave vibe", "cozy elegant background", "highly contrast", "glossy premium finish", "dreamy ethereal mood", "bold digital art style", "smooth color blending", "high-end wallpaper design", "mesmerizing geometric flow"]

# Bank Data Dasar Elemen 3D Isometric
subjek_isometric = ["cozy gaming room setup", "futuristic cyberpunk street alley", "miniature warm coffee shop", "smart tech workspace office", "magic wizard laboratory", "modern plants greenhouse", "digital cloud server room", "crypto mining farm", "minimalist virtual art gallery", "kawaii bedroom interior", "retro arcade zone", "mini space station cabin"]
detail_isometric = ["with glowing neon PC and soft lighting", "with giant smartphone and floating boxes", "with holographic screens and robotic arms", "with ancient books and bubbling potions", "with pastel color palette and cute low poly furniture", "with rainy glossy floor reflections", "with detailed miniature foliage and glass walls", "with isometric grid layout and 3d render", "with cozy cyber aesthetic", "with bright cinematic studio lighting"]

# Menggunakan seed berdasarkan tanggal hari ini agar kombinasi 100% unik setiap harinya
hari_ini = datetime.now().strftime("%Y%m%d")
random.seed(int(hari_ini))

# Acak urutan database berdasarkan seed tanggal hari ini
random.shuffle(subjek_abstract)
random.shuffle(gaya_abstract)
random.shuffle(subjek_isometric)
random.shuffle(detail_isometric)

html_grid_gambar = ""

# 1. GENERATE 6 PROMPT ABSTRACT UNIK UNTUK HARI INI
for i in range(6):
    subjek = subjek_abstract[i]
    gaya = gaya_abstract[i]
    title = subjek.title()
    prompt_final = f"abstract {subjek}, {gaya}, highly detailed, 8k resolution, commercial microstock trend, professional studio lighting"
    
    html_grid_gambar += f'''
    <div class="ai-card">
        <div class="image-box">
            <img src="https://images.unsplash.com/photo-1618005198143-e5283b519a7f?w=400" alt="Abstract">
            <span class="category-badge">ABSTRACT FLUID</span>
        </div>
        <div class="ai-info">
            <div class="ai-title">{title}</div>
            <textarea class="prompt-box" readonly onclick="this.select(); document.execCommand('copy'); alert('Prompt berhasil disalin!');">{prompt_final}</textarea>
            <p style="font-size:10px; color:#6b7280; margin:5px 0 0 0;">💡 Klik teks untuk menyalin otomatis</p>
        </div>
    </div>
    '''

# 2. GENERATE 6 PROMPT ISOMETRIC UNIK UNTUK HARI INI
for i in range(6):
    subjek = subjek_isometric[i]
    detail = detail_isometric[i]
    title = subjek.title()
    prompt_final = f"cute 3d isometric {subjek} {detail}, unreal engine 5 render, vibrant flat colors, low poly model, microstock seller trend, smooth shading"
    
    html_grid_gambar += f'''
    <div class="ai-card">
        <div class="image-box">
            <img src="https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=400" alt="Isometric">
            <span class="category-badge">3D ISOMETRIC</span>
        </div>
        <div class="ai-info">
            <div class="ai-title">{title}</div>
            <textarea class="prompt-box" readonly onclick="this.select(); document.execCommand('copy'); alert('Prompt berhasil disalin!');">{prompt_final}</textarea>
            <p style="font-size:10px; color:#6b7280; margin:5px 0 0 0;">💡 Klik teks untuk menyalin otomatis</p>
        </div>
    </div>
    '''

isi_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asisten Riset AI Studio 21</title>
    <style>
        body {{ background-color: #0b0f19; color: #f3f4f6; font-family: sans-serif; margin: 0; padding: 0; }}
        .header {{ background: linear-gradient(135deg, #0f172a, #1e1b4b); padding: 30px 15px; text-align: center; border-bottom: 2px solid #3b82f6; }}
        .header h1 {{ margin: 0; font-size: 24px; color: #38bdf8; }}
        .header p {{ margin: 8px 0 0 0; font-size: 13px; color: #9ca3af; }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 20px; }}
        .grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; }}
        @media(min-width: 600px) {{ .grid {{ grid-template-columns: repeat(4, 1fr); }} }}
        .ai-card {{ background: #111827; border-radius: 8px; overflow: hidden; border: 1px solid #1f2937; padding-bottom: 10px; margin-bottom: 10px; }}
        .image-box {{ position: relative; width: 100%; padding-top: 100%; background: #000; }}
        .image-box img {{ position: absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; }}
        .category-badge {{ position: absolute; top: 8px; right: 8px; background: #2563eb; color: white; padding: 3px 8px; font-size: 9px; font-weight: bold; border-radius: 4px; }}
        .ai-info {{ padding: 12px 10px; text-align: center; }}
        .ai-title {{ font-size: 13px; font-weight: bold; margin-bottom: 8px; color: #38bdf8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
        .prompt-box {{ width: 90%; height: 65px; background: #1f2937; color: #e5e7eb; border: 1px solid #374151; border-radius: 4px; padding: 5px; font-size: 11px; font-family: monospace; resize: none; cursor: pointer; text-align: left; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>AI STUDIO 21 - PRIVATE PANEL</h1>
        <p>📋 Engine: Auto-Combination 6 AM | Update otomatis setiap pukul 06.00 Pagi.</p>
    </div>
    <div class="container"><div class="grid">{html_grid_gambar}</div></div>
</body>
</html>
'''

with open("index.html", "w") as f:
    f.write(isi_html)

print("-> BERHASIL: Script pendeteksi tanggal unik telah siap!")
