import maya.cmds as mc

def createFkZeroGrp(zGrpName='', ojName=''):
    mc.group(em=True, n=str(zGrpName))
    zGrpCon = mc.parentConstraint(ojName, zGrpName, mo=False)
    mc.delete(zGrpCon)
    mc.parent(ojName, zGrpName)
    # mc.select( clear=True )

def stretchFk(nodeMultName, nodeAddName):
    ctrl = mc.ls(sl=True)[0]
    ojStretch = mc.ls(sl=True)[1]
    mc.createNode('multDoubleLinear', n=nodeMultName)
    mc.createNode('addDoubleLinear', n=nodeAddName)
    mc.addAttr(ctrl, ln='Stretch', at="double", dv=0, k=True)
    ojStretchTy = mc.getAttr(ojStretch + '.ty')
    mc.setAttr(nodeMultName+ '.input2', 0.1 )
    mc.setAttr(nodeAddName + '.input2', ojStretchTy )
    mc.connectAttr(ctrl + '.Stretch', nodeMultName + '.input1')
    mc.connectAttr(nodeMultName + '.output', nodeAddName + '.input1')
    mc.connectAttr(nodeAddName + '.output', ojStretch + '.ty')
    # mc.select( clear=True )

# gr.StretchFk('test1_stretchFk_Mult1', 'test1_stretchFk_add1')
    
def squashFk(nodeMultName, nodeAddName):
    ctrl = mc.ls(sl=True)[0]
    ojSquash = mc.ls(sl=True)[1]
    mc.createNode('multDoubleLinear', n=nodeMultName)
    mc.createNode('addDoubleLinear', n=nodeAddName)
    mc.addAttr(ctrl, ln='Squash', at="double", dv=0, k=True)
    mc.setAttr(nodeMultName+ '.input2', 0.1 )
    mc.setAttr(nodeAddName + '.input2', 1 )
    mc.connectAttr(ctrl + '.Squash', nodeMultName + '.input1')
    mc.connectAttr(nodeMultName + '.output', nodeAddName + '.input1')
    mc.connectAttr(nodeAddName + '.output', ojSquash + '.sx')
    mc.connectAttr(nodeAddName + '.output', ojSquash + '.sz')
    # mc.select( clear=True )

def createGmbl(gmblName, ojName):
    sx =  mc.getAttr(ojName + '.sx')
    sz =  mc.getAttr(ojName + '.sz')
    mc.circle(nr=(0, 1, 0), c=(0, 0, 0), n=gmblName)
    mc.setAttr(gmblName + '.sx', sx*0.70)
    mc.setAttr(gmblName + '.sz', sz*0.70)
    gmblCon = mc.parentConstraint(ojName, gmblName, mo=False)
    mc.delete(gmblCon)
    mc.parent(gmblName, ojName)
    mc.makeIdentity(gmblName, apply=True )
    mc.delete(gmblName, ch = 1)

def createCtrlSet():
    ctrlList = mc.ls(sl=True)
    for item in ctrlList:
        ojName = item.split('_')[0]
        zGrpName = ojName + '_L_zGrp'
        gmblName = ojName + '_L_gmblCtrl'
        createFkZeroGrp(zGrpName, item)
        createGmbl(gmblName, item)

##############################################

def zeroGroup(obj1 = '', obj2 = '', name = ''):

    ord = mc.xform(obj1, q = True, roo  = True)

    grp = mc.group(em = True , n = name)
    mc.xform(grp, roo = ord)

    con = mc.parentConstraint(obj2, grp, mo = False)
    mc.delete(con)

    mc.parent(obj1, grp)
    mc.makeIdentity(obj1, a = True)
    mc.setAttr(obj1 + '.rp', 0,0,0)
    mc.setAttr(obj1 + '.sp', 0,0,0)

    mc.select(obj1, obj2)

def createFkZeroGrp(zGrpName='', ojName=''):
    mc.group(em=True, n=str(zGrpName))
    zGrpCon = mc.parentConstraint(ojName, zGrpName, mo=False)
    mc.delete(zGrpCon)
    mc.parent(ojName, zGrpName)
    # mc.select( clear=True )

def nameing(obj):
    list = obj.split('_')
    name = list[0]
    type = list[-1].capitalize()
    side = ''
    desc = ''
    if len(list) > 2 :
        sideList = ('CNT', 'LFT', 'RGT', 'UPR', 'LWR', 'FNT', 'BCK') 
        for each in sideList :
            if each in list[1] :
                side = each
                desc = list[1].split(side)[0]
                break
            else :
                desc = list[1]
    print (name, desc, side, type)
    tmpDesc1 = desc + type + 'Zro' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    grpName = ('_').join (nameList)
    print grpName


