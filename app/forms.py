from flask_wtf import FlaskForm
import wtforms as wf


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=8),
    ])
    submit = wf.SubmitField('OK')


class EmployeeForm(FlaskForm):
    fullname = wf.StringField('ФИО', validators=[wf.validators.DataRequired()])
    phone = wf.StringField('Номер телефона', validators=[wf.validators.DataRequired()])
    short_info = wf.TextAreaField('Краткая информация', validators=[wf.validators.DataRequired()])
    experience = wf.StringField('Опыт работы', validators=[wf.validators.DataRequired()])
    preferred_position = wf.StringField('Предпочитаемая должность')
    submit = wf.SubmitField('OK')

    def validate(self, **kwargs):
        if not super().validate():
            return False
        if " " in self.fullname.data.strip():
            self.fullname.errors.append('Введите ФИО полностью')
            return False
        return True
