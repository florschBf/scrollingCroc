import json
from os.path import exists

class HighscoreController:

    def __init__(self, db_file, scene):
        # lade highscore.json - sqlite would be overkill
        f = open('assets/highscore.json', encoding='utf-8')
        self.highscore = json.load(f)["scores"]
        self.highscore_sorted = self.sort_json(self.highscore)
        print(self.return_position_name(2))
        print(self.return_position_score(0))

    def return_position_name(self, place_on_list):
        if place_on_list >= len(self.highscore_sorted):
            return ""
        else:
            return self.highscore_sorted[place_on_list]['name']

    def return_position_score(self, place_on_list):
        if place_on_list >= len(self.highscore_sorted):
            return ""
        else:
            return str(self.highscore_sorted[place_on_list]['score'])

    def get_lowest_score(self):
        print('checking my list')
        if len(self.highscore_sorted) < 5:
            print('there is room')
            # room on list, return 0
            return 0
        else:
            print('returning lowest ' + str(self.highscore_sorted[-1]['score']))
            #returning lowest entry
            return self.highscore_sorted[-1]['score']

    def write_entry(self, name, score):
        print("updating scores")

        new_entry = {}
        new_entry["name"] = name
        new_entry["score"] = score
        print(new_entry)

        # add new_entry to list and sort it again
        self.highscore_sorted.append(new_entry)
        print(self.highscore_sorted)
        self.highscore_sorted = self.sort_json(self.highscore_sorted)

        # if list too long, cut one
        if len(self.highscore_sorted) > 5:
            print('removing last entry')
            self.highscore_sorted.remove(self.highscore_sorted[-1])
        print("updated the list" + str(self.highscore_sorted))

        new_json_list = {}
        new_json_list["scores"] = self.highscore_sorted

        # list finished, write it to file
        with open('assets/highscore.json', 'w') as outfile:
            outfile.write(json.dumps(new_json_list, indent = 4))


    def sort_json(self, json):
        entry_list = []
        for entry in json:
            print(entry["score"])
            entry_list.append(entry)
        return sorted(entry_list, key=lambda i: i['score'], reverse=True)










