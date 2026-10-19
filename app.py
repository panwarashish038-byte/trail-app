from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head><meta charset="utf-8"><title>Northern Node - Trial</title></head>
    <body style="font-family:sans-serif;text-align:center;padding:60px;background:#f0f4f3;color:#1d2b26;">
      <div style="font-size:64px;">🎉</div>
      <h1>Namaste, Ashish!</h1>
      <p style="font-size:20px;">Ye page <b>cloud</b> se aa raha hai —<br>tumhare PC se <b>nahi</b>!</p>
      <p style="font-size:18px;color:#0b5c63;"><b>Northern Node</b> — deployment trial successful ✅</p>
      <p style="color:#888;">Ab tum cloud par deploy karna jaante ho! ☁️</p>
    </body>
    </html>
    """
