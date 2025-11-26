import os
from .config import load_settings,save_settings
from .models import ProjectData
from .xml_utils import ensure_base_files,upsert_text
from .projects import save_project,list_projects
from .generators.items import create_item_xml
from .generators.afflictions import create_affliction_xml

def run_cli():
    s=load_settings()
    while True:
        print("\nMenu: 1)set root 2)base files 3)item 4)affliction 5)projects 0)exit")
        c=input("> ").strip()
        if c=="1":
            p=input("mod root: ").strip()
            if p: s["mod_root"]=os.path.abspath(p); save_settings(s)
        elif c=="2":
            ensure_base_files(s.get("mod_root",""))
        elif c=="3":
            m=s.get("mod_root",""); print("Item:")
            ident=input("identifier: ")
            name=f"{ident}.name"
            desc=f"{ident}.description"
            p=ProjectData(type="Item",identifier=ident,name_tag=name,description_tag=desc)
            rel=create_item_xml(m,p)
            upsert_text(m,name,ident); upsert_text(m,desc,ident+" desc")
            save_project(m,p); print("created",rel)
        elif c=="4":
            m=s.get("mod_root",""); print("Affliction:")
            ident=input("identifier: ")
            name=f"{ident}.name"
            desc=f"{ident}.description"
            p=ProjectData(type="Affliction",identifier=ident,name_tag=name,description_tag=desc)
            rel=create_affliction_xml(m,p)
            upsert_text(m,name,ident); upsert_text(m,desc,ident+" desc")
            save_project(m,p); print("created",rel)
        elif c=="5":
            print(list_projects(s.get("mod_root","")))
        elif c=="0": break
        else: print("invalid")
