#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
秋芝创意生成器 - 快速开始
"""

import os
import sys

def display_welcome():
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "欢迎使用秋芝创意生成器" + " " * 18 + "║")
    print("║" + " " * 15 + "A FRESH, MODERN BITE" + " " * 15 + "║")
    print("║" + " " * 12 + "健康轻食主义 · 3D萌虾IP" + " " * 12 + "║")
    print("╚" + "═" * 60 + "╝")
    print()

def display_menu():
    print("📋 请选择您要创建的物料类型：")
    print()
    print("1.  🎨 海报设计")
    print("    - 春季新品海报")
    print("    - 夏日饮品海报") 
    print("    - 节日促销海报")
    print("    - 活动宣传海报")
    print()
    print("2.  📄 菜单设计")
    print("    - 新品菜单设计")
    print("    - 套餐菜单")
    print("    - 价目表")
    print("    - 季节性菜单")
    print()
    print("3.  📦 包装设计")
    print("    - 外卖餐盒包装")
    print("    - 饮品杯套")
    print("    - 打包袋设计")
    print("    - 礼品包装")
    print()
    print("4.  🏯 横幅设计")
    print("    - 店铺横幅")
    print("    - 易拉宝设计")
    print("    - 展架设计")
    print("    - 年庆横幅")
    print()
    print("5.  📱 社媒素材")
    print("    - 小红书封面")
    print("    - 微博配图")
    print("    - 朋友圈配图")
    print("    - 抖音封面")
    print()
    print("6.  💡 自定义物料")
    print("    - 输入您想要的任意物料类型")
    print()
    print("7.  ℹ️  查看系统信息")
    print("8.  📚 查看完整使用说明")
    print("9.  ❓ 帮助")
    print("0.  🚪 退出")
    print()

def get_user_choice():
    try:
        choice = input("请输入您的选择 (0-9): ").strip()
        return choice
    except KeyboardInterrupt:
        print("\n\n👋 感谢使用秋芝创意生成器！")
        sys.exit(0)

def handle_choice(choice):
    if choice == "0":
        print("👋 感谢使用秋芝创意生成器！")
        sys.exit(0)
    elif choice == "1":
        print("\n🎨 请选择海报类型：")
        print("  1.1 - 春季新品海报")
        print("  1.2 - 夏日饮品海报")
        print("  1.3 - 节日促销海报")
        print("  1.4 - 活动宣传海报")
        print("  1.5 - 自定义海报")
        sub_choice = input("请选择 (1.1-1.5): ").strip()
        
        if sub_choice == "1.1":
            material = "春季新品海报"
        elif sub_choice == "1.2":
            material = "夏日饮品海报"
        elif sub_choice == "1.3":
            material = "节日促销海报"
        elif sub_choice == "1.4":
            material = "活动宣传海报"
        elif sub_choice == "1.5":
            material = input("请输入自定义海报类型: ")
        else:
            print("❌ 无效选择，使用默认海报")
            material = "创意海报"
            
        generate_creative(material)
    elif choice == "2":
        print("\n📄 请选择菜单类型：")
        print("  2.1 - 新品菜单设计")
        print("  2.2 - 套餐菜单")
        print("  2.3 - 价目表")
        print("  2.4 - 季节性菜单")
        print("  2.5 - 自定义菜单")
        sub_choice = input("请选择 (2.1-2.5): ").strip()
        
        if sub_choice == "2.1":
            material = "新品菜单设计"
        elif sub_choice == "2.2":
            material = "套餐菜单"
        elif sub_choice == "2.3":
            material = "价目表"
        elif sub_choice == "2.4":
            material = "季节性菜单"
        elif sub_choice == "2.5":
            material = input("请输入自定义菜单类型: ")
        else:
            print("❌ 无效选择，使用默认菜单")
            material = "菜单设计"
            
        generate_creative(material)
    elif choice == "3":
        print("\n📦 请选择包装类型：")
        print("  3.1 - 外卖餐盒包装")
        print("  3.2 - 饮品杯套")
        print("  3.3 - 打包袋设计")
        print("  3.4 - 礼品包装")
        print("  3.5 - 自定义包装")
        sub_choice = input("请选择 (3.1-3.5): ").strip()
        
        if sub_choice == "3.1":
            material = "外卖餐盒包装"
        elif sub_choice == "3.2":
            material = "饮品杯套"
        elif sub_choice == "3.3":
            material = "打包袋设计"
        elif sub_choice == "3.4":
            material = "礼品包装"
        elif sub_choice == "3.5":
            material = input("请输入自定义包装类型: ")
        else:
            print("❌ 无效选择，使用默认包装")
            material = "包装设计"
            
        generate_creative(material)
    elif choice == "4":
        print("\n🏯 请选择横幅类型：")
        print("  4.1 - 店铺横幅")
        print("  4.2 - 易拉宝设计")
        print("  4.3 - 展架设计")
        print("  4.4 - 年庆横幅")
        print("  4.5 - 自定义横幅")
        sub_choice = input("请选择 (4.1-4.5): ").strip()
        
        if sub_choice == "4.1":
            material = "店铺横幅"
        elif sub_choice == "4.2":
            material = "易拉宝设计"
        elif sub_choice == "4.3":
            material = "展架设计"
        elif sub_choice == "4.4":
            material = "年庆横幅"
        elif sub_choice == "4.5":
            material = input("请输入自定义横幅类型: ")
        else:
            print("❌ 无效选择，使用默认横幅")
            material = "横幅设计"
            
        generate_creative(material)
    elif choice == "5":
        print("\n📱 请选择社媒素材类型：")
        print("  5.1 - 小红书封面")
        print("  5.2 - 微博配图")
        print("  5.3 - 朋友圈配图")
        print("  5.4 - 抖音封面")
        print("  5.5 - 自定义社媒素材")
        sub_choice = input("请选择 (5.1-5.5): ").strip()
        
        if sub_choice == "5.1":
            material = "小红书封面"
        elif sub_choice == "5.2":
            material = "微博配图"
        elif sub_choice == "5.3":
            material = "朋友圈配图"
        elif sub_choice == "5.4":
            material = "抖音封面"
        elif sub_choice == "5.5":
            material = input("请输入自定义社媒素材类型: ")
        else:
            print("❌ 无效选择，使用默认社媒素材")
            material = "社媒配图"
            
        generate_creative(material)
    elif choice == "6":
        material = input("\n💡 请输入您想要的物料类型: ")
        generate_creative(material)
    elif choice == "7":
        show_system_info()
    elif choice == "8":
        show_documentation()
    elif choice == "9":
        show_help()
    else:
        print("❌ 无效选择，请重新输入")
        return False
    return True

def generate_creative(material):
    print(f"\n🚀 正在为 '{material}' 生成创意方案...")
    print()
    
    # 导入并运行主程序
    from main import generate_creative_for_material
    result = generate_creative_for_material(material)
    
    print()
    print("✨ 创意方案生成完成！")
    print()
    
    # 询问是否需要图像生成
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if api_key:
        gen_image = input("🖼️  是否需要生成图像文件? (y/n): ").strip().lower()
        if gen_image == 'y':
            print("\n🔧 正在生成图像文件...")
            import subprocess
            from datetime import datetime
            
            # 创建输出目录
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
            os.makedirs(output_dir, exist_ok=True)
            
            # 生成带时间戳的文件名
            timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            filename = f"{timestamp}-creative.png"
            output_path = os.path.join(output_dir, filename)
            
            # 构建完整的 prompt
            prompt = f"{result['creative_theme']}。{result.get('visual_style', '')} {result.get('main_elements', '')}"
            
            # 查找脚本路径
            script_paths = [
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts/generate_image.py"),
                os.path.expanduser("~/.openclaw/workspace/skills/qiuzhi-creative/scripts/generate_image.py"),
            ]
            script_path = None
            for p in script_paths:
                if os.path.exists(p):
                    script_path = p
                    break
            
            # 查找 Logo 路径
            logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "qiuzhi-restaurant-logo.png")
            
            if script_path:
                cmd = [
                    "uv", "run", script_path,
                    "--prompt", prompt,
                    "--filename", output_path,
                    "--resolution", "1K",
                    "--api-key", api_key
                ]
                
                # 如果 Logo 存在，则加入指令
                if os.path.exists(logo_path):
                    print("   检测到品牌 Logo，将自动应用...")
                    cmd.extend(["-i", logo_path])
                    # 更新 prompt，指导 AI 如何使用 Logo
                    cmd[4] = f"根据这段文字描述 '{prompt}' 生成一张图片，并把输入的 Logo 图片优雅地、不突兀地融合到画面的角落（比如右下角），保持整体风格协调。"

                print(f"   Prompt: {cmd[4][:60]}...")
                print(f"   输出路径: {output_path}")
                try:
                    result_proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
                    if result_proc.returncode == 0:
                        print(f"\n✅ 图像生成成功！")
                        print(f"   保存位置: {output_path}")
                    else:
                        print(f"\n❌ 图像生成失败: {result_proc.stderr}")
                except subprocess.TimeoutExpired:
                    print("\n⏰ 图像生成超时，请稍后重试")
                except Exception as e:
                    print(f"\n❌ 生成出错: {e}")
            else:
                print("❌ 未找到图像生成脚本，请确保已安装 qiuzhi-creative skill")
    else:
        print("💡 提示: 如需生成图像文件，请先设置 Google API 密钥")
        print("   命令: export GOOGLE_API_KEY='your_api_key_here'")
    
    print()
    continue_choice = input("🔄 是否继续创建其他物料? (y/n): ").strip().lower()
    if continue_choice != 'y':
        print("\n👋 感谢使用秋芝创意生成器！")
        sys.exit(0)

def show_system_info():
    print("""
📊 系统信息
═══════════════════════════════════════════════════════════════

品牌信息:
┌─────────────────────────────────────────────────────────────┐
│ • 品牌名称: 秋芝餐厅                                        │
│ • 品牌口号: A FRESH, MODERN BITE 健康轻食主义                │
│ • 主色调: 薄荷绿 #5DDEB5                                   │
│ • IP形象: 3D薄荷绿卡通萌虾                                  │
│ • 风格定位: 3D卡通、清新时尚、年轻活力                       │
└─────────────────────────────────────────────────────────────┘

系统功能:
• 创意方案生成 ✓
• 品牌合规检查 ✓  
• 多种物料支持 ✓
• 图像生成功能 (需API密钥) ✓

支持物料类型:
• 海报设计 (促销、活动、新品等)
• 菜单设计 (套餐、价目、季节性等) 
• 包装设计 (外卖、饮品、礼品等)
• 横幅设计 (店铺、展架、庆典等)
• 社媒素材 (小红书、微博、朋友圈等)

系统状态: 正常运行
""")
    
    input("\n按回车键返回主菜单...")

def show_documentation():
    print("""
📖 完整使用说明
═══════════════════════════════════════════════════════════════

1. 快速开始
   直接运行: python main.py "物料类型"
   示例: python main.py "春季新品海报"

2. 系统演示
   运行: python demo_system.py "物料类型"

3. 图像生成 (需API密钥)
   设置API密钥: export GOOGLE_API_KEY='your_api_key_here'
   生成图像: python generate_image.py "创意描述" ./output

4. 查看支持类型
   运行: python main.py --help-more

5. 查看项目结构
   运行: cat README.md

系统特点:
• 自动生成符合品牌规范的创意方案
• 包含完整的视觉指导（颜色、风格、构图）
• 支持多种物料类型
• 确保品牌一致性
• 可扩展的图像生成功能
""")
    
    input("\n按回车键返回主菜单...")

def show_help():
    print("""
❓ 帮助信息
═══════════════════════════════════════════════════════════════

常见问题:

Q: 如何生成创意方案?
A: 在主菜单中选择相应物料类型，或直接运行:
   python main.py "物料类型"

Q: 如何生成实际图像?
A: 需要设置Google API密钥:
   export GOOGLE_API_KEY='your_api_key_here'
   然后运行图像生成脚本

Q: 支持哪些物料类型?
A: 海报、菜单、包装、横幅、社媒素材等多种类型

Q: 如何确保品牌一致性?
A: 系统自动检查品牌元素并确保合规性

Q: 可以自定义物料类型吗?
A: 可以，在主菜单选择"自定义物料"或直接输入物料类型

技术支持:
如有问题请联系系统管理员
""")
    
    input("\n按回车键返回主菜单...")

def main():
    display_welcome()
    
    while True:
        display_menu()
        choice = get_user_choice()
        success = handle_choice(choice)
        if not success:
            continue

if __name__ == "__main__":
    main()