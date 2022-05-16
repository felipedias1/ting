from importlib.resources import path
import sys
from ting_file_management.file_management import txt_importer



def process(path_file, instance):
    file_exists = True if path_file in instance.data else False
    lines = txt_importer(path_file)
    previous_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    if file_exists is False:
        instance.enqueue(path_file)
    sys.stdout.write(f"{previous_process}\n")


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write('Não há elementos\n')      
    remove = instance.dequeue()
    return sys.stdout.write(f"Arquivo {remove} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        process(file, instance)
    except IndexError:
        sys.stderr.write('Posição inválida\n')
