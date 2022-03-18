from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password', 'placeholder': 'Password'},
        write_only=True,
        label="Senha",
        
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password', 'placeholder': 'Password'},
        write_only=True,
        label="Confirme a senha",

    )

    publisher = serializers.BooleanField(
        label="Publicador",
        help_text="Indica que o usuário é publicador."
    )

    admin = serializers.BooleanField(
        label="Administrador",
        help_text="Indica que o usuário tem todas as permissões"
    )
    is_active = serializers.BooleanField(
        label="Ativo",
        help_text="Indica que o usuário esta ativo"
    )



    class Meta:
        model = User
        fields = ('cpf','password', 'password_confirm', 'publisher', 'admin','created_at', 'updated_at', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        conta = User(
            cpf=self.validated_data['cpf'],
            publisher=self.validated_data['publisher'],
            admin=self.validated_data['admin'],
            is_superuser=self.validated_data['admin'],
            is_staff=self.validated_data['admin']
            
        )

        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta