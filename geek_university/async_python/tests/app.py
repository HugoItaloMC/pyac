#  Dados em alto nível `Schemas`
import os

from dotenv import load_dotenv

load_dotenv()
env_character: dict = {'class': os.environ['CLASS_PLAYER'].split(),
                       'race': os.environ['PLAYER_RACE'].split(),
                       'lobby_npc': os.environ['LOBBY_NPC'].split()}

class Schema:

    def __getattr__(self, attr):
        valur = attr
        setattr(self, valur, attr)
        return valur

    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__dict__.keys()}


def schema_data():
    schema = Schema()
    print('***\tSIGN WHAS CHARACTER TO GAMER FLOW\t***')
    while True:
        oop = input('::\tCHOICE [PLAYER | NPC]:\t').lower()

        if oop == 'npc':
            schema.npc: bool = True
            schema.type_loby: str = input('::\tTYPE LOBBY TO NPC\n%s\n::\t' % "".join(map(str, env_character.get('lobby_npc'))))
            schema.name_npc: str = input("::\tNAME TO NPC:\t")

        elif oop == 'player':
            schema.player: bool = True
            schema.race_player: str = input('::\tRACE TO PLAYER\n%s\n::\t' % ",".join(map(str, env_character.get('race'))))
            schema.class_player: str = input("::\tCLASS TO PLAYER\n%s\n::\t" % ",".join(map(str, env_character.get('class'))))

        else:
            print("***\t\tERROR ###\t\t***")
            continue

        break

    return schema.to_dict()


if __name__ == '__main__':
    #import cProfile
    #import io
    #from pstats import SortKey

    #profile = cProfile.Profile()
    #profile.enable()
    schema_data()

    #profile.disable()
    #profile.dump_stats('stats/app.stats')
    #_str = io.StringIO()

    #_stats = pstats.Stats(profile, stream=_str).sort_stats(SortKey.TIME)
    #_stats.print_stats()
    #print(_str.getvalue())

