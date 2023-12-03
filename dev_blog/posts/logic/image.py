import uuid


def generate_unique_filename(instance, filename):
    #Genera un nombre de archivo único utilizando un UUID.

    extension = filename.split('.')[-1]  # Obtener la extensión del archivo original
    unique_filename = f"uploads/posts/{uuid.uuid4()}.{extension}"
    return unique_filename