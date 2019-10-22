import maya.cmds as mc


def createFkZeroGrp(Gmbl=False, side=''):
    # Gmbl = True
    def createGmbl():
        mc.circle(nr=(0, 1, 0), c=(0, 0, 0),
                  r=ctrlRadius*0.65, n=gmblCtrlName)
        mc.group(em=True, n=str(zGrpName))
        zGrpCon = mc.parentConstraint(sel, zGrpName, mo=False)
        gmblCtrlCon = mc.parentConstraint(sel, gmblCtrlName, mo=False)
        mc.delete(zGrpCon)
        mc.delete(gmblCtrlCon)
        mc.parent(sel, zGrpName)
        mc.parent(gmblCtrlName, sel)

    # Gmbl = False
    def createWithOutGmbl():
        mc.group(em=True, n=str(zGrpName))
        zGrpCon = mc.parentConstraint(sel, zGrpName, mo=False)
        mc.delete(zGrpCon)
        mc.parent(sel, zGrpName)

    sel = mc.ls(sl=True)
    ctrlRadius = mc.circle(sel[0], q=True, r=True)

    # side = ''
    if side == '':
        zGrpName = sel[0][0:sel[0].index('_')] + '_fkCtrlZro_grp'
        if Gmbl == True:
            gmblCtrlName = sel[0][0:sel[0].index('_')] + '_fkGmbl_ctrl'
            createGmbl()
            return
        createWithOutGmbl()
    # side != ''
    else:
        zGrpName = sel[0][0:sel[0].index('_')] + '_fkCtrlZro_' + side + '_grp'
        if Gmbl == True:
            gmblCtrlName = sel[0][0:sel[0].index(
                '_')] + '_Gmbl_' + side + '_ctrl'
            createGmbl()
            return
        createWithOutGmbl()


def createFkZeroGrp2(zGrpName=''):
    ctrl = mc.ls(sl=True)[0]
    mc.group(em=True, n=str(zGrpName))
    zGrpCon = mc.parentConstraint(ctrl, zGrpName, mo=False)
    mc.delete(zGrpCon)
    mc.parent(ctrl, zGrpName)
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

def createGmbl(gmblName):
    ctrl = mc.ls(sl=True)[0]
    ctrlRadius = mc.circle(ctrl, q=True, r=True)
    mc.circle(nr=(0, 1, 0), c=(0, 0, 0),r=ctrlRadius*0.65, n=gmblName)
    gmblCon = mc.parentConstraint(ctrl, gmblName, mo=False)
    mc.delete(gmblCon)
    mc.parent(gmblName, ctrl)

# gr.SquashFk('test1_SquashFk_Mult1', 'test1_SquashFk_add1')

    #createFkZeroGrp(Gmbl = True, side ='R')
    #createFkZeroGrp(Gmbl = False)

    # def createFkZeroGrp(Gmbl=False):

    #     sel = mc.ls(sl=True)
    #     print sel

    #     ctrlRadius = mc.circle(sel[0], q=True, r=True)
    #     if sel[0].find('_L_') or sel[0].find('_R_'):
    #         zGrpName = sel[0][0:sel[0].index('_')] + '_fkCtrlZro_grp'

    #         if Gmbl == True:
    #             gmblCtrlName = sel[0][0:sel[0].index('_')] + '_fkGmbl_ctrl'
    #             mc.circle(nr=(0, 1, 0), c=(0, 0, 0),
    #                       r=ctrlRadius*0.65, n=gmblCtrlName)
    #             mc.group(em=True, n=str(zGrpName))
    #             zGrpCon = mc.parentConstraint(sel, zGrpName, mo=False)
    #             gmblCtrlCon = mc.parentConstraint(sel, gmblCtrlName, mo=False)
    #             mc.delete(zGrpCon)
    #             mc.delete(gmblCtrlCon)
    #             mc.parent(sel, zGrpName)
    #             mc.parent(gmblCtrlName, sel)
    #             return
    #         print sel[0], Gmbl
    #         mc.group(em=True, n=str(zGrpName))
    #         zGrpCon = mc.parentConstraint(sel, zGrpName, mo=False)
    #         mc.delete(zGrpCon)
    #         mc.parent(sel, zGrpName)

    #     else:
    #         zGrpName = sel[0][0:sel[0].index('_')] + '_fkCtrlZro_' + side + '_grp'

    #         if Gmbl == True:
    #             gmblCtrlName = sel[0][0:sel[0].index(
    #                 '_')] + '_Gmbl_' + side + '_ctrl'
    #             mc.circle(nr=(0, 1, 0), c=(0, 0, 0),
    #                       r=ctrlRadius*0.65, n=gmblCtrlName)
    #             mc.group(em=True, n=str(zGrpName))
    #             zGrpCon = mc.parentConstraint(sel, zGrpName, mo=False)
    #             gmblCtrlCon = mc.parentConstraint(sel, gmblCtrlName, mo=False)
    #             mc.delete(zGrpCon)
    #             mc.delete(gmblCtrlCon)
    #             mc.parent(sel, zGrpName)
    #             mc.parent(gmblCtrlName, sel)
    #             return
    #         print sel[0], Gmbl
    #         mc.group(em=True, n=str(zGrpName))
    #         zGrpCon = mc.parentConstraint(sel, zGrpName, mo=False)
    #         mc.delete(zGrpCon)
    #         mc.parent(sel, zGrpName)
    #         def parent():
    #             mc.circle(nr=(0, 1, 0), c=(0, 0, 0),
    #                       r=ctrlRadius*0.65, n=gmblCtrlName)
    #             mc.group(em=True, n=str(zGrpName))
    #             zGrpCon = mc.parentConstraint(sel, zGrpName, mo=False)
    #             gmblCtrlCon = mc.parentConstraint(sel, gmblCtrlName, mo=False)
    #             mc.delete(zGrpCon)
    #             mc.delete(gmblCtrlCon)
    #             mc.parent(sel, zGrpName)
    #             mc.parent(gmblCtrlName, sel)
