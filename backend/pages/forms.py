from django import forms
class UserForm(forms.Form):
    nome = forms.CharField(
        label='Seu Nome', 
        max_length=100
    )
    conteudo = forms.TextField()
#     nome = StringField('Seu Nome', validators=[DataRequired()], render_kw={'maxlength': 100})
#     conteudo = TextAreaField('Mensagem', validators=[DataRequired()], render_kw={'maxlength': 140})
#     enviar = SubmitField('Enviar mensagem')
