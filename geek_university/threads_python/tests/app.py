class Schema:

    def __init__(self):
        self.nome: str = input("::\tDADOS DO CLIENTE\nNOME:\t")
        self.modelo: str = input("::\tDADOS DO VEÍCULO\nMODELO:\t")
        self.ano: str= input("ANO:\t")
        self.descricao: str = input("***\tDESCRICÃO DA MANUTENCÃO\t***\nDESCRICÃO:\t")
        self.status: bool = ...
        self.ordem: str = input("***\tSTATUS DO SERVICO\t***\n::\tSERVICO FOI CONCLUIDO ? [Y\\N]: ".lower())

        if self.ordem == 'y':
            self.status = True
        elif self.ordem == 'n':
            self.status = False


def schema_data(**kwargs):
    schema = Schema()
    for attrs in schema.__dict__.keys():
        kwargs[attrs] = getattr(schema, attrs)
    return kwargs
