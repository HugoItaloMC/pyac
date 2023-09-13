import aiofiles
import csv


async def pool_queue(queue, _class):
    await queue.put(_class)


class LabelJson:

    async def mk_file_json(self, _schema) -> None:
        if not hasattr(self, '_schema'):
            self._schema = _schema
            async with aiofiles.open('schema.jsonl', 'a+') as file:
                await file.write('{"schema_character": "%s"}\n' % self._schema)
