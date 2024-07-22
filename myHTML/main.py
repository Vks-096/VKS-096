from flask import Flask, render_template, request


app = Flask(__name__)


# 定义主页路由
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        return render_template('index.html')
    else:
        return render_template('登录.html')


# 定义信息页面路由
@app.route('/information')
def information():
    return render_template('消息.html')


@app.route('/works')
def community():
    return render_template('个人作品.html')


@app.route('/personal')
def personal():
    return render_template('个人简介.html')


@app.route('/contact')
def contact():
    h = 'hello world'
    return render_template('基础模板.html', h=h)


# 运行 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
