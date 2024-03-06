from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <html>
            <body>
                <form action="/resize" method="post" enctype="multipart/form-data">
                    <input type="file" name="image" required />
                    <input type="number" name="target_size" placeholder="目標サイズ（MB単位）" required />
                    <input type="submit" value="resize" />
                </form>
            </body>
        </html>
    '''


def resize_picture():
    image_file = request.files['image']
    target_size_mb = float(request.form['target_size'])
    target_size = target_size_mb * 1024 * 1024  #バイトに変換

    img = Image.open(image_file)
    buffer = io.BytesIO()
    
    # 画質を下げながら調整
    for quality in range(100,0,-5):
        buffer.seek(0)
        img.save(buffer,'JPEG',quality=quality)
        size = buffer.tell()
        if size <= target_size : break
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='resized_image.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)