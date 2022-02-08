import webbrowser

def html_page_download(content):
  html_content_download=f"<!DOCTYPE html><html lang='en'><head><link rel='stylesheet' href='/static/download_page.css'><title>OSG - Video Transcription Tool</title></head><meta charset='utf-8'><body><div class='logo'><br/><img src='/static/osg_logo.jpg' height='50'></div><h3>Transcription Status:</h3><br><p>{content}</p><br><p><div class='btnss' align ='center'><br/><a href='download' download class='download-btn'>Download Transcribed Documents</a><br/><a href='logs' class='logs-btn'>Logs</a><br/></div><br/></p></body></html>"

  return html_content_download


def html_page_logs(content):
  html_content_logs=f"<!DOCTYPE html><html lang='en'><head><link rel='stylesheet' href='/static/download_page.css'><title>OSG - Video Transcription Tool</title></head><meta charset='utf-8'><body><div class='logo'><br/><img src='/static/osg_logo.jpg' height='50'></div><p>{content}</p></body></html>"

  return html_content_logs


def html_webpage():
  html_webpage_content =f"<!DOCTYPE html><html lang='en'><head><link rel='stylesheet' href='/static/webpage.css'><title>OSG - Video Transcription Tool</title></head><meta charset='utf-8'><body><div class='logo' align='center'><br/><br/><br/><br/><br/><img src='static/osg_logo.jpg' height='100'></div><br/><br/><br/><br/><div class='head' align ='center'><br/><h1>Video Transcription Tool</h1><h2><form enctype='multipart/form-data' method='post' align='center'><input name='files' class='upload-box' type='file' multiple><button type=submit class='btn' onclick='><span class='btn_text'>Transcribe</span></button><script>btn_ = document.querySelector('.btn_text');btn_.onclick = function() {this.innerHTML = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; transcribing...'this.classList.toggle('btn_loading')}</script></h2><br/></div></body></html>"

  return html_webpage_content