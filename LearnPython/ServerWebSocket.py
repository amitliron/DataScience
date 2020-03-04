#!/usr/bin/env python

import asyncio
import websockets
import json
import DBManagerInterface

class ServerWebSocket:

    def __init__(self, db_manager: DBManagerInterface):
        self.db_manager = db_manager
        None

    async def main_server_function(self, websocket, path):
        msg = await websocket.recv()
        print("Got: " + msg)
        pmsg = json.loads(msg)
        print("Get: ", pmsg["FIRST_NAME"])
        self.db_manager.add_emloyee(pmsg["FIRST_NAME"], pmsg["LAST_NAME"], pmsg["AGE"], pmsg["SEX"], pmsg["INCOME"],pmsg["LOCATION"])
        #await websocket.send("Updated")
        count = self.db_manager.get_number_of_records()
        await websocket.send(str(count))

    def start(self):
        start_server = websockets.serve(self.main_server_function, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        None
