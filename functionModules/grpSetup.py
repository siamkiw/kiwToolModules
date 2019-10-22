import maya.cmds as mc

def grpSetup(placementCtrlRadius):

    mc.circle( nr=(0, 1, 0), c=(0, 0, 0), r=placementCtrlRadius, n='placement_ctrl')
    mc.circle( nr=(0, 1, 0), c=(0, 0, 0), r=placementCtrlRadius*0.80 , n='offset_ctrl')
    mc.group(em=True, name='modelName')
    mc.group(em=True, name='geo_grp')
    mc.group(em=True, name='rig_grp')
    mc.group(em=True, name='still_grp')
    mc.group(em=True, name='anim_grp')
    mc.group(em=True, name='skin_grp')

    mc.parent( 'geo_grp', 'modelName' )
    mc.parent( 'rig_grp', 'modelName' )
    mc.parent( 'placement_ctrl', 'rig_grp' )
    mc.parent( 'still_grp', 'rig_grp' )
    mc.parent( 'offset_ctrl', 'placement_ctrl' )
    mc.parent( 'anim_grp', 'offset_ctrl' )
    mc.parent( 'skin_grp', 'offset_ctrl' )
