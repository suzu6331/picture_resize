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
                    <input type="submit" value="リサイズ" />
                </form>
            </body>
        </html>
    '''

