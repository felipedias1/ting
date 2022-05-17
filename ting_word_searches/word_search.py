def exists_word(word, instance):
    occurrences = []
    for file in instance.data:
        occurrences_lines = []
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences_lines.append({
                    'linha': index + 1
                })
        if len(occurrences_lines) > 0:
            occurrences.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences_lines
            })
    return occurrences


def search_by_word(word, instance):
    occurrences = []
    for file in instance.data:
        occurrences_lines = []
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences_lines.append({
                    'conteudo': line,
                    'linha': index + 1
                })
        if len(occurrences_lines) > 0:
            occurrences.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences_lines
            })
    return occurrences
