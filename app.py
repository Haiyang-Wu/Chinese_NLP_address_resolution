from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        addrStr_py = request.form.get('addrStr')
        print(addrStr_py)
        # 处理代码
    provinceName_py = "北京市"
    cityName_py = "北京市"
    areaName_py = "海淀区"
    countyName_py = "学院路"
    otherName_py = "北京科技大学"
    return render_template('index.html', provinceName=provinceName_py,cityName=cityName_py,areaName=areaName_py,countyName=countyName_py,otherName=otherName_py)


if __name__ == '__main__':
    app.run()
