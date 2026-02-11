import os
import sys
import time
import subprocess
from datetime import datetime
from PIL import Image

LOGO_PATH = "assets/qiuzhi-restaurant-logo.png"
OUTPUT_DIR = "output"

SCENARIOS = {
    "1": {"name": "春季新品海报 (Spring Poster)", "prompt": "Commercial photography of delicious spring food set menu, mint green and warm orange color palette, C4D style, 3D render, Pop Mart style, blind box toy style, cute and soft, volumetric lighting, high detail, 8k resolution, minimalist composition"},
    "2": {"name": "门店装修设计 (Shop Decoration)", "prompt": "Interior design of a modern trendy chinese restaurant, mint green and warm wood theme, cozy atmosphere, futuristic but warm, C4D render, isometric view, high ceiling, soft lighting, 8k resolution, architectural visualization"},
    "3": {"name": "外卖包装设计 (Packaging Design)", "prompt": "Product photography of restaurant takeout packaging, paper bags and boxes, mint green branding, clean studio lighting, 3D render, high texture, minimalist design, elegant and cute"},
    "4": {"name": "社交媒体推广图 (Social Media)", "prompt": "Close-up shot of a cute 3D character eating dim sum, Pop Mart style, blind box toy, mint green background, soft focus, bokeh, happy expression, high quality render"},
    "5": {"name": "精美菜单设计 (Menu Design)", "prompt": "Graphic design of a restaurant menu layout, high quality paper texture, mint green and orange typography, clean layout, appetizing food photos embedded, 3D render style, elegant and modern"},
    "6": {"name": "员工制服设计 (Staff Uniform)", "prompt": "Fashion design of restaurant staff uniform, apron and t-shirt, mint green color with logo, 3D character wearing the uniform, cute style, clean background, studio lighting"},
    "7": {"name": "精致餐具摆盘 (Tableware)", "prompt": "Top down view of creative table setting, mint green ceramic plates and bowls, wooden chopsticks, delicate plating of chinese food, high end restaurant vibe, 3D render, depth of field"},
    "8": {"name": "门头招牌效果 (Outdoor Signage)", "prompt": "Architectural facade of a restaurant entrance, 3D neon sign with text 'Qiuzhi', mint green glowing light, night view, cozy street atmosphere, C4D render, realistic texture"},
    "9": {"name": "会员卡面设计 (Membership Card)", "prompt": "Design of a premium loyalty card, credit card size, mint green metallic gradient, minimalist 3D logo embossing, high value feel, studio lighting"},
    "10": {"name": "IP公仔盲盒 (IP Character)", "prompt": "A set of collectible blind box toys for the restaurant brand, cute food-themed characters, dumplings and noodles with faces, plastic texture, studio box packaging background, C4D render"}
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def remove_white_bg(img, threshold=220):
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        brightness = (item[0] + item[1] + item[2]) / 3
        if brightness > threshold:
            new_data.append((255, 255, 255, 0))
        elif brightness > threshold - 30:
            alpha = int(255 * (threshold - brightness) / 30)
            new_data.append((item[0], item[1], item[2], alpha))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img

def add_logo(bg_path, logo_path, output_path):
    try:
        bg = Image.open(bg_path).convert("RGBA")
        logo = Image.open(logo_path).convert("RGBA")
        
        logo = remove_white_bg(logo)

        target_width = int(bg.width * 0.35)
        ratio = target_width / logo.width
        target_height = int(logo.height * ratio)
        logo = logo.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        x = bg.width - logo.width
        y = bg.height - logo.height
        
        overlay = Image.new("RGBA", bg.size, (0, 0, 0, 0))
        overlay.paste(logo, (x, y), logo)
        final = Image.alpha_composite(bg, overlay)
        
        final.save(output_path)
        print("✅ Logo 已合成 (智能去底+贴角)")
        return True
    except Exception as e:
        print(f"❌ Logo 错误: {e}")
        return False

def generate(scenario_key):
    scenario = SCENARIOS[scenario_key]
    print(f"\n🚀 生成: {scenario['name']}")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, "scripts", "generate_image.py")
    full_logo_path = os.path.join(current_dir, LOGO_PATH)
    full_output_dir = os.path.join(current_dir, OUTPUT_DIR)
    os.makedirs(full_output_dir, exist_ok=True)

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("❌ 缺 API Key")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    raw_path = os.path.join(full_output_dir, f"{timestamp}-{scenario_key}-raw.png")
    final_path = os.path.join(full_output_dir, f"{timestamp}-{scenario_key}-final.png")

    cmd = [sys.executable, script_path, "--prompt", scenario['prompt'], "--filename", raw_path, "--api-key", api_key]
    
    try:
        subprocess.run(cmd, check=True)
        if os.path.exists(full_logo_path):
            add_logo(raw_path, full_logo_path, final_path)
            print(f"✨ 完成: {final_path}")
        else:
            print(f"⚠️ 无 Logo, 原图: {raw_path}")
    except subprocess.CalledProcessError:
        print("❌ 生成失败")

def main():
    while True:
        clear_screen()
        print("\n=== 秋芝创意中心 (Pro Max) ===")
        for i in range(1, 11):
            key = str(i)
            print(f"[{key:>2}] {SCENARIOS[key]['name']}")
        print("[ q] 退出")
        
        c = input("\n👉 请输入选项: ").strip().lower()
        if c == 'q': break
        if c in SCENARIOS:
            generate(c)
            input("\n按回车继续...")

if __name__ == "__main__":
    main()
