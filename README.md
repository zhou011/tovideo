# ToVideo 视频生成工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub issues](https://img.shields.io/github/issues/zhou011/tovideo)](https://github.com/zhou011/tovideo/issues)
[![GitHub stars](https://img.shields.io/github/stars/zhou011/tovideo)](https://github.com/zhou011/tovideo/stargazers)

> **作者**: baozi  
> **在线演示**: [http://localhost:8080](http://localhost:8080) (本地运行后访问)

一个强大的视频生成工具，可以自动将文本、图片和音频内容组合成视频。支持多种输出格式和自定义配置。

## ✨ 功能特性

- 🎬 **自动视频生成**: 将文本、图片、音频智能组合成视频
- 🖼️ **多格式支持**: 支持 JPG、PNG、GIF 等图片格式
- 🎵 **音频集成**: 支持背景音乐和语音合成
- 🌐 **Web界面**: 直观的网页操作界面，支持实时预览
- ⚙️ **灵活配置**: 丰富的参数设置，满足不同需求
- 📱 **响应式设计**: 支持桌面和移动设备
- 🔧 **命令行工具**: 支持批量处理和自动化

## 🚀 快速开始

### 安装依赖

#### 1. 安装 FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
1. 从 [FFmpeg官网](https://ffmpeg.org/download.html) 下载
2. 解压并添加到系统PATH

#### 2. 安装 Python 依赖

```bash
pip install flask moviepy pillow requests
```

### 使用方法

#### Web 界面 (推荐)

1. 启动 Web 服务器：
```bash
python3 run_web.py
```

2. 打开浏览器访问：`http://localhost:8080`

3. 在网页界面中：
   - 输入 JSON 配置
   - 使用 "清空" 按钮清除输入
   - 使用 "格式化" 按钮美化 JSON 格式
   - 点击 "生成视频" 开始处理

#### 命令行使用

```bash
python3 app.py
```

**示例 JSON 配置：**
```json
{
  "output_file": "output.mp4",
  "cover_img": "cover.jpg",
  "cover_speech": "欢迎观看我的视频",
  "background_music": "background.mp3",
  "video_duration": 10,
  "resolution": [1920, 1080],
  "fps": 30
}
```

## ⚙️ 配置说明

| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| `output_file` | string | 输出视频文件名 | "output.mp4" |
| `cover_img` | string | 封面图片路径 | 必填 |
| `cover_speech` | string | 封面语音文本 | 可选 |
| `background_music` | string | 背景音乐路径 | 可选 |
| `video_duration` | number | 视频时长(秒) | 10 |
| `resolution` | array | 视频分辨率 [宽, 高] | [1920, 1080] |
| `fps` | number | 帧率 | 30 |

## 📝 注意事项

- 确保所有输入文件路径正确且文件存在
- 支持的图片格式：JPG, PNG, GIF, BMP
- 支持的音频格式：MP3, WAV, AAC, M4A
- 生成的视频将保存在当前目录
- Web 服务器默认运行在端口 8080

## 🔧 常见问题

### Q: FFmpeg 未找到
A: 请确保 FFmpeg 已正确安装并添加到系统 PATH

### Q: 图片无法加载
A: 检查图片路径是否正确，支持相对路径和绝对路径

### Q: 音频同步问题
A: 调整 `video_duration` 参数以匹配音频长度

### Q: 内存不足
A: 降低视频分辨率或减少视频时长

## 🤝 贡献指南

我们欢迎所有形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细信息。

### 贡献者

- [@baozi](https://github.com/baozi) - 项目创建者和主要维护者

## 📋 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新历史。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

MIT 许可证允许您：
- ✅ 商业使用
- ✅ 修改代码
- ✅ 分发代码
- ✅ 私人使用

## 🙏 致谢

- [FFmpeg](https://ffmpeg.org/) - 强大的多媒体处理框架
- [MoviePy](https://zulko.github.io/moviepy/) - Python 视频编辑库
- [Flask](https://flask.palletsprojects.com/) - 轻量级 Web 框架
- [Pillow](https://pillow.readthedocs.io/) - Python 图像处理库

## 📞 联系方式

- 项目主页: [https://github.com/zhou011/tovideo](https://github.com/zhou011/tovideo)
- 问题反馈: [GitHub Issues](https://github.com/zhou011/tovideo/issues)
- 邮箱: [联系邮箱]

---

⭐ 如果这个项目对您有帮助，请给我们一个 Star！