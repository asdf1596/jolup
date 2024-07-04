from flask import Flask # Flask
from joluppy2 import main
app = Flask(__name__)

@app.route('/users')
def users():
	# users 데이터를 Json 형식으로 반환한다
    val = main()
    return {"val": val}
           

if __name__ == "__main__":
    app.run(debug = True)