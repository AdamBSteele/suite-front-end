

from flask.ext.wtf import Form
from flask.ext.wtf.html5 import URLField, EmailField, TelField
from wtforms import (ValidationError, TextField, HiddenField, PasswordField,
    SubmitField, TextAreaField, IntegerField, RadioField,FileField,
    DecimalField, SelectField, DateField, Field, widgets)
from wtforms.validators import (Required, Length, EqualTo, Email, NumberRange, AnyOf, Optional)
from flask.ext.babel import lazy_gettext as _
from .models import Echo
from ..extensions import db
from datetime import datetime

class CreateEchoForm(Form):
    text = TextField(_('What do you want to post?'), [Required()],
            description=_("Post will appear on your time line"))
    time = TextField(_('When do you want to post?'), [Required()],
        description=_("Post will be made at this time"))
    submit = SubmitField(_('Create Post'))

    def add_echo(self,user):
    	self.populate_obj(user)
    	echo = Echo()
        echo.text = self.text.data
        echo.time = self.time.data
        echo.user_id = user.id


        db.session.add(echo)
        db.session.commit()