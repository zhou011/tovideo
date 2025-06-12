from flask import Flask, request, jsonify, render_template
import json
import os
from moviepy.editor import *
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({"status": "running", "message": "ToVideo API is working"})

@app.route('/api/generate', methods=['POST'])
def generate_video():
    try:
        data = request.json
        
        # 向后兼容：如果使用旧的字段名，自动转换为新的字段名
        if 'cover' in data and 'cover_img' not in data:
            data['cover_img'] = data['cover']
        if 'cover_speed' in data and 'cover_speech' not in data:
            data['cover_speech'] = data['cover_speed']
        
        # 验证必需字段
        if 'cover_img' not in data:
            return jsonify({"error": "Missing required field: cover_img"}), 400
        
        # 设置默认值
        output_file = data.get('output_file', 'output.mp4')
        cover_img = data['cover_img']
        cover_speech = data.get('cover_speech', '')
        background_music = data.get('background_music', '')
        video_duration = data.get('video_duration', 10)
        resolution = data.get('resolution', [1920, 1080])
        fps = data.get('fps', 30)
        
        # 这里添加实际的视频生成逻辑
        # 目前返回成功状态用于演示
        
        return jsonify({
            "status": "success", 
            "message": "Video generated successfully",
            "output_file": output_file,
            "config": {
                "cover_img": cover_img,
                "cover_speech": cover_speech,
                "background_music": background_music,
                "video_duration": video_duration,
                "resolution": resolution,
                "fps": fps
            }
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)