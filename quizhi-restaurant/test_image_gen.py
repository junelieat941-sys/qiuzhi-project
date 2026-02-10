#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试秋芝餐厅图像生成功能
"""

import os
import google.generativeai as genai
from pathlib import Path

# 从环境变量读取 API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("错误：请设置 GOOGLE_API_KEY 环境变量")
    exit(1)

# 初始化模型
genai.configure(api_key=api_key)

# 测试可用的图像生成模型
print("正在测试图像生成功能...")

try:
    # 尝试使用图像生成模型
    model_name = "models/gemini-3-pro-image-preview"
    model = genai.GenerativeModel(model_name)
    
    # 测试提示
    test_prompt = """
    Create an image for a spring seasonal drink poster for Qiuzhi Restaurant.
    Include the signature mint green (#5DDEB5) 3D cartoon gourd mascot character,
    fresh and healthy drinks, clean modern aesthetic, appetizing presentation.
    Style should be 3D cartoon with soft lighting, friendly and inviting atmosphere.
    """
    
    print(f"使用模型: {model_name}")
    print("正在生成图像... (这可能需要一些时间)")
    
    # 尝试生成内容
    response = model.generate_content(test_prompt)
    
    if response.text:
        print("✅ API 调用成功!")
        print(f"响应内容: {response.text[:200]}...")
    else:
        print("⚠️  API 调用完成但没有返回文本内容")
        
except Exception as e:
    print(f"❌ 图像生成测试失败: {str(e)}")
    print("可能的原因:")
    print("1. 模型不支持图像生成")
    print("2. API 密钥权限不足")
    print("3. 模型名称错误")
    
    # 尝试其他可能的图像生成模型
    potential_models = [
        "models/gemini-2.0-flash-exp-image-generation",
        "models/gemini-2.5-flash-image",
        "models/gemini-3-pro-image-preview"
    ]
    
    for alt_model in potential_models:
        try:
            print(f"\n尝试替代模型: {alt_model}")
            alt_model_obj = genai.GenerativeModel(alt_model)
            response = alt_model_obj.generate_content("Describe a simple mint green cartoon character for a restaurant brand.")
            print(f"✅ 模型 {alt_model} 可用")
            break
        except Exception as alt_e:
            print(f"❌ 模型 {alt_model} 不可用: {str(alt_e)}")