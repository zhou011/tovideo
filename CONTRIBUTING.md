# 贡献指南

感谢您对 ToVideo 项目的关注！我们欢迎任何形式的贡献。

## 如何贡献

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 开发环境设置

请参考 README.md 中的安装说明来设置开发环境。

### 环境要求

- Python 3.7+
- FFmpeg
- 所有在 requirements.txt 中列出的依赖

### 本地开发

1. 克隆您 fork 的仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 启动开发服务器：`python run_web.py`
4. 访问 http://localhost:8080 进行测试

## 代码规范

- 遵循 Python PEP 8 代码风格
- 为新功能添加适当的注释和文档字符串
- 确保代码通过现有测试
- 为新功能编写测试用例

## 提交信息规范

请使用清晰、描述性的提交信息：

- `feat: 添加新功能`
- `fix: 修复bug`
- `docs: 更新文档`
- `style: 代码格式调整`
- `refactor: 代码重构`
- `test: 添加测试`

## 报告问题

如果您发现了 bug 或有功能建议，请：

1. 检查是否已有相关的 issue
2. 如果没有，请创建新的 issue
3. 提供详细的描述和重现步骤
4. 如果可能，请提供错误日志或截图

## 功能请求

我们欢迎新功能的建议！请在 issue 中详细描述：

- 功能的用途和价值
- 预期的行为
- 可能的实现方案

## 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。