from dataclasses import dataclass,asdict
@dataclass
class ProjectData:
    type:str="Item"
    identifier:str=""
    name_tag:str=""
    description_tag:str=""
    category_path:str=""
    sprite_texture:str=""
    base_price:int=100
    max_strength:float=100.0
    add_to_filelist:bool=True
    add_texts:bool=True
    def to_dict(self): return asdict(self)
    @staticmethod
    def from_dict(d): return ProjectData(**d)
