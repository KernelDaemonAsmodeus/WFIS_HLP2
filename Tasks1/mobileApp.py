import json


class MobileApp:
    downloads = 0

    def __init__(self, name, version):
        self.name = name
        self.version = version


    @classmethod
    def new_download(cls):
        cls.downloads += 1

    @classmethod
    def downloads_quantity(cls):
        return cls.downloads

    @classmethod
    def from_json(cls, file_name):
        with open(file_name, "rt") as f:
            text = json.load(f)
        return cls(text["name"], text["version"])


mobile_app_1 = MobileApp("name1", "1.4.5")
mobile_app_1.new_download()

MobileApp.new_download()
print("downloads:", MobileApp.downloads_quantity())

mobile_app_2 = MobileApp.from_json("mobileAppData.json")
print("name:", mobile_app_2.name,"\nversion:", mobile_app_2.version)
