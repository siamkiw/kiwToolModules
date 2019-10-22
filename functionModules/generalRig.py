import maya.cmds as mc

def nameingZero(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + type + 'Zro' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingRbn(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + side
    tmpDesc2 = tmpDesc1[0] + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'nrb']
    rbnName = ('_').join (nameList)
    # print grpName
    return rbnName

def nameingRbnGrp(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + type + 'Pos' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    rbnNameGrp = ('_').join (nameList)
    # print grpName
    return rbnNameGrp

def nameingEff(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + type + 'Zro' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'eff']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingIkh(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + 'Ik' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'ikh']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingPiv(obj, jntList):
    jntList = jntList.split('_')
    name = obj
    type = jntList[-1].capitalize()
    side = ''
    desc = ''
    if len(jntList) > 2 :
        sideList = ('CNT', 'LFT', 'RGT', 'UPR', 'LWR', 'FNT', 'BCK') 
        for each in sideList :
            if each in jntList[1] :
                side = each
                desc = jntList[1].split(side)[0]
                break
            else :
                desc = jntList[1]
    # print (name, desc, side, type)
    tmpDesc1 = desc + 'Piv' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName
    
def nameingPosJnt(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + 'Pos' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'jnt']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingDistGrp(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + type + 'Dist' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingLocalGrp(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + type + 'Local' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingWorldGrp(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + type + 'Wrold' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingRigGrp(obj):
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
    # print (name, desc, side, type)
    tmpDesc1 = desc + 'Rig' + side
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

    # create zGrp for obj1 and parentConstraint to obj2
def zeroGroup(obj1 = '', obj2 = ''):
    name = nameingZero(obj1)
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
    return name

# Parent Constraint off Maintain offset
def parentConOffMainTain(obj1, obj2):
    con = mc.parentConstraint(obj2, obj1, mo = False)
    mc.delete(con)
    return obj1

def pointConOffMainTain(obj1, obj2):
    con = mc.pointConstraint(obj2, obj1, mo = False)
    mc.delete(con)
    return obj1

# put all object in list in to zGrp
def inZeroGroup(objList = [], zGrpName = ''):
    mc.group(em = True, n = zGrpName)
    for i in objList:
        mc.parent(i, zGrpName)
    return zGrpName

def getPosition(obj):
    return mc.xform(obj, t=True, q=True)

def getWorldPosition(obj):
    return mc.xform(obj, t=True, q=True, ws = True)

def getRotation(obj):
    return mc.xform(obj, ro=True, q=True)

def getJointOrient(obj):
    return mc.getAttr(obj + '.jointOrient')[0]

def findRel(jntName = ''):
    listJoint = mc.listRelatives(jntName, ad = True, typ = 'joint')
    listJoint.append(jntName)
    return listJoint[::-1]

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

def delHist(obj = str):
    mc.makeIdentity(obj, apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
    mc.delete(obj, ch = 1)

def cleanObj(obj):
        mc.select(obj)
        mc.makeIdentity(obj, apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
        mc.delete(obj, ch = 1)

def spaceing(ctrlName = str, rootJnt = str, grp = str, worldSpaceObj = str, ikFk = str) :

    def parentConOffMainTainSpace(obj1, obj2):
        name = obj1
        grp = mc.group(em = True , n = name)
        ord = mc.xform(obj1, q = True, roo  = True)
        mc.xform(grp, roo = ord)
        con = mc.parentConstraint(obj2, obj1, mo = False)
        mc.delete(con)
        return name

    if ikFk.lower() not in ['ik', 'fk']:
        print 'function spaceingIk attr ikFk must be String ik or fk'
        return

    name = rootJnt.split('_')[0]
    side = rootJnt.split('_')[1]
    ctrlZeroName = nameingZero(ctrlName)
    localGrpName = nameingLocalGrp(ctrlName)
    wroldGrpName = nameingWorldGrp(ctrlName)

    parentConOffMainTainSpace(localGrpName, ctrlName)
    parentConOffMainTainSpace(wroldGrpName, ctrlName)

    mc.parent(localGrpName, grp)
    mc.parent(wroldGrpName, grp)
    revNodeName = mc.createNode('reverse', n = name + '_ikSpace' + side + '_rev')

    mc.addAttr(ctrlName, ln = '__Space__', at = "double", dv = 0, k = True)
    mc.setAttr(ctrlName + '.__Space__', lock = True)
    mc.addAttr(ctrlName, ln = 'space', at = "enum", en = 'Local:World', k = True)

    if ikFk.lower() == 'ik': 
        mc.parentConstraint(worldSpaceObj, wroldGrpName, mo = True)
        ctrlZeroNameCon = mc.orientConstraint([localGrpName, wroldGrpName], grp, mo = True)
        mc.connectAttr(ctrlName + '.space', revNodeName + '.inputX')
        mc.connectAttr(ctrlName + '.space', ctrlZeroNameCon[0] + '.' + wroldGrpName + 'W1')
        mc.connectAttr(revNodeName + '.outputX', ctrlZeroNameCon[0] + '.' + localGrpName + 'W0')
    elif ikFk.lower() == 'fk':
        mc.orientConstraint(worldSpaceObj, wroldGrpName, mo = True)
        ctrlZeroNameCon = mc.parentConstraint([localGrpName, wroldGrpName], grp, mo = True)
        mc.connectAttr(ctrlName + '.space', revNodeName + '.inputX')
        mc.connectAttr(ctrlName + '.space', ctrlZeroNameCon[0] + '.' + wroldGrpName + 'W1')
        mc.connectAttr(revNodeName + '.outputX', ctrlZeroNameCon[0] + '.' + localGrpName + 'W0')
    
    print ikFk.lower() + ' Spaceing ' + 'done.'

def createRotGrp(ctrlList = [], rotGrpDescList = []):
    zGrpList = []
    rotGrpList = []
    # find zGrp
    zGrpList = (map(lambda ctrl: mc.listRelatives (ctrl,p = True)[0], ctrlList))
    # unparent if obj had parent
    mc.parent(list(filter(lambda ctrl: mc.listRelatives(ctrl, p = True) != None, ctrlList)), world = True)
    mc.parent(list(filter(lambda zGrp: mc.listRelatives(zGrp, p = True) != None, zGrpList)), world = True)
    # create rotGrp
    for i in range(0, len(zGrpList)):
        ampRotList = []
        rotGrpAmp = ctrlList[i].split('_')
        name = rotGrpAmp[0]
        objType = 'grp'
        # create each rotGrp
        for j in range(0, len(rotGrpDescList)):
            dup = mc.duplicate (zGrpList[i], po = True)[0]
            desc = rotGrpDescList[j]
            rotGrpName = name + '_' + desc + '_' + objType
            mc.rename(dup, rotGrpName)
            ampRotList.append(rotGrpName)
        # parent each rotGrp
        if len(ampRotList) != 0:
            for i in range(0, len(ampRotList)):
                if i == len(ampRotList)-1:
                    break
                mc.parent(ampRotList[i], ampRotList[i+1])
        # add ampRotList to rotGrpList
        rotGrpList.append(ampRotList[::-1])
    # preant pathF
    for i in range(0, len(ctrlList)):
        # parent top rotGrp to zGrp
        mc.parent(rotGrpList[i][0], zGrpList[i])
        # parent ctrl to lowest rotGrp
        mc.parent(ctrlList[i], rotGrpList[i][-1])
        # if zGrp is not a fist zGrp parent it to ctrl 
        if i != 0:
            mc.parent(zGrpList[i], ctrlList[i-1])
    return rotGrpList


def fkIkBlend(fkIkCtrl = '', pelvisJnt = '', mainJntList = [], fkJntList = [], ikJntList = []):
    # addAttr to ctrl
    mc.addAttr(fkIkCtrl, ln = 'fkIk', at = 'double', min = 0, max = 1, dv = 0, k = True)
    for i in range(0, len(mainJntList)):
        # create bcTransNode
        name = mainJntList[i].split('_')[0] + '_'
        transDesc = 'fkIkTrans' + mainJntList[i].split('_')[1] + '_bc'
        bcTransNodeName = name + transDesc
        mc.createNode('blendColors', name = bcTransNodeName)
        # create bcRotNode
        name = mainJntList[i].split('_')[0] + '_'
        rotDesc = 'fkIkRot' + mainJntList[i].split('_')[1] + '_bc'
        bcRotNodeName = name + rotDesc
        mc.createNode('blendColors', name = bcRotNodeName)
        # connect ctrl to bcTransNode
        mc.connectAttr(fkIkCtrl + '.fkIk', bcTransNodeName + '.blender')
        mc.connectAttr(ikJntList[i] + '.translate', bcTransNodeName + '.color1')
        mc.connectAttr(fkJntList[i] + '.translate', bcTransNodeName + '.color2')
        # connect ctrl to bcRotNode
        mc.connectAttr(fkIkCtrl + '.fkIk', bcRotNodeName + '.blender')
        mc.connectAttr(ikJntList[i] + '.rotate', bcRotNodeName + '.color1')
        mc.connectAttr(fkJntList[i] + '.rotate', bcRotNodeName + '.color2')
        # connect bcTransNode to mainJnt
        mc.connectAttr(bcTransNodeName + '.output', mainJntList[i] + '.translate') 
        # connect bcRotNode to mainJnt
        mc.connectAttr(bcRotNodeName + '.output', mainJntList[i] + '.rotate')        
    # createGrp fk ik
    name = mainJntList[0].split('_')[0] + '_'
    fkDesc = 'fkRig' + mainJntList[1].split('_')[1] + '_grp'
    ikDesc = 'ikRig' + mainJntList[1].split('_')[1] + '_grp'
    fkGrpName = name + fkDesc
    ikGrpName = name + ikDesc
    mc.rename(zeroGroup(fkJntList[0], pelvisJnt), fkGrpName)
    mc.rename(zeroGroup(ikJntList[0], pelvisJnt), ikGrpName)
    # make fkikCtrlZgrp
    fkIkCtrlZgrpName = zeroGroup(fkIkCtrl, fkIkCtrl)
    print 'create node'
    # create node and connect fkikCtrl to fkZGrp, ikZGrp
    nodeName = mainJntList[1].split('_')[0] + '_'
    nodeSide = mainJntList[1].split('_')[1] + '_'
    revNode = mc.createNode('reverse', n = nodeName + '_fkIk' + nodeSide + '_rev')
    mc.connectAttr(fkIkCtrl + '.fkIk', revNode + '.input.inputX', )
    mc.connectAttr(revNode + '.output.outputX', fkGrpName + '.visibility')
    mc.connectAttr(fkIkCtrl + '.fkIk', ikGrpName + '.visibility')
    
    return [fkGrpName, ikGrpName, fkIkCtrlZgrpName]

def createRigGrp(parent = str, child = str):
    rigGrpName = nameingRigGrp(child)
    mc.group( em = True, n = rigGrpName)
    mc.parentConstraint(parent, rigGrpName, mo = False)
    return rigGrpName




        



    

# 
# def createRotGrp(ctrlList = [], rotGrpName = []):
#     zGrpList = []
#     rotGrpList = []
#     ampParentList = []
#     # find zGrp
#     zGrpList = (map(lambda ctrl: mc.listRelatives (ctrl,p = True)[0], ctrlList))
#     # find ParentGrp zGrp
#     ampParentList = list(filter(lambda zGrp: mc.listRelatives(zGrp, p = True) != None, zGrpList))
#     print ampParentList
#     # unparent if obj had parent
#     mc.parent(list(filter(lambda ctrl: mc.listRelatives(ctrl, p = True) != None, ctrlList)), world = True)
#     mc.parent(list(filter(lambda zGrp: mc.listRelatives(zGrp, p = True) != None, zGrpList)), world = True)
#     # dupduplicate zGrp and nameing
#     for i in range(0, len(zGrpList)):
#         dup = mc.duplicate (zGrpList[i], po = True)[0]
#         print dup
#         rotGrpAmp = ctrlList[i].split('_')
#         name = rotGrpAmp[0]
#         side = rotGrpAmp[1] + 'CtrlRot_'
#         objType = 'grp'
#         rotGrpName = name + '_' + side + objType
#         mc.rename(dup, rotGrpName)
#         rotGrpList.append(rotGrpName)
#     # parent Path
#     for i in range(0, len(ctrlList)):
#         rotGrp = mc.parent(rotGrpList[i], zGrpList[i])
#         mc.parent(ctrlList[i], rotGrp)
#         if i != 0:
#             mc.parent(zGrpList[i], ctrlList[i-1])

    
    