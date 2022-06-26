from core.models import Model, Ticket

import codecs

class File():

    tickets = None
    def __init__(self):

        self.read_file()


    def read_file(self):
        file = codecs.open("temp.json", "r", "utf_8_sig")
        print('read...')
        str = file.read()
        self.tickets = Model.parse_raw(str)
        file.close()
        print('read is complete...')


class Queue(File):

    def get_all_queues(self):
        services = {}
        for el in self.tickets.backup:
                if el.state == "STATE_WAIT":
                    if el.to_service.name in services:
                        count = services[el.to_service.name]
                        count += 1
                        services[el.to_service.name] = count
                    else:
                        services[el.to_service.name] = 1
        return services

    def get_one_queue(self,service_name):
        result = []
        for item in self.tickets.backup:
            for el_service in service_name:
                if item.to_service.id == el_service and item.state == "STATE_WAIT":
                    m = Ticket(number=item.number,prefix=item.prefix,status=item.state, service_id=item.to_service.id,
                               service_name=item.to_service.name, stand_time=item.stand_time)

                    result.append(m)

        print(result)
        return result


