import maya.cmds as mc
import functionModules.generalRig as gn

def nameingStretchFkNodeMult(obj):
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
    tmpDesc1 = desc + 'Stretch' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'mult']
    nodeName = ('_').join (nameList)
    # print grpName
    return nodeName

def nameingStretchFkNodeAdd(obj):
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
    tmpDesc1 = desc + 'Stretch' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'add']
    nodeName = ('_').join (nameList)
    # print grpName
    return nodeName

def nameingSquashFkNodeMult(obj):
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
    tmpDesc1 = desc + 'Squash' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'mult']
    nodeName = ('_').join (nameList)
    # print grpName
    return nodeName

def nameingSquashFkNodeAdd(obj):
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
    tmpDesc1 = desc + 'squashFk' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'add']
    nodeName = ('_').join (nameList)
    # print grpName
    return nodeName

def nameingGmblCtrl(obj):
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
    tmpDesc1 = desc + 'Gmbl' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'ctrl']
    nodeName = ('_').join (nameList)
    # print grpName
    return nodeName

def nameingFkCtrl(obj):
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
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'ctrl']
    grpName = ('_').join (nameList)
    # print grpName
    return grpName

def nameingFkLocalGrp(obj):
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
    tmpDesc1 = 'fkLocal' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    nodeName = ('_').join (nameList)
    # print grpName
    return nodeName

def nameingFkWorldGrp(obj):
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
    tmpDesc1 = 'fkWorld' + side 
    tmpDesc2 = tmpDesc1[0].lower() + tmpDesc1[1:]
    nameList = [name, tmpDesc2, 'grp']
    nodeName = ('_').join (nameList)
    # print grpName
    return nodeName

# add posJnt to every Jnt
def createPosFkJntTest(rootJnt):
    # list all jnt that Relatives to rootJnt
    listJoint = mc.listRelatives(rootJnt, ad = True, typ = 'joint')
    rootJntParent = mc.listRelatives(rootJnt, p = True)
    listJoint.append(rootJnt)
    # unparent all jnt 
    for jnt in listJoint:
        if mc.listRelatives (jnt, p = True) != None:
            mc.parent(jnt, world = True)
    # Sort listJnt 
    listJoint = listJoint[::-1]
    # get pos from listJoint
    posJntPosList = list(map(gn.getPosition, listJoint))
    rotationPosJntList = list(map(gn.getRotation, listJoint))
    # nameing posJnt
    posJntNameList = list(map(gn.nameingPosJnt, listJoint))
    mc.select(cl = True)
    # create posJnt from posJntPosList
    for i in range(0, len(posJntNameList)):
        mc.joint(n = posJntNameList[i], p = posJntPosList[i])
    # set posJnt Orientation Axis
    for i in range(0, len(posJntNameList)):
        mc.select(posJntNameList[i])
        mc.joint(n = posJntNameList[i], edit = True, zso = True, oj = 'yxz', sao = 'xdown')
        mc.setAttr(posJntNameList[i] + '.radius', 0)
        mc.select(clear=True)
    # parent posJntNameList and listJoint
    for i in range(0, len(posJntNameList)):
        if i == len(posJntNameList)-1:
            mc.parent(listJoint[i], listJoint[i-1])
        if i < len(posJntNameList)-1:
            par = mc.parent(listJoint[i], posJntNameList[i])
        if i != len(posJntNameList)-1:
            mc.parent(posJntNameList[i+1], par)
    # delete last posJnt
    mc.delete(posJntNameList[-1])
    mc.setAttr(listJoint[-1] + '.jointOrient' , 0, 0, 0)
    # if rootJnt has parent to obj
    if rootJntParent != None:
        mc.parent(posJntNameList[0], rootJntParent)
    mc.select(posJntNameList[0])
    parList = []
    # return all parent List
    for i in range(0, len(listJoint)):
        if posJntNameList[i] != posJntNameList[-1]:
            parList.append(posJntNameList[i])
        parList.append(listJoint[i])
    return parList

def createPosFkJnt(rootJnt):
    posJntList = []
    mainJntList = []
    rootJntParent = []
    parList = []

    listJointAmp = mc.listRelatives(rootJnt, ad = True, typ = 'joint')
    rootJntParent = mc.listRelatives(rootJnt, p = True)
    mainJntList.append(rootJnt)
    mainJntList.extend(listJointAmp[::-1])
    # nameing posJnt from mainJnt
    posJntList = list(map(gn.nameingPosJnt, mainJntList))
    # unparent mainJnt
    mainJntListUnParent = list(filter(lambda jnt: mc.listRelatives (jnt, p = True) != None, mainJntList))
    mc.parent(mainJntListUnParent, world = True)
    # get rotation from mainJnt
    for i in range(0, len(mainJntList)):
        mc.duplicate(mainJntList[i], po = True, n = posJntList[i])
    # parent every jnt
    for i in range(0, len(mainJntList)):
        if i != len(mainJntList)-1:
            par = mc.parent(mainJntList[i], posJntList[i])
        if i != len(posJntList)-1:
            mc.parent(posJntList[i+1], par)
        elif i == len(mainJntList)-1:
            mc.parent(mainJntList[i], mainJntList[i-1])
    # delect last posJnt 
    mc.delete(posJntList[-1])
    # clear every jnt
    for i in range(0, len(posJntList)-1):
        mc.select(posJntList[i])
        mc.setAttr(posJntList[i] + '.radius', 0)
        mc.makeIdentity(posJntList[i], apply = 1, t = 1, r = 1, s = 1, n = 0, pn = 1)
    for i in range(0, len(mainJntList)):
        mc.select(mainJntList[i])
        mc.makeIdentity(mainJntList[i], apply = 1, t = 1, r = 1, s = 1, n = 0, pn = 1)  
    # return all parent List
    for i in range(0, len(mainJntList)):
        if posJntList[i] != posJntList[-1]:
            parList.append(posJntList[i])
        parList.append(mainJntList[i])
    # if rootJntParent is not None parent posJnt to rootJntParent
    if rootJntParent != None:
        mc.parent(posJntList[0], rootJntParent[0])
    return parList

def stretchFk(ctrl, ojStretch):
    nodeMultName = nameingStretchFkNodeMult(ctrl)
    nodeAddName = nameingStretchFkNodeAdd(ctrl)
    mc.createNode('multDoubleLinear', n = nodeMultName)
    mc.createNode('addDoubleLinear', n = nodeAddName)
    mc.addAttr(ctrl, ln = 'Stretch', at = "double", dv = 0, k = True)
    ojStretchTy = mc.getAttr(ojStretch + '.ty')
    if nodeMultName.split('_')[1] == 'fkStretchRGT':
        mc.setAttr(nodeMultName + '.input2', -0.1)
    else:
        mc.setAttr(nodeMultName + '.input2', 0.1)
    mc.setAttr(nodeAddName + '.input2', ojStretchTy)
    mc.connectAttr(ctrl + '.Stretch', nodeMultName + '.input1')
    mc.connectAttr(nodeMultName + '.output', nodeAddName + '.input1')
    mc.connectAttr(nodeAddName + '.output', ojStretch + '.ty')

def squashFk(ctrl, ojSquash):
    nodeMultName = nameingSquashFkNodeMult(ctrl)
    nodeAddName = nameingSquashFkNodeAdd(ctrl)
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

def cleanObj(obj):
        mc.select(obj)
        mc.makeIdentity(obj, apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
        mc.delete(obj, ch = 1)

def createGmbl(gmblList = [], radius = 1):
    gmblCtrlList = []
    for item in gmblList:
        gmblName = nameingGmblCtrl(item)
        gmblCtrlList.append(gmblName)
        mc.circle(nr = (0, 1, 0), c = (0, 0, 0), n = gmblName)
        mc.setAttr(gmblName + '.sx', radius)
        mc.setAttr(gmblName + '.sz', radius)
        mc.addAttr(item + 'Shape', ln = 'gimblCtrl', at = 'enum',
                   enumName = 'off=0:on=1:', dv = 0, k = True)
        gmblCon = mc.parentConstraint(item, gmblName, mo = False)
        mc.delete(gmblCon)
        mc.parent(gmblName, item)
        mc.connectAttr(item + 'Shape.gimblCtrl', gmblName + 'Shape.visibility')
        mc.select(gmblName)
        mc.makeIdentity(gmblName, apply = True)
        mc.delete(gmblName, ch = 1)
    return gmblCtrlList

def createCtrlFk(jntList = [], radius = 1, gmbl = True):
    mainCtrlList = []
    zGrpCtrlList = []
    gmblCtrlList = []

    # if create one ctrl
    if len(jntList) == 1:
        mainCtrlList.append(nameingFkCtrl(jntList[0]))
        mc.circle(nr = (0, 1, 0), c = (0, 0, 0), n = mainCtrlList[0])
        mc.setAttr(mainCtrlList[0] + '.sx', radius)
        mc.setAttr(mainCtrlList[0] + '.sz', radius)
        ctrlConstraint = mc.parentConstraint(jntList[0], mainCtrlList[0], mo = False)
        mc.delete(ctrlConstraint)
        zGrpCtrlList.append(gn.zeroGroup(mainCtrlList[0], jntList[0]))
        # if gmbl is True also create gmblCtrl
        if gmbl == True:
            gmblCtrlList.append(createGmbl(mainCtrlList, radius*0.70))        
        return mainCtrlList

    # filter only mainJnt
    jntList = list(filter(lambda jnt: (jnt.split('_')[1] == jntList[1].split('_')[1]) , jntList))
    # create mainCtrl
    for i in range(0, len(jntList)-1):
        mainCtrlList.append(nameingFkCtrl(jntList[i]))
        mc.circle(nr = (0, 1, 0), c = (0, 0, 0), n = mainCtrlList[i])
        mc.setAttr(mainCtrlList[i] + '.sx', radius)
        mc.setAttr(mainCtrlList[i] + '.sz', radius)
        ctrlConstraint = mc.parentConstraint(jntList[i], mainCtrlList[i], mo = False)
        mc.delete(ctrlConstraint)
        zGrpCtrlList.append(gn.zeroGroup(mainCtrlList[i], jntList[i]))
    # if gmbl is True also create gmblCtrl
    if gmbl == False:
        for i in range(0, len(zGrpCtrlList)):
            objChild = mc.listRelatives(zGrpCtrlList[i], c = True)
            if i == len(zGrpCtrlList)-1:
                break
            mc.parent(zGrpCtrlList[i+1], objChild)
    if gmbl == True:
        gmblCtrlList.append(createGmbl(mainCtrlList, radius*0.70))
        for i in range(0, len(zGrpCtrlList)):
            objChild =  mc.listRelatives(zGrpCtrlList[i], ad = True, typ = 'transform')
            objChild = objChild[::-1]
            if i == len(zGrpCtrlList)-1:
                break
            mc.parent(zGrpCtrlList[i+1], objChild[-1])
    print mainCtrlList
    return mainCtrlList

def createCtrlFkTest(mainRootJnt = '', jntList = [] , radius = 1, gmbl = False):
    zGrpCtrlNameList = []
    mainCtrlList = []
    posCtrlList = []
    
    # filter mainJnt
    jntList = list(filter(lambda jnt: (jnt.split('_')[1] == jntList[1].split('_')[1]) , jntList))

    ctrlName = list(map(nameingFkCtrl, jntList))
    # create ctrl on every jnt make zGrp make ctrl has the same Axis to jnt
    for i in range(0, len(jntList)-1):
        # if desc of jnt == main jnt create ctrl on it
        if jntList[i].split('_')[1] == mainRootJnt.split('_')[1]:
            # add mainCtrl to mainCtrlList
            mainCtrlList.append(ctrlName[i])
            mc.circle(nr = (0, 1, 0), c = (0, 0, 0), n = ctrlName[i])
            mc.setAttr(ctrlName[i] + '.sx', radius)
            mc.setAttr(ctrlName[i] + '.sz', radius)
            ctrlConstraint = mc.parentConstraint(jntList[i], ctrlName[i], mo = False)
            mc.delete(ctrlConstraint)
            zGrpCtrlName = gn.zeroGroup(ctrlName[i], ctrlName[i])
            zGrpCtrlNameList.append(zGrpCtrlName)
    if gmbl == False:
        for i in range(0, len(zGrpCtrlNameList)):
            objChild = mc.listRelatives(zGrpCtrlNameList[i], c = True)
            if i == len(zGrpCtrlNameList)-1:
                break
            mc.parent(zGrpCtrlNameList[i+1], objChild)
    if gmbl == True:
        posCtrlList = createGmbl(mainCtrlList, radius*0.70)
        for i in range(0, len(zGrpCtrlNameList)):
            objChild =  mc.listRelatives(zGrpCtrlNameList[i], ad = True, typ = 'transform')
            objChild = objChild[::-1]
            if i == len(zGrpCtrlNameList)-1:
                break
            mc.parent(zGrpCtrlNameList[i+1], objChild[-1])
    # return ctrl that will use latter
    if gmbl == True:
        # print posCtrlList
        print posCtrlList, ctrlName
        return [posCtrlList, ctrlName]
    else:
        # print mainCtrlList
        print mainCtrlList, ctrlName
        return [mainCtrlList, ctrlName]

    # jnt and ctrl you want to parent together
def parentFk(jntList, ctrlList):
    # find posJnt from jntList
    posJntList = []
    for posJnt in jntList:
        if posJnt.split('_')[1] == jntList[0].split('_')[1]:
            posJntList.append(posJnt)
    # find mainJnt from jntList
    jntList = list(filter(lambda jnt: (jnt.split('_')[1] == jntList[1].split('_')[1]) , jntList))

    if jntList != posJntList:
        # pointConstraint ctrl to posJnt
        for i in range(0, len(posJntList)):
            mc.pointConstraint(ctrlList[i], posJntList[i], w=1, mo=True)
        # parentConstraint ctrl to mainJnt
        for i in range(0, len(jntList)-1):
            mc.parentConstraint(ctrlList[i], jntList[i], w=1, mo=True)
            # print len(ctrlList[0]), len(jntList)
    elif jntList == posJntList:
        # parentConstraint ctrl to mainJnt
        for i in range(0, len(jntList)-1):
            mc.parentConstraint(ctrlList[i], jntList[i], w=1, mo=True)
            # print len(ctrlList[0]), len(jntList)

def listStretch(jntList = [], ctrlList = []):
    # find mainCtrl
    ctrlList = list(filter(lambda ctrl: (ctrl.split('_')[1] == ctrlList[1].split('_')[1]) , ctrlList))
    # nameingZero(ctrlList)
    ctrlZroList = list(map(gn.nameingZero, ctrlList))
    # stretchFk
    for i in range(0, len(ctrlList)):
        if i < len(ctrlList)-1:
            stretchFk(ctrlList[i], ctrlZroList[i+1])
        else:
            stretchFk(ctrlList[i], jntList[-1])
            break

def listSquash(jntList = [], ctrlList = []):
    # find mainCtrl
    jntList = list(filter(lambda jnt: (jnt.split('_')[1] == jntList[1].split('_')[1]) , jntList))
    # squashFk
    for i in range(0, len(ctrlList)):
            squashFk(ctrlList[i], jntList[i])

def rigFk(rootJnt = '', radius = 1, gmbl = True):
    jntList = createPosFkJnt(rootJnt)
    ctrlList = createCtrlFk(jntList, radius, gmbl)
    parentFk(jntList, ctrlList)
    listStretch(jntList, ctrlList)
    listSquash(jntList, ctrlList)

def legFk(fkJntList = list, radius = 1, gmbl = True):
    ctrlList = createCtrlFk(fkJntList, radius, gmbl)
    parentFk(fkJntList, ctrlList)
    listStretch(fkJntList, ctrlList)
    # listSquash(fkJntList, ctrlList)
    return gn.nameingZero(ctrlList[0])

def fkSpaceing(worldSpaceObj = str, ctrlGrp = str, fkCtrlGrp = str, side = str):

    localGrpName = mc.group(em = True, n = nameingFkLocalGrp(ctrlGrp))
    gn.parentConOffMainTain(localGrpName, ctrlGrp)
    mc.parent(localGrpName, fkCtrlGrp)

    worldGrpName = mc.group(em = True, n = nameingFkWorldGrp(ctrlGrp))
    gn.parentConOffMainTain(worldGrpName, ctrlGrp)
    mc.parent(worldGrpName, fkCtrlGrp)
    mc.orientConstraint(worldSpaceObj, worldGrpName, mo = True)

    conCtrlName = mc.orientConstraint([localGrpName, worldGrpName], ctrlGrp, mo = True)[0]
    
    # create revNode
    revNodeName = mc.createNode('reverse', n = ctrlGrp.split('_')[0] + '_fkSpace' + side + '_rev')

    # attr to upLegCtrl
    upLegCtrlName = mc.listRelatives(ctrlGrp, c = True)[0]
    # connectAttr
    mc.addAttr(upLegCtrlName, ln = '__Space__', at = "double", dv = 0, k = True)
    mc.setAttr(upLegCtrlName + '.__Space__', lock = True)
    mc.addAttr(upLegCtrlName, ln = 'space', at = "enum", en = 'Local:World', k = True)

    mc.connectAttr(upLegCtrlName + '.space', revNodeName + '.inputX')
    mc.connectAttr(upLegCtrlName + '.space', conCtrlName + '.' + worldGrpName + 'W1')
    mc.connectAttr(revNodeName + '.outputX', conCtrlName + '.' + localGrpName + 'W0')



###################################################################


