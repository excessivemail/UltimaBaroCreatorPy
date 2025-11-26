import json, os
DEFAULT_SETTINGS={"mod_root":""}
def _settings_path():
    here=os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here,"..","baro_creator.settings.json")
def load_settings():
    p=_settings_path()
    if os.path.exists(p):
        try:
            return json.load(open(p,encoding="utf-8"))
        except: pass
    return DEFAULT_SETTINGS.copy()
def save_settings(s):
    json.dump(s,open(_settings_path(),"w",encoding="utf-8"),indent=2)
