import wtforms
from flask_wtf import FlaskForm
from wtforms import DecimalField, TextAreaField, StringField, SubmitField, RadioField, BooleanField
from wtforms.validators import data_required


class NumericForm(FlaskForm):
    from_ = DecimalField(u'From', [data_required()])
    to = DecimalField(u'To', [data_required()])
    delimiter = StringField(u'Delimiter')
    source = TextAreaField(u'Source', [data_required()])
    submit = SubmitField("")

class Base64Form(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])
    radio = RadioField(u'Option', choices=["Encode", "Decode"])
    submit = SubmitField("")

class URLForm(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])
    radio = RadioField(u'Option', choices=["Encode", "Decode"], validators=[data_required()])
    submit = SubmitField("")

class ROTForm(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])
    turn = DecimalField(u'Turn', [data_required()])
    submit = SubmitField("")

class XORForm(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])
    key = StringField(u'Key', [data_required()])
    radio = RadioField(u'Type', choices=["UTF-8", "Hex number", "Decimal number"],validators=[data_required()])
    submit = SubmitField("")

class HexForm(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])
    radio = RadioField(u'Option', choices=["From Hex", "To Hex"], validators=[data_required()])
    delimiter = StringField(u'Delimiter')

class ReverseForm(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])

class WhitespaceForm(FlaskForm):
    source = TextAreaField(u'Source')
    space = BooleanField(u' ' )
    n = BooleanField(u'\n' )
    r = BooleanField(u'\r' )
    f = BooleanField(u'\f')
    select = [space,n,r,f]

class ToCaseForm(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])
    radio = RadioField(u'Choice', choices=["To upper", "To lower"], validators=[data_required()])

class LineNumbersForm(FlaskForm):
    source = TextAreaField(u'Source', [data_required()])
    radio = RadioField(u'Option', choices=["Add", "Remove"])