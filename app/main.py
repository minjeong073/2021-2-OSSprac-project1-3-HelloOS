from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def student():
   return render_template('main.html')


@app.route('/detail', methods=['POST', 'GET'])
def detail():
   if request.method == 'POST':
      detail = dict()
      detail['Name'] = request.form.get('Name')
      detail['StudentNumber'] = request.form.get('StudentNumber')
      detail['Gender'] = request.form.get('Gender')
      detail['Major'] = request.form.get('Major')
      res = make_response(render_template("detail.html", detail=detail))
      res.set_cookie("Name", detail['Name'])
      res.set_cookie("StudentNumber", detail['StudentNumber'])
      res.set_cookie("Gender", detail['Gender'])
      res.set_cookie("Major", detail['Major'])
      return res


@app.route('/result', methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.cookies.get('Name')
      result['StudentNumber'] = request.cookies.get('StudentNumber')
      result['Gender'] = request.cookies.get('Gender')
      result['Major'] = request.cookies.get('Major')
      return render_template("result.html", result=result)


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
