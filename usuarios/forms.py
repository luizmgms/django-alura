from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = "Nome de Login",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'EX.: Luiz Magno'
            }
        )
    )
    senha = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'EX.: Digite sua senha'
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = "Nome de Cadastro",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'EX.: Luiz Magno'
            }
        )
    )

    email = forms.EmailField(
        label = 'Email',
        required=True,
        max_length= 100,
        widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'EX.: luiz@email.com'
            }
        )
    )

    senha1 = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'EX.: Digite sua senha'
            }
        )
    )

    senha2 = forms.CharField(
        label = "Confirmar Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'EX.: Digite sua senha novamente'
            }
        )
    )

