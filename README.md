# Markdown to PDF 转换器

这个项目提供了一套工具，用于将Markdown文件转换为PDF格式，特别支持Mermaid图表的渲染。它包含命令行工具和图形用户界面(GUI)应用程序，适合不同用户的需求。

## 功能特点

- 将Markdown文件转换为高质量PDF
- 支持Mermaid图表渲染
- 支持图片和表格
- 自动处理资源路径
- 提供简单易用的图形界面
- 支持命令行操作

## 使用要求

要使用这些工具，您需要安装以下软件：

1. **Pandoc** - 用于Markdown转PDF的核心工具
   - 安装说明: [https://pandoc.org/installing.html](https://pandoc.org/installing.html)

2. **LaTeX** - PDF引擎（由Pandoc使用）
   - 建议安装 [MiKTeX](https://miktex.org/download) (Windows) 或 [MacTeX](https://www.tug.org/mactex/) (macOS)

3. **Python 3.6+** - 运行脚本需要
   - 安装说明: [https://www.python.org/downloads/](https://www.python.org/downloads/)

4. **Mermaid-CLI** (可选，用于Mermaid图表渲染)
   - 安装命令: `npm install -g @mermaid-js/mermaid-cli`
   - 需要先安装 [Node.js](https://nodejs.org/)

## 使用方法

### 图形用户界面 (GUI)

最简单的使用方式是通过图形界面：

1. 运行GUI应用程序：
   ```bash
   python md_to_pdf_gui.py
   ```

2. 使用界面选择Markdown文件并设置输出选项
3. 点击"转换为PDF"按钮
4. 转换完成后可以直接打开生成的PDF文件

### 命令行工具

#### 基本命令行工具

使用简单的命令行工具：

```bash
python md_to_pdf.py input.md -o output.pdf
```

#### 带Mermaid支持的命令行工具

使用支持Mermaid图表的高级命令行工具：

```bash
python md_to_pdf_with_mermaid.py input.md -o output.pdf
```

## 样式和格式

转换后的PDF将保持原始Markdown的格式和样式。包括：

- 标题和章节结构
- 图片和表格
- 代码块和引用
- Mermaid图表（当启用该功能时）
- 链接和引用

## 常见问题

1. **Mermaid图表不显示？**
   - 确保已安装mermaid-cli
   - 检查Mermaid代码格式是否正确

2. **中文或特殊字符显示乱码？**
   - 确保使用UTF-8编码保存Markdown文件
   - PDF引擎使用XeLaTeX，应该能正常支持各种语言字符

3. **图片无法显示？**
   - 确保图片路径正确，最好使用相对路径
   - 可以将图片放在与Markdown文件相同的目录或专门的image目录下

## 项目文件说明

- `md_to_pdf.py` - 基本的Markdown到PDF转换工具
- `md_to_pdf_with_mermaid.py` - 支持Mermaid图表的Markdown到PDF转换工具
- `md_to_pdf_gui.py` - 图形用户界面应用程序
- `README.md` - 项目文档

## 许可协议

本项目采用MIT许可证。

## 贡献者

欢迎贡献代码或提出建议！

## 更新日志

### 1.0.0 (2023-04-01)
- 初始版本发布
- 支持基本Markdown转PDF功能
- 添加Mermaid图表支持
- 提供图形用户界面 