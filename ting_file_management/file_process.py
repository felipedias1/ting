import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_exists = False
    for element in instance.data:
        if path_file == element["nome_do_arquivo"]:
            file_exists = True
    lines = txt_importer(path_file)
    previous_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    if file_exists is False:
        instance.enqueue(previous_process)
    sys.stdout.write(f"{previous_process}\n")


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write('Não há elementos\n')
    remove = instance.dequeue()['nome_do_arquivo']
    return sys.stdout.write(f"Arquivo {remove} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        process(file['nome_do_arquivo'], instance)
    except IndexError:
        sys.stderr.write('Posição inválida\n')
