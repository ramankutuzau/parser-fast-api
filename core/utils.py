from core.models import Model, BackupItem, Ticket
import json

class File():

    tickets = None
    def __init__(self):

        self.read_file()


    def read_file(self):
        with open('temp.json','r') as f:
            print('read...')
            str = f.read()
            self.tickets = Model.parse_raw(str)
            f.close()
            print('read is complete...')


class Queue(File):

    def get_all_queues(self):
        services = {}
        for el in self.tickets.backup:
                if el.state == "STATE_WAIT":
                    if el.to_service.id in services:
                        count = services[el.to_service.id]
                        count += 1
                        services[el.to_service.id] = count
                    else:
                        services[el.to_service.id] = 1
        return services

    async def get_one_queue(self,service_name):
        result = {}
        for item in self.tickets.backup:
            for el_service in service_name:
                if item.to_service.id == el_service and item.state == "STATE_WAIT":
                    m = Ticket(status=item.state, service_id=item.to_service.id,
                               service_name=item.to_service.name, stand_time=item.stand_time)

                    result[item.number] = m

        return result