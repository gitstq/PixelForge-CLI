<!-- language-switcher -->
<div align="center">

# 🔥 PixelForge-CLI

**轻量级终端 ASCII 艺术智能生成与转换引擎**
**Lightweight Terminal ASCII Art Intelligent Generation & Conversion Engine**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-v1.0.0-orange.svg)](https://github.com/gitstq/PixelForge-CLI)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

---

**🌐 [简体中文](#-项目介绍--简体中文) | [繁體中文](#-專案介紹--繁體中文) | [English](#-project-introduction--english)**

---

</div>

---

## 📑 目录导航

- [简体中文](#-项目介绍--简体中文)
  - [项目介绍](#-项目介绍--简体中文)
  - [核心特性](#-核心特性--简体中文)
  - [快速开始](#-快速开始--简体中文)
  - [详细使用指南](#-详细使用指南--简体中文)
  - [设计思路与迭代规划](#-设计思路与迭代规划--简体中文)
  - [打包与部署指南](#-打包与部署指南--简体中文)
  - [贡献指南](#-贡献指南--简体中文)
  - [开源协议](#-开源协议--简体中文)
- [繁體中文](#-專案介紹--繁體中文)
  - [專案介紹](#-專案介紹--繁體中文)
  - [核心特性](#-核心特性--繁體中文)
  - [快速開始](#-快速開始--繁體中文)
  - [詳細使用指南](#-詳細使用指南--繁體中文)
  - [設計思路與迭代規劃](#-設計思路與迭代規劃--繁體中文)
  - [打包與部署指南](#-打包與部署指南--繁體中文)
  - [貢獻指南](#-貢獻指南--繁體中文)
  - [開源協議](#-開源協議--繁體中文)
- [English](#-project-introduction--english)
  - [Project Introduction](#-project-introduction--english)
  - [Core Features](#-core-features--english)
  - [Quick Start](#-quick-start--english)
  - [Detailed Usage Guide](#-detailed-usage-guide--english)
  - [Design Philosophy & Roadmap](#-design-philosophy--roadmap--english)
  - [Packaging & Deployment Guide](#-packaging--deployment-guide--english)
  - [Contributing Guide](#-contributing-guide--english)
  - [License](#-license--english)

---

<!-- ============================================================ -->
<!-- ======================== 简体中文 ======================== -->
<!-- ============================================================ -->

## 🎉 项目介绍 · 简体中文

<div align="center">
<img src="https://img.shields.io/badge/语言-简体中文-red.svg" />
</div>

> 💡 **PixelForge-CLI** 是一款专为终端爱好者打造的 **轻量级 ASCII 艺术生成与转换工具**。它将你的文字和图片转化为令人惊叹的 ASCII 艺术作品，支持丰富的色彩渲染和多格式导出。

### 🌟 为什么选择 PixelForge-CLI？

在终端的世界里，ASCII 艺术是一种独特的表达方式。然而，现有的工具往往存在以下痛点：

- 🔗 **依赖臃肿** — 动辄需要 figlet、libcaca 等外部工具
- 🎨 **色彩贫乏** — 大多数工具仅支持单色输出
- 📦 **安装复杂** — 需要编译 C 扩展、配置环境变量
- 🖼️ **功能单一** — 文字和图片转换割裂在不同工具中

**PixelForge-CLI** 从根本上解决了这些问题：

| 对比维度 | 传统工具 | PixelForge-CLI |
|---------|---------|----------------|
| 核心依赖 | figlet / libcaca | **零依赖** |
| ASCII 字体 | 依赖外部字体库 | **9 种自研内置字体** |
| 色彩支持 | 单色 / 有限色彩 | **16 色 + 9 渐变 + 彩虹** |
| 导出格式 | TXT | **TXT / HTML / JSON / SVG / PNG** |
| 图片转 ASCII | 单独工具 | **一体化集成** |

### 🏗️ 技术架构概览

```
pixelforge/
├── cli.py              # 🎛️ 命令行接口入口
├── fonts/              # 🔤 9种自研ASCII字体引擎
│   ├── standard.py     #    Standard 经典字体
│   ├── block.py        #    Block 块状字体
│   ├── shadow.py       #    Shadow 阴影字体
│   ├── thin.py         #    Thin 纤细字体
│   ├── banner.py       #    Banner 横幅字体
│   ├── slant.py        #    Slant 倾斜字体
│   ├── small.py        #    Small 小型字体
│   ├── mini.py         #    Mini 迷你字体
│   └── dotmatrix.py    #    DotMatrix 点阵字体
├── renderers/          # 🎨 色彩渲染引擎
│   └── color.py        #    16色 + 9渐变 + 彩虹
├── converters/         # 🖼️ 图片转ASCII引擎
│   └── image.py        #    5种字符密度梯度
└── exporters/          # 📦 多格式导出引擎
```

---

## ✨ 核心特性 · 简体中文

### 🔤 文本转 ASCII 艺术

**9 种精心设计的内置字体**，每一种都经过逐字符优化，确保在各种终端环境下的显示效果：

| 字体名称 | 风格描述 | 适用场景 |
|---------|---------|---------|
| `standard` | 📝 经典等宽风格 | 通用文本展示 |
| `block` | 🧱 粗壮块状风格 | 标题、横幅 |
| `shadow` | 🌑 立体阴影风格 | 3D 效果标题 |
| `thin` | ✏️ 纤细线条风格 | 优雅文本 |
| `banner` | 🏁 大号横幅风格 | 醒目展示 |
| `slant` | 📐 倾斜风格 | 动感文本 |
| `small` | 🔤 紧凑小型风格 | 空间受限场景 |
| `mini` | 🤏 超迷你风格 | 极致压缩 |
| `dotmatrix` | ⚫ 点阵风格 | 复古终端风格 |

> 🎯 **零外部依赖** — 所有字体引擎完全自研，无需安装 figlet 或任何外部字体库。

### 🖼️ 图片转 ASCII 艺术

将任意图片转换为 ASCII 字符画，支持 **5 种字符密度梯度**：

| 密度梯度 | 字符集丰富度 | 适用场景 |
|---------|------------|---------|
| `simple` | 10 级灰度字符 | 快速预览 |
| `detailed` | 70 级灰度字符 | 高精度还原 |
| `blocks` | Unicode 方块字符 | 像素风格 |
| `dots` | Braille 点阵字符 | 精细纹理 |
| `braille` | Braille 盲文字符 | 极致细节 |

> ⚠️ 图片转 ASCII 功能需要安装 **Pillow**：`pip install Pillow`

### 🎨 色彩渲染系统

PixelForge-CLI 拥有业界领先的终端色彩渲染能力：

#### 🌈 16 种纯色

```
■ black    ■ red      ■ green    ■ yellow
■ blue     ■ magenta  ■ cyan     ■ white
■ bright-black    ■ bright-red    ■ bright-green    ■ bright-yellow
■ bright-blue     ■ bright-magenta ■ bright-cyan     ■ bright-white
```

#### 🎨 9 种渐变调色板

| 调色板名称 | 色彩风格 | 视觉效果 |
|-----------|---------|---------|
| `fire` | 🔥 火焰 | 红橙黄渐变 |
| `ocean` | 🌊 海洋 | 蓝青绿渐变 |
| `forest` | 🌲 森林 | 绿色系渐变 |
| `sunset` | 🌅 日落 | 暖色系渐变 |
| `rainbow` | 🌈 彩虹 | 全色谱渐变 |
| `purple` | 💜 紫罗兰 | 紫色系渐变 |
| `cyber` | 💻 赛博朋克 | 霓虹色渐变 |
| `pastel` | 🍬 马卡龙 | 柔和色渐变 |
| `grayscale` | ⬜ 灰度 | 黑白灰渐变 |

#### 🌈 彩虹模式

一键启用彩虹色渲染，每个字符自动映射到彩虹色谱上，打造最炫酷的终端视觉效果！

### 📦 多格式导出

| 格式 | 扩展名 | 特点 |
|-----|--------|------|
| 纯文本 | `.txt` | 原始 ASCII 字符，最大兼容性 |
| 网页 | `.html` | 内嵌 CSS 样式，可直接浏览器打开 |
| 数据 | `.json` | 结构化数据，便于程序处理 |
| 矢量图 | `.svg` | 无损缩放，适合打印 |
| 位图 | `.png` | 光栅化输出，即开即看 |

### 💻 跨平台支持

| 平台 | 支持状态 | 终端兼容 |
|-----|---------|---------|
| 🪟 Windows | ✅ 完全支持 | CMD / PowerShell / Windows Terminal |
| 🍎 macOS | ✅ 完全支持 | Terminal.app / iTerm2 / Alacritty |
| 🐧 Linux | ✅ 完全支持 | GNOME Terminal / Konsole / Alacritty |

---

## 🚀 快速开始 · 简体中文

### 📦 安装

```bash
# 通过 pip 安装（推荐）
pip install pixelforge-cli

# 从源码安装
git clone https://github.com/gitstq/PixelForge-CLI.git
cd PixelForge-CLI
pip install -e .

# 可选：安装 Pillow 以启用图片转 ASCII 功能
pip install Pillow
```

### ⚡ 5 秒上手

```bash
# 🎯 基础文字转 ASCII
pixelforge text "HELLO" --font block --color cyan
```

输出效果：
```
 ██  ██                  ██
███  ███                ███
████ ████   ██████  █████████  ██████
████████   ██  ██  █████████  ██  ██
████████   ██████  █████████  ██████
████ ████   ██      ███  ███  ██
███  ███   ████     ███  ███  ████
███  ███    █████   ███  ███   █████
```

```bash
# 🌈 渐变色彩渲染
pixelforge text "WORLD" --font shadow --gradient fire
```

```bash
# 🌊 彩虹模式
pixelforge text "LOVE" --font standard --rainbow
```

```bash
# 🖼️ 图片转 ASCII
pixelforge image photo.jpg --width 100 --ramp detailed
```

```bash
# 📦 导出为 HTML 文件
pixelforge text "BANNER" --font banner --output art.txt --format html
```

### 🔗 管道操作

PixelForge-CLI 完美支持 Unix 管道操作：

```bash
# 从管道读取输入
echo "PIXELFORGE" | pixelforge text --font slant --color green

# 输出到文件
pixelforge text "OUTPUT" --font block > output.txt

# 组合使用
pixelforge text "DATA" --font mini --format json | jq '.metadata'
```

---

## 📖 详细使用指南 · 简体中文

### 🎛️ 命令行参数完整参考

#### `pixelforge text` — 文本转 ASCII

```bash
pixelforge text <TEXT> [OPTIONS]
```

| 参数 | 缩写 | 说明 | 默认值 |
|-----|------|------|--------|
| `--font` | `-f` | 字体选择 | `standard` |
| `--color` | `-c` | 纯色渲染 | 无（白色） |
| `--gradient` | `-g` | 渐变调色板 | 无 |
| `--rainbow` | `-r` | 启用彩虹模式 | `False` |
| `--output` | `-o` | 输出文件路径 | 标准输出 |
| `--format` | `-F` | 导出格式 | `txt` |
| `--width` | `-w` | 输出宽度限制 | 无限制 |

**可用字体值：**
`standard` · `block` · `shadow` · `thin` · `banner` · `slant` · `small` · `mini` · `dotmatrix`

**可用纯色值：**
`black` · `red` · `green` · `yellow` · `blue` · `magenta` · `cyan` · `white` · `bright-black` · `bright-red` · `bright-green` · `bright-yellow` · `bright-blue` · `bright-magenta` · `bright-cyan` · `bright-white`

**可用渐变值：**
`fire` · `ocean` · `forest` · `sunset` · `rainbow` · `purple` · `cyber` · `pastel` · `grayscale`

#### `pixelforge image` — 图片转 ASCII

```bash
pixelforge image <IMAGE_PATH> [OPTIONS]
```

| 参数 | 缩写 | 说明 | 默认值 |
|-----|------|------|--------|
| `--width` | `-w` | 输出宽度（字符数） | `80` |
| `--height` | `-h` | 输出高度（字符数） | 自动计算 |
| `--ramp` | `-r` | 字符密度梯度 | `simple` |
| `--color` | `-c` | 启用彩色模式 | `False` |
| `--invert` | `-i` | 反转亮度映射 | `False` |
| `--output` | `-o` | 输出文件路径 | 标准输出 |
| `--format` | `-F` | 导出格式 | `txt` |

**可用密度梯度值：**
`simple` · `detailed` · `blocks` · `dots` · `braille`

### 🎨 色彩使用示例

#### 纯色渲染

```bash
# 红色标准字体
pixelforge text "ERROR" --font block --color red

# 青色阴影字体
pixelforge text "SYSTEM" --font shadow --color cyan

# 黄色纤细字体
pixelforge text "WARNING" --font thin --color yellow
```

#### 渐变渲染

```bash
# 🔥 火焰渐变
pixelforge text "BURN" --font banner --gradient fire

# 🌊 海洋渐变
pixelforge text "WAVE" --font slant --gradient ocean

# 🌲 森林渐变
pixelforge text "TREE" --font standard --gradient forest

# 🌅 日落渐变
pixelforge text "DUSK" --font block --gradient sunset

# 💜 紫罗兰渐变
pixelforge text "DREAM" --font shadow --gradient purple

# 💻 赛博朋克渐变
pixelforge text "NEON" --font slant --gradient cyber

# 🍬 马卡龙渐变
pixelforge text "SWEET" --font thin --gradient pastel
```

#### 彩虹模式

```bash
# 🌈 全彩虹渲染
pixelforge text "RAINBOW" --font banner --rainbow

# 🌈 小字体彩虹
pixelforge text "COLOR" --font mini --rainbow
```

### 📦 导出格式示例

```bash
# 导出为纯文本
pixelforge text "HELLO" --font block --output hello.txt --format txt

# 导出为 HTML（可在浏览器中查看）
pixelforge text "HELLO" --font block --output hello.html --format html

# 导出为 JSON（程序化处理）
pixelforge text "HELLO" --font block --output hello.json --format json

# 导出为 SVG（矢量图，可无损缩放）
pixelforge text "HELLO" --font block --output hello.svg --format svg

# 导出为 PNG（位图，即开即看）
pixelforge text "HELLO" --font block --output hello.png --format png
```

### 🖼️ 图片转 ASCII 示例

```bash
# 基础用法 — 100 字符宽度，简单梯度
pixelforge image photo.jpg --width 100 --ramp simple

# 高精度还原 — 150 字符宽度，详细梯度
pixelforge image photo.jpg --width 150 --ramp detailed

# 像素风格 — Unicode 方块字符
pixelforge image photo.jpg --width 80 --ramp blocks

# 点阵风格 — Braille 字符
pixelforge image photo.jpg --width 120 --ramp braille

# 反转亮度 — 适合浅色背景图片
pixelforge image photo.jpg --width 100 --ramp detailed --invert

# 彩色模式 — 保留原图色彩信息
pixelforge image photo.jpg --width 100 --ramp detailed --color
```

### 🛠️ 高级技巧

#### 组合使用多个选项

```bash
# 大号横幅 + 火焰渐变 + 导出 HTML
pixelforge text "AMAZING" --font banner --gradient fire --output amazing.html --format html

# 迷你字体 + 彩虹 + 导出 SVG
pixelforge text "TINY" --font mini --rainbow --output tiny.svg --format svg
```

#### 在脚本中使用

```python
# Python 脚本中调用
import subprocess

result = subprocess.run(
    ["pixelforge", "text", "HELLO", "--font", "block", "--format", "json"],
    capture_output=True,
    text=True
)
print(result.stdout)
```

#### 批量处理

```bash
# Bash 批量生成
for word in HELLO WORLD PIXEL FORGE; do
    pixelforge text "$word" --font block --gradient cyber --output "${word}.html" --format html
done
```

---

## 💡 设计思路与迭代规划 · 简体中文

### 🎯 设计哲学

PixelForge-CLI 的设计遵循以下核心原则：

1. **🪶 轻量至上** — 零核心依赖，安装即用，不污染系统环境
2. **🎨 美学驱动** — 每种字体都经过精心设计，不是简单的字符堆叠
3. **🔌 可扩展性** — 模块化架构，字体、渲染器、导出器均可独立扩展
4. **🌍 用户友好** — 清晰的 CLI 接口，丰富的文档，完善的错误提示

### 🔄 版本迭代规划

#### v1.0.0 — 当前版本 ✅

- ✅ 9 种自研 ASCII 字体引擎
- ✅ 16 色纯色渲染
- ✅ 9 种渐变调色板 + 彩虹模式
- ✅ 5 种导出格式（TXT/HTML/JSON/SVG/PNG）
- ✅ 图片转 ASCII（5 种密度梯度）
- ✅ 跨平台支持

#### v1.1.0 — 计划中 🚧

- 🔲 动画 ASCII 艺术（GIF/视频转 ASCII 动画）
- 🔲 自定义字体加载（用户字体文件）
- 🔲 终端实时预览模式
- 🔲 配置文件支持（`~/.pixelforge/config.toml`）

#### v1.2.0 — 远期规划 🔭

- 🔲 Web UI 在线编辑器
- 🔲 ASCII 艺术字体市场
- 🔲 AI 辅助字体生成
- 🔲 插件系统

### 🏗️ 架构设计亮点

```
┌─────────────────────────────────────────────┐
│                  CLI Layer                   │
│            (argparse + entry_point)          │
├──────────┬──────────┬──────────┬─────────────┤
│  Fonts   │Renderer  │Converter │  Exporter   │
│  Engine  │  Engine  │  Engine  │   Engine    │
│ (9 fonts)│(16+9+🌈) │(5 ramps) │(5 formats) │
├──────────┴──────────┴──────────┴─────────────┤
│              Core Processing Pipeline         │
├─────────────────────────────────────────────┤
│           Platform Abstraction Layer          │
│        (Windows / macOS / Linux)             │
└─────────────────────────────────────────────┘
```

- **模块解耦** — 字体、渲染、转换、导出四大引擎完全解耦，可独立开发和测试
- **插件友好** — 新增字体只需添加一个 Python 文件，无需修改核心代码
- **管道设计** — 输入 → 字体渲染 → 色彩处理 → 格式导出，流水线式处理

---

## 📦 打包与部署指南 · 简体中文

### 🏗️ 项目结构

```
PixelForge-CLI/
├── src/
│   └── pixelforge/          # 📂 核心源码
│       ├── __init__.py
│       ├── cli.py           # 🎛️ CLI 入口
│       ├── fonts/           # 🔤 字体引擎
│       ├── renderers/       # 🎨 渲染引擎
│       ├── converters/      # 🖼️ 转换引擎
│       └── exporters/       # 📦 导出引擎
├── tests/                   # 🧪 测试用例
├── pyproject.toml           # ⚙️ 项目配置
├── LICENSE                  # 📄 MIT 许可证
├── .gitignore              # 🚫 Git 忽略规则
└── README.md               # 📖 项目文档
```

### 📦 构建发布包

```bash
# 1. 安装构建工具
pip install build

# 2. 构建分发包
python -m build

# 3. 生成的文件位于 dist/ 目录
#    dist/pixelforge_cli-1.0.0-py3-none-any.whl
#    dist/pixelforge_cli-1.0.0.tar.gz
```

### 🚀 发布到 PyPI

```bash
# 1. 安装 Twine
pip install twine

# 2. 检查包内容
twine check dist/*

# 3. 上传到 PyPI（生产环境）
twine upload dist/*

# 4. 或上传到 TestPyPI（测试环境）
twine upload --repository testpypi dist/*
```

### 🐍 环境要求

| 项目 | 要求 |
|-----|------|
| Python 版本 | **>= 3.8** |
| 核心依赖 | **无**（零依赖） |
| 可选依赖 | **Pillow**（图片转 ASCII） |
| 操作系统 | Windows / macOS / Linux |

### 🔧 开发环境搭建

```bash
# 克隆仓库
git clone https://github.com/gitstq/PixelForge-CLI.git
cd PixelForge-CLI

# 安装开发模式（可编辑安装）
pip install -e .

# 可选：安装 Pillow
pip install Pillow

# 运行测试
python -m pytest tests/

# 验证安装
pixelforge text "TEST" --font block
```

---

## 🤝 贡献指南 · 简体中文

> 🙌 首先，感谢你对 PixelForge-CLI 的关注！无论是提交 Bug、改进文档还是贡献代码，每一份力量都很珍贵。

### 📋 贡献流程

1. **🍴 Fork 本仓库** — 点击 GitHub 页面右上角的 Fork 按钮
2. **📥 克隆到本地** — `git clone https://github.com/<your-username>/PixelForge-CLI.git`
3. **🌿 创建特性分支** — `git checkout -b feature/your-feature-name`
4. **✏️ 进行开发** — 编写代码并确保通过所有测试
5. **🧪 运行测试** — `python -m pytest tests/`
6. **📝 提交变更** — `git commit -m "feat: 描述你的改动"`
7. **📤 推送分支** — `git push origin feature/your-feature-name`
8. **🔀 创建 Pull Request** — 在 GitHub 上提交 PR

### ✍️ 提交信息规范

请遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
feat: 新增 DotMatrix 字体支持
fix: 修复 Shadow 字体宽度计算错误
docs: 更新 README 快速开始章节
style: 统一代码缩进格式
refactor: 重构色彩渲染引擎
test: 新增字体引擎单元测试
chore: 更新 pyproject.toml 版本号
```

### 🆕 添加新字体

PixelForge-CLI 的字体引擎采用模块化设计，添加新字体非常简单：

```python
# src/pixelforge/fonts/your_font.py

CHAR_MAP = {
    'A': [
        " ██ ",
        "█  █",
        "████",
        "█  █",
        "█  █",
    ],
    # ... 其他字符映射
}

HEIGHT = 5  # 字体高度
```

然后在 `fonts/__init__.py` 中注册即可。

### 🐛 报告 Bug

请使用 [GitHub Issues](https://github.com/gitstq/PixelForge-CLI/issues) 提交 Bug 报告，并包含以下信息：

- 🖥️ 操作系统及版本
- 🐍 Python 版本
- 📦 PixelForge-CLI 版本
- 📝 复现步骤
- 📸 错误截图或日志

### 📜 行为准则

- 尊重所有贡献者
- 接受建设性的代码审查
- 保持友好和专业的沟通
- 关注代码质量和可维护性

---

## 📄 开源协议 · 简体中文

本项目基于 **[MIT License](LICENSE)** 开源。

```
MIT License

Copyright (c) 2024 PixelForge-CLI Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

> 📌 简而言之：你可以**自由使用、修改、分发**本软件，唯一的要求是保留版权声明和许可声明。

---

<div align="center">

**[⬆ 回到顶部](#-pixelforge-cli) · [🌐 切换语言](#-目录导航)**

---

</div>

<!-- ============================================================ -->
<!-- ======================== 繁體中文 ======================== -->
<!-- ============================================================ -->

## 🎉 專案介紹 · 繁體中文

<div align="center">
<img src="https://img.shields.io/badge/語言-繁體中文-red.svg" />
</div>

> 💡 **PixelForge-CLI** 是一款專為終端愛好者打造的 **輕量級 ASCII 藝術生成與轉換工具**。它能將你的文字和圖片轉化為令人驚嘆的 ASCII 藝術作品，支援豐富的色彩渲染和多格式匯出。

### 🌟 為什麼選擇 PixelForge-CLI？

在終端的世界裡，ASCII 藝術是一種獨特的表達方式。然而，現有的工具往往存在以下痛點：

- 🔗 **依賴臃腫** — 動輒需要 figlet、libcaca 等外部工具
- 🎨 **色彩貧乏** — 大多數工具僅支援單色輸出
- 📦 **安裝複雜** — 需要編譯 C 擴充、配置環境變數
- 🖼️ **功能單一** — 文字和圖片轉換割裂在不同工具中

**PixelForge-CLI** 從根本上解決了這些問題：

| 對比維度 | 傳統工具 | PixelForge-CLI |
|---------|---------|----------------|
| 核心依賴 | figlet / libcaca | **零依賴** |
| ASCII 字型 | 依賴外部字型庫 | **9 種自研內建字型** |
| 色彩支援 | 單色 / 有限色彩 | **16 色 + 9 漸層 + 彩虹** |
| 匯出格式 | TXT | **TXT / HTML / JSON / SVG / PNG** |
| 圖片轉 ASCII | 單獨工具 | **一體化整合** |

### 🏗️ 技術架構概覽

```
pixelforge/
├── cli.py              # 🎛️ 命令列介面入口
├── fonts/              # 🔤 9種自研ASCII字型引擎
│   ├── standard.py     #    Standard 經典字型
│   ├── block.py        #    Block 塊狀字型
│   ├── shadow.py       #    Shadow 陰影字型
│   ├── thin.py         #    Thin 纖細字型
│   ├── banner.py       #    Banner 橫幅字型
│   ├── slant.py        #    Slant 傾斜字型
│   ├── small.py        #    Small 小型字型
│   ├── mini.py         #    Mini 迷你字型
│   └── dotmatrix.py    #    DotMatrix 點陣字型
├── renderers/          # 🎨 色彩渲染引擎
│   └── color.py        #    16色 + 9漸層 + 彩虹
├── converters/         # 🖼️ 圖片轉ASCII引擎
│   └── image.py        #    5種字元密度梯度
└── exporters/          # 📦 多格式匯出引擎
```

---

## ✨ 核心特性 · 繁體中文

### 🔤 文字轉 ASCII 藝術

**9 種精心設計的內建字型**，每一種都經過逐字元優化，確保在各種終端環境下的顯示效果：

| 字型名稱 | 風格描述 | 適用場景 |
|---------|---------|---------|
| `standard` | 📝 經典等寬風格 | 通用文字展示 |
| `block` | 🧱 粗壯塊狀風格 | 標題、橫幅 |
| `shadow` | 🌑 立體陰影風格 | 3D 效果標題 |
| `thin` | ✏️ 纖細線條風格 | 優雅文字 |
| `banner` | 🏁 大號橫幅風格 | 醒目展示 |
| `slant` | 📐 傾斜風格 | 動感文字 |
| `small` | 🔤 緊湊小型風格 | 空間受限場景 |
| `mini` | 🤏 超迷你風格 | 極致壓縮 |
| `dotmatrix` | ⚫ 點陣風格 | 復古終端風格 |

> 🎯 **零外部依賴** — 所有字型引擎完全自研，無需安裝 figlet 或任何外部字型庫。

### 🖼️ 圖片轉 ASCII 藝術

將任意圖片轉換為 ASCII 字元畫，支援 **5 種字元密度梯度**：

| 密度梯度 | 字元集豐富度 | 適用場景 |
|---------|------------|---------|
| `simple` | 10 級灰度字元 | 快速預覽 |
| `detailed` | 70 級灰度字元 | 高精度還原 |
| `blocks` | Unicode 方塊字元 | 像素風格 |
| `dots` | Braille 點陣字元 | 精細紋理 |
| `braille` | Braille 盲文字元 | 極致細節 |

> ⚠️ 圖片轉 ASCII 功能需要安裝 **Pillow**：`pip install Pillow`

### 🎨 色彩渲染系統

PixelForge-CLI 擁有業界領先的終端色彩渲染能力：

#### 🌈 16 種純色

```
■ black    ■ red      ■ green    ■ yellow
■ blue     ■ magenta  ■ cyan     ■ white
■ bright-black    ■ bright-red    ■ bright-green    ■ bright-yellow
■ bright-blue     ■ bright-magenta ■ bright-cyan     ■ bright-white
```

#### 🎨 9 種漸層調色板

| 調色板名稱 | 色彩風格 | 視覺效果 |
|-----------|---------|---------|
| `fire` | 🔥 火焰 | 紅橙黃漸層 |
| `ocean` | 🌊 海洋 | 藍青綠漸層 |
| `forest` | 🌲 森林 | 綠色系漸層 |
| `sunset` | 🌅 日落 | 暖色系漸層 |
| `rainbow` | 🌈 彩虹 | 全光譜漸層 |
| `purple` | 💜 紫羅蘭 | 紫色系漸層 |
| `cyber` | 💻 賽博龐克 | 霓虹色漸層 |
| `pastel` | 🍬 馬卡龍 | 柔和色漸層 |
| `grayscale` | ⬜ 灰度 | 黑白灰漸層 |

#### 🌈 彩虹模式

一鍵啟用彩虹色渲染，每個字元自動映射到彩虹光譜上，打造最炫酷的終端視覺效果！

### 📦 多格式匯出

| 格式 | 副檔名 | 特點 |
|-----|--------|------|
| 純文字 | `.txt` | 原始 ASCII 字元，最大相容性 |
| 網頁 | `.html` | 內嵌 CSS 樣式，可直接瀏覽器開啟 |
| 資料 | `.json` | 結構化資料，便於程式處理 |
| 向量圖 | `.svg` | 無損縮放，適合列印 |
| 點陣圖 | `.png` | 光柵化輸出，即開即看 |

### 💻 跨平台支援

| 平台 | 支援狀態 | 終端相容 |
|-----|---------|---------|
| 🪟 Windows | ✅ 完全支援 | CMD / PowerShell / Windows Terminal |
| 🍎 macOS | ✅ 完全支援 | Terminal.app / iTerm2 / Alacritty |
| 🐧 Linux | ✅ 完全支援 | GNOME Terminal / Konsole / Alacritty |

---

## 🚀 快速開始 · 繁體中文

### 📦 安裝

```bash
# 透過 pip 安裝（推薦）
pip install pixelforge-cli

# 從原始碼安裝
git clone https://github.com/gitstq/PixelForge-CLI.git
cd PixelForge-CLI
pip install -e .

# 可選：安裝 Pillow 以啟用圖片轉 ASCII 功能
pip install Pillow
```

### ⚡ 5 秒上手

```bash
# 🎯 基礎文字轉 ASCII
pixelforge text "HELLO" --font block --color cyan
```

輸出效果：
```
 ██  ██                  ██
███  ███                ███
████ ████   ██████  █████████  ██████
████████   ██  ██  █████████  ██  ██
████████   ██████  █████████  ██████
████ ████   ██      ███  ███  ██
███  ███   ████     ███  ███  ████
███  ███    █████   ███  ███   █████
```

```bash
# 🌈 漸層色彩渲染
pixelforge text "WORLD" --font shadow --gradient fire
```

```bash
# 🌊 彩虹模式
pixelforge text "LOVE" --font standard --rainbow
```

```bash
# 🖼️ 圖片轉 ASCII
pixelforge image photo.jpg --width 100 --ramp detailed
```

```bash
# 📦 匯出為 HTML 檔案
pixelforge text "BANNER" --font banner --output art.txt --format html
```

### 🔗 管道操作

PixelForge-CLI 完美支援 Unix 管道操作：

```bash
# 從管道讀取輸入
echo "PIXELFORGE" | pixelforge text --font slant --color green

# 輸出到檔案
pixelforge text "OUTPUT" --font block > output.txt

# 組合使用
pixelforge text "DATA" --font mini --format json | jq '.metadata'
```

---

## 📖 詳細使用指南 · 繁體中文

### 🎛️ 命令列參數完整參考

#### `pixelforge text` — 文字轉 ASCII

```bash
pixelforge text <TEXT> [OPTIONS]
```

| 參數 | 縮寫 | 說明 | 預設值 |
|-----|------|------|--------|
| `--font` | `-f` | 字型選擇 | `standard` |
| `--color` | `-c` | 純色渲染 | 無（白色） |
| `--gradient` | `-g` | 漸層調色板 | 無 |
| `--rainbow` | `-r` | 啟用彩虹模式 | `False` |
| `--output` | `-o` | 輸出檔案路徑 | 標準輸出 |
| `--format` | `-F` | 匯出格式 | `txt` |
| `--width` | `-w` | 輸出寬度限制 | 無限制 |

**可用字型值：**
`standard` · `block` · `shadow` · `thin` · `banner` · `slant` · `small` · `mini` · `dotmatrix`

**可用純色值：**
`black` · `red` · `green` · `yellow` · `blue` · `magenta` · `cyan` · `white` · `bright-black` · `bright-red` · `bright-green` · `bright-yellow` · `bright-blue` · `bright-magenta` · `bright-cyan` · `bright-white`

**可用漸層值：**
`fire` · `ocean` · `forest` · `sunset` · `rainbow` · `purple` · `cyber` · `pastel` · `grayscale`

#### `pixelforge image` — 圖片轉 ASCII

```bash
pixelforge image <IMAGE_PATH> [OPTIONS]
```

| 參數 | 縮寫 | 說明 | 預設值 |
|-----|------|------|--------|
| `--width` | `-w` | 輸出寬度（字元數） | `80` |
| `--height` | `-h` | 輸出高度（字元數） | 自動計算 |
| `--ramp` | `-r` | 字元密度梯度 | `simple` |
| `--color` | `-c` | 啟用彩色模式 | `False` |
| `--invert` | `-i` | 反轉亮度映射 | `False` |
| `--output` | `-o` | 輸出檔案路徑 | 標準輸出 |
| `--format` | `-F` | 匯出格式 | `txt` |

**可用密度梯度值：**
`simple` · `detailed` · `blocks` · `dots` · `braille`

### 🎨 色彩使用範例

#### 純色渲染

```bash
# 紅色標準字型
pixelforge text "ERROR" --font block --color red

# 青色陰影字型
pixelforge text "SYSTEM" --font shadow --color cyan

# 黃色纖細字型
pixelforge text "WARNING" --font thin --color yellow
```

#### 漸層渲染

```bash
# 🔥 火焰漸層
pixelforge text "BURN" --font banner --gradient fire

# 🌊 海洋漸層
pixelforge text "WAVE" --font slant --gradient ocean

# 🌲 森林漸層
pixelforge text "TREE" --font standard --gradient forest

# 🌅 日落漸層
pixelforge text "DUSK" --font block --gradient sunset

# 💜 紫羅蘭漸層
pixelforge text "DREAM" --font shadow --gradient purple

# 💻 賽博龐克漸層
pixelforge text "NEON" --font slant --gradient cyber

# 🍬 馬卡龍漸層
pixelforge text "SWEET" --font thin --gradient pastel
```

#### 彩虹模式

```bash
# 🌈 全彩虹渲染
pixelforge text "RAINBOW" --font banner --rainbow

# 🌈 小字型彩虹
pixelforge text "COLOR" --font mini --rainbow
```

### 📦 匯出格式範例

```bash
# 匯出為純文字
pixelforge text "HELLO" --font block --output hello.txt --format txt

# 匯出為 HTML（可在瀏覽器中檢視）
pixelforge text "HELLO" --font block --output hello.html --format html

# 匯出為 JSON（程式化處理）
pixelforge text "HELLO" --font block --output hello.json --format json

# 匯出為 SVG（向量圖，可無損縮放）
pixelforge text "HELLO" --font block --output hello.svg --format svg

# 匯出為 PNG（點陣圖，即開即看）
pixelforge text "HELLO" --font block --output hello.png --format png
```

### 🖼️ 圖片轉 ASCII 範例

```bash
# 基礎用法 — 100 字元寬度，簡單梯度
pixelforge image photo.jpg --width 100 --ramp simple

# 高精度還原 — 150 字元寬度，詳細梯度
pixelforge image photo.jpg --width 150 --ramp detailed

# 像素風格 — Unicode 方塊字元
pixelforge image photo.jpg --width 80 --ramp blocks

# 點陣風格 — Braille 字元
pixelforge image photo.jpg --width 120 --ramp braille

# 反轉亮度 — 適合淺色背景圖片
pixelforge image photo.jpg --width 100 --ramp detailed --invert

# 彩色模式 — 保留原圖色彩資訊
pixelforge image photo.jpg --width 100 --ramp detailed --color
```

### 🛠️ 進階技巧

#### 組合使用多個選項

```bash
# 大號橫幅 + 火焰漸層 + 匯出 HTML
pixelforge text "AMAZING" --font banner --gradient fire --output amazing.html --format html

# 迷你字型 + 彩虹 + 匯出 SVG
pixelforge text "TINY" --font mini --rainbow --output tiny.svg --format svg
```

#### 在腳本中使用

```python
# Python 腳本中呼叫
import subprocess

result = subprocess.run(
    ["pixelforge", "text", "HELLO", "--font", "block", "--format", "json"],
    capture_output=True,
    text=True
)
print(result.stdout)
```

#### 批次處理

```bash
# Bash 批次產生
for word in HELLO WORLD PIXEL FORGE; do
    pixelforge text "$word" --font block --gradient cyber --output "${word}.html" --format html
done
```

---

## 💡 設計思路與迭代規劃 · 繁體中文

### 🎯 設計哲學

PixelForge-CLI 的設計遵循以下核心原則：

1. **🪶 輕量至上** — 零核心依賴，安裝即用，不汙染系統環境
2. **🎨 美學驅動** — 每種字型都經過精心設計，不是簡單的字元堆疊
3. **🔌 可擴展性** — 模組化架構，字型、渲染器、匯出器均可獨立擴展
4. **🌍 使用者友善** — 清晰的 CLI 介面，豐富的文件，完善的錯誤提示

### 🔄 版本迭代規劃

#### v1.0.0 — 當前版本 ✅

- ✅ 9 種自研 ASCII 字型引擎
- ✅ 16 色純色渲染
- ✅ 9 種漸層調色板 + 彩虹模式
- ✅ 5 種匯出格式（TXT/HTML/JSON/SVG/PNG）
- ✅ 圖片轉 ASCII（5 種密度梯度）
- ✅ 跨平台支援

#### v1.1.0 — 規劃中 🚧

- 🔲 動畫 ASCII 藝術（GIF/影片轉 ASCII 動畫）
- 🔲 自訂字型載入（使用者字型檔案）
- 🔲 終端即時預覽模式
- 🔲 設定檔支援（`~/.pixelforge/config.toml`）

#### v1.2.0 — 遠期規劃 🔭

- 🔲 Web UI 線上編輯器
- 🔲 ASCII 藝術字型市場
- 🔲 AI 輔助字型生成
- 🔲 外掛系統

### 🏗️ 架構設計亮點

```
┌─────────────────────────────────────────────┐
│                  CLI Layer                   │
│            (argparse + entry_point)          │
├──────────┬──────────┬──────────┬─────────────┤
│  Fonts   │Renderer  │Converter │  Exporter   │
│  Engine  │  Engine  │  Engine  │   Engine    │
│ (9 fonts)│(16+9+🌈) │(5 ramps) │(5 formats) │
├──────────┴──────────┴──────────┴─────────────┤
│              Core Processing Pipeline         │
├─────────────────────────────────────────────┤
│           Platform Abstraction Layer          │
│        (Windows / macOS / Linux)             │
└─────────────────────────────────────────────┘
```

- **模組解耦** — 字型、渲染、轉換、匯出四大引擎完全解耦，可獨立開發和測試
- **外掛友善** — 新增字型只需新增一個 Python 檔案，無需修改核心程式碼
- **管道設計** — 輸入 → 字型渲染 → 色彩處理 → 格式匯出，流水線式處理

---

## 📦 打包與部署指南 · 繁體中文

### 🏗️ 專案結構

```
PixelForge-CLI/
├── src/
│   └── pixelforge/          # 📂 核心原始碼
│       ├── __init__.py
│       ├── cli.py           # 🎛️ CLI 入口
│       ├── fonts/           # 🔤 字型引擎
│       ├── renderers/       # 🎨 渲染引擎
│       ├── converters/      # 🖼️ 轉換引擎
│       └── exporters/       # 📦 匯出引擎
├── tests/                   # 🧪 測試用例
├── pyproject.toml           # ⚙️ 專案配置
├── LICENSE                  # 📄 MIT 授權條款
├── .gitignore              # 🚫 Git 忽略規則
└── README.md               # 📖 專案文件
```

### 📦 建構發布包

```bash
# 1. 安裝建構工具
pip install build

# 2. 建構分發包
python -m build

# 3. 產生的檔案位於 dist/ 目錄
#    dist/pixelforge_cli-1.0.0-py3-none-any.whl
#    dist/pixelforge_cli-1.0.0.tar.gz
```

### 🚀 發布到 PyPI

```bash
# 1. 安裝 Twine
pip install twine

# 2. 檢查包內容
twine check dist/*

# 3. 上傳到 PyPI（正式環境）
twine upload dist/*

# 4. 或上傳到 TestPyPI（測試環境）
twine upload --repository testpypi dist/*
```

### 🐍 環境要求

| 項目 | 要求 |
|-----|------|
| Python 版本 | **>= 3.8** |
| 核心依賴 | **無**（零依賴） |
| 可選依賴 | **Pillow**（圖片轉 ASCII） |
| 作業系統 | Windows / macOS / Linux |

### 🔧 開發環境建置

```bash
# 複製倉庫
git clone https://github.com/gitstq/PixelForge-CLI.git
cd PixelForge-CLI

# 安裝開發模式（可編輯安裝）
pip install -e .

# 可選：安裝 Pillow
pip install Pillow

# 執行測試
python -m pytest tests/

# 驗證安裝
pixelforge text "TEST" --font block
```

---

## 🤝 貢獻指南 · 繁體中文

> 🙌 首先，感謝你對 PixelForge-CLI 的關注！無論是提交 Bug、改進文件還是貢獻程式碼，每一份力量都很珍貴。

### 📋 貢獻流程

1. **🍴 Fork 本倉庫** — 點擊 GitHub 頁面右上角的 Fork 按鈕
2. **📥 複製到本地** — `git clone https://github.com/<your-username>/PixelForge-CLI.git`
3. **🌿 建立特性分支** — `git checkout -b feature/your-feature-name`
4. **✏️ 進行開發** — 撰寫程式碼並確保通過所有測試
5. **🧪 執行測試** — `python -m pytest tests/`
6. **📝 提交變更** — `git commit -m "feat: 描述你的變更"`
7. **📤 推送分支** — `git push origin feature/your-feature-name`
8. **🔀 建立 Pull Request** — 在 GitHub 上提交 PR

### ✍️ 提交資訊規範

請遵循 [Conventional Commits](https://www.conventionalcommits.org/) 規範：

```
feat: 新增 DotMatrix 字型支援
fix: 修復 Shadow 字型寬度計算錯誤
docs: 更新 README 快速開始章節
style: 統一程式碼縮排格式
refactor: 重構色彩渲染引擎
test: 新增字型引擎單元測試
chore: 更新 pyproject.toml 版本號
```

### 🆕 新增字型

PixelForge-CLI 的字型引擎採用模組化設計，新增字型非常簡單：

```python
# src/pixelforge/fonts/your_font.py

CHAR_MAP = {
    'A': [
        " ██ ",
        "█  █",
        "████",
        "█  █",
        "█  █",
    ],
    # ... 其他字元映射
}

HEIGHT = 5  # 字型高度
```

然後在 `fonts/__init__.py` 中註冊即可。

### 🐛 回報 Bug

請使用 [GitHub Issues](https://github.com/gitstq/PixelForge-CLI/issues) 提交 Bug 報告，並包含以下資訊：

- 🖥️ 作業系統及版本
- 🐍 Python 版本
- 📦 PixelForge-CLI 版本
- 📝 重現步驟
- 📸 錯誤截圖或日誌

### 📜 行為準則

- 尊重所有貢獻者
- 接受建設性的程式碼審查
- 保持友善和專業的溝通
- 關注程式碼品質和可維護性

---

## 📄 開源協議 · 繁體中文

本專案基於 **[MIT License](LICENSE)** 開源。

```
MIT License

Copyright (c) 2024 PixelForge-CLI Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

> 📌 簡而言之：你可以**自由使用、修改、分發**本軟體，唯一的要求是保留版權聲明和許可聲明。

---

<div align="center">

**[⬆ 回到頂部](#-pixelforge-cli) · [🌐 切換語言](#-目錄導航)**

---

</div>

<!-- ============================================================ -->
<!-- ========================= English ========================= -->
<!-- ============================================================ -->

## 🎉 Project Introduction · English

<div align="center">
<img src="https://img.shields.io/badge/Language-English-blue.svg" />
</div>

> 💡 **PixelForge-CLI** is a **lightweight ASCII art generation and conversion tool** crafted for terminal enthusiasts. It transforms your text and images into stunning ASCII art masterpieces with rich color rendering and multi-format export capabilities.

### 🌟 Why PixelForge-CLI?

In the world of terminals, ASCII art is a unique form of expression. However, existing tools often suffer from these pain points:

- 🔗 **Bloated dependencies** — Requiring figlet, libcaca, and other external tools
- 🎨 **Limited colors** — Most tools only support monochrome output
- 📦 **Complex installation** — Requiring C extension compilation and environment configuration
- 🖼️ **Single-purpose** — Text and image conversion split across different tools

**PixelForge-CLI** fundamentally solves these problems:

| Dimension | Traditional Tools | PixelForge-CLI |
|-----------|-------------------|----------------|
| Core Dependencies | figlet / libcaca | **Zero dependencies** |
| ASCII Fonts | External font libraries | **9 built-in custom fonts** |
| Color Support | Monochrome / Limited | **16 colors + 9 gradients + Rainbow** |
| Export Formats | TXT | **TXT / HTML / JSON / SVG / PNG** |
| Image to ASCII | Separate tool | **Integrated solution** |

### 🏗️ Architecture Overview

```
pixelforge/
├── cli.py              # 🎛️ CLI interface entry point
├── fonts/              # 🔤 9 custom ASCII font engines
│   ├── standard.py     #    Standard classic font
│   ├── block.py        #    Block bold font
│   ├── shadow.py       #    Shadow 3D font
│   ├── thin.py         #    Thin elegant font
│   ├── banner.py       #    Banner large font
│   ├── slant.py        #    Slant italic font
│   ├── small.py        #    Small compact font
│   ├── mini.py         #    Mini tiny font
│   └── dotmatrix.py    #    DotMatrix retro font
├── renderers/          # 🎨 Color rendering engine
│   └── color.py        #    16 colors + 9 gradients + rainbow
├── converters/         # 🖼️ Image to ASCII engine
│   └── image.py        #    5 character density ramps
└── exporters/          # 📦 Multi-format export engine
```

---

## ✨ Core Features · English

### 🔤 Text to ASCII Art

**9 meticulously designed built-in fonts**, each optimized character-by-character for display across various terminal environments:

| Font Name | Style | Best For |
|-----------|-------|----------|
| `standard` | 📝 Classic monospace | General text display |
| `block` | 🧱 Bold block style | Headlines, banners |
| `shadow` | 🌑 3D shadow style | 3D effect titles |
| `thin` | ✏️ Thin line style | Elegant text |
| `banner` | 🏁 Large banner style | Eye-catching display |
| `slant` | 📐 Slanted italic style | Dynamic text |
| `small` | 🔤 Compact small style | Space-constrained scenarios |
| `mini` | 🤏 Ultra-mini style | Maximum compression |
| `dotmatrix` | ⚫ Dot matrix style | Retro terminal look |

> 🎯 **Zero external dependencies** — All font engines are fully custom-built. No figlet or external font libraries needed.

### 🖼️ Image to ASCII Art

Convert any image into ASCII character art with **5 character density ramps**:

| Density Ramp | Character Set Richness | Best For |
|-------------|----------------------|----------|
| `simple` | 10-level grayscale characters | Quick preview |
| `detailed` | 70-level grayscale characters | High-fidelity reproduction |
| `blocks` | Unicode block characters | Pixel art style |
| `dots` | Braille dot characters | Fine texture |
| `braille` | Braille characters | Maximum detail |

> ⚠️ Image to ASCII requires **Pillow**: `pip install Pillow`

### 🎨 Color Rendering System

PixelForge-CLI boasts industry-leading terminal color rendering capabilities:

#### 🌈 16 Solid Colors

```
■ black    ■ red      ■ green    ■ yellow
■ blue     ■ magenta  ■ cyan     ■ white
■ bright-black    ■ bright-red    ■ bright-green    ■ bright-yellow
■ bright-blue     ■ bright-magenta ■ bright-cyan     ■ bright-white
```

#### 🎨 9 Gradient Palettes

| Palette Name | Color Style | Visual Effect |
|-------------|------------|---------------|
| `fire` | 🔥 Flame | Red-orange-yellow gradient |
| `ocean` | 🌊 Ocean | Blue-cyan-green gradient |
| `forest` | 🌲 Forest | Green spectrum gradient |
| `sunset` | 🌅 Sunset | Warm tone gradient |
| `rainbow` | 🌈 Rainbow | Full spectrum gradient |
| `purple` | 💜 Purple | Purple spectrum gradient |
| `cyber` | 💻 Cyberpunk | Neon color gradient |
| `pastel` | 🍬 Pastel | Soft color gradient |
| `grayscale` | ⬜ Grayscale | Black-white-gray gradient |

#### 🌈 Rainbow Mode

Enable rainbow color rendering with a single flag — each character automatically maps to the rainbow spectrum, creating the coolest terminal visual effects!

### 📦 Multi-Format Export

| Format | Extension | Features |
|--------|-----------|----------|
| Plain Text | `.txt` | Raw ASCII characters, maximum compatibility |
| Web Page | `.html` | Embedded CSS styling, viewable in browser |
| Data | `.json` | Structured data for programmatic processing |
| Vector | `.svg` | Lossless scaling, print-ready |
| Raster | `.png` | Rasterized output, ready to view |

### 💻 Cross-Platform Support

| Platform | Status | Terminal Compatibility |
|----------|--------|----------------------|
| 🪟 Windows | ✅ Fully Supported | CMD / PowerShell / Windows Terminal |
| 🍎 macOS | ✅ Fully Supported | Terminal.app / iTerm2 / Alacritty |
| 🐧 Linux | ✅ Fully Supported | GNOME Terminal / Konsole / Alacritty |

---

## 🚀 Quick Start · English

### 📦 Installation

```bash
# Install via pip (recommended)
pip install pixelforge-cli

# Install from source
git clone https://github.com/gitstq/PixelForge-CLI.git
cd PixelForge-CLI
pip install -e .

# Optional: Install Pillow for image-to-ASCII support
pip install Pillow
```

### ⚡ Up and Running in 5 Seconds

```bash
# 🎯 Basic text to ASCII
pixelforge text "HELLO" --font block --color cyan
```

Output:
```
 ██  ██                  ██
███  ███                ███
████ ████   ██████  █████████  ██████
████████   ██  ██  █████████  ██  ██
████████   ██████  █████████  ██████
████ ████   ██      ███  ███  ██
███  ███   ████     ███  ███  ████
███  ███    █████   ███  ███   █████
```

```bash
# 🌈 Gradient color rendering
pixelforge text "WORLD" --font shadow --gradient fire
```

```bash
# 🌊 Rainbow mode
pixelforge text "LOVE" --font standard --rainbow
```

```bash
# 🖼️ Image to ASCII
pixelforge image photo.jpg --width 100 --ramp detailed
```

```bash
# 📦 Export to HTML file
pixelforge text "BANNER" --font banner --output art.txt --format html
```

### 🔗 Pipe Operations

PixelForge-CLI fully supports Unix pipe operations:

```bash
# Read input from pipe
echo "PIXELFORGE" | pixelforge text --font slant --color green

# Output to file
pixelforge text "OUTPUT" --font block > output.txt

# Chain commands
pixelforge text "DATA" --font mini --format json | jq '.metadata'
```

---

## 📖 Detailed Usage Guide · English

### 🎛️ Complete CLI Reference

#### `pixelforge text` — Text to ASCII

```bash
pixelforge text <TEXT> [OPTIONS]
```

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--font` | `-f` | Font selection | `standard` |
| `--color` | `-c` | Solid color rendering | None (white) |
| `--gradient` | `-g` | Gradient palette | None |
| `--rainbow` | `-r` | Enable rainbow mode | `False` |
| `--output` | `-o` | Output file path | stdout |
| `--format` | `-F` | Export format | `txt` |
| `--width` | `-w` | Output width limit | Unlimited |

**Available font values:**
`standard` · `block` · `shadow` · `thin` · `banner` · `slant` · `small` · `mini` · `dotmatrix`

**Available solid color values:**
`black` · `red` · `green` · `yellow` · `blue` · `magenta` · `cyan` · `white` · `bright-black` · `bright-red` · `bright-green` · `bright-yellow` · `bright-blue` · `bright-magenta` · `bright-cyan` · `bright-white`

**Available gradient values:**
`fire` · `ocean` · `forest` · `sunset` · `rainbow` · `purple` · `cyber` · `pastel` · `grayscale`

#### `pixelforge image` — Image to ASCII

```bash
pixelforge image <IMAGE_PATH> [OPTIONS]
```

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--width` | `-w` | Output width (characters) | `80` |
| `--height` | `-h` | Output height (characters) | Auto-calculated |
| `--ramp` | `-r` | Character density ramp | `simple` |
| `--color` | `-c` | Enable color mode | `False` |
| `--invert` | `-i` | Invert brightness mapping | `False` |
| `--output` | `-o` | Output file path | stdout |
| `--format` | `-F` | Export format | `txt` |

**Available density ramp values:**
`simple` · `detailed` · `blocks` · `dots` · `braille`

### 🎨 Color Usage Examples

#### Solid Color Rendering

```bash
# Red block font
pixelforge text "ERROR" --font block --color red

# Cyan shadow font
pixelforge text "SYSTEM" --font shadow --color cyan

# Yellow thin font
pixelforge text "WARNING" --font thin --color yellow
```

#### Gradient Rendering

```bash
# 🔥 Fire gradient
pixelforge text "BURN" --font banner --gradient fire

# 🌊 Ocean gradient
pixelforge text "WAVE" --font slant --gradient ocean

# 🌲 Forest gradient
pixelforge text "TREE" --font standard --gradient forest

# 🌅 Sunset gradient
pixelforge text "DUSK" --font block --gradient sunset

# 💜 Purple gradient
pixelforge text "DREAM" --font shadow --gradient purple

# 💻 Cyberpunk gradient
pixelforge text "NEON" --font slant --gradient cyber

# 🍬 Pastel gradient
pixelforge text "SWEET" --font thin --gradient pastel
```

#### Rainbow Mode

```bash
# 🌈 Full rainbow rendering
pixelforge text "RAINBOW" --font banner --rainbow

# 🌈 Mini font rainbow
pixelforge text "COLOR" --font mini --rainbow
```

### 📦 Export Format Examples

```bash
# Export as plain text
pixelforge text "HELLO" --font block --output hello.txt --format txt

# Export as HTML (viewable in browser)
pixelforge text "HELLO" --font block --output hello.html --format html

# Export as JSON (for programmatic processing)
pixelforge text "HELLO" --font block --output hello.json --format json

# Export as SVG (vector, lossless scaling)
pixelforge text "HELLO" --font block --output hello.svg --format svg

# Export as PNG (raster, ready to view)
pixelforge text "HELLO" --font block --output hello.png --format png
```

### 🖼️ Image to ASCII Examples

```bash
# Basic usage — 100 character width, simple ramp
pixelforge image photo.jpg --width 100 --ramp simple

# High-fidelity — 150 character width, detailed ramp
pixelforge image photo.jpg --width 150 --ramp detailed

# Pixel style — Unicode block characters
pixelforge image photo.jpg --width 80 --ramp blocks

# Dot matrix style — Braille characters
pixelforge image photo.jpg --width 120 --ramp braille

# Inverted brightness — for light-background images
pixelforge image photo.jpg --width 100 --ramp detailed --invert

# Color mode — preserve original image colors
pixelforge image photo.jpg --width 100 --ramp detailed --color
```

### 🛠️ Advanced Tips

#### Combining Multiple Options

```bash
# Large banner + fire gradient + export HTML
pixelforge text "AMAZING" --font banner --gradient fire --output amazing.html --format html

# Mini font + rainbow + export SVG
pixelforge text "TINY" --font mini --rainbow --output tiny.svg --format svg
```

#### Using in Scripts

```python
# Calling from Python scripts
import subprocess

result = subprocess.run(
    ["pixelforge", "text", "HELLO", "--font", "block", "--format", "json"],
    capture_output=True,
    text=True
)
print(result.stdout)
```

#### Batch Processing

```bash
# Bash batch generation
for word in HELLO WORLD PIXEL FORGE; do
    pixelforge text "$word" --font block --gradient cyber --output "${word}.html" --format html
done
```

---

## 💡 Design Philosophy & Roadmap · English

### 🎯 Design Principles

PixelForge-CLI is built on the following core principles:

1. **🪶 Lightweight First** — Zero core dependencies, install and run, no system pollution
2. **🎨 Aesthetics-Driven** — Every font is meticulously designed, not just character stacking
3. **🔌 Extensibility** — Modular architecture; fonts, renderers, and exporters are independently extensible
4. **🌍 User-Friendly** — Clean CLI interface, rich documentation, helpful error messages

### 🔄 Version Roadmap

#### v1.0.0 — Current Release ✅

- ✅ 9 custom ASCII font engines
- ✅ 16-color solid rendering
- ✅ 9 gradient palettes + rainbow mode
- ✅ 5 export formats (TXT/HTML/JSON/SVG/PNG)
- ✅ Image to ASCII (5 density ramps)
- ✅ Cross-platform support

#### v1.1.0 — Planned 🚧

- 🔲 Animated ASCII art (GIF/video to ASCII animation)
- 🔲 Custom font loading (user font files)
- 🔲 Terminal live preview mode
- 🔲 Configuration file support (`~/.pixelforge/config.toml`)

#### v1.2.0 — Long-term Vision 🔭

- 🔲 Web UI online editor
- 🔲 ASCII art font marketplace
- 🔲 AI-assisted font generation
- 🔲 Plugin system

### 🏗️ Architecture Highlights

```
┌─────────────────────────────────────────────┐
│                  CLI Layer                   │
│            (argparse + entry_point)          │
├──────────┬──────────┬──────────┬─────────────┤
│  Fonts   │Renderer  │Converter │  Exporter   │
│  Engine  │  Engine  │  Engine  │   Engine    │
│ (9 fonts)│(16+9+🌈) │(5 ramps) │(5 formats) │
├──────────┴──────────┴──────────┴─────────────┤
│              Core Processing Pipeline         │
├─────────────────────────────────────────────┤
│           Platform Abstraction Layer          │
│        (Windows / macOS / Linux)             │
└─────────────────────────────────────────────┘
```

- **Module Decoupling** — Font, rendering, conversion, and export engines are fully decoupled for independent development and testing
- **Plugin-Friendly** — Adding a new font requires only a single Python file with no core code modifications
- **Pipeline Design** — Input → Font Rendering → Color Processing → Format Export, assembly-line processing

---

## 📦 Packaging & Deployment Guide · English

### 🏗️ Project Structure

```
PixelForge-CLI/
├── src/
│   └── pixelforge/          # 📂 Core source code
│       ├── __init__.py
│       ├── cli.py           # 🎛️ CLI entry point
│       ├── fonts/           # 🔤 Font engines
│       ├── renderers/       # 🎨 Rendering engines
│       ├── converters/      # 🖼️ Conversion engines
│       └── exporters/       # 📦 Export engines
├── tests/                   # 🧪 Test cases
├── pyproject.toml           # ⚙️ Project configuration
├── LICENSE                  # 📄 MIT License
├── .gitignore              # 🚫 Git ignore rules
└── README.md               # 📖 Project documentation
```

### 📦 Building Distribution Packages

```bash
# 1. Install build tools
pip install build

# 2. Build distribution packages
python -m build

# 3. Generated files are in the dist/ directory
#    dist/pixelforge_cli-1.0.0-py3-none-any.whl
#    dist/pixelforge_cli-1.0.0.tar.gz
```

### 🚀 Publishing to PyPI

```bash
# 1. Install Twine
pip install twine

# 2. Check package contents
twine check dist/*

# 3. Upload to PyPI (production)
twine upload dist/*

# 4. Or upload to TestPyPI (testing)
twine upload --repository testpypi dist/*
```

### 🐍 Environment Requirements

| Item | Requirement |
|------|-------------|
| Python Version | **>= 3.8** |
| Core Dependencies | **None** (zero dependencies) |
| Optional Dependencies | **Pillow** (image to ASCII) |
| Operating System | Windows / macOS / Linux |

### 🔧 Development Environment Setup

```bash
# Clone the repository
git clone https://github.com/gitstq/PixelForge-CLI.git
cd PixelForge-CLI

# Install in development mode (editable install)
pip install -e .

# Optional: Install Pillow
pip install Pillow

# Run tests
python -m pytest tests/

# Verify installation
pixelforge text "TEST" --font block
```

---

## 🤝 Contributing Guide · English

> 🙌 First of all, thank you for your interest in PixelForge-CLI! Whether it's reporting a bug, improving documentation, or contributing code, every effort is valued.

### 📋 Contribution Workflow

1. **🍴 Fork this repository** — Click the Fork button in the top-right corner of the GitHub page
2. **📥 Clone locally** — `git clone https://github.com/<your-username>/PixelForge-CLI.git`
3. **🌿 Create a feature branch** — `git checkout -b feature/your-feature-name`
4. **✏️ Start developing** — Write code and ensure all tests pass
5. **🧪 Run tests** — `python -m pytest tests/`
6. **📝 Commit your changes** — `git commit -m "feat: describe your changes"`
7. **📤 Push the branch** — `git push origin feature/your-feature-name`
8. **🔀 Create a Pull Request** — Submit a PR on GitHub

### ✍️ Commit Message Convention

Please follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
feat: add DotMatrix font support
fix: fix Shadow font width calculation error
docs: update README quick start section
style: unify code indentation format
refactor: refactor color rendering engine
test: add font engine unit tests
chore: update pyproject.toml version number
```

### 🆕 Adding a New Font

PixelForge-CLI's font engine uses a modular design. Adding a new font is straightforward:

```python
# src/pixelforge/fonts/your_font.py

CHAR_MAP = {
    'A': [
        " ██ ",
        "█  █",
        "████",
        "█  █",
        "█  █",
    ],
    # ... other character mappings
}

HEIGHT = 5  # Font height
```

Then register it in `fonts/__init__.py`.

### 🐛 Reporting Bugs

Please use [GitHub Issues](https://github.com/gitstq/PixelForge-CLI/issues) to submit bug reports with the following information:

- 🖥️ Operating system and version
- 🐍 Python version
- 📦 PixelForge-CLI version
- 📝 Steps to reproduce
- 📸 Error screenshots or logs

### 📜 Code of Conduct

- Respect all contributors
- Accept constructive code reviews
- Maintain friendly and professional communication
- Focus on code quality and maintainability

---

## 📄 License · English

This project is licensed under the **[MIT License](LICENSE)**.

```
MIT License

Copyright (c) 2024 PixelForge-CLI Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

> 📌 In short: You are **free to use, modify, and distribute** this software. The only requirement is to retain the copyright and license notices.

---

<div align="center">

**[⬆ Back to Top](#-pixelforge-cli) · [🌐 Switch Language](#-table-of-contents)**

---

<br/>

<img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red.svg" />
<img src="https://img.shields.io/badge/PixelForge--CLI-v1.0.0-orange.svg" />

</div>
