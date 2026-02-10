# 秋芝餐厅 (Qiuzhi Restaurant)
# Qiuzhi Restaurant Project

一个专注于**秋芝餐厅**品牌创意与自动化运营的 Python 项目。集成 Google Gemini API，实现智能设计与内容生成。
A Python project dedicated to the creative branding and automated operations of **Qiuzhi Restaurant**. Integrated with Google Gemini API for intelligent design and content generation.

---

## 🚀 快速开始 (30 秒)
## 🚀 Quick Start (30 Seconds)

如果您使用 GitHub Codespaces，则无需安装任何环境！
No installation required if you use GitHub Codespaces!

1.  **Fork 此仓库**
    **Fork this Repository**
    点击页面右上角的 **Fork** 按钮。
    Click the **Fork** button at the top right of this page.

2.  **在 Codespaces 中打开**
    **Open in Codespaces**
    - 点击绿色的 **Code** 按钮。
      Click the green **Code** button.
    - 切换到 **Codespaces** 标签页。
      Switch to the **Codespaces** tab.
    - 点击 **Create codespace on main**。
      Click **Create codespace on main**.

3.  **运行餐厅系统**
    **Run the System**
    终端准备好后，运行以下命令启动创意中心：
    Once the terminal is ready, run the following command to start the creative hub:

    ```bash
    # 安装依赖 / Install dependencies
    pip install google-genai pillow

    # 运行创意生成器 (需要 API Key) / Run the generator (Requires GOOGLE_API_KEY)
    # export GOOGLE_API_KEY="your_api_key_here"
    python3 start_here.py
    ```

---

## 🔑 必要条件
## 🔑 Requirements

运行此项目需要：
To run this project, you need:

-   **Google Gemini API Key**: 可在 [Google AI Studio](https://aistudio.google.com/) 免费获取。
    **Google Gemini API Key**: Get one for free at [Google AI Studio](https://aistudio.google.com/).

---

## 📂 项目结构
## 📂 Project Structure

-   `start_here.py`: **创意控制台**。生成菜单、海报、文案的核心入口。
    **Creative Console**. The core entry point for generating menus, posters, and copy.
-   `scripts/generate_image.py`: **图像生成引擎**。
    **Image Generation Engine**.
-   `assets/`: **品牌资产库**。存放 Logo、吉祥物等核心素材。
    **Brand Assets**. Stores core materials like logos and mascots.
-   `output/`: **成品展示区**。生成的最终设计图将保存在这里。
    **Output Gallery**. Final generated designs will be saved here.

---

## 🤝 贡献
## 🤝 Contributing

欢迎为秋芝餐厅的数字化建设添砖加瓦！
Welcome to contribute to the digital transformation of Qiuzhi Restaurant!
