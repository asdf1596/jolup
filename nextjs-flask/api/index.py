from flask import Flask
from joluppy2 import main  # 외부 파일에서 main 함수를 가져옵니다.
import time
app = Flask(__name__)

@app.route("/api/python")
def run_main():
    main_result = main()  # main 함수를 호출하고 결과를 저장합니다.
    return f"<p>{main_result}</p>"  # main 함수의 결과를 응답으로 반환합니다.

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5328)
