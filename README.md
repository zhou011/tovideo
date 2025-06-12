# ToVideo 视频生成工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

这是一个自动将文本、图片和音频内容组合成视频的工具。支持Web界面和命令行两种使用方式，能够快速生成包含封面页和内容页的视频文件。


## 功能特点

- 支持封面页面生成
- 支持多个内容页面
- 自动处理英文和中文音频
- 支持文字叠加和转场效果
- 自动下载和缓存媒体文件

## 安装说明

1. 克隆项目到本地：
```bash
git clone https://github.com/zhou011/tovideo.git
cd tovideo
```

2. 创建并激活虚拟环境（推荐）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 安装 FFmpeg（必需）：

   **Windows:**
   - 访问 [FFmpeg官网](https://ffmpeg.org/download.html#build-windows) 下载预编译版本
   - 或使用 Chocolatey：`choco install ffmpeg`
   - 或使用 Scoop：`scoop install ffmpeg`

   **macOS:**
   ```bash
   # 使用 Homebrew（推荐）
   brew install ffmpeg
   
   # 或使用 MacPorts
   sudo port install ffmpeg
   ```

   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

   **Linux (CentOS/RHEL/Fedora):**
   ```bash
   # CentOS/RHEL
   sudo yum install epel-release
   sudo yum install ffmpeg
   
   # Fedora
   sudo dnf install ffmpeg
   ```

   安装完成后，验证安装：
   ```bash
   ffmpeg -version
   ```

## 使用方法

### AI智能生成JSON素材（推荐）

如果您不想手动编写JSON配置文件，可以使用我们的AI助手来自动生成：

1. 访问AI助手页面：[https://www.coze.cn/s/dJ58QS_8Sgg/](https://www.coze.cn/s/dJ58QS_8Sgg/)

2. 在对话框中描述您想要制作的视频内容，例如：
**语言学习类**：
- 10条电铁见面打招呼的常用语
- 日常购物必备英语对话
- 商务会议常用表达

3. AI助手会根据您的描述自动生成完整的JSON配置文件



### 方法一：Web界面（推荐）

1. 启动Web服务：
```bash
python run_web.py
```

2. 打开浏览器访问：http://localhost:8080

3. 在Web界面中：
   - 输入JSON配置内容（可使用"清除"和"格式化"按钮管理JSON内容）
   - 设置输出文件名
   - 点击"生成视频"按钮
   - 查看实时进度
   - 预览和下载生成的视频

### 方法二：命令行

1. 准备输入JSON文件，格式如下：
```json
{
    "content": [
        {
            "cn": "中文文本",
            "en": "English Text",
            "img": "图片URL",
            "cn_speech": "中文语音URL",
            "en_speech": "英文语音URL"
        }
        // ... 更多内容
    ],
    "cover_img": "封面图片URL",
    "cover_speech": "封面音频URL",
    "cover_txt": "封面文字"
}
```

2. 运行程序：
```bash
python main.py -i input.json -o output.mp4
```

参数说明：
- `-i` 或 `--input`：输入JSON文件路径（必需）
- `-o` 或 `--output`：输出视频文件路径（可选，默认为 output.mp4）

## 配置说明

可以在 `config/settings.py` 中修改以下配置：

- 视频尺寸和质量
- 转场效果时长
- 文字样式和位置
- 输出视频编码参数

## 注意事项

1. 确保所有URL可以正常访问
2. 建议使用高质量的图片和音频文件
3. 运行过程中会在temp目录下缓存媒体文件
4. 生成完成后会自动清理缓存

## 常见问题

1. 如果出现字体相关错误，请确保系统安装了相应的字体
2. 如果下载媒体文件失败，请检查网络连接和URL有效性
3. 如果生成视频时内存不足，可以尝试降低视频质量设置

## 🤝 贡献

我们欢迎任何形式的贡献！请查看 [贡献指南](CONTRIBUTING.md) 了解如何参与项目开发。

### 贡献者

感谢所有为这个项目做出贡献的人！

- [@baozi](https://github.com/zhou011) - 项目创建者和维护者

## 📝 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细的版本更新历史。

## 📄 许可证

本项目基于 MIT 许可证开源 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢 [FFmpeg](https://ffmpeg.org/) 提供强大的视频处理能力
- 感谢 [Flask](https://flask.palletsprojects.com/) 提供Web框架支持

## 📞 联系方式

如果您有任何问题或建议，请通过以下方式联系我们：

- 创建 [Issue](https://github.com/baozi/tovideo/issues)
- 提交 [Pull Request](https://github.com/baozi/tovideo/pulls)

---

⭐ 如果这个项目对您有帮助，请给我们一个星标！