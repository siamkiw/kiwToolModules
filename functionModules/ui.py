import maya.cmds as mc

import sys

path = 'C:/Users/USER/Documents/GitHub/autoRigKiw'

sys.path.append(path)

import skr.rbnRig as rbn
import skr.fingerRig as fg
import skr.fkRig as fkr
import skr.generalRig as gn
import skr.legIkRig as ikr

reload(rbn)
reload(fg)
reload(fkr)
reload(gn)
reload(ikr)

#check to see if window exists
if mc.window("KiwTool", exists = True):
	mc.deleteUI("KiwTool")
#create window
ToolWindow = mc.window("KiwTool", title = "Kiw's RigTool", mnb = True, widthHeight=(200, 55))
#create a main layout
mainLayout = mc.columnLayout ()

######## setupGroup rig ###########

setupGroupLayout = mc.frameLayout (w = 1100, label = "Setup Group", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Setup Group' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))
    
mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList)

mc.text( label='placemant Radius :' )
placemantRadius = mc.floatField(editable = True, v = 8.0)

mc.button(label = 'Setup Group', command = 'grpSetup()')

######## rbn rig ###########

ribbonLayout = mc.frameLayout (w = 1100, label = "Ribbon Rig", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Ribbon Rig' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))
    
mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='rootJnt :' )
rootJntRbn = mc.textField(editable = True)

mc.text( label='endJnt :')
endJntRbn = mc.textField(editable = True)

mc.text( label='ctrl size :' )
ctrlSizeRbn = mc.floatField(editable = True, v = 1)

jntPosition = mc.optionMenuGrp( l='Joint Position')
mc.menuItem( label='LFT')
mc.menuItem( label='RGT')

mc.button(label = 'Rbn Rig', command = 'rbnRig()')

######## finger Attr rig ###########

fingerLayout = mc.frameLayout (w = 1100, label = "Add Attr Finger", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Finger Rig' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))
    
mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='Ctrl name :')
addAttrFingerName = mc.textField(editable = True)

mc.button(label = 'Add Attr Finger', command = 'AddAttrFinger()')

######## finger rig ###########

fingerLayout = mc.frameLayout (w = 1100, label = "Finger Rig", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Finger Rig' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))
    
mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='root joint :' )
rootJnt = mc.textField(editable = True)

mc.text( label='wrist joint :')
wristJnt = mc.textField(editable = True)

mc.text( label='fkIk ctrl:')
ctrlFkIk = mc.textField(editable = True) 

mc.text( label='ctrl size :' )
ctrlSizeFg = mc.floatField(editable = True, v = 0.2)

gmblOnOff = mc.optionMenuGrp( l='gimbal ctrl')
mc.menuItem( label = 'True')
mc.menuItem( label = 'False')

mc.button(label = 'Finger Rig', command = 'fingerRig()')

######## hand side rig ###########

fingerSideLayout = mc.frameLayout (w = 1100, label = "Hand Side Rig", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Hand Side Rig' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))
    
mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='ctrl size :' )
ctrlSideSizeFg = mc.floatField(editable = True, v = 0.2)

fingerSide = mc.optionMenuGrp( l='hand side Rig')
mc.menuItem( label = 'LFT')
mc.menuItem( label = 'RGT')

gmblSideOnOff = mc.optionMenuGrp( l='gimbal ctrl')
mc.menuItem( label = 'True')
mc.menuItem( label = 'False')

mc.button(label = 'hand side Rig', command = 'fingerSideRig()')

######## fk rig ###########

fkLayout = mc.frameLayout (w = 1100, label = "Fk Rig", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Fk Rig' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))
    
mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='root joint :' )
rootFkJnt = mc.textField(editable = True)

mc.text( label='ctrl size :' )
ctrlSizeFk = mc.floatField(editable = True, v = 1)

gmblFkOnOff = mc.optionMenuGrp( l='gimbal ctrl')
mc.menuItem( label = 'True')
mc.menuItem( label = 'False')

mc.button(label = 'fk Rig', command = 'rigFk()')

######## zero group rig ###########

zeroGroupLayout = mc.frameLayout (w = 1100, label = "zero Group", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='zero Group' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))

mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='child Object :' )
childObject = mc.textField(editable = True)

mc.text( label='parent Object :' )
parentObject = mc.textField(editable = True)

mc.button(label = 'zero Group', command = 'zeroGroup()')

mc.button(label = 'zero Group', command = 'gn.zeroGroup(mc.ls(sl = True)[0], mc.ls(sl = True)[1])', w = 280, h = 50, parent = zeroGroupLayout)

######## spaceing ###########

spaceingLayout = mc.frameLayout (w = 1100, label = "Spaceing", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Spaceing' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,10)))

mc.rowColumnLayout( numberOfColumns=10, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='ctrl ikFk :' )
ctrlSpace = mc.textField(editable = True)

mc.text( label='root Joint :' )
rootJntSpace = mc.textField(editable = True)

mc.text( label='space Object :' )
grpSpace = mc.textField(editable = True)

mc.text( label='world Space Object :' )
worldSpaceObjSpace = mc.textField(editable = True)

fkIkSpace = mc.optionMenuGrp( l='Ik-Fk')
mc.menuItem( label = 'fk')
mc.menuItem( label = 'ik')

mc.button(label = 'spaceing', command = 'spaceing()')

######## fkikBlend ###########

fkIkBlendLayout = mc.frameLayout (w = 1100, label = "fkIkBlend", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='fkIkBlend' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,11)))

mc.rowColumnLayout( numberOfColumns=11, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='ctrl ikFk :' )
ctrlBlend = mc.textField(editable = True)

mc.text( label='pivot Joint :' )
pivotJntBlend = mc.textField(editable = True)

mc.text( label='main Joint :' )
mainJntBlend = mc.textField(editable = True)

mc.text( label='fk Joint :' )
fkJntBlend = mc.textField(editable = True)

mc.text( label='ik Joint :' )
ikJntBlend = mc.textField(editable = True)

mc.button(label = 'fkikBlend', command = 'fkikBlend()')

######## legIkRig ###########

legIkRigLayout = mc.frameLayout (w = 1100, label = "leg Ik Rig", collapse = True, collapsable = True, parent = mainLayout)
mc.rowColumnLayout( numberOfColumns=1,  rowSpacing = (1, 3))
mc.text( label='Blend' )

rbnColmnSpacingList = list(map(lambda num : (num + 1, 3), range(0,11)))

mc.rowColumnLayout( numberOfColumns=11, rowSpacing = (1,5), columnSpacing = rbnColmnSpacingList )

mc.text( label='ankle Ctrl :' )
ankleCtrlLeg = mc.textField(editable = True)

mc.text( label='root Ctrl :' )
rootCtrlLeg = mc.textField(editable = True)

mc.text( label='knee Ctrl :' )
kneeCtrlLeg = mc.textField(editable = True)

mc.text( label='root Joint :' )
rootJntLeg = mc.textField(editable = True)

mc.button(label = 'leg Rig', command = 'legIkCtrl()')

#show window
mc.showWindow(ToolWindow)

def grpSetup():
    placemantRadiusNum = mc.floatField(placemantRadius, query = True, value = True)
    gn.grpSetup(placementCtrlRadius = placemantRadiusNum)

def rbnRig():
    # get attr form UI
    firstJnt = mc.textField(rootJntRbn, query = True, text = True)
    secondJnt = mc.textField(endJntRbn, query = True, text = True)
    radius = mc.floatField(ctrlSizeRbn, query = True, value = True)
    side = mc.optionMenuGrp(jntPosition, query = True, value = True)

    rbn.rbnRig(firstJnt = firstJnt, secondJnt = secondJnt, jntNum = 5, radius = radius, side = side)

def AddAttrFinger():
	ctrlFkIk = mc.textField(addAttrFingerName, query = True, text = True)

	# add attr to fkIk ctrl
	mc.addAttr(ctrlFkIk, ln = 'fist', at = 'double', dv = 0, k = True)
	mc.addAttr(ctrlFkIk, ln = 'cup', at = 'double', dv = 0, k = True)
	mc.addAttr(ctrlFkIk, ln = 'spread', at = 'double', dv = 0, k = True)
	mc.addAttr(ctrlFkIk, ln = 'baseSpread', at = 'double', dv = 0, k = True)

def fingerRig():

    fingerBool = {'True' : True, 'False' : False}
    # get attr form UI
    firstJntName = mc.textField(rootJnt, query = True, text = True)
    wristJntName = mc.textField(wristJnt, query = True, text = True)
    ctrlFkIkName = mc.textField(ctrlFkIk, query = True, text = True)
    radius = mc.floatField(ctrlSizeFg, query = True, value = True)
    gmbl = fingerBool[mc.optionMenuGrp(gmblOnOff, query = True, value = True)]

    fg.fingerRig(jntName = firstJntName, wristJntName = wristJntName, ctrlFkIk = ctrlFkIkName, radius = radius, gmbl = gmbl)

def fingerSideRig():
    fingerBool = {'True' : True, 'False' : False}
    fingerList = ['thumb1', 'index1', 'middle1', 'ring1', 'pinky1']
    # get attr form UI
    side = mc.optionMenuGrp(fingerSide, query = True, value = True)
    radius = mc.floatField(ctrlSideSizeFg, query = True, value = True)
    gmbl = fingerBool[mc.optionMenuGrp(gmblSideOnOff, query = True, value = True)]

    for i in range(0, len(fingerList)):
        firstJntName = fingerList[i] + '_' + side + '_jnt'
        wristJntName = 'wrist_' + side + '_jnt'
        ctrlFkIkName = 'arm_' + side + '_ctrl'

        fg.fingerRig(jntName = firstJntName, wristJntName = wristJntName, ctrlFkIk = ctrlFkIkName, radius = radius, gmbl = gmbl)

def rigFk():

    fkBool = {'True' : True, 'False' : False}

    rootFkJntName = mc.textField(rootFkJnt, query = True, text = True)
    radius = mc.floatField(ctrlSizeFk, query = True, value = True)
    gmbl = fkBool[mc.optionMenuGrp(gmblFkOnOff, query = True, value = True)]

    fkr.rigFk(rootJnt = rootFkJntName, radius = radius, gmbl = gmbl)

def zeroGroup():

    childObjectName = mc.textField(childObject, query = True, text = True)
    parentObjectName = mc.textField(parentObject, query = True, text = True)
    gn.zeroGroup(childObjectName, parentObjectName)

def spaceing():

    ctrlSpaceName = mc.textField(ctrlSpace, query = True, text = True)
    rootJntSpaceName = mc.textField(rootJntSpace, query = True, text = True)
    grpSpaceName = mc.textField(grpSpace, query = True, text = True)
    worldSpaceObjSpaceName = mc.textField(worldSpaceObjSpace, query = True, text = True)
    fkIkSpaceName = mc.optionMenuGrp(fkIkSpace, query = True, value = True)

    gn.spaceing(ctrlName = ctrlSpaceName, rootJnt = rootJntSpaceName, grp = grpSpaceName, worldSpaceObj = worldSpaceObjSpaceName, ikFk = fkIkSpaceName)

def fkikBlend():

    ctrlBlendName = mc.textField(ctrlBlend, query = True, text = True)
    pivotJntBlendName = mc.textField(pivotJntBlend, query = True, text = True)
    mainJntBlendName = mc.textField(mainJntBlend, query = True, text = True)
    fkJntBlendName = mc.textField(fkJntBlend, query = True, text = True)
    ikJntBlendName = mc.textField(ikJntBlend, query = True, text = True)

    mainJntBlendList = gn.findRel(mainJntBlendName)
    fkJntBlendList = gn.findRel(fkJntBlendName)
    ikJntBlendList = gn.findRel(ikJntBlendName)

    print ctrlBlendName
    print pivotJntBlendName

    print mainJntBlendList
    print fkJntBlendList
    print ikJntBlendList

    gn.fkIkBlend(fkIkCtrl = ctrlBlendName, pelvisJnt = pivotJntBlendName, mainJntList = mainJntBlendList, fkJntList = fkJntBlendList, ikJntList = ikJntBlendList)

def legIkCtrl():

    ankleCtrlLegName = mc.textField(ankleCtrlLeg, query = True, text = True)
    rootCtrlLegName = mc.textField(rootCtrlLeg, query = True, text = True)
    kneeCtrlLegName = mc.textField(kneeCtrlLeg, query = True, text = True)
    rootJntLegName = mc.textField(rootJntLeg, query = True, text = True)
    
    ikr.legIkCtrl(ankleCtrlName = ankleCtrlLegName, rootCtrlName = rootCtrlLegName, kneeCtrlName = kneeCtrlLegName, rootJnt = rootJntLegName)

