import maya.cmds as mc


def createFkZeroGrp3(zGrpList):
    for item in zGrpList:
        ojName = item.split('_')[0]
        side = item.split('_')[1]
        print side, item
        zGrpName = ojName + '_' + side + '_zGrp'
        mc.group(em = True, n = str(zGrpName))
        zGrpCon = mc.parentConstraint(item, zGrpName, mo = False)
        mc.delete(zGrpCon)
        mc.parent(item, zGrpName)
        # mc.select( clear=True )


def createGmbl3(gmblList):
    for item in gmblList:
        ojName = item.split('_')[0]
        side = item.split('_')[1]
        gmblName = ojName + '_' + side + '_gmblCtrl'
        sX = mc.getAttr(item + '.sx')
        sZ = mc.getAttr(item + '.sz')
        mc.circle(nr = (0, 1, 0), c = (0, 0, 0), n = gmblName)
        mc.setAttr(gmblName + '.sx', sX * 0.70)
        mc.setAttr(gmblName + '.sz', sZ * 0.70)
        mc.addAttr(item + 'Shape', ln = 'gimblCtrl', at = 'enum',
                   enumName = 'off=0:on=1:', dv = 1, k = True)
        gmblCon = mc.parentConstraint(item, gmblName, mo = False)
        mc.delete(gmblCon)
        mc.parent(gmblName, item)
        mc.connectAttr(item + 'Shape.gimblCtrl', gmblName + 'Shape.visibility')
        mc.makeIdentity(gmblName, apply = True, t=True, r=True)
        mc.delete(gmblName, ch = 1)


def stretchFk(nodeMultName, nodeAddName):
    ctrl = mc.ls(sl = True)[0]
    ojStretch = mc.ls(sl = True)[1]
    mc.createNode('multDoubleLinear', n = nodeMultName)
    mc.createNode('addDoubleLinear', n = nodeAddName)
    mc.addAttr(ctrl, ln = 'Stretch', at = "double", dv = 0, k = True)
    ojStretchTy = mc.getAttr(ojStretch + '.ty')
    mc.setAttr(nodeMultName + '.input2', 0.1)
    mc.setAttr(nodeAddName + '.input2', ojStretchTy)
    mc.connectAttr(ctrl + '.Stretch', nodeMultName + '.input1')
    mc.connectAttr(nodeMultName + '.output', nodeAddName + '.input1')
    mc.connectAttr(nodeAddName + '.output', ojStretch + '.ty')
    # mc.select( clear=True )

# gr.StretchFk('test1_stretchFk_Mult1', 'test1_stretchFk_add1')


def squashFk(nodeMultName, nodeAddName):
    ctrl = mc.ls(sl = True)[0]
    ojSquash = mc.ls(sl = True)[1]
    mc.createNode('multDoubleLinear', n = nodeMultName)
    mc.createNode('addDoubleLinear', n = nodeAddName)
    mc.addAttr(ctrl, ln = 'Squash', at = "double", dv = 0, k = True)
    mc.setAttr(nodeMultName + '.input2', 0.1)
    mc.setAttr(nodeAddName + '.input2', 1)
    mc.connectAttr(ctrl + '.Squash', nodeMultName + '.input1')
    mc.connectAttr(nodeMultName + '.output', nodeAddName + '.input1')
    mc.connectAttr(nodeAddName + '.output', ojSquash + '.sx')
    mc.connectAttr(nodeAddName + '.output', ojSquash + '.sz')
    # mc.select( clear=True )
    
def cleanCtrl(ctrlList):
    for i in ctrlList:
        mc.makeIdentity(i, apply = True)
        mc.delete(i, ch = 1)

# def createCtrlSet():
#     ctrlList = mc.ls(sl=True)
#     for item in ctrlList:
#         ojName = item.split('_')[0]
#         zGrpName = ojName + '_L_zGrp'
#         gmblName = ojName + '_L_gmblCtrl'
#         createFkZeroGrp(zGrpName, item)
#         createGmbl(gmblName, item)

def changeColor (col = '') :
	sel = mc.ls (sl = True)
	if not sel :
		print ('No Selection')
		return
	for each in sel :
		shp = mc.listRelatives (each, s = True)[0]
		colorDict = {'red' : 13, 'blue' : 6, 'green' : 14, 'white' : 16}
		if col not in colorDict :
			print (col + ' not in Dict')
			return
		mc.setAttr (shp + '.overrideEnabled', 1)
		mc.setAttr (shp + '.overrideColor', colorDict[col])

def createCtrlSet2():
    List = mc.ls(sl = True)
    if not List:
        print 'No Selection'
        return
    createFkZeroGrp3 (List)
    createGmbl3 (List)
    cleanCtrl (List)