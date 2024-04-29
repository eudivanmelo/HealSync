import os

def upload_rg(instance, filename):
    return upload_to_user_directory(instance, filename, 'rg')

def upload_medical_identity(instance, filename):
    return upload_to_user_directory(instance, filename, 'medical_identity')

def upload_photo(instance, filename):
    return upload_to_user_directory(instance, filename, 'photo')

def upload_to_user_directory(instance, filename, prefix):
    # Obtém a extensão original do arquivo
    ext = filename.split('.')[-1]
    # Define um nome de arquivo predefinido com o prefixo fornecido, seguido pelo número de registro e a extensão
    new_filename = f"{prefix}_{instance.crm}.{ext}"

    # Define o caminho com base no nome de usuário (username) da instância de usuário (user)
    user_directory = os.path.join('doctors', str(instance.user.username))
    # Retorna o caminho completo para salvar o arquivo
    return os.path.join(user_directory, new_filename)