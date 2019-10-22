import maya.cmds as mc
import skr.generalRig as gn
import skr.fkRig as fkr

# todo create NURBS
def createNurbs(firstJnt = '', secondJnt = '', jntNum = 5):
    posList = []
    posJnt  = []
    curveList = []
    # nameing nameRbn
    nameRbn = gn.nameingRbn(firstJnt)
    # get pos form jnt
    posList.extend(list(map(gn.getWorldPosition, [firstJnt, secondJnt])))
    # create posJnt
    mc.select(cl = True)
    jnt = mc.joint(n = 'pos_CNT_jnt', p = [0, 0, 0])
    mc.select(cl = True)
    ampCon = mc.parentConstraint([firstJnt, secondJnt], jnt)
    posList.append(gn.getWorldPosition(jnt))
    posJnt.append(jnt)
    mc.delete(ampCon)
    # delete posJnt
    map(mc.delete, posJnt)
    # create ampCurve
    ampCurve = mc.curve(n = 'ampCurve', d = 3, ep = [posList[0], posList[2], posList[1]])
    # create NURBS
    for i in range(0, 2):
        curve = mc.duplicate(ampCurve)
        curve = mc.rename(curve, 'curve' + str(i+1))
        curveList.append(curve)
    curveList.append(ampCurve)
    mc.setAttr(curveList[0] + '.tx', 0.4)
    mc.setAttr(curveList[1] + '.tx', -0.4)
    # loft
    mc.loft(curveList[1], curveList[0], n = nameRbn, ch = True, u = True, c = False, ar = 1, d = 1, ss = 1, rn = False, po = False, rsn = True)
    # delete curveList
    map(mc.delete, curveList)
    # rebuild Surface
    mc.rebuildSurface(nameRbn, ch = 1, rpo = 1, end = 1, kr = 0, kcp = 0, su = 0, du = 3, sv = 0, dv = 1, tol = 0.01, fr = 0, dir = 2)
    return nameRbn 

# todo create grp that stick on NURBS
def createGroupOnSurface(NURBS = '', jntNum = 5):
    nameRbnCrv = ''
    nameRbnPosGrpList = []
    nameRbnPosiList = []
    nameRbnAimList = []
    jntDistance = [0.050, 0.275, 0.500, 0.725, 0.950]
    ampNum = 0
    name = NURBS.split('_')[0]
    side = NURBS.split('_')[1]
    # create em Grp, pointOnSurfaceInfo Node, aimConstraint Node
    for i in range(0, jntNum):
        # em
        grp = mc.group(em = True , n = name + str(i+1) + '_rbnPos' + side + '_grp')
        # pointOnSurfaceInfo
        posiNode = mc.createNode('pointOnSurfaceInfo', n = name + str(i+1) + '_rbnPos' + side + '_posi')
        # aimConstraint
        aimNode = mc.createNode('aimConstraint', n = name + str(i+1) + '_rbnPos' + side + '_aim',  parent = grp)
        # add to List
        nameRbnPosGrpList.append(grp)
        nameRbnPosiList.append(posiNode)
        nameRbnAimList.append(aimNode)
        # connect Node Path
        mc.connectAttr(NURBS + 'Shape.worldSpace', posiNode + '.inputSurface')
        mc.connectAttr(posiNode + '.normal', aimNode + '.worldUpVector')
        mc.connectAttr(posiNode + '.tangentU', aimNode + '.target[0].targetTranslate')
        mc.connectAttr(posiNode + '.position', grp + '.translate')
        mc.connectAttr(aimNode + '.constraintRotate', grp + '.rotate')
        # set grp's Position 
        mc.setAttr(posiNode + '.parameterV', 0.5)
        mc.setAttr(posiNode + '.parameterU', jntDistance[i])
        # set aimVector
        mc.setAttr(aimNode + '.aimVector', 0, 1, 0)
        mc.setAttr(aimNode + '.upVector', 0, 0, 1)
    # create crv
    crvName = mc.duplicateCurve(NURBS + '.v[0.5]', ch = 0, rn = 1, local = 1, n = name + '_rbn' + side + '_crv')[0]
    # create curveFromSurfaceIso Node and connect
    cfsNodeName = mc.createNode('curveFromSurfaceIso', n  = name + '_rbnPos' + side + '_cfs')
    mc.setAttr(cfsNodeName + '.isoparmValue', 0.5)
    mc.connectAttr(NURBS + 'Shape.worldSpace', cfsNodeName + '.inputSurface')
    mc.connectAttr(cfsNodeName + '.outputCurve', crvName + '.create')
    # create still grp
    stillGrpName = mc.group(em = True, n = name + '_rbnStill' + side + '_grp')
    mc.parent(nameRbnPosGrpList, stillGrpName)
    mc.parent(NURBS, stillGrpName)
    mc.parent(crvName, stillGrpName)
    mc.setAttr(NURBS + '.v', False)
    mc.setAttr(crvName + '.v', False)
    
    return {'stillGrpName' : stillGrpName, 'nameRbnPosGrpList' : nameRbnPosGrpList, 'crvName' : crvName}

# todo create ctrl
def createRbnCtrl(posGrpList = [], radius = 1, side = '' , firstJnt = '', secondJnt = '', nurbsName = ''):
    skinJntNameList = []
    dtlCtrlNameList = []
    dtlCtrlZgrpNameList = []
    mainJntNameList = []
    mainCtrlNameList = []
    mainCtrlZgrpNameList = []
    posMainJntList = [firstJnt, secondJnt]
    mainJntPosList = []
    posMainJntDesList = ['_rbnStart', '_rbnMid', '_rbnEnd']
    firstJntName = firstJnt.split('_')[0]
    skinGrpName = firstJntName + '_rbnSkin' + side + '_grp'
    # * create skinJnt dltCtrl
    for i in range(0, len(posGrpList)):
        # nameing 
        ctrlName =  posGrpList[i].split('_')[0] + '_rbnDtl' + side + '_ctrl'
        jntName =  posGrpList[i].split('_')[0] + '_rbnDtl' + side + '_jnt'
        # add jnt to List
        skinJntNameList.append(jntName)
        # create ctrl
        mc.circle(nr = (0, 1, 0), c = (0, 0, 0), n = ctrlName)
        mc.setAttr(ctrlName + '.sx', radius)
        mc.setAttr(ctrlName + '.sz', radius)
        mc.delete(ctrlName , ch = True)
        # create jnt
        mc.select(cl = True)
        mc.joint(n = jntName, p = [0, 0, 0])
        mc.select(cl = True)
        # make ctrl and jnt have the same pviot
        gn.parentConOffMainTain(jntName, posGrpList[i])
        gn.parentConOffMainTain(ctrlName, posGrpList[i])
        mc.makeIdentity(jntName, apply=True, t=1, r=1, s=1, n=2 )
        # add dtlCtrl to list 
        dtlCtrlNameList.append(ctrlName)
        # make zGrp
        dtlCtrlZgrpNameList.append(gn.zeroGroup(ctrlName, posGrpList[i]))
        # parentConstrain
        mc.parentConstraint(posGrpList[i], dtlCtrlZgrpNameList[i])
        # parent jnt to ctrl
        mc.parentConstraint(ctrlName, jntName, mo = False)
    # create skinGrp
    mc.group(em = True , n = skinGrpName)
    # parent skinJnt into skinGrp
    mc.parent(skinJntNameList, skinGrpName)
    # * create mainCtrl
    # get ThridJnt world Position
    mc.select(cl = True)
    thirdJnt = mc.joint(n = 'thirdJnt', p = [0, 0, 0])
    ampCon = mc.parentConstraint([firstJnt, secondJnt], thirdJnt)
    mc.delete(ampCon)
    # app posJnt to List at index 1
    posMainJntList.insert(1, thirdJnt)
    # get jnt position from posJnt
    mainJntPosList = list(map(gn.getWorldPosition, posMainJntList))
    # delete thirdJnr
    mc.delete(thirdJnt)
    for i in range(0, 3):
        mc.select(cl = True)
        jnt = mc.joint(n = firstJntName + posMainJntDesList[i] + side + '_jnt', p = [0, 0, 0])
        ampCon = mc.parentConstraint(posGrpList[1], jnt, mo = False)
        mc.delete(ampCon)
        mc.setAttr(jnt + '.t', mainJntPosList[i][0], mainJntPosList[i][1], mainJntPosList[i][2])
        # add each jnt to the List
        mainJntNameList.append(jnt)
        # nameing mainCtrl
        mainCtrlName = mainJntNameList[i].split('_')[0] + posMainJntDesList[i] + side + '_ctrl'
        # create mainCtrl
        mainCtrlAmp = mc.curve(p=[(-1, 0, -1), (-1, 0, 1), (1, 0, 1),(1, 0, -1), (-1, 0, -1)], k=[0, 1, 2, 3, 4], d = 1)
        mc.rename(mainCtrlAmp, mainCtrlName)
        mc.setAttr(mainCtrlName + '.sx', radius)
        mc.setAttr(mainCtrlName + '.sz', radius)
        # mark ctrl has same direction to jnt 
        gn.parentConOffMainTain(mainCtrlName, jnt)
        # create zGrp and put into list
        mainCtrlZgrpNameList.append(gn.zeroGroup(mainCtrlName, mainCtrlName))
        mainCtrlNameList.append(mainCtrlName)
        mc.parent(jnt, mainCtrlName)
    
    # create ctrlGrp
    ctrlGrpName = mc.group(em = True, n = firstJntName + '_rbnCtrl' + side + '_grp')
    # parentConstraint ctrlGrpName -> firstJnt
    mc.parentConstraint(firstJnt, ctrlGrpName)
    # pontConstraint endCtrl -> secondJnt
    mc.pointConstraint(secondJnt, mainCtrlZgrpNameList[-1], mo = True)
    # put all mainCtrl in to ctrlGrpName
    mc.parent(mainCtrlZgrpNameList, ctrlGrpName)

    dtlCtrlGrpName = mc.group(em = True, n = firstJntName + '_rbnDtlCtrl' + side + '_grp')
    # parentConstraint ctrlGrpName -> dtlCtrlGrpName and then delete parent
    mc.delete(mc.parentConstraint(ctrlGrpName, dtlCtrlGrpName))
    # parent dtlCtrlGrpName -> ctrlGrpName
    mc.parent(dtlCtrlGrpName, ctrlGrpName)
    # parent dtlCtrlZgrpNameList -> dtlCtrlGrpName
    mc.parent(dtlCtrlZgrpNameList, dtlCtrlGrpName)
    # parentConstraint ctrlGrpName -> skinGrpName
    mc.parentConstraint(ctrlGrpName, skinGrpName, mo = True)
    mc.pointConstraint(mainJntNameList[0], mainJntNameList[-1], mainCtrlZgrpNameList[1])

    # aim startJnt and ndJnt to midJnt
    if side == 'LFT':
        mc.aimConstraint(mainJntNameList[1], mainJntNameList[0], weight = 1, aimVector = (0, 1, 0), upVector = (0, 0, 1), worldUpType = 'objectrotation', worldUpVector = (0 , 0, 1), worldUpObject = mainJntNameList[1])
        mc.aimConstraint(mainJntNameList[1], mainJntNameList[2], weight = 1, aimVector = (0, 1, 0), upVector = (0, 0, 1), worldUpType = 'objectrotation', worldUpVector = (0 , 0, 1), worldUpObject = mainJntNameList[1])
        mc.aimConstraint(mainJntNameList[2], mainCtrlZgrpNameList[1], weight = 1, aimVector = (0, 1, 0), upVector = (0, 0, 1), worldUpType = 'objectrotation', worldUpVector = (0 , 0, 1), worldUpObject = firstJnt)
    elif side == 'RGT':
        mc.aimConstraint(mainJntNameList[1], mainJntNameList[0], weight = 1, aimVector = (0, 1, 0), upVector = (0, 0, 1), worldUpType = 'objectrotation', worldUpVector = (0 , 0, 1), worldUpObject = mainJntNameList[1])
        mc.aimConstraint(mainJntNameList[1], mainJntNameList[2], weight = 1, aimVector = (0, 1, 0), upVector = (0, 0, 1), worldUpType = 'objectrotation', worldUpVector = (0 , 0, 1), worldUpObject = mainJntNameList[1])
        mc.aimConstraint(mainJntNameList[2], mainCtrlZgrpNameList[1], weight = 1, aimVector = (0, 1, 0), upVector = (0, 0, 1), worldUpType = 'objectrotation', worldUpVector = (0 , 0, 1), worldUpObject = secondJnt)
        
    # bindSkin
    mc.skinCluster(mainJntNameList[0], mainJntNameList[1], mainJntNameList[2], nurbsName)
    # setAttr skinGrp, startCtrl and endCtrl to be unseen
    mc.setAttr(skinGrpName + '.v', False)
    mc.setAttr(mainCtrlNameList[0] + '.v', False)
    mc.setAttr(mainCtrlNameList[2] + '.v', False)
    mc.setAttr(mainJntNameList[1] + '.v', False)
    # add attr dtlCtrl to mid ctrl
    mc.addAttr(mainCtrlNameList[1] + 'Shape', ln = 'detailCtrl', at = 'double', min = 0, max = 1, dv = 0, k = True)
    # connecting Attr
    mc.connectAttr(mainCtrlNameList[1] + 'Shape.detailCtrl', dtlCtrlGrpName + '.v')
    # return dtlCtrlZgrpNameList ,mainCtrlZgrpNameList, skinJntNameList
    return {'dtlCtrlNameList' : dtlCtrlNameList, 'mainCtrlNameList' : mainCtrlNameList, 'skinJntNameList' : skinJntNameList}

def rbnSlide(midCtrl = '', nrbShape = '', crvShape = '', posGrpList = []):
    pociNodeList = []
    clspNodeList = []
    bcNodeList = []
    disData = [0.050, 0.275, 0.500, 0.725, 0.950]
    # add Attr to midCtrl
    mc.addAttr(midCtrl, ln = 'autoSlide', at = 'double', min = 0, max = 1, dv = 0, k = True)
    # rebuild and rename
    rebuildName = mc.rebuildCurve(crvShape, ch = 1, rpo = 1, end = 1, kr = 0, kcp = 0, kt = 0, s = 0, d = 0, tol = 0.01)[0]
    # rebuildName = crvShape.split('_')[0] + '_' + crvShape.split('_')[0] + '_rebld'
    # mc.rename(rebuildAmpName, rebuildName)
    for i in range(0, len(posGrpList)):
        name = posGrpList[i].split('_')[0] + '_'
        desc = posGrpList[i].split('_')[1] + '_'
        # create Node
        pociNode = mc.createNode('pointOnCurveInfo', n = name + desc + 'poci')
        clspNode = mc.createNode('closestPointOnSurface', n = name + desc + 'clsp')
        bcNode = mc.createNode('blendColors', n = name + desc + 'bc')
        # add node to List
        pociNodeList.append(pociNode)
        clspNodeList.append(clspNode)
        pociNodeList.append(bcNode)
        # setAttr 
        mc.setAttr(bcNode + '.color2.color2R', disData[i])
        mc.setAttr(pociNode + '.parameter', disData[i])
        # connect Attr
        mc.connectAttr(midCtrl + '.autoSlide', bcNode + '.blender')
        mc.connectAttr(crvShape + 'Shape.worldSpace', pociNode + '.inputCurve')
        mc.connectAttr(nrbShape + 'Shape.worldSpace', clspNode + '.inputSurface')
        mc.connectAttr(pociNode + '.result.position', clspNode + '.inPosition')
        mc.connectAttr(clspNode + '.result.parameterU', bcNode + '.color1.color1R')
        mc.connectAttr(bcNode + '.output.outputR', name + desc + 'posi.parameterU')



def rbnSquash(midCtrl = '', ctrlGrpName = '', crvShape = '', dtlCtrlList = [], skinJntNameList = [], side = ''):
    squashRatio = [0.15, 0.5, 1.0, 0.5, 0.15]
    autoSquashName = midCtrl.split('_')[0]
    # globalCrv setup
    globalCrvName = autoSquashName + '_rbnGlobal' + side + '_crv'
    cifAutoGlobalNode = autoSquashName + '_rbnGlobal' + side + '_cif'
    cifAutoNode = midCtrl.split('_')[0] + '_rbn' + side + '_cif'
    mc.duplicate(crvShape, n = globalCrvName)
    mc.createNode('curveInfo', n = cifAutoGlobalNode)
    mc.createNode('curveInfo', n = cifAutoNode)
    mc.parent(globalCrvName, ctrlGrpName)
    mc.connectAttr(globalCrvName + 'Shape.worldSpace', cifAutoGlobalNode + '.inputCurve')
    mc.connectAttr(crvShape + 'Shape.worldSpace', cifAutoNode + '.inputCurve')
    # autoSquash setup
    autoNodeDesc = 'rbnAutoSquash' + side
    mdvAutoNodeName = mc.createNode('multiplyDivide', n = autoSquashName + '_' + autoNodeDesc + '_mdv')
    addAutoNodeName = mc.createNode('addDoubleLinear', n = autoSquashName + '_' + autoNodeDesc + '_add')
    multAutoNodeName = mc.createNode('multDoubleLinear', n = autoSquashName + '_' + autoNodeDesc + '_mult')
    mc.setAttr(addAutoNodeName + '.input2', -1)
    mc.setAttr(mdvAutoNodeName + '.operation', 2)
    # midCtrl setup
    mc.addAttr(midCtrl, ln = 'autoSquash', at = 'double', min = 0, max = 1, dv = 0, k = True)
    mc.addAttr(midCtrl, ln = 'squash', at = 'double', dv = 0, k = True)
    mc.connectAttr(midCtrl + '.autoSquash', multAutoNodeName + '.input2')
    # autoSquash connect
    mc.connectAttr(cifAutoGlobalNode + '.arcLength', mdvAutoNodeName + '.input1.input1X')
    mc.connectAttr(cifAutoNode + '.arcLength', mdvAutoNodeName + '.input2.input2X')
    mc.connectAttr(mdvAutoNodeName + '.output.outputX', addAutoNodeName + '.input1')
    mc.connectAttr(addAutoNodeName + '.output', multAutoNodeName + '.input1')

    for i in range(0, len(skinJntNameList)):
        # setup mdv, pma Node   
        squashName = skinJntNameList[i].split('_')[0]
        mdvNodeName = squashName + '_rbnSquash' + side + '_mdv'
        pmaNodeName = squashName + '_rbnSquash' + side + '_pma'
        mc.createNode('multiplyDivide', n = mdvNodeName)
        mc.createNode('plusMinusAverage', n = pmaNodeName)
        mc.setAttr(pmaNodeName + '.input2D[0].input2Dx', 1)
        mc.setAttr(mdvNodeName + '.input2X', squashRatio[i])
        mc.setAttr(mdvNodeName + '.input2Y', squashRatio[i])
        # connect mdv, pma Node        
        mc.connectAttr(mdvNodeName + '.outputX', pmaNodeName + '.input2D[1].input2Dx')
        mc.connectAttr(mdvNodeName + '.outputY', pmaNodeName + '.input2D[2].input2Dx')
        mc.connectAttr(mdvNodeName + '.outputZ', pmaNodeName + '.input2D[3].input2Dx')
        mc.connectAttr(pmaNodeName + '.output2D.output2Dx', skinJntNameList[i] + '.scale.scaleX')
        mc.connectAttr(pmaNodeName + '.output2D.output2Dx', skinJntNameList[i] + '.scale.scaleZ')
        # dtlCtrl setup
        mc.addAttr(dtlCtrlList[i], ln = 'squash', at = 'double', dv = 0, k = True)
        # dtlCtrl connect   
        mc.connectAttr(dtlCtrlList[i] + '.squash', mdvNodeName + '.input1.input1Z')
        # dtlCtrl connect   
        mc.connectAttr(midCtrl + '.squash', mdvNodeName + '.input1.input1Y')
        # midCtrl connect
        mc.connectAttr(multAutoNodeName + '.output', mdvNodeName + '.input1.input1X')


def rbnTwist(midCtrl = '', dtlCtrlList = [], side = ''):
    # todo create twistRatioList
    twistRatioIXList = [-0.0, -0.25, -0.5, -0.75, -1.0]
    twistRatioIYList = twistRatioIXList[::-1]
    # todo create twistMdv create twistadd connect Node
    # addAttr midCtrl
    mc.addAttr(midCtrl, ln = 'rootTwist', at = 'double', dv = 0, k = True)
    mc.addAttr(midCtrl, ln = 'endTwist', at = 'double', dv = 0, k = True)
    for i in range(0, len(dtlCtrlList)):
        # create Node
        name = dtlCtrlList[i].split('_')[0] + '_'
        desc = 'rbnTwist' + side + '_'
        twistMdvNodeName = name + desc + 'mdv'
        twistAddNodeName = name + desc + 'add'
        mc.createNode('multiplyDivide', n = twistMdvNodeName)
        mc.createNode('addDoubleLinear', n = twistAddNodeName)
        # setAttr
        if side == 'RGT':
            mc.setAttr(twistMdvNodeName + '.input2X', twistRatioIXList[i])
            mc.setAttr(twistMdvNodeName + '.input2Y', twistRatioIYList[i])
        elif side == 'LFT':
            mc.setAttr(twistMdvNodeName + '.input2X', twistRatioIYList[i])
            mc.setAttr(twistMdvNodeName + '.input2Y', twistRatioIXList[i])
        # connectAttr
        mc.connectAttr(midCtrl + '.rootTwist', twistMdvNodeName + '.input1X')
        mc.connectAttr(midCtrl + '.endTwist', twistMdvNodeName + '.input1Y')
        mc.connectAttr(twistMdvNodeName + '.outputX', twistAddNodeName + '.input1')
        mc.connectAttr(twistMdvNodeName + '.outputY', twistAddNodeName + '.input2')
        # create RotGrp
        dtlCtrlZRot = str(gn.createRotGrp([dtlCtrlList[i]], ['rbnDtl' + side + 'LFT'])[0][0])
        mc.connectAttr(twistAddNodeName + '.output', dtlCtrlZRot + '.rotateY')
    # find dtlCtrlGrpName
    dtlCtrlGrpName = midCtrl.split('_')[0] + '_rbnDtlCtrl' + side + '_grp'
    # parent back to rbnDtlCtrlGrp
    dtlCtrlZgrpList = list(map(lambda i: gn.nameingZero(i), dtlCtrlList))
    mc.parent(dtlCtrlZgrpList, dtlCtrlGrpName)
        
    


def rbnRig(firstJnt = '', secondJnt = '', jntNum = 5, radius = 1, side = ''):
    stillGrpName = firstJnt.split('_')[0] + '_rbnStill' + side + '_grp'
    skinGrpName = firstJnt.split('_')[0] + '_rbnSkin' + side + '_grp'
    ctrlGrpName = firstJnt.split('_')[0] + '_rbnCtrl' + side + '_grp'

    # create nurbs
    nameRbn = createNurbs(firstJnt, secondJnt, jntNum)
    # create grp and make it stick on nurbs
    onSurfaceObj = createGroupOnSurface(nameRbn, jntNum)
    # create all Ctrl
    rbnCtrl = createRbnCtrl(onSurfaceObj['nameRbnPosGrpList'], radius, side, firstJnt, secondJnt, nameRbn)

    rbnSlide(midCtrl = rbnCtrl['mainCtrlNameList'][1], nrbShape = nameRbn, crvShape = onSurfaceObj['crvName'], posGrpList = onSurfaceObj['nameRbnPosGrpList'])
    rbnSquash(midCtrl = rbnCtrl['mainCtrlNameList'][1], ctrlGrpName = ctrlGrpName, crvShape = onSurfaceObj['crvName'], dtlCtrlList = rbnCtrl['dtlCtrlNameList'], skinJntNameList = rbnCtrl['skinJntNameList'], side = side)
    rbnTwist(midCtrl = rbnCtrl['mainCtrlNameList'][1], dtlCtrlList = rbnCtrl['dtlCtrlNameList'], side = side)