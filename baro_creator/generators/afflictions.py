import os,xml.etree.ElementTree as ET
from ..xml_utils import add_filelist_entry
def create_affliction_xml(mod_root,data):
    cat=(data.category_path or "Afflictions").strip("\/") or "Afflictions"
    ident=data.identifier or "affliction"
    rel=f"{cat}/{ident}.xml"
    ad=os.path.join(mod_root,cat);os.makedirs(ad,exist_ok=True)
    ap=os.path.join(ad,f"{ident}.xml")
    root=ET.Element("Afflictions")
    af=ET.SubElement(root,"Affliction")
    af.set("identifier",ident)
    af.set("maxstrength",str(data.max_strength))
    if data.name_tag: af.set("nameidentifier",data.name_tag)
    if data.description_tag: af.set("descriptionidentifier",data.description_tag)
    af.append(ET.Comment(" TODO "))
    ET.ElementTree(root).write(ap,encoding="utf-8",xml_declaration=True)
    if data.add_to_filelist: add_filelist_entry(mod_root,rel)
    return rel
