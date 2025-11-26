import os,json
from .models import ProjectData
def _dir(m): return os.path.join(m,"_ultima_projects")
def save_project(m,p):
    os.makedirs(_dir(m),exist_ok=True)
    ident=p.identifier or "unnamed"
    json.dump(p.to_dict(),open(os.path.join(_dir(m),f"{ident}.json"),"w",encoding="utf-8"),indent=2)
def list_projects(m):
    d=_dir(m)
    if not os.path.isdir(d): return []
    return [f for f in os.listdir(d) if f.endswith(".json")]
def load_project(m,f):
    return ProjectData.from_dict(json.load(open(os.path.join(_dir(m),f),encoding="utf-8")))
