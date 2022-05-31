import base64
from flask import Flask
from flask import render_template
import forms
import crypto_tools
import urllib.parse


app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/crypto')
def crypto():
    return render_template("crypto/crypto.html")

@app.route('/crypto/numeric', methods = ['GET', 'POST'])
def crypto_numeric():
    form = forms.NumericForm()
    result = ""
    error = ""
    if form.validate_on_submit():
        source = form.source.data
        from_ = form.from_.data
        to = form.to.data
        delimiter = " " if form.delimiter.data == "" else form.delimiter.data
        try:
            result = crypto_tools.numeric(source, from_, to, delimiter)
        except:
            error = "Incorrect numeric system"
    return render_template("crypto/numeric.html",
                           form=form, result=result, add_error=error)

@app.route('/crypto/base64', methods = ['get', 'post'])
def crypto_base64():
    form = forms.Base64Form()
    result = ""
    error = ""
    if form.validate_on_submit():
        if form.radio.data == "Encode":
            result = base64.b64encode(bytes(form.source.data, 'UTF-8')).decode('UTF-8')
        else:
            try:
                result = base64.b64decode(bytes(form.source.data, 'UTF-8')).decode('UTF-8')
            except:
                error = "Entered string is not in base64 format"
    return render_template("crypto/base64.html",
                           form=form, result=result, add_error=error)

@app.route('/crypto/url', methods = ['get', 'post'])
def url():
    form = forms.URLForm()
    result = ""
    error = ""
    if form.validate_on_submit():
        if form.radio.data == "Encode":
            result = urllib.parse.quote_plus(bytes(form.source.data, 'UTF-8'))
        else:
            result = str(urllib.parse.unquote(form.source.data))
    return render_template("crypto/url.html",
                           form=form, result=result, add_error=error)


@app.route('/crypto/rot', methods = ['get', 'post'])
def rot():
    form = forms.ROTForm()
    result = ""
    error = ""
    if form.validate_on_submit():
        result = crypto_tools.rotx(form.source.data, form.turn.data)
    return render_template("crypto/rot.html",
                           form=form, result=result)

@app.route('/crypto/xor', methods = ['get', 'post'])
def xor():
    form = forms.XORForm()
    result = ""
    error = ""
    if form.validate_on_submit() :
        if form.radio.data == "UTF-8":
            result = crypto_tools.xor_str(form.source.data, form.key.data)
        elif form.radio.data == "Hex number":
            result = crypto_tools.xor_num(form.source.data, int(form.key.data, 16))
        else:
            result = crypto_tools.xor_num(form.source.data, int(form.key.data))
    return render_template("crypto/xor.html",
                           form=form, result=result)

@app.route('/crypto/hex', methods=['post','get'])
def hex():
    form = forms.HexForm()
    result = ""
    error = ""
    if form.validate_on_submit():
        if form.radio.data == "From Hex":
            try:
                result = crypto_tools.from_hex(form.source.data, " " if form.delimiter.data == "" else form.delimiter.data)
            except:
                error = "Entered data is not hex numbers"
        elif form.radio.data == "To Hex":
            result = crypto_tools.to_hex(form.source.data, " " if form.delimiter.data == "" else form.delimiter.data)
    return render_template("crypto/hex.html",
                           form=form, result=result, add_error=error)

if __name__ == '__main__':
    app.run()