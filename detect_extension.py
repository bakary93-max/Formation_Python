def detect_extension(nom_fichier):
    list_reduct = nom_fichier.split(".")
    if len(list_reduct) > 1:
        return list_reduct[-1]
    return None




def get_definition_extension(extension,definition):
    for d in definition:
        if d[0].lower() == extension.lower():
            return d[1]
    return None