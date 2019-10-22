import classModules.objClass as cl
import maya.cmds as mc 
import functionModules.generalRig as gn
import functionModules.fkRig as fk
import functionModules.ikRig as ik

def makeAxis(jntName):
    mc.select(jntName)
    mc.joint(edit=True, zso=True, n=(jntName), oj='yxz', sao='xdown')
    # mc.select(clear=True)
    print jntName + ' makeAxis Done'

# createPosJnt and return list of posJntNameList, footInPiv, footOutPiv, heelPiv dict
def createLegPosJnt(side = str):
    posJntName = []
    posJntList = []
    posLft = [[2,15,0], [4, 13, 0], [4, 6, 1], [4, 1, 0], [4, 0, 2], [4, 0, 3], [3, 0, 2], [5, 0, 2], [4, 0, -1]]
    posRgt = [[-2,15,0], [-4, 13, 0], [-4, 6, 1], [-4, 1, 0], [-4, 0, 2], [-4, 0, 3], [-3, 0, 2], [-5, 0, 2], [-4, 0, -1]]
    footInPosPiv = tuple
    footOutPosPiv = tuple
    heelPosPiv = tuple

    if side.upper() == 'LFT':
        posJntList = posLft
        print 'posJntList', posJntList
    elif side.upper() == 'RGT':
        posJntList = posRgt
        print 'posJntList', posJntList

    # create each posJntName
    for i in range(1, 10):
        posJntAmp = 'posJnt' + str(i) + '_' + side + '_jnt'
        posJntName.append(posJntAmp)
    
    for i in range(0, len(posJntName)):
        print i

    # create posJnt in maya
    posJnt1 = cl.Joint(posJntName[0])
    posJnt1.setT(posJntList[0][0], posJntList[0][1], posJntList[0][2])
    # posJnt1.setRz(180)
    mc.select(cl = True)

    posJnt2 = cl.Joint(posJntName[1])
    posJnt2.setT(posJntList[1][0], posJntList[1][1], posJntList[1][2])
    mc.select(cl = True)

    posJnt3 = cl.Joint(posJntName[2])
    posJnt3.setT(posJntList[2][0], posJntList[2][1], posJntList[2][2])
    mc.select(cl = True)

    posJnt4 = cl.Joint(posJntName[3])
    posJnt4.setT(posJntList[3][0], posJntList[3][1], posJntList[3][2])
    mc.select(cl = True)

    posJnt5 = cl.Joint(posJntName[4])
    posJnt5.setT(posJntList[4][0], posJntList[4][1], posJntList[4][2])
    mc.select(cl = True)

    posJnt6 = cl.Joint(posJntName[5])
    posJnt6.setT(posJntList[5][0], posJntList[5][1], posJntList[5][2])
    mc.select(cl = True)

    # footOutPosPiv
    posJnt7 = cl.Joint(posJntName[6])
    posJnt7.setT(posJntList[6][0], posJntList[6][1], posJntList[6][2])
    footInPosPiv = posJnt7.getT()
    mc.select(cl = True)

    # footInPosPiv
    posJnt8 = cl.Joint(posJntName[7])
    posJnt8.setT(posJntList[7][0], posJntList[7][1], posJntList[7][2])
    footOutPosPiv = posJnt8.getT()
    mc.select(cl = True)

    # heelPosPiv
    posJnt9 = cl.Joint(posJntName[8])
    posJnt9.setT(posJntList[8][0], posJntList[8][1], posJntList[8][2])
    heelPosPiv = posJnt9.getT()
    mc.select(cl = True)

    # parent posJnt
    mc.parent([posJnt8, posJnt7], posJnt5)
    mc.parent(posJnt9, posJnt4)
    for i in range(5, -1, -1):
        if i > 0:
            mc.parent(posJntName[i], posJntName[i-1])

    mc.select(posJnt1)

    # return only jnt that we will useing
    return posJntName


#! --- end of create posJnt ----


# createMainJnt
def createMainJnt(side = str):

    def duplicateFkIkJnt(mainJntList = list, side = str):
        fkJntName = []
        ikJntName = []
        for jnt in mainJntList:

            if mc.listRelatives (jnt, p = True) != None:
                mc.parent(jnt, world = True)
            
            # dup FK jnt
            dupAmpFkJnt = mc.duplicate(jnt)[0]
            nameFk = dupAmpFkJnt.split('_')[0] + '_fk'
            fkJntName.append(mc.rename(dupAmpFkJnt, nameFk + side + '_jnt'))

            # dup iK jnt
            dupAmpikJnt = mc.duplicate(jnt)[0]
            nameik = dupAmpikJnt.split('_')[0] + '_ik'
            ikJntName.append(mc.rename(dupAmpikJnt, nameik + side + '_jnt'))

        for i in range(len(mainJntList)-1, -1, -1):
            # parent every Jnt
            if i > 0:
                mc.parent(mainJntList[i], mainJntList[i-1])
                mc.parent(fkJntName[i], fkJntName[i-1])
                mc.parent(ikJntName[i], ikJntName[i-1])

            # delete history and FT all jnt
            mc.makeIdentity(mainJntList[i], apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
            mc.delete(mainJntList[i], ch = 1)

            mc.makeIdentity(fkJntName[i], apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
            mc.delete(fkJntName[i], ch = 1)

            mc.makeIdentity(ikJntName[i], apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
            mc.delete(ikJntName[i], ch = 1)

        mc.select(cl = True)
            
        return fkJntName, ikJntName
            
    hipJntRotate = []
    hipLft = 180
    hipRGT = 180
    #! mainJnt end at index 5 or posJnt6
    posJntNameList = []
    # find posJnt Name
    for i in range(1, 10):
        posJntAmp = 'posJnt' + str(i) + '_' + side + '_jnt'
        posJntNameList.append(posJntAmp)

    mainJntNameList = []
    jntName = ['hip', 'upLeg', 'lowLeg', 'ankle', 'ball', 'toe']
    # find mainJnt Name
    for i in range(0, len(jntName)):
        mainJntAmp = jntName[i] + '_' + side + '_jnt'
        mainJntNameList.append(mainJntAmp)

    posJnt = []
    # create posJnt object
    for i in range(0, len(posJntNameList)):
        # create posJnt object
        posJnt.append(cl.Joint(posJntNameList[i]))
        # if joint has no parent, parent it to world 
        if posJnt[i].findRel() != None:
            mc.parent(posJnt[i], world = True)

    #! foot piv
    footInPosPiv = posJnt[6].getT()
    footOutPosPiv = posJnt[7].getT()
    heelPosPiv = posJnt[8].getT()

    # todo create mainJnt and fkikCtrl

    if side.upper() == 'LFT':

        mc.select(cl = True)
        hipJnt = cl.Joint(mainJntNameList[0])
        hipJnt.setT(posJnt[0].getTx(), posJnt[0].getTy(), posJnt[0].getTz())
        hipJnt.setRz(180)    
        mc.select(cl = True)

        upLegJnt = cl.Joint(mainJntNameList[1])
        upLegJnt.setT(posJnt[1].getTx(), posJnt[1].getTy(), posJnt[1].getTz())
        mc.select(cl = True)

        lowLegJnt = cl.Joint(mainJntNameList[2])
        lowLegJnt.setT(posJnt[2].getTx(), posJnt[2].getTy(), posJnt[2].getTz())
        mc.select(cl = True)

        ankleJnt = cl.Joint(mainJntNameList[3])
        ankleJnt.setT(posJnt[3].getTx(), posJnt[3].getTy(), posJnt[3].getTz())
        mc.select(cl = True)

        ballJnt = cl.Joint(mainJntNameList[4])
        ballJnt.setT(posJnt[4].getTx(), posJnt[4].getTy(), posJnt[4].getTz())
        ballJnt.setR(90, 0, 180)
        mc.select(cl = True)

        toeJnt = cl.Joint(mainJntNameList[5])
        toeJnt.setT(posJnt[5].getTx(), posJnt[5].getTy(), posJnt[5].getTz())
        toeJnt.setR(90, 0, 180)
        mc.select(cl = True)

        mc.parent(lowLegJnt, upLegJnt)
        mc.parent(ankleJnt, lowLegJnt)
        makeAxis(upLegJnt.getName())
        makeAxis(lowLegJnt.getName())
        mc.parent(lowLegJnt, world = True)
        mc.parent(ankleJnt, world = True)
        ankleJnt.setR(90, 0, 180)

        # duplicate mainJnt to fk and ik Jnt
        fkIkJntList = duplicateFkIkJnt(mainJntNameList, side)
        fkJntList = fkIkJntList[0]
        ikJntList = fkIkJntList[1]
        

    elif side.upper() == 'RGT':
        mc.select(cl = True)
        hipJnt = cl.Joint(mainJntNameList[0])
        hipJnt.setT(posJnt[0].getTx(), posJnt[0].getTy(), posJnt[0].getTz())
        hipJnt.setRz(180)    
        hipJnt.setRx(180)    
        mc.select(cl = True)

        upLegJnt = cl.Joint(mainJntNameList[1])
        upLegJnt.setT(posJnt[1].getTx(), posJnt[1].getTy(), posJnt[1].getTz())
        mc.select(cl = True)

        lowLegJnt = cl.Joint(mainJntNameList[2])
        lowLegJnt.setT(posJnt[2].getTx(), posJnt[2].getTy(), posJnt[2].getTz())
        mc.select(cl = True)

        ankleJnt = cl.Joint(mainJntNameList[3])
        ankleJnt.setT(posJnt[3].getTx(), posJnt[3].getTy(), posJnt[3].getTz())
        mc.select(cl = True)

        ballJnt = cl.Joint(mainJntNameList[4])
        ballJnt.setT(posJnt[4].getTx(), posJnt[4].getTy(), posJnt[4].getTz())
        ballJnt.setR(270, 0, 180)
        mc.select(cl = True)

        toeJnt = cl.Joint(mainJntNameList[5])
        toeJnt.setT(posJnt[5].getTx(), posJnt[5].getTy(), posJnt[5].getTz())
        toeJnt.setR(270, 0, 180)
        mc.select(cl = True)

        mc.parent(lowLegJnt, upLegJnt)
        mc.parent(ankleJnt, lowLegJnt)
        makeAxis(upLegJnt.getName())
        makeAxis(lowLegJnt.getName())
        mc.parent(lowLegJnt, world = True)
        mc.parent(ankleJnt, world = True)
        upLegJnt.setRx(180)
        lowLegJnt.setRx(180)
        ankleJnt.setR(270, 0, 180)
        
        # duplicate mainJnt to fk and ik Jnt
        fkIkJntList = duplicateFkIkJnt(mainJntNameList, side)
        fkJntList = fkIkJntList[0]
        ikJntList = fkIkJntList[1]
    
    
    # delete posJnt
    map(lambda jnt: jnt.delete(), posJnt)

    footPiv = {
        'footInPosPiv' : footInPosPiv,
        'footOutPosPiv' :footOutPosPiv,
        'heelPosPiv' : heelPosPiv
    }

    return [mainJntNameList, fkJntList, ikJntList, footPiv]

def legRig(side = str, pivotJnt = str, radius = float):
    createMainJntReturned = createMainJnt(side)
    # index 0 -> mainJntNameList
    mainJntNameList = createMainJntReturned[0]
    # index 1 -> fkJntList
    fkJntList = createMainJntReturned[1]
    # index 2 -> ikJntList
    ikJntList = createMainJntReturned[2]
    # index 3 -> footPivList
    footPivList = createMainJntReturned[3]

    # create fkIkCtrl
    fkikCtrl = cl.Ctrl('leg_' + side + '_ctrl', 'stick')
    fkikCtrl.setRx(-90)
    # get world translate of ankleJnt
    ankleJntPos = mc.xform(mainJntNameList[3], t=True, q=True, ws = True)
    # set ankleJntPos to fkikCtrl
    fkikCtrl.setT(ankleJntPos[0], ankleJntPos[1], ankleJntPos[2])
    mc.parent(mainJntNameList[0], pivotJnt)

    # fkIkBlend
    fkIkBlendReturned = gn.fkIkBlend(fkikCtrl.getName(), pivotJnt, mainJntNameList, fkJntList, ikJntList)
    # rename zGrp 'hip' -> 'leg'
    fkIkAmpName = map(lambda zGrp: mc.rename(zGrp, zGrp.replace('hip', 'leg')), [fkIkBlendReturned[0], fkIkBlendReturned[1]])

    fkZGrpJntName = fkIkAmpName[0]
    ikZGrpJntName = fkIkAmpName[1]
    zGrpCtrlName = fkIkBlendReturned[2]

    # create rigGrp
    rigGrpName = gn.createRigGrp(pivotJnt, mainJntNameList[0])
    # put fkGrp and ikGrp to rigGrp
    mc.parent(fkZGrpJntName, rigGrpName)
    mc.parent(ikZGrpJntName, rigGrpName)
    mc.parent(zGrpCtrlName, rigGrpName)
    
    # rigFk start at upLegJnt
    # make upleg lowLeg ankle ball toe into upLegJntList
    upLegJntList = fkJntList[1:len(fkJntList)]
    # fk Rig
    upLegZGrpName = fk.legFk(upLegJntList, radius)
    # parent upLegZGrp to fkGrp
    mc.parent(upLegZGrpName, fkZGrpJntName)

    fk.fkSpaceing('anim_grp', upLegZGrpName, fkZGrpJntName, side)

    mc.select(cl = True)

    # ik Rig
    # maping Joint
    hipIkJnt = cl.Joint(ikJntList[0])
    upLegIkJnt = cl.Joint(ikJntList[1])
    upLowIkJnt = cl.Joint(ikJntList[2])
    ankleIkJnt = cl.Joint(ikJntList[3])
    ballIkJnt = cl.Joint(ikJntList[4])
    toeIkJnt = cl.Joint(ikJntList[5])

    # create ikCtrl
    upLegikCtrlName = cl.Ctrl(ik.nameingIkCtrl(upLegIkJnt.getName()), 'box')
    upLegikCtrlName.setS(3.3, 0.3, 3.3)
    gn.pointConOffMainTain(upLegikCtrlName.getName(), 'upLeg_ik' + side + '_jnt')

    lowLegikCtrlName = cl.Ctrl(ik.nameingIkCtrl(ankleIkJnt.getName()), 'box')
    lowLegikCtrlName.setS(3.3, 0.3, 3.3)
    gn.pointConOffMainTain(lowLegikCtrlName.getName(), 'ankle_ik' + side + '_jnt')
    
    gimblNameList = ik.createGmbl([upLegikCtrlName.getName(), lowLegikCtrlName.getName()], 3.3*0.70)

    gn.cleanObj(upLegikCtrlName.getName())
    gn.cleanObj(lowLegikCtrlName.getName())
    gn.cleanObj(gimblNameList[0])
    gn.cleanObj(gimblNameList[1])
    upLegikCtrlZroName = gn.zeroGroup(upLegikCtrlName.getName(), upLegikCtrlName.getName())
    lowLegikCtrlZroName = gn.zeroGroup(lowLegikCtrlName.getName(), lowLegikCtrlName.getName())

    mc.parent(upLegikCtrlZroName, ikZGrpJntName)
    mc.parent(lowLegikCtrlZroName, ikZGrpJntName, )

    # create ikh
    upLegIkName = ik.createIkhIk(upLegIkJnt.getName(), ankleIkJnt.getName(), gn.nameingIkh(upLegIkJnt.getName()), 'ikRPsolver')
    ankleIkName = ik.createIkhIk(ankleIkJnt.getName(), ballIkJnt.getName(), gn.nameingIkh(ballIkJnt.getName()), 'ikSCsolver')
    toeIkName = ik.createIkhIk(ballIkJnt.getName(), toeIkJnt.getName(), gn.nameingIkh(toeIkJnt.getName()), 'ikSCsolver')

    upLegIkZroName =  gn.zeroGroup(upLegIkName, upLegIkName)
    ankleIkZroName =  gn.zeroGroup(ankleIkName, ankleIkName)
    toeIkZroName =  gn.zeroGroup(toeIkName, toeIkName)

    # create ikhGrp
    ikhGrpNameAmpList = ['leg_ikhPiv#_grp', 'toe_ikhPiv#_grp', 'heel_ikhPiv#_grp', 'footIn_ikhPiv#_grp', 'footOut_ikhPiv#_grp', 'ballRoll_ikhPiv#_grp', 'toeBlend_ikhPiv#_grp']
    ikhGrpNameList = []
    
    for i in range(0, len(ikhGrpNameAmpList)):
        ikhName = mc.group(em = True, n = ikhGrpNameAmpList[i].replace('#', side))
        if side == 'LFT':
            mc.setAttr(ikhName + '.rx', 90)
            mc.setAttr(ikhName + '.rz', -180)
        if side == 'RGT':
            mc.setAttr(ikhName + '.rx', -90)
        ikhGrpNameList.append(ikhName)
    
    # set all ikhGrp.T
    gn.parentConOffMainTain(ikhGrpNameList[0], 'ankle_ik' + side + '_jnt')
    gn.parentConOffMainTain(ikhGrpNameList[1], 'toe_ik' + side + '_jnt')
    mc.setAttr(ikhGrpNameList[2] + '.t', footPivList['heelPosPiv'][0], footPivList['heelPosPiv'][1], footPivList['heelPosPiv'][2])
    mc.setAttr(ikhGrpNameList[3] + '.t', footPivList['footInPosPiv'][0], footPivList['footInPosPiv'][1], footPivList['footInPosPiv'][2])
    mc.setAttr(ikhGrpNameList[4] + '.t', footPivList['footOutPosPiv'][0], footPivList['footOutPosPiv'][1], footPivList['footOutPosPiv'][2])
    gn.parentConOffMainTain(ikhGrpNameList[5], 'ball_ik' + side + '_jnt')
    gn.parentConOffMainTain(ikhGrpNameList[6], 'toe_ik' + side + '_jnt')

    mc.parent(upLegIkZroName, ikhGrpNameList[5])
    mc.parent(ankleIkZroName, ikhGrpNameList[5])
    mc.parent(toeIkZroName, ikhGrpNameList[6])
    mc.parent(ikhGrpNameList[0], gimblNameList[1])
    mc.pointConstraint(gimblNameList[0], upLegIkJnt.getName())

    # parent all ikhGrp
    for i in range(0, len(ikhGrpNameList)):
        if i == len(ikhGrpNameList)-2:
            mc.parent(ikhGrpNameList[i+1], ikhGrpNameList[i-1])
            break
        mc.parent(ikhGrpNameList[i+1], ikhGrpNameList[i])

    ik.addAttrLegCtrlIk(fkikCtrl.getName())
    ik.legIkAttrConnection(lowLegikCtrlName.getName(), side)
    

createLegPosJnt('LFT')
legRig('LFT', 'pelvis_CNT_jnt', 2)