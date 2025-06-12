#!/usr/bin/env python3
"""
ToVideo Web Server Launcher
启动 ToVideo 的 Web 服务器
"""

import os
import sys
from app import app

def main():
    print("🎬 ToVideo Web Server")
    print("=" * 50)
    print("Starting web server...")
    print("Access the application at:")
    print("  Local:   http://localhost:8080")
    print("  Network: http://0.0.0.0:8080")
    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        app.run(debug=True, host='0.0.0.0', port=8080)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()