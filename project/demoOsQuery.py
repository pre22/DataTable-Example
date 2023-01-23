import osquery, json


class Querys():
    def __init__(self):
        self.instance = osquery.SpawnInstance()
        self.instance.open()

    # def get_os_info(self):
    #     query = self.instance.client.query()
    #     if query:
    #         return json.dumps(query.response)
    #     else:
    #         return "Couldn't get any"

    def get_programs(self):
        query = self.instance.client.query("select * from programs")
        a = query.response
        b = []

        for app in a:
            b.append(f'{app["name"]}-{app["publisher"]}-{app["version"]}-{app["install_date"]}')
            # for k,v in app.items():
                # b.append(apps["publisher"])
                # b.append(f'{app["name"]}-{app["publisher"]}-{app["version"]}-{app["install_date"]}')
        return b
        # if len(json.dumps(query.response)) > 2:
        #     return json.dumps(query.response)
        # else:
        #     return "None"

    def listening_ports(self):
        query = self.instance.client.query("select * from programs")
        if len(json.dumps(query.response)) > 2:
            return json.dumps(query.response)
        else:
            return "None"

    # def users(self):
    #     query = self.instance.client.query("select * from programs")


program = Querys()
a = program.get_programs()
print(a)
# for app in a:
#     print(f'{app["name"]}-app{["publisher"]}-{app["version"]}-{app["install_date"]}')
