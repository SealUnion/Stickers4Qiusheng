# 凌秋升 表情包库

一个现代化的表情包展示和搜索网页应用，基于 MDUI v1 框架构建。

## 功能特性

✨ **核心功能**
- 📸 响应式网格展示所有表情包
- 🔍 实时搜索和过滤表情包
- 🎨 深色/浅色主题切换
- 📱 优化的手机端UI
- 💾 离线支持（Service Worker）
- ⌨️ 键盘快捷键支持

## 快速开始

### 方式一：使用Python服务器（推荐）

```bash
python3 server.py
```

然后在浏览器中访问：`http://localhost:8000`

### 方式二：直接打开HTML文件

在浏览器中打开 `index.html` 文件。

注意：某些功能（如搜索）需要通过HTTP服务器访问才能正常工作。

### 方式三：使用其他HTTP服务器

```bash
# Node.js
npx http-server

# PHP
php -S localhost:8000

# Ruby
ruby -run -ehttpd . -p8000
```

## 文件结构

```
Stickers4Qiusheng/
├── index.html                    # 主页面
├── stickers_metadata.json        # 元数据（中文描述 -> 图片路径）
├── stickers/                     # 表情包目录
│   ├── 1.gif
│   ├── 2.gif
│   └── ...（1-113.gif）
├── server.py                     # Python HTTP服务器
├── sw.js                         # Service Worker（离线支持）
├── generate_metadata.py          # 元数据生成脚本
├── rename_stickers.sh            # 文件重命名脚本
└── README.md                     # 本文件
```

## 使用说明

### 搜索表情包

1. 在搜索框中输入关键词
2. 支持按中文描述或序号搜索
3. 实时显示匹配结果数

### 暗色/浅色主题切换

- **点击方式**：点击顶部右角的主题图标
- **快捷键**：`Ctrl+Shift+L` (Windows/Linux) 或 `Cmd+Shift+L` (Mac)

### 查看详细信息

1. 点击任何表情包卡片
2. 在弹出窗口中查看大图和描述
3. 可以直接下载表情包

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+K` / `Cmd+K` | 快速搜索 |
| `Ctrl+Shift+L` / `Cmd+Shift+L` | 切换主题 |

## 技术栈

- **前端框架**：MDUI v1
- **样式**：CSS3 + Material Design
- **功能语言**：HTML + JavaScript + Python
- **离线支持**：Service Worker
- **主题系统**：localStorage 持久化

## 浏览器兼容性

- Chrome/Chromium 50+
- Firefox 45+
- Safari 10+
- Edge 15+
- 移动浏览器（iOS Safari, Chrome Mobile 等）

## 元数据格式

`stickers_metadata.json` 文件格式：

```json
{
  "中文描述": "/stickers/1.gif",
  "另一个描述": "/stickers/2.gif",
  ...
}
```

## 生成新的元数据

如果添加或修改了表情包，需要重新运行生成脚本：

```bash
python3 generate_metadata.py
```

此脚本会：
1. 自动重命名文件为 `1.gif` 到 `113.gif`
2. 提取文件名中的中文描述
3. 生成新的 `stickers_metadata.json`

## 重命名文件

如果需要将文件名从 `LingQiusheng_*` 改为其他格式，运行：

```bash
bash rename_stickers.sh
```

## 性能优化

- 🚀 **CDN**: 使用 jsDelivr CDN 加载 MDUI
- 📦 **缓存**: Service Worker 缓存资源
- 🖼️ **图片**: 使用 pixelated 渲染保持清晰度
- 📱 **响应式**: 移动端自动调整布局

## 离线支持

首次访问后，应用会缓存所有资源。即使没有网络连接，也可以离线浏览已缓存的表情包。

## 开发建议

### 自定义样式

编辑 `index.html` 中的 `<style>` 部分：

```css
/* 修改网格列数 */
.grid {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
}

/* 修改主题色 */
.mdui-appbar {
    background-color: #your-color;
}
```

### 添加新功能

1. 在 `<script>` 中添加新的事件监听器
2. 修改 `renderStickers()` 函数来改变展示方式
3. 更新 Service Worker 以缓存新资源

## 许可证

MIT License

## 致谢

- 表情包资源：凌秋升
- UI框架：[MDUI](https://mdui.org)
- 图标：[Material Icons](https://fonts.google.com/icons)

---

**最后更新**：2026-04-16

**版本**：1.0.0
