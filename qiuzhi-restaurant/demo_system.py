#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
秋芝创意生成器演示系统
完整展示系统功能，包括创意生成和图像生成流程
"""

import os
import sys
import json
from datetime import datetime
import subprocess

def display_demo_header():
    """显示演示头部"""
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 18 + "秋芝创意生成器演示" + " " * 18 + "║")
    print("║" + " " * 15 + "A FRESH, MODERN BITE" + " " * 15 + "║")
    print("║" + " " * 12 + "健康轻食主义 · 3D萌虾IP" + " " * 12 + "║")
    print("╚" + "═" * 60 + "╝")
    print()

def demo_creative_generation(material_type):
    """演示创意生成功能"""
    print(f"🎯 步骤 1: 为 '{material_type}' 生成创意方案")
    print("="*80)
    
    # 导入主程序的创意生成功能
    sys.path.insert(0, os.path.dirname(__file__))
    from main import generate_creative_for_material
    
    # 生成创意方案
    creative_output = generate_creative_for_material(material_type)
    
    print()
    return creative_output

def demo_image_generation_capability(material_type, creative_desc):
    """演示图像生成能力说明"""
    print(f"🖼️  步骤 2: 图像生成能力")
    print("="*80)
    
    # 检查API密钥
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        print("✅ API密钥已设置")
        print("📋 准备生成图像...")
        print(f"📝 使用创意描述生成图像: {material_type}")
        print()
        print("💡 实际图像生成需要调用Google Gemini API，这可能需要:")
        print("   - 网络连接到Google服务")
        print("   - API调用配额")
        print("   - 适当的模型权限")
        print()
        print("🔧 如果要生成实际图像，请使用以下命令:")
        print(f"   python .claude/skills/qiuzhi-creative/scripts/generate_image.py \"{creative_desc}\" ./output")
    else:
        print("⚠️  未检测到Google API密钥")
        print("   要启用图像生成功能，请设置环境变量:")
        print("   export GOOGLE_API_KEY='your_api_key_here'")
        print()
        print("📋 创意方案已生成，可使用以下方式创建实际图像:")
        print("   1. 将创意方案交给设计师")
        print("   2. 使用AI图像生成工具（如Midjourney、DALL-E）")
        print("   3. 在Figma、Photoshop等设计软件中实现")
    
    print("="*80)
    print()

def demo_brand_compliance_check(creative_output):
    """演示品牌合规检查"""
    print(f"✅ 步骤 3: 品牌合规性检查")
    print("="*80)
    
    # 检查品牌元素是否包含
    brand_elements = [
        "薄荷绿 #5DDEB5",
        "3D卡通",
        "萌虾IP",
        "清新时尚",
        "年轻活力"
    ]
    
    compliant_elements = []
    for element in brand_elements:
        # 检查创意输出中是否包含品牌元素
        output_text = str(creative_output)
        if element.lower() in output_text.lower():
            compliant_elements.append(element)
    
    print(f"品牌元素合规检查:")
    for element in brand_elements:
        status = "✅" if element in str(creative_output) else "❌"
        print(f"  {status} {element}")
    
    print()
    print(f"合规率: {len(compliant_elements)}/{len(brand_elements)}")
    print("品牌一致性: 高" if len(compliant_elements) >= len(brand_elements) - 1 else "中")
    print("="*80)
    print()

def main():
    display_demo_header()
    
    # 默认物料类型
    material_type = "春季新品海报"
    
    # 如果提供了参数，使用参数
    if len(sys.argv) > 1:
        material_type = sys.argv[1]
    
    print(f"🚀 开始演示秋芝创意生成器完整流程")
    print(f"📋 物料类型: {material_type}")
    print()
    
    # 步骤1: 生成创意方案
    creative_output = demo_creative_generation(material_type)
    
    # 步骤2: 演示图像生成能力
    demo_image_generation_capability(material_type, creative_output['creative_theme'])
    
    # 步骤3: 品牌合规检查
    demo_brand_compliance_check(creative_output)
    
    print("🎉 演示完成!")
    print()
    print("💡 系统特点:")
    print("   • 自动生成符合品牌规范的创意方案")
    print("   • 包含完整的视觉指导（颜色、风格、构图）")
    print("   • 支持多种物料类型")
    print("   • 确保品牌一致性")
    print("   • 可扩展的图像生成功能")

if __name__ == "__main__":
    main()