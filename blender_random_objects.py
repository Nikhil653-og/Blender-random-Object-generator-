bl_info = {
    "name": "Random addon",
    "author": "Spy_rov673",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
from random import randint
from bpy.types import(Panel,operator)



class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.random.1_operator"
    bl_label = "Simple random Operator"


    def execute(self, context):
        main(context)
for i in range(25):
    randomScale = randint(0,3)
    x = randint(-40,40)
    y = randint(-40,40)
    z = randint(-40,40)
    bpy.ops.mesh.primitive_icosphere_add(Subdivisions = 1, radius = randomScale,enter_editmode = false,align = 'WORLD',location = (x,y,z),scale = (1,1,1))
   return {'FINISHED'}
    
class CustomPanel(bpy.types.Panel):
      bl_label = "Random Panel"
      bl_idname = "OBJECT_PT_random"
      bl_space_type = 'VIEW_3D'
      bl_region_type = 'UI'
      bl_category = "random ico-spheres"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator(ButtonOPerator.bl_idname.text="Generate", icon='SPHERE')
from bpy.utils.import register_class,unregister_class
_classes = [
           buttonOperator,
           CustomPanel
           ]        

def register():
    for cls in _classes:
        register_class(cls)


def unregister():
    for cls in _classes:
        register_class(cls)



if __name__ == "__main__":
    register()
