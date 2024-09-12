def coding_to_string(coding):
    # Converte uma lista de floats para uma string separada por vírgulas
    return ",".join(map(str, coding))

def string_to_coding(coding_string):
    # Converte uma string separada por vírgulas de volta para uma lista de floats
    return [float(x) for x in coding_string.split(",")]
