from flask import Flask, render_template, request, url_for
import poi

app = Flask(__name__)
app.config['SECRET_KEY'] = '1456719640@qq.com'


@app.route("/", methods=['GET', 'POST'])
def root():
    """
    主页
    :return: Index.html
    """

    if request.method == 'GET':
        return render_template('hello.html')
    elif request.method == 'POST':
        a = request.values.get('按钮一')
        b = request.values.get('按钮二')
        print(a, b)
        if a == '咖啡厅':
            return render_template('index.html', a=a)
        if b == '驻马店':
            return render_template('b.html', message='按钮二被点击', location=poi.location)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
