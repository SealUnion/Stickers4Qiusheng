#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单的HTTP服务器脚本
用于本地查看表情包库页面

使用方法:
    python3 server.py
    
然后在浏览器中访问: http://localhost:8000
"""

import http.server
import socketserver
import os
from pathlib import Path

# 获取脚本所在目录
script_dir = Path(__file__).parent
os.chdir(script_dir)

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加缓存控制头，防止浏览器过度缓存
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

Handler = MyHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"HTTP 服务器运行在: http://localhost:{PORT}")
    print(f"项目目录: {script_dir}")
    print("")
    print("按 Ctrl+C 停止服务器")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
