init python:
    import inspect
    import json
    enhance_who_replace_file_name = 'enhance_who_replace.json'
    def replace_text(s):
        target_file = 'game/tl/' + str(renpy.game.preferences.language) + '/' + enhance_who_replace_file_name
        if os.path.isfile(target_file) and os.path.getsize(target_file):
            f = io.open(target_file, 'r', encoding='utf-8')
            loaded_data = json.load(f)
            f.close()
            for key,value in loaded_data.items():
                s = s.replace(key,value)
        return s
    config.replace_text = replace_text