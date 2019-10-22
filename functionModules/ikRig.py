import maya.cmds as mc
import functionModules.generalRig as gn

def nameingIkCtrl(obj):
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

# def createGmbl(gmblList = [], radius = 1):
#     gmblCtrlList = []
#     for item in gmblList:
#         gmblName = nameingGmblCtrl(item)
#         gmblCtrlList.append(gmblName)
#         mc.circle(nr = (0, 1, 0), c = (0, 0, 0), n = gmblName)
#         mc.setAttr(gmblName + '.sx', radius)
#         mc.setAttr(gmblName + '.sz', radius)
#         mc.addAttr(item + 'Shape', ln = 'gimblCtrl', at = 'enum',
#                    enumName = 'off=0:on=1:', dv = 0, k = True)
#         gmblCon = mc.parentConstraint(item, gmblName, mo = False)
#         mc.delete(gmblCon)
#         mc.parent(gmblName, item)
#         mc.connectAttr(item + 'Shape.gimblCtrl', gmblName + 'Shape.visibility')
#         mc.select(gmblName)
#         mc.makeIdentity(gmblName, apply = True)
#         mc.delete(gmblName, ch = 1)
#     return gmblCtrlList

# ankleCtrl
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

# kneeCtrl
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
    mc.setAttr(ikName + '.v', False)
    print 'createIkhIk ' + ikName + ' Done.'
    return ikName

def legCtrlIkh(rootJnt, ankleCtrlName, rootCtrlName, kneeCtrlName):
    # find jnt that rel to rootJnt
    listJoint = gn.findRel(rootJnt)
    upLegJnt = listJoint[1]
    ankleJnt = listJoint[3]
    ballJnt = listJoint[4]
    toeJnt = listJoint[5]

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
    ballRollPiv = gn.parentConOffMainTain(gn.nameingPiv('ballRoll', ankleJnt), ankleJnt)
    toeBendPiv = gn.parentConOffMainTain(gn.nameingPiv('toeBend', ankleJnt), ankleJnt)
    footInPiv = gn.parentConOffMainTain(gn.nameingPiv('footIn', ankleJnt), ankleJnt)
    footOutPiv = gn.parentConOffMainTain(gn.nameingPiv('footOut', ankleJnt), ankleJnt)
    toePiv = gn.parentConOffMainTain(gn.nameingPiv('toe', ankleJnt), ankleJnt)
    heelPiv = gn.parentConOffMainTain(gn.nameingPiv('heel', ankleJnt), ankleJnt)
    anklePiv = gn.parentConOffMainTain(gn.nameingPiv('ankle', ankleJnt), ankleJnt)

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

def legIkAttrConnection(ankleCtrlName, side):
    mc.connectAttr(ankleCtrlName + '.toeRoll', 'toe_ikPiv' + side + '_grp' + '.rx')
    mc.connectAttr(ankleCtrlName + '.ballRoll', 'ballRoll_ikPiv' + side + '_grp' + '.rx')
    mc.connectAttr(ankleCtrlName + '.heelRoll', 'heel_ikPiv' + side + '_grp' + '.rx')
    mc.connectAttr(ankleCtrlName + '.toeTwist', 'toe_ikPiv' + side + '_grp' + '.rz')
    mc.connectAttr(ankleCtrlName + '.heelTwist', 'heel_ikPiv' + side + '_grp' + '.rz')
    mc.connectAttr(ankleCtrlName + '.legTwist', 'leg_ik' + side + '_ikh' + '.twist')
    mc.connectAttr(ankleCtrlName + '.toeBend', 'toeBend_ikPiv' + side + '_grp' + '.rx')
    mc.connectAttr(ankleCtrlName + '.footRock', 'footIn_ikPiv' + side + '_grp' + '.ry')
    mc.connectAttr(ankleCtrlName + '.footRock', 'footOut_ikPiv' + side + '_grp' + '.ry')
    mc.transformLimits('footOut_ikPiv' + side + '_grp', ry = (0, 180), ery = (1 ,0))
    mc.transformLimits('footIn_ikPiv' + side + '_grp', ry = (-180, 0), ery = (0 ,1))

def createGmbl(gmblList = [], radius = 1):
    gmblCtrlList = []
    for item in gmblList:
        gmblName = nameingGmblCtrl(item)
        gmblCtrlList.append(gmblName)
        mc.duplicate(item, n = gmblName)
        itemPos = mc.getAttr(item + '.s')[0]
        mc.setAttr(gmblName + '.s', itemPos[0]*0.70, itemPos[1], itemPos[2]*0.70)
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

def hipRig(rootCtrlName, ankleCtrlName , kneeCtrlName, rootJnt):
    pass