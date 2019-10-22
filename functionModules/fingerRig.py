import fkRig as fkr
import generalRig as gn 
import maya.cmds as mc


# add attr to fkIk ctrl
    # mc.addAttr(ctrlFkIk, ln = 'fist',  at = "double", dv = 0, k = True)
    # mc.addAttr(ctrlFkIk, ln = 'cup',  at = "double", dv = 0, k = True)
    # mc.addAttr(ctrlFkIk, ln = 'spread',  at = "double", dv = 0, k = True)
    # mc.addAttr(ctrlFkIk, ln = 'baseSpread',  at = "double", dv = 0, k = True)

def fingerRig(jntName = '', wristJntName = '', ctrlFkIk = '', radius = 1, gmbl = True):

    def fingerFist(ctrlList = [] , rotGrp = [], ctrlFkIk = '', pmaList = []):
        ctrlFkIkShape = ctrlFkIk + 'Shape'
        print ctrlFkIk + 'Shape' + '-----------------'
        for i in range(0, len(ctrlList)):
            # nameing path
            name = ctrlList[i].split('_')[0]
            mdvName = name + '_fistAmp' + side + '_mdv'
            nameFistRx = name + 'FistRx' + side
            nameFistRy = name + 'FistRy' + side
            nameFistRz = name + 'FistRz' + side
            # addAttr to ctrlFkIkShape
            mc.addAttr(ctrlFkIkShape, ln = nameFistRx , at = "double", dv = -1, k = True)
            mc.addAttr(ctrlFkIkShape, ln = nameFistRy , at = "double", dv = -1, k = True)
            mc.addAttr(ctrlFkIkShape, ln = nameFistRz , at = "double", dv = -1, k = True)
            # create mdvNode
            mc.createNode('multiplyDivide', n = mdvName)
            # connect ctrlFkIk to nodeMdv
            mc.connectAttr(ctrlFkIk + '.fist',  mdvName + '.input1.input1X')
            mc.connectAttr(ctrlFkIk + '.fist',  mdvName + '.input1.input1Y')
            mc.connectAttr(ctrlFkIk + '.fist',  mdvName + '.input1.input1Z')
            # connect ctrlFkIkShape to nodeMdv
            mc.connectAttr(ctrlFkIkShape + '.' + nameFistRx, mdvName + '.input2.input2X')
            mc.connectAttr(ctrlFkIkShape + '.' + nameFistRy, mdvName + '.input2.input2Y')
            mc.connectAttr(ctrlFkIkShape + '.' + nameFistRz, mdvName + '.input2.input2Z')
            # connect mdvNode to pmaNode
            mc.connectAttr(mdvName + '.output', pmaList[i] + '.input3D[0]')

    def fingerCup(ctrlList = [], rotGrp = [], ctrlFkIk = [], pmaList = []):
        ctrlFkIkShape = ctrlFkIk + 'Shape'
        for i in range(0, len(ctrlList)):
            # nameing path
            name = ctrlList[i].split('_')[0]
            multName = name + '_cupAmp' + side + '_mult'
            nameCupRx = name + 'CupRx' + side
            # addAttr to ctrlFkIkShape
            mc.addAttr(ctrlFkIkShape, ln = nameCupRx , at = "double", dv = -1, k = True)
            # create multNode
            mc.createNode('multDoubleLinear', n = multName)
            # connect ctrlFkIk to multNode
            mc.connectAttr(ctrlFkIk + '.cup',  multName + '.input1')
            # connect ctrlFkIkShape to multNode
            mc.connectAttr(ctrlFkIkShape + '.' + nameCupRx,  multName + '.input2')
            # connect mdvNode to pmaNode
            mc.connectAttr(multName + '.output', pmaList[i] + '.input3D[1].input3Dx')

    def fingerSpread(ctrlList = [], rotGrp = [], ctrlFkIk = [], pmaList = []):
        # nameing path
        ctrlFkIkShape = ctrlFkIk + 'Shape'
        name = ctrlList[1].split('_')[0]
        multName = name + '_spreadAmp' + side + '_mult'
        nameSpreadRy = name + 'SpreadRx' + side
        # addAttr to ctrlFkIkShape
        mc.addAttr(ctrlFkIkShape, ln = nameSpreadRy , at = "double", dv = -1, k = True)
        # create multNode
        mc.createNode('multDoubleLinear', n = multName)
        # connect ctrlFkIk to multNode
        mc.connectAttr(ctrlFkIk + '.spread',  multName + '.input1')
        # connect ctrlFkIkShape to multNode
        mc.connectAttr(ctrlFkIkShape + '.' + nameSpreadRy,  multName + '.input2')
        # connect mdvNode to pmaNode
        mc.connectAttr(multName + '.output', pmaList[1] + '.input3D[2].input3Dz')

    def fingerBaseSpread(ctrlList = [], rotGrp = [], ctrlFkIk = [], pmaList = []):
        # nameing path
        ctrlFkIkShape = ctrlFkIk + 'Shape'
        name = ctrlList[0].split('_')[0]
        multName = name + '_BaseSpreadAmp' + side + '_mult'
        nameBaseSpreadRy = name + 'BaseSpreadRx' + side
        # addAttr to ctrlFkIkShape
        mc.addAttr(ctrlFkIkShape, ln = nameBaseSpreadRy , at = "double", dv = -1, k = True)
        # create multNode
        mc.createNode('multDoubleLinear', n = multName)
        # connect ctrlFkIk to multNode
        mc.connectAttr(ctrlFkIk + '.baseSpread',  multName + '.input1')
        # connect ctrlFkIkShape to multNode
        mc.connectAttr(ctrlFkIkShape + '.' + nameBaseSpreadRy,  multName + '.input2')
        # connect mdvNode to pmaNode
        mc.connectAttr(multName + '.output', pmaList[0] + '.input3D[3].input3Dz')

    # find jntList
    jntList = gn.findRel(jntName)
    # parent jnt to wristJnt
    mc.parent(jntList[0], wristJntName)
    # create posJnt
    fkr.createPosFkJnt(jntList[0])
    # create rigGrp
    side = jntList[0].split('_')[1]
    rigGrpName = jntName.split('_')[0][0:-1] + '_rig' + side + '_grp'
    mc.select(clear = True)
    mc.group(em = True , n = rigGrpName)
    mc.parentConstraint(wristJntName, rigGrpName, mo = False)
    # create Ctrl 
    ctrlList = fkr.createCtrlFk(jntList, radius, gmbl)
    firstZGrp =  mc.listRelatives (ctrlList[0],p = True)
    # create rotGrp
    if jntName.split('_')[1] == 'LFT':
        rotGrpList = gn.createRotGrp(ctrlList, ['LFTCtrlRot'])
    elif jntName.split('_')[1] == 'RGT':
        rotGrpList = gn.createRotGrp(ctrlList, ['RGTCtrlRot'])
    # parentConstraint ctrl to jnt 
    fkr.parentFk(jntList, ctrlList)
    # parent ctrlGrp to rigGrp
    mc.parent(firstZGrp, rigGrpName)
    # create node pma for each ctrl
    pmaList = list(map(lambda ctrl: mc.createNode('plusMinusAverage', n= ctrl.split('_')[0] + '_Amp' + side + '_pma'), ctrlList))

    # connect pmaNode to rotGrp
    for i in range(0, len(ctrlList)):
        mc.connectAttr(pmaList[i] + '.output3D', rotGrpList[i][0] + '.rotate')
    # fingerFist
    fingerFist(ctrlList = ctrlList, ctrlFkIk = ctrlFkIk, pmaList = pmaList)
    # fingerCup
    fingerCup(ctrlList = ctrlList, ctrlFkIk = ctrlFkIk, pmaList = pmaList)
    # fingerSpread
    fingerSpread(ctrlList = ctrlList, ctrlFkIk = ctrlFkIk, pmaList = pmaList)
    # fungerBaseSpread
    fingerBaseSpread(ctrlList = ctrlList, ctrlFkIk = ctrlFkIk, pmaList = pmaList)