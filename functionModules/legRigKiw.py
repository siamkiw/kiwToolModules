import maya.cmds as mc

# ui
# Start with the Window
mc.window(title="Leg Auto Rig")

# Add a single column layout to add controls into
mc.columnLayout(columnAttach=('both', 10), rowSpacing=20, columnWidth=250)

# Add controls to the Layout
mc.button(label="Create Position Point", command="createPositionJoint()")
mc.button(label="rig", command="rig()")

# Display the window
mc.showWindow()

#--------------------------------------------------------------------------------------#

# jntPosXYZ
upLeg_L_jnt = []
lowLeg_L_jnt = []
ankle_L_jnt = []
ball_L_jnt = []
toe_L_jnt = []

legPosition = [
    [0.8999999761581421, 8.93725872039795, 1.6670938407514768e-07],
    [0.8999999761581421, 5.082729195445287, 0.3260868489742279],
    [0.8999999761581421, 1.0029856157909955, -0.03706564009189606],
    [0.8999999761581421, 0.23651546239852905, 1.4054166078567505],
    [0.9068282005372641, 0.1441195495991089, 2.1694516265006833]
]

def createPositionJoint():
    mc.select(clear=True)
    mc.joint(p=(legPosition[0][0], legPosition[0]
                [1], legPosition[0][2]), n='posLeg_1')
    mc.joint(p=(legPosition[1][0], legPosition[1]
                [1], legPosition[1][2]), n='posLeg_2')
    mc.joint(p=(legPosition[2][0], legPosition[2]
                [1], legPosition[2][2]), n='posLeg_3')
    mc.joint(p=(legPosition[3][0], legPosition[3]
                [1], legPosition[3][2]), n='posLeg_4')
    mc.joint(p=(legPosition[4][0], legPosition[4]
                [1], legPosition[4][2]), n='posLeg_5')

# Main function rig()

def rig():
    mc.select(clear=True)
    upLeg_L_jnt.extend(getPosition("posLeg_1"))
    lowLeg_L_jnt.extend(getPosition("posLeg_2"))
    ankle_L_jnt.extend(getPosition("posLeg_3"))
    ball_L_jnt.extend(getPosition("posLeg_4"))
    toe_L_jnt.extend(getPosition("posLeg_5"))

    createJoint(upLeg_L_jnt, "upLeg_L_jnt")
    createJoint(lowLeg_L_jnt, "lowLeg_L_jnt")
    createJoint(ankle_L_jnt, "ankle_L_jnt")
    createJoint(ball_L_jnt, "ball_L_jnt")
    createJoint(toe_L_jnt, "toe_L_jnt")

    makeAxis('upLeg_L_jnt')
    makeAxis('lowLeg_L_jnt')
    makeAxis('ankle_L_jnt')
    makeAxis('ball_L_jnt')
    makeAxis('toe_L_jnt')

    duplicateJnt('upLeg_L_jnt')

    mc.delete('posLeg_1')

    iKFkBiend('upLeg_Fk_L_jnt', 'upLeg_IK_L_jnt', 'upLeg_L_jnt')

    makeFkIkCtrl('legFkIk_L_ctrl', 'ankle_L_jnt')

    createNode('reverse', 'legFkIk_L_rev')

    legFkIkConnection('L')

    createCtrlFk(selectRelatives('legCtrlFk_L_grp'), 'L', 2.5, 0.90)

    doRigGrp('upLeg_L_jnt', 'legRig_L_grp', 'L', 'pelvis_C_jnt')

def getPosition(posJntName):
    position = []
    position.append(mc.xform(posJntName, t=True, q=True))
    print position
    return position

def createJoint(jnt, jntName):
    mc.joint(n=(jntName))
    mc.xform(str(jntName), t=(jnt[0][0], jnt[0][1], jnt[0][2]))

def makeAxis(jntName):
    mc.select(jntName)
    mc.joint(edit=True, zso=True, n=(jntName), oj='yxz', sao='xdown')
    mc.select(clear=True)
    print jntName + ' makeAxis Done'

def duplicateJnt(jntName):
    # select the chain
    mc.select(jntName)
    # duplicate the original chain
    dup = mc.duplicate(rc=True)
    selected = mc.select(dup)
    jntList = mc.ls(sl=True)
    for i in jntList:
        mc.rename(i, i[0:-6] + 'Fk' + '_L_jnt')

    # select the chain
    mc.select(jntName)
    # duplicate the original chain
    dup = mc.duplicate(rc=True)
    selected = mc.select(dup)
    jntList = mc.ls(sl=True)
    for i in jntList:
        mc.rename(i, i[0:-6] + 'IK' + '_L_jnt')

def iKFkBiend(fkJnt, ikJnt, mainJnt):
    fkJntList = []
    ikJntList = []
    mainJntList = []

    mc.select(fkJnt)
    children_joints = mc.listRelatives(allDescendents=True, type='joint')
    mc.select(children_joints, add=True)
    fkJntList = mc.ls(sl=True)
    # print fkJntList

    mc.select(ikJnt)
    children_joints = mc.listRelatives(allDescendents=True, type='joint')
    mc.select(children_joints, add=True)
    ikJntList = mc.ls(sl=True)
    # print ikJntList

    mc.select(mainJnt)
    children_joints = mc.listRelatives(allDescendents=True, type='joint')
    mc.select(children_joints, add=True)
    mainJntList = mc.ls(sl=True)
    # print mainJntList

    for i in range(0, len(mainJntList)):
        mc.parentConstraint(
            fkJntList[i], ikJntList[i], mainJntList[i], w=1, mo=True)
        print mainJntList[i], 'parentConstraint completed'

    mc.group(fkJnt, n='legCtrlFk_L_grp')
    mc.group(ikJnt, n='legCtrlIk_L_grp')

def makeFkIkCtrl(fkIkCtrlName, conObject):
    zGrpName = fkIkCtrlName[0:fkIkCtrlName.index('Fk')] + 'CtrlFkIk_L_zGrp'
    fkIkCtrl = mc.curve(p=[(0, 0, 0), (0, 0, -2), (-1, 0, -4),
                           (1, 0, -4), (0, 0, -2)], k=[0, 1, 2, 3, 4], d=1, n=fkIkCtrlName)
    mc.select(fkIkCtrlName)
    mc.group(n=zGrpName)
    mc.select(zGrpName)
    mc.move(0, 0, 0, zGrpName + '.scalePivot',
            zGrpName + '.rotatePivot', rpr=True)
    mc.addAttr(fkIkCtrlName, ln='FkIk', at="float", min=0, max=1.0, k=True)
    mc.pointConstraint(conObject, zGrpName)

def createNode(nodeType, nodeName):
    mc.createNode(nodeType, n=str(nodeName))

def legFkIkConnection(side):
    mc.connectAttr('legFkIk_' + side + '_ctrl.FkIk',
                   'legFkIk_' + side + '_rev.inputX')

    mc.connectAttr('legFkIk_' + side + '_ctrl.FkIk', 'toe_' +
                   side + '_jnt_parentConstraint1.toe_IK_' + side + '_jntW1')
    mc.connectAttr('legFkIk_' + side + '_ctrl.FkIk', 'upLeg_' +
                   side + '_jnt_parentConstraint1.upLeg_IK_' + side + '_jntW1')
    mc.connectAttr('legFkIk_' + side + '_ctrl.FkIk', 'lowLeg_' +
                   side + '_jnt_parentConstraint1.lowLeg_IK_' + side + '_jntW1')
    mc.connectAttr('legFkIk_' + side + '_ctrl.FkIk', 'ankle_' +
                   side + '_jnt_parentConstraint1.ankle_IK_' + side + '_jntW1')
    mc.connectAttr('legFkIk_' + side + '_ctrl.FkIk', 'ball_' +
                   side + '_jnt_parentConstraint1.ball_IK_' + side + '_jntW1')

    mc.connectAttr('legFkIk_' + side + '_rev.outputX', 'toe_' +
                   side + '_jnt_parentConstraint1.toe_Fk_' + side + '_jntW0')
    mc.connectAttr('legFkIk_' + side + '_rev.outputX', 'upLeg_' +
                   side + '_jnt_parentConstraint1.upLeg_Fk_' + side + '_jntW0')
    mc.connectAttr('legFkIk_' + side + '_rev.outputX', 'lowLeg_' +
                   side + '_jnt_parentConstraint1.lowLeg_Fk_' + side + '_jntW0')
    mc.connectAttr('legFkIk_' + side + '_rev.outputX', 'ankle_' +
                   side + '_jnt_parentConstraint1.ankle_Fk_' + side + '_jntW0')
    mc.connectAttr('legFkIk_' + side + '_rev.outputX', 'ball_' +
                   side + '_jnt_parentConstraint1.ball_Fk_' + side + '_jntW0')

    mc.connectAttr('legFkIk_' + side + '_rev.outputX',
                   'legCtrlFk_' + side + '_grp.visibility')
    mc.connectAttr('legFkIk_' + side + '_ctrl.FkIk',
                   'legCtrlIk_' + side + '_grp.visibility')

def selectRelatives(ctrlFkGrp):
    mc.select(ctrlFkGrp)
    jntList = mc.listRelatives(ctrlFkGrp, ad=True)
    return jntList

def createCtrlFk(relativesJntList, side, ctrlRadius, DecreaseCtrlPercent):
    relativesJntListNum = len(relativesJntList)
    zGrpNameList = []
    zGrpNameNumList = []
    ctrlNameList = []
    for i in range(relativesJntListNum-1, 0, -1):
        if i == 0:
            pass
        else:
            print relativesJntList[i]
            ctrlName = relativesJntList[i][0:relativesJntList[i].index(
                '_')] + 'Fk_' + side + '_Ctrl'
            zGrpName = relativesJntList[i][0:relativesJntList[i].index(
                '_')] + 'CtrlFk_' + side + '_zGrp'
            mc.group(em=True, name=zGrpName)
            mc.circle(nr=(0, 1, 0), c=(0, 0, 0), r=ctrlRadius, n=ctrlName)
            mc.parent(ctrlName, zGrpName)
            mc.parentConstraint(relativesJntList[i], zGrpName, mo=False)
            mc.delete(zGrpName + '_parentConstraint1')
            zGrpNameList.append(zGrpName)
            ctrlNameList.append(ctrlName)
            ctrlRadius = ctrlRadius*DecreaseCtrlPercent
            print 'createCtrl ' + ctrlName
    print relativesJntListNum
    print zGrpNameList[0]
    for i in range(relativesJntListNum-2, 0, -1):
        mc.parent(zGrpNameList[i], ctrlNameList[i-1])
    for i in range(len(ctrlNameList)):
        print 'ctrlNameList', ctrlNameList
        mc.parentConstraint(ctrlNameList[i], ctrlNameList[i][0:ctrlNameList[i].index('Fk')] + '_Fk_' + side + '_jnt')
    mc.parent(zGrpNameList[0], 'legCtrlFk_L_grp')

def doRigGrp(mainJntName, rigGrpName, side, parentJnt):
    mc.group(em=True, name=rigGrpName)
    mc.parentConstraint(parentJnt, rigGrpName, mo=False)

    fKGrpName = rigGrpName[0:rigGrpName.index(
        'Rig')] + 'CtrlFk_' + side + '_grp'
    iKGrpName = rigGrpName[0:rigGrpName.index(
        'Rig')] + 'CtrlIk_' + side + '_grp'
    fkikGrpName = rigGrpName[0:rigGrpName.index(
        'Rig')] + 'CtrlFkIk_' + side + '_zGrp'

    mc.parent(fKGrpName, rigGrpName)
    mc.parent(iKGrpName, rigGrpName)
    mc.parent(fkikGrpName, rigGrpName)
    mc.parent(mainJntName, parentJnt)
