#!/usr/bin/env python3
"""
普拉提健身App原型查看器
========================

这个简单的脚本会在默认浏览器中打开普拉提健身App的原型设计HTML文件。
"""

import os
import sys
import webbrowser
import http.server
import socketserver
import threading
import time

# HTML文件名
HTML_FILE = "pilates_app_prototype.html"

def open_in_browser():
    """在默认浏览器中打开HTML文件"""
    # 检查文件是否存在
    if not os.path.exists(HTML_FILE):
        print(f"错误: 找不到文件 '{HTML_FILE}'")
        return False
    
    # 获取当前目录的绝对路径
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, HTML_FILE)
    
    # 转换为URL格式
    file_url = f"http://localhost:8000/{HTML_FILE}"
    
    print(f"正在打开原型设计文件...")
    print(f"如果浏览器没有自动打开，请访问: {file_url}")
    
    # 等待服务器启动
    time.sleep(1)
    
    # 在默认浏览器中打开
    webbrowser.open(file_url)
    
    return True

def start_server():
    """启动一个简单的HTTP服务器来提供HTML文件"""
    # 获取当前目录
    current_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(current_dir)
    
    # 创建HTTP服务器
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", 8000), handler) as httpd:
            print("服务器启动在 http://localhost:8000")
            print("按 Ctrl+C 停止服务器")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except OSError as e:
        if e.errno == 48:  # 地址已被使用
            print("错误: 端口8000已被占用，请关闭其他应用后重试")
        else:
            print(f"服务器错误: {e}")

def main():
    """主函数"""
    print("普拉提健身App原型查看器")
    print("========================")
    
    # 检查文件是否存在
    if not os.path.exists(HTML_FILE):
        print(f"错误: 找不到原型设计文件 '{HTML_FILE}'")
        print("请确保文件位于当前目录，并且文件名正确")
        return
    
    # 启动HTTP服务器
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # 在浏览器中打开
    open_in_browser()
    
    try:
        # 保持主线程运行，等待用户终止
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序已结束")

if __name__ == "__main__":
    main() 