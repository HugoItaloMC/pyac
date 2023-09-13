from model import CharacterGenerator
from app import schema_data
from helper import LabelJson, pool_queue


async def request_data(queue):
    await pool_queue(queue=queue, _class=CharacterGenerator())
    task = await queue.get()
    data = schema_data()
    file_json = LabelJson()

    if data.get('npc', False):
        npc = task.character('npc')
        lobby = npc.npc_begin(data['type_loby'], data['name_npc'])
        await file_json.mk_file_json(lobby.__str__())

    elif data.get('player', False):
        player = task.character('player')
        lobby = player.player_begin(data['race_player'], data['class_player'])
        await file_json.mk_file_json(lobby.__str__())
