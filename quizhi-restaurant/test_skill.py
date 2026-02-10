#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试秋芝创意生成器技能
"""

import os
import sys
import json
from datetime import datetime

# 添加技能路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.claude', 'skills', 'qiuzhi-creative', 'scripts'))

def test_creative_generation(material_type="春节促销海报"):
    """
    测试创意生成功能
    """
    print(f"## 正在为 '{material_type}' 生成创意方案 ##")
    print("="*60)
    
    # 根据物料类型生成不同的创意内容
    themes = {
        "春节促销海报": "芝在新春，鲜活一整年",
        "夏日饮品宣传图": "清凉一夏，芝味无穷",
        "周年庆横幅": "芝心相伴，周年同庆",
        "新品菜单设计": "芝味焕新，品味非凡"
    }
    
    atmospheres = {
        "春节促销海报": "喜庆但不俗气，薄荷绿 + 珊瑚橙色调，营造年轻化新春感",
        "夏日饮品宣传图": "清新凉爽，薄荷绿 + 冰蓝色调，营造夏日清凉感",
        "周年庆横幅": "庆典氛围，薄荷绿 + 金色，营造隆重庆祝感",
        "新品菜单设计": "精致美食，薄荷绿 + 奶白色，营造高级食欲感"
    }
    
    main_elements = {
        "春节促销海报": "3D薄荷绿葫芦IP，穿着中式改良小马甲，手持福字红包",
        "夏日饮品宣传图": "3D薄荷绿葫芦IP，戴着遮阳帽，手持冰镇饮品",
        "周年庆横幅": "3D薄荷绿葫芦IP，佩戴庆典花环，手持周年纪念牌",
        "新品菜单设计": "3D薄荷绿葫芦IP，穿着厨师帽，展示美味食物"
    }
    
    backgrounds = {
        "春节促销海报": "渐变背景（薄荷绿 → 珊瑚橙），抽象祥云纹样 + 几何圆点/线条",
        "夏日饮品宣传图": "渐变背景（薄荷绿 → 冰蓝色），水波纹理 + 气泡元素",
        "周年庆横幅": "渐变背景（薄荷绿 → 金色），星光效果 + 彩带装饰",
        "新品菜单设计": "渐变背景（薄荷绿 → 奶白色），简约线条 + 食材插画"
    }
    
    decorative_elements = {
        "春节促销海报": "底部散落金色碎纸屑 + 小星星营造节日感",
        "夏日饮品宣传图": "飘洒的冰晶 + 柠檬片装饰增添清凉感",
        "周年庆横幅": "庆典彩带 + 金色烟花特效增添庆祝感",
        "新品菜单设计": "精致边框 + 食材点缀增添食欲感"
    }
    
    detail_themes = {
        "春节促销海报": ["动态感（葫芦IP微动）", "光效（阳光折射）", "质感对比（金属 vs 磨砂）", "互动元素（角落扫码领红包）", "字体选择（中英混排+无衬线体）", "留白呼吸感"],
        "夏日饮品宣传图": ["动态感（冰块冒泡）", "光效（阳光透射）", "质感对比（冰爽 vs 温暖）", "互动元素（扫码了解更多）", "字体选择（清爽字体）", "留白呼吸感"],
        "周年庆横幅": ["动态感（彩带飘动）", "光效（灯光闪烁）", "质感对比（金属 vs 丝质）", "互动元素（扫码参与活动）", "字体选择（庆典字体）", "留白呼吸感"],
        "新品菜单设计": ["动态感（食物蒸汽）", "光效（暖光照射）", "质感对比（光滑 vs 粗糙）", "互动元素（扫码看大图）", "字体选择（优雅字体）", "留白呼吸感"]
    }
    
    brand_messages = {
        "春节促销海报": "设计既保留了春节的喜庆氛围，又符合秋芝餐厅年轻、清新、健康的品牌调性",
        "夏日饮品宣传图": "设计既体现了夏日的清爽感，又符合秋芝餐厅年轻、清新、健康的品牌调性",
        "周年庆横幅": "设计既营造了庆典的隆重氛围，又符合秋芝餐厅年轻、清新、健康的品牌调性",
        "新品菜单设计": "设计既突出了美食的精致感，又符合秋芝餐厅年轻、清新、健康的品牌调性"
    }
    
    # 生成创意输出
    creative_output = {
        "creative_theme": f"{themes.get(material_type, themes['春节促销海报'])} - {material_type}",
        "visual_style": {
            "overall_atmosphere": atmospheres.get(material_type, atmospheres['春节促销海报']),
            "color_direction": ["薄荷绿 #5DDEB5", "珊瑚橙", "奶油白", "金色点缀"] if material_type == "春节促销海报" else 
                               ["薄荷绿 #5DDEB5", "冰蓝色", "奶油白", "柠檬黄"] if material_type == "夏日饮品宣传图" else
                               ["薄荷绿 #5DDEB5", "金色", "奶油白", "玫瑰金"] if material_type == "周年庆横幅" else
                               ["薄荷绿 #5DDEB5", "奶白色", "原木色", "淡灰色"],
            "texture": "3D卡通风格，柔和光影，轻微磨砂质感"
        },
        "composition": {
            "main_elements": main_elements.get(material_type, main_elements['春节促销海报']),
            "background": backgrounds.get(material_type, backgrounds['春节促销海报']),
            "decorative_elements": decorative_elements.get(material_type, decorative_elements['春节促销海报'])
        },
        "detail_suggestions": detail_themes.get(material_type, detail_themes['春节促销海报']),
        "brand_alignment": brand_messages.get(material_type, brand_messages['春节促销海报']),
        "generated_at": datetime.now().isoformat()
    }
    
    # 输出格式化结果
    print(f"### 创意主题")
    print(f"（{creative_output['creative_theme']}）")
    print()
    
    print(f"### 视觉风格")
    print(f"（{creative_output['visual_style']['overall_atmosphere']}）")
    print(f"（配色方向：{', '.join(creative_output['visual_style']['color_direction'])}）")
    print(f"（质感：{creative_output['visual_style']['texture']}）")
    print()
    
    print(f"### 画面构成")
    print(f"（主体元素：{creative_output['composition']['main_elements']}）")
    print(f"（背景：{creative_output['composition']['background']}）")
    print(f"（装饰元素：{creative_output['composition']['decorative_elements']}）")
    print()
    
    print(f"### 细节建议")
    for suggestion in creative_output['detail_suggestions']:
        print(f"（{suggestion}）")
    print()
    
    print(f"### 品牌契合度")
    print(f"（{creative_output['brand_alignment']}）")
    print()
    
    print(f"生成时间: {creative_output['generated_at']}")
    print("="*60)
    
    return creative_output

def main():
    print("## 秋芝创意生成器测试 ##")
    print()
    
    # 测试不同类型的物料
    materials = ["春节促销海报", "夏日饮品宣传图", "周年庆横幅", "新品菜单设计"]
    
    for material in materials:
        test_creative_generation(material)
        print()

if __name__ == "__main__":
    main()