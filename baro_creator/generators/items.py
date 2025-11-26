import os,xml.etree.ElementTree as ET
from ..xml_utils import add_filelist_entry
def create_item_xml(mod_root,data):
    cat=(data.category_path or "Items").strip("\/") or "Items"
    ident=data.identifier or "item"
    rel=f"{cat}/{ident}.xml"
    ad=os.path.join(mod_root,cat);os.makedirs(ad,exist_ok=True)
    ap=os.path.join(ad,f"{ident}.xml")
    root=ET.Element("Items")
    it=ET.SubElement(root,"Item")
    it.set("identifier",ident)
    it.set("price",str(data.base_price))
    if data.name_tag: it.set("nameidentifier",data.name_tag)
    if data.description_tag: it.set("descriptionidentifier",data.description_tag)
    if data.sprite_texture:
        sp=ET.SubElement(it,"Sprite");sp.set("texture",data.sprite_texture)
    it.append(ET.Comment(" TODO "))
    ET.ElementTree(root).write(ap,encoding="utf-8",xml_declaration=True)
    if data.add_to_filelist: add_filelist_entry(mod_root,rel)
    return rel
