from flask import Flask, jsonify
from joluppy2 import main
import threading
import time

app = Flask(__name__)

# 전역 변수로 최신 값을 저장
latest_result = ""

# 주기적으로 값을 업데이트하는 함수
def update_result():
    global latest_result
    while True:
        latest_result = main()
        time.sleep(0.1)

# Flask 엔드포인트에서 최신 값을 반환
@app.route("/api/python")
def hello_world():
    return(f"<p>{latest_result}</p>")

if __name__ == "__main__":
    # 별도의 스레드에서 주기적으로 값을 업데이트
    threading.Thread(target=update_result, daemon=True).start()
    app.run(port=5328)
