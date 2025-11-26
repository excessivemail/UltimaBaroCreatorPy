import os,xml.etree.ElementTree as ET
def ensure_base_files(mod_root):
    os.makedirs(mod_root,exist_ok=True)
    fl=os.path.join(mod_root,"filelist.xml")
    if os.path.exists(fl):
        try: tree=ET.parse(fl);root=tree.getroot()
        except: root=ET.Element("ContentPackage");tree=ET.ElementTree(root)
    else:
        root=ET.Element("ContentPackage");tree=ET.ElementTree(root)
    if not any(c.tag.lower()=="text" and c.attrib.get("file")=="Text/English.xml" for c in root):
        t=ET.SubElement(root,"Text");t.set("file","Text/English.xml")
    tree.write(fl,encoding="utf-8",xml_declaration=True)
    td=os.path.join(mod_root,"Text");os.makedirs(td,exist_ok=True)
    en=os.path.join(td,"English.xml")
    if os.path.exists(en):
        try: t2=ET.parse(en);r2=t2.getroot()
        except: r2=ET.Element("Texts");r2.set("Language","English");t2=ET.ElementTree(r2)
    else:
        r2=ET.Element("Texts");r2.set("Language","English");t2=ET.ElementTree(r2)
    t2.write(en,encoding="utf-8",xml_declaration=True)

def upsert_text(mod_root,tag,text):
    ensure_base_files(mod_root)
    en=os.path.join(mod_root,"Text","English.xml")
    t=ET.parse(en);r=t.getroot()
    el=None
    for e in r.findall("Text"):
        if e.attrib.get("Tag")==tag: el=e;break
    if el is None:
        el=ET.SubElement(r,"Text");el.set("Tag",tag);el.text=text
    else: el.text=text
    t.write(en,encoding="utf-8",xml_declaration=True)

def add_filelist_entry(mod_root,rel):
    ensure_base_files(mod_root)
    # Normalize path separators to ensure consistent XML entries on all platforms
    rel=rel.replace("\\","/")
    fl=os.path.join(mod_root,"filelist.xml")
    t=ET.parse(fl);r=t.getroot()
    if rel.lower().startswith("items/"): tag="Item"
    elif rel.lower().startswith("afflictions/"): tag="Afflictions"
    elif rel.lower().startswith("text/"): tag="Text"
    else: tag="File"
    if not any(c.tag==tag and c.attrib.get("file")==rel for c in r):
        e=ET.SubElement(r,tag);e.set("file",rel)
    t.write(fl,encoding="utf-8",xml_declaration=True)
