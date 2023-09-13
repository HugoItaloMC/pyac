import pstats
from collections import namedtuple


# Gerando Objetos Referenciando Dados
class NonPlayerCharacter:

    def npc_begin(self, type_loby, name):
        _Character = namedtuple('NPC', ('type_loby', 'name'))
        return _Character(type_loby=type_loby, name=name)


class PlayerCharacter:

    def player_begin(self, race_player, class_player):
        _Player = namedtuple('Player', ('race_player', 'class_player'))
        return _Player(race_player=race_player, class_player=class_player)


class CharacterGenerator:

    def character(self, name: str):
        if not hasattr(self, '_character'):
            if name.lower() == 'npc':
                self._character = NonPlayerCharacter()
            elif name.lower() == 'player':
                self._character = PlayerCharacter()
        return self._character

    def __await__(self):
        return self.character


if __name__ == '__main__':
    import cProfile
    import io
    from pstats import SortKey

    profiler = cProfile.Profile()
    profiler.enable()

    npc_create = CharacterGenerator()
    player_create = CharacterGenerator()

    class_npc = npc_create.character('NPC')
    class_player = player_create.character('PLAYER')

    begin_npc = class_npc.npc_begin('stored', 'jeff')
    begin_player = class_player.player_begin('elf', 'warrior')

    profiler.disable()
    profiler.dump_stats('model.stats')

    _str = io.StringIO()
    _sort_by = SortKey.TIME
    ps = pstats.Stats(profiler, stream=_str).sort_stats(_sort_by)
    ps.print_stats()
    print(_str.getvalue())


