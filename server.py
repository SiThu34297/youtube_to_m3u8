from flask import Flask,render_template,request,redirect,send_file
from utils.audio_converter import download
import os
import shlex

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/convert-audio', methods=['POST'])
def convert_audio():
    youtube_link = str(request.form['youtube_link'])
    if youtube_link.strip() != "" and (youtube_link.startswith("https://youtu.be") or youtube_link.startswith('https://www.youtube.com')):
        exists,download_link,path = download(youtube_link)
        if exists:
            return send_file(download_link,as_attachment=True)
        else:
            if download_link:
                os.system("rm -rf %s"%(shlex.quote(path)))
                return send_file(download_link,as_attachment=True)
    return redirect('/',error="Error")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)