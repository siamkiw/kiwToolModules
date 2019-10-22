import maya.cmds as mc
import skr.generalRig as gn

reload(gn)

# add attr to LegCtrl
def addAttrLegCtrlIk(ctrlName):
    mc.addAttr(ctrlName, ln = '__Foot__', at = "double", dv = 0, k = True)
    mc.setAttr(ctrlName + '.__Foot__', lock = True)
    mc.addAttr(ctrlName, ln = 'toeRoll', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'ballRoll', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'heelRoll', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'toeTwist', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'heelTwist', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'legTwist', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'toeBend', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'footRock', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = '__Stretch__', at = "double", dv = 0, k = True)
    mc.setAttr(ctrlName + '.__Stretch__', lock = True)
    mc.addAttr(ctrlName, ln = 'autoStretch', at = "double", dv = 1, min = 0, max = 1, k = True)
    mc.addAttr(ctrlName, ln = 'upLegStretch', at = "double", dv = 0, k = True)
    mc.addAttr(ctrlName, ln = 'lowLegStretch', at = "double", dv = 0, k = True)
    print 'addAttrLegCtrlIk ' + ctrlName + ' Done.'

def addAttrkneeCtrlIk(ctrlName):
    mc.addAttr(ctrlName, ln = '__Stretch__', at = "double", dv = 0, k = True)
    mc.setAttr(ctrlName + '.__Stretch__', lock = True)
    mc.addAttr(ctrlName, ln = 'kneeLock', at = "double", dv = 0, min = 0, max = 1, k = True)
    print 'addAttrkneeCtrlIk ' + ctrlName + ' Done.'

# create Ik 
def createIkhIk(rootJnt, effectorJnt, ikName, ikhType):
    mc.select(rootJnt)
    mc.select(effectorJnt, add = True)
    mc.ikHandle( n = ikName, sj = rootJnt, ee = effectorJnt, sol = ikhType )
    mc.ikHandle(ikName, srp = True ,e = True )
    print 'createIkhIk ' + ikName + ' Done.'
    return ikName

# create all ikh for legIk and setup leg Piv
def legCtrlIkh(rootJnt, ankleCtrlName, rootCtrlName, kneeCtrlName):
    listJoint = mc.listRelatives(rootJnt, ad = True, typ = 'joint')
    listJoint.append(rootJnt)
    listJoint =  listJoint[::-1]
    upLegJnt = listJoint[0]
    ankleJnt = listJoint[2]
    ballJnt = listJoint[3]
    toeJnt = listJoint[4]

# create Ikh
    upLegIkName = createIkhIk(upLegJnt, ankleJnt, gn.nameingIkh(upLegJnt), 'ikRPsolver')
    ankleIkName = createIkhIk(ankleJnt, ballJnt, gn.nameingIkh(ballJnt), 'ikSCsolver')
    toeIkName = createIkhIk(ballJnt, toeJnt, gn.nameingIkh(toeJnt), 'ikSCsolver')

# set ikh visibility to False
    mc.setAttr(upLegIkName + '.v', False )
    mc.setAttr(ankleIkName + '.v', False )
    mc.setAttr(toeIkName + '.v', False )

# create zGro for ikh
    pivlegAxisName = gn.zeroGroup(gn.nameingIkh(upLegJnt), gn.nameingIkh(upLegJnt))
    pivBallAxisName = gn.zeroGroup(gn.nameingIkh(ballJnt), gn.nameingIkh(ballJnt))
    pivToeAxisName = gn.zeroGroup(gn.nameingIkh(toeJnt), gn.nameingIkh(toeJnt))

# Parent Constraint off Maintain offset pivZeroGrp to ankleJnt
    ballRollPiv = parentConOffMainTainLegIk(gn.nameingPiv('ballRoll', ankleJnt), ankleJnt)
    toeBendPiv = parentConOffMainTainLegIk(gn.nameingPiv('toeBend', ankleJnt), ankleJnt)
    footInPiv = parentConOffMainTainLegIk(gn.nameingPiv('footIn', ankleJnt), ankleJnt)
    footOutPiv = parentConOffMainTainLegIk(gn.nameingPiv('footOut', ankleJnt), ankleJnt)
    toePiv = parentConOffMainTainLegIk(gn.nameingPiv('toe', ankleJnt), ankleJnt)
    heelPiv = parentConOffMainTainLegIk(gn.nameingPiv('heel', ankleJnt), ankleJnt)
    anklePiv = parentConOffMainTainLegIk(gn.nameingPiv('ankle', ankleJnt), ankleJnt)

# get pivBall and pivToe position (ikh position)
    pivBallAxisList = mc.xform(pivBallAxisName, q = True, t = True)
    pivToeAxisList = mc.xform(pivToeAxisName, q = True, t = True)
    # print pivBallAxisList[0], pivBallAxisList[1], pivBallAxisList[2]
    # print pivBallAxisName, pivBallAxisList

# move all Piv to the right position
    mc.xform(ballRollPiv, t = (pivBallAxisList[0], pivBallAxisList[1], pivBallAxisList[2]))
    mc.xform(toeBendPiv, t = (pivBallAxisList[0], pivBallAxisList[1], pivBallAxisList[2]))

    ###############
    mc.xform(footInPiv, t = (pivBallAxisList[0]+1, pivBallAxisList[1], pivBallAxisList[2]))
    mc.xform(footOutPiv, t = (pivBallAxisList[0]-1, pivBallAxisList[1], pivBallAxisList[2]))
    ##############

    mc.xform(toePiv, t = (pivToeAxisList[0], pivToeAxisList[1], pivToeAxisList[2]))

    ##############
    mc.xform(heelPiv, t = (pivBallAxisList[0], pivBallAxisList[1]-0.1, pivBallAxisList[2]-1.5))
    ##############

# parent all pivZroGrp 
    mc.parent(pivlegAxisName, ballRollPiv)
    mc.parent(pivBallAxisName, ballRollPiv)
    mc.parent(pivToeAxisName, toeBendPiv)
    mc.parent(ballRollPiv, footInPiv)
    mc.parent(toeBendPiv, footInPiv)
    mc.parent(footInPiv, footOutPiv)
    mc.parent(footOutPiv, toePiv)
    mc.parent(toePiv, heelPiv)
    mc.parent(heelPiv, anklePiv)
    mc.parent(anklePiv, ankleCtrlName)

# pointConstraint rootJnt to rootCtrlName
    mc.pointConstraint(rootCtrlName, rootJnt)

# poleVectorConstraint upLegIkName to kneeCtrlName
    mc.poleVectorConstraint(kneeCtrlName, upLegIkName)

# RGT -> if // LFT -> else
    if footOutPiv.split('_')[1] == 'pivRGT':
        # set min and max to footInPiv Attr and footOutPiv Attr
        mc.transformLimits(footInPiv, ry = (0, 180), ery = (1 ,0))
        mc.transformLimits(footOutPiv, ry = (-180, 0), ery = (0 ,1))
    else:
        mc.transformLimits(footOutPiv, ry = (0, 180), ery = (1 ,0))
        mc.transformLimits(footInPiv, ry = (-180, 0), ery = (0 ,1))

    print 'legCtrlIkh ' + ankleCtrlName + ' Done.'

    return {
        'ballRollPiv' : ballRollPiv,
        'toeBendPiv' : toeBendPiv,
        'footInPiv' : footInPiv,
        'footOutPiv' : footOutPiv,
        'toePiv' : toePiv,
        'heelPiv' : heelPiv,
        'anklePiv' : anklePiv,
        'upLegIkName' : upLegIkName
    }

# create attr Connection 
def legIkAttrConnection(pivList, ankleCtrlName):
    mc.connectAttr(ankleCtrlName + '.toeRoll', pivList['toePiv'] + '.rx')
    mc.connectAttr(ankleCtrlName + '.ballRoll', pivList['ballRollPiv'] + '.rx')
    mc.connectAttr(ankleCtrlName + '.heelRoll', pivList['heelPiv'] + '.rx')
    mc.connectAttr(ankleCtrlName + '.toeTwist', pivList['toePiv'] + '.rz')
    mc.connectAttr(ankleCtrlName + '.heelTwist', pivList['heelPiv'] + '.rz')
    mc.connectAttr(ankleCtrlName + '.legTwist', pivList['upLegIkName'] + '.twist')
    mc.connectAttr(ankleCtrlName + '.toeBend', pivList['toeBendPiv'] + '.rx')
    mc.connectAttr(ankleCtrlName + '.footRock', pivList['footInPiv'] + '.ry')
    mc.connectAttr(ankleCtrlName + '.footRock', pivList['footOutPiv'] + '.ry')

    print 'legIkAttrConnection ' + ankleCtrlName + ' Done.'

# create Dist group and pointConstraint to ctrl
def ikDistGrp(ctrlName):
    distGrp = mc.group(em = True, n = gn.nameingDistGrp(ctrlName))
    mc.pointConstraint(ctrlName, distGrp, mo = False)
    print 'ikDistGrp' + distGrp + ' Done.'
    return distGrp

# create Ik node and connect Attr to Ctrl
def createLegIkNode(rootJnt, ankleDistGrp, rootDistGrp, kneeDistGrp, ankleCtrlName, kneeCtrlName):
    listName = rootJnt.split('_')
    name = listName[0]
    side = listName[1]

    listJoint = mc.listRelatives(rootJnt, ad = True, typ = 'joint')
    listJoint.append(rootJnt)
    listJoint =  listJoint[::-1]
    upLegJnt = listJoint[0]
    lowLeg = listJoint[1]
    ankleJnt = listJoint[2]
    ballJnt = listJoint[3]
    toeJnt = listJoint[4]

# create node
    ikAutoStretchDtw = mc.createNode('distanceBetween', n = name + '_ikAutoStretch' + side + '_dtw')
    ikKneeLock1Dtw = mc.createNode('distanceBetween', n = name + '_ikKneeLock1' + side + '_dtw')
    ikKneeLock2Dtw = mc.createNode('distanceBetween', n = name + '_ikKneeLock2' + side + '_dtw')
    ikAutoStretchMdv = mc.createNode('multiplyDivide', n = name + '_ikAutoStretch' + side + '_mdv')
    ikStretchMdv = mc.createNode('multiplyDivide', n = name + '_ikStretch' + side + '_mdv')
    ikStretchAmpMdv = mc.createNode('multiplyDivide', n = name + '_ikStretchAmp' + side + '_mdv')
    ikKneeLockMdv = mc.createNode('multiplyDivide', n = name + '_ikKneeLock' + side + '_mdv')
    ikAutoStretchCnd = mc.createNode('condition', n = name + '_ikAutoStretch' + side + '_cnd')
    ikStretchBc = mc.createNode('blendColors', n = name + '_ikAutoStretch' + side + '_bc')
    ikKneeLockBc = mc.createNode('blendColors', n = name + '_ikKneeLock' + side + '_bc')
    ikStretchPma = mc.createNode('plusMinusAverage', n = name + '_ikStretch' + side + '_pma')

# get joint.ty
    lowLegTy = mc.getAttr(lowLeg + '.ty')
    ankleTy = mc.getAttr(ankleJnt + '.ty')

    mc.connectAttr(rootDistGrp + '.t', ikAutoStretchDtw + '.p1')
    mc.connectAttr(ankleDistGrp + '.t', ikAutoStretchDtw + '.p2')
    mc.connectAttr(ikAutoStretchDtw + '.distance', ikAutoStretchMdv + '.input1X')

    mc.setAttr(ikAutoStretchMdv + '.input2X', lowLegTy + ankleTy)
    mc.setAttr(ikAutoStretchMdv + '.operation', 2)

    mc.connectAttr(ikAutoStretchMdv + '.outputX', ikAutoStretchCnd + '.colorIfTrueR')
    mc.connectAttr(ikAutoStretchDtw + '.distance', ikAutoStretchCnd + '.firstTerm')

    mc.setAttr(ikAutoStretchCnd + '.operation', 2)

    if side == 'RGT':
        mc.setAttr(ikAutoStretchCnd + '.secondTerm', (lowLegTy + ankleTy)*-1)
    else:
        mc.setAttr(ikAutoStretchCnd + '.secondTerm', (lowLegTy + ankleTy))

    mc.connectAttr(ankleCtrlName + '.autoStretch', ikStretchBc + '.blender')
    mc.connectAttr(ikAutoStretchCnd + '.outColorR', ikStretchBc + '.color1R')

    mc.setAttr(ikStretchBc + '.color2R', 1)

    mc.connectAttr(ikStretchBc + '.outputR', ikStretchMdv + '.input1X')
    mc.connectAttr(ikStretchBc + '.outputR', ikStretchMdv + '.input1Y')
    
    mc.connectAttr(ikStretchMdv + '.outputX', ikStretchPma + '.input2D[1].input2Dx')
    mc.connectAttr(ikStretchMdv + '.outputY', ikStretchPma + '.input2D[1].input2Dy')
    mc.setAttr(ikStretchMdv + '.input2X', lowLegTy)
    mc.setAttr(ikStretchMdv + '.input2Y', ankleTy)

    mc.connectAttr(ikStretchPma + '.output2Dx', ikKneeLockBc + '.color2R')
    mc.connectAttr(ikStretchPma + '.output2Dy', ikKneeLockBc + '.color2G')

    mc.connectAttr(kneeCtrlName + '.kneeLock', ikKneeLockBc + '.blender')

    mc.connectAttr(ikKneeLockBc + '.outputR', lowLeg + '.ty')
    mc.connectAttr(ikKneeLockBc + '.outputG', ankleJnt + '.ty')

# kneeLock Path
    mc.connectAttr(rootDistGrp + '.t', ikKneeLock1Dtw + '.p1')
    mc.connectAttr(kneeDistGrp + '.t', ikKneeLock1Dtw + '.p2')

    mc.connectAttr(ankleDistGrp + '.t', ikKneeLock2Dtw + '.p1')
    mc.connectAttr(kneeDistGrp + '.t', ikKneeLock2Dtw + '.p2')

    mc.connectAttr(ikKneeLock1Dtw + '.distance', ikKneeLockMdv + '.input1X')
    mc.connectAttr(ikKneeLock2Dtw + '.distance', ikKneeLockMdv + '.input1Y')

    if side == 'RGT':
        mc.setAttr(ikKneeLockMdv + '.input2X', 1)
        mc.setAttr(ikKneeLockMdv + '.input2Y', 1)
    else :
        mc.setAttr(ikKneeLockMdv + '.input2X', 1)
        mc.setAttr(ikKneeLockMdv + '.input2Y', 1)

    mc.connectAttr(ikKneeLockMdv + '.outputX', ikKneeLockBc + '.color1R')
    mc.connectAttr(ikKneeLockMdv + '.outputY', ikKneeLockBc + '.color1G')

# ik Stretch Path
    mc.connectAttr(ankleCtrlName + '.upLegStretch', ikStretchAmpMdv + '.input1X')
    mc.connectAttr(ankleCtrlName + '.lowLegStretch', ikStretchAmpMdv + '.input1Y')

    if side == 'RGT':
        mc.setAttr(ikStretchAmpMdv + '.input2X', -0.1)
        mc.setAttr(ikStretchAmpMdv + '.input2Y', -0.1)
    else :
        mc.setAttr(ikStretchAmpMdv + '.input2X', 0.1)
        mc.setAttr(ikStretchAmpMdv + '.input2Y', 0.1)

    mc.connectAttr(ikStretchAmpMdv + '.outputX', ikStretchPma + '.input2D[2].input2Dx')
    mc.connectAttr(ikStretchAmpMdv + '.outputY', ikStretchPma + '.input2D[2].input2Dy')

    print 'createIkNode ' + ankleCtrlName +  ' Done.'

def parentConOffMainTainLegIk(obj1, obj2):
    name = obj1
    grp = mc.group(em = True , n = name)
    ord = mc.xform(obj1, q = True, roo  = True)
    mc.xform(grp, roo = ord)
    con = mc.parentConstraint(obj2, obj1, mo = False)
    mc.delete(con)
    return name
    

def legIkCtrl(ankleCtrlName, rootCtrlName, kneeCtrlName, rootJnt):
    # add Attr to Ctrl
    addAttrLegCtrlIk(ankleCtrlName)
    addAttrkneeCtrlIk(kneeCtrlName)
    
    # create ankleCtrl zeroGroup
    ankleZGrpName = gn.zeroGroup(ankleCtrlName, ankleCtrlName)
    rootZGrpName = gn.zeroGroup(rootCtrlName, rootCtrlName)
    kneeZGrpName = gn.zeroGroup(kneeCtrlName, kneeCtrlName)

    #  create ikh parent Ctrl
    ikPivList = legCtrlIkh(rootJnt, ankleCtrlName, rootCtrlName, kneeCtrlName)

    # connect attr Connection
    legIkAttrConnection( ikPivList, ankleCtrlName )
    
    # create distGrp from jnt name
    ankleDistGrp = ikDistGrp(ankleCtrlName)
    rootDistGrp = ikDistGrp(rootCtrlName)
    kneeDistGrp = ikDistGrp(kneeCtrlName)

    # create all Ik node and connect Attr to Ctrl
    createLegIkNode(rootJnt, ankleDistGrp, rootDistGrp, kneeDistGrp, ankleCtrlName, kneeCtrlName)

    ikGrpName = gn.nameingRigGrp(ankleCtrlName)

    if mc.objExists('upLeg_ikRigRGT_grp'):
        print 'upLeg_ikRigRGT_grp exits'
        objInLegIKGroupList = [ankleZGrpName, rootZGrpName, kneeZGrpName, ankleDistGrp, rootDistGrp, kneeDistGrp]
        map(lambda parentObj : mc.parent(parentObj, 'upLeg_ikRigRGT_grp'), objInLegIKGroupList)

    else:
        print 'upLeg_ikRigRGT_grp Not exits'
        objInLegIKGroupList = [rootJnt, ankleZGrpName, rootZGrpName, kneeZGrpName, ankleDistGrp, rootDistGrp, kneeDistGrp]
        ikGrpName = gn.inZeroGroup(objInLegIKGroupList, ikGrpName)

    print 'legIkCtrl ' + rootJnt + ' Done.'

    return ikGrpName

#ikGrp = ikr.legIkCtrl('leg_ikRGT_ctrl', 'leg_ikRootRGT_ctrl', 'knee_ikRGT_ctrl', 'upLeg_RGT_jnt')

#gn.spaceing('leg_ikRGT_ctrl', 'upLeg_RGT_jnt', ikGrp, 'placement_ctrl', 'ik')
