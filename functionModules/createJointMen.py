import maya.cmds as mc

allListJoint = []
allListJointZeroGroup = []

bodyListJoint = []
legListJoint = []
legRListJoint = []
handListJoint = []
handRListJoint = []
middleFingerListJoint = []
indexFingerList = []
thumbListJoint = []
pelvisListJoint = []

jointNameList = []
allObjectList = []

bodyPosition = [
    [0.0, 9.66, 1.55067301221834e-08],
    [0.0, 9.776872260388057, 1.55067301221834e-08],
    [0.0, 12.021614623815573, 1.55067301221834e-08],
    [0.0, 14.500078006699566, 1.55067301221834e-08],
    [2.449310281756816e-32, 16.05142763774015, 0.0],
    [2.449310281756816e-32, 19.11067370383484, 0.0]
]

pelvisPosition = [
    [0.0, 9.55, 1.55067301221834e-08],
]

legPosition = [
    [0.8999999761581421, 8.93725872039795, 1.6670938407514768e-07],
    [0.8999999761581421, 5.082729195445287, 0.3260868489742279],
    [0.8999999761581421, 1.0029856157909955, -0.03706564009189606],
    [0.8999999761581421, 0.23651546239852905, 1.4054166078567505],
    [0.9068282005372641, 0.1441195495991089, 2.1694516265006833],
]

handPosition = [
    [1.1970683336257935, 15.82430648803711, -5.201671871013502e-10],
    [4.737703222731867, 15.82430648803711, 1.2478963418161015e-09],
    [8.161396980285645, 15.824305534362793, 0.6032961010932922],
    [8.624753813263801, 15.824305534362793, 0.6032961010932922],
]

middleFinger = [
    [9.13911247253418, 15.880372047424316, 0.6095081567764282],
    [9.659500122070312, 15.8983736038208, 0.7008184790611267],
    [10.137022972106934, 15.910866737365723, 0.7852953672409058],
]

indexFinger = [
    [9.040735244750977, 15.880426406860352, 1.167433261871338],
    [9.575387954711914, 15.89799690246582, 1.2618736028671265],
    [10.0661039352417, 15.912100791931152, 1.3486303091049194],
]

thumb = [
    [8.571440696716309, 15.76047420501709, 1.2893385887145996],
    [8.733711242675781, 15.590843200683594, 1.6130642890930176],
    [8.882830619812012, 15.432160377502441, 1.9083538055419922]
]

# for i in range(0, len(bodyPosition)):
#     if i == 0:
#         bodyListJoint.append(mc.joint(p=(bodyPosition[i][0], bodyPosition[i][1], bodyPosition[i][2]), n=('root_C_jnt')))
#     else:
#         bodyListJoint.append(mc.joint(p=(bodyPosition[i][0], bodyPosition[i][1], bodyPosition[i][2]),
#                                       n=('body' + str(i + 1) + '_C_jnt')))
# mc.select(clear=True)
#
# # for i in range(0, len(bodyPosition)):
# #     if i == 0:
# #         bodyListJoint.append(mc.joint(p=(bodyPosition[i][0], bodyPosition[i][1], bodyPosition[i][2]), n=('root_C_zGrp')))
# #     else:
# #         bodyListJoint.append(mc.joint(p=(bodyPosition[i][0], bodyPosition[i][1], bodyPosition[i][2]), n=('body' + str(i+1) + '_C_zGrp')))
# # mc.select(clear=True)
#
#
# for i in range(0, len(legPosition)):
#     if i == 0:
#         legListJoint.append(mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n='upperLeg_L_jnt'))
#     elif len(legPosition) - 4 == i:
#         legListJoint.append(mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n='lowerLeg_L_jnt'))
#     elif len(legPosition) - 3 == i:
#         legListJoint.append(
#             mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n=('foot' + str(i + 1) + '_L_jnt')))
#     elif len(legPosition) - 2 == i:
#         legListJoint.append(mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]),
#                                      n=('midFoot' + str(i + 1) + '_L_jnt')))
#     elif len(legPosition) - 1 == i:
#         legListJoint.append(
#             mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n=('toe' + str(i + 1) + '_L_jnt')))
#     else:
#         legListJoint.append(
#             mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n=('leg' + str(i) + '_L_jnt')))
# mc.select(clear=True)
#
# for i in range(0, len(handPosition)):
#     handListJoint.append(
#         mc.joint(p=(handPosition[i][0], handPosition[i][1], handPosition[i][2]), n=('hand' + str(i + 1) + '_L_jnt')))
# mc.select(clear=True)
#
# for i in range(0, len(middleFinger)):
#     middleFingerListJoint.append(mc.joint(p=(middleFinger[i][0], middleFinger[i][1], middleFinger[i][2]),
#                                           n=('middleFinger' + str(i + 1) + '_L_jnt')))
# mc.select(clear=True)
#
# for i in range(0, len(indexFinger)):
#     indexFingerList.append(mc.joint(p=(indexFinger[i][0], indexFinger[i][1], indexFinger[i][2]),
#                                     n=('indexFinger' + str(i + 1) + '_L_jnt')))
# mc.select(clear=True)
#
# for i in range(0, len(thumb)):
#     thumbListJoint.append(mc.joint(p=(thumb[i][0], thumb[i][1], thumb[i][2]), n=('thumb' + str(i + 1) + '_L_jnt')))
# mc.select(clear=True)
#
# mc.parent('middleFinger1_L_jnt', handListJoint[-1])
# mc.parent('indexFinger1_L_jnt', handListJoint[-1])
# mc.parent('thumb1_L_jnt', handListJoint[-1])
# mc.parent(handListJoint[0], 'body3_C_jnt')
# mc.parent('upperLeg_L_jnt', 'root_C_jnt')
#
# mc.mirrorJoint(handListJoint[0], mirrorYZ=True, searchReplace=("L", "R"))
# mc.mirrorJoint('upperLeg_L_jnt', mirrorYZ=True, searchReplace=("L", "R"))
#
# mc.select(clear=True)
#
# allObjectList.extend(mc.ls(dag=True))
#
# # stored joint name in list
# for i in range(0, len(allObjectList)):
#     if mc.objectType(allObjectList[i]) == 'joint':
#         jointNameList.append(allObjectList[i])
#
# # create zGrp parentCon joint to the zGrp and delete it
# for i in range(0, len(jointNameList) - 1):
#     zGrpName = jointNameList[i].replace("jnt", "zGrp")
#     mc.group(em=True, n=zGrpName)
#     mc.parentConstraint(jointNameList[i], zGrpName, w=1)


# ui
# Start with the Window
mc.window(title="Auto Rigging")

# Add a single column layout to add controls into
mc.columnLayout(columnAttach=('both', 10), rowSpacing=20, columnWidth=250)

# Add controls to the Layout
mc.button(label="create position joint", command="createPositionJoint()")
mc.button(label="create zGrp", command="createZeroGrp()")

# Display the window
mc.showWindow()


def createPositionJoint():
    for i in range(0, len(bodyPosition)):
        if i == 0:
            bodyListJoint.append(
                mc.joint(p=(bodyPosition[i][0], bodyPosition[i][1], bodyPosition[i][2]), n=('root_C_jnt')))
        else:
            bodyListJoint.append(mc.joint(p=(bodyPosition[i][0], bodyPosition[i][1], bodyPosition[i][2]),
                                          n=('body' + str(i) + '_C_jnt')))
    mc.select(clear=True)

    for i in range(0, len(pelvisPosition)):
        pelvisListJoint.append(
            mc.joint(p=(pelvisPosition[i][0], pelvisPosition[i][1], pelvisPosition[i][2]), n=('pelvis_C_jnt')))
    mc.select(clear=True)

    for i in range(0, len(legPosition)):
        if i == 0:
            legListJoint.append(mc.joint(
                p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n='upperLeg_L_jnt'))
        elif len(legPosition) - 4 == i:
            legListJoint.append(mc.joint(
                p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n='lowerLeg_L_jnt'))
        elif len(legPosition) - 3 == i:
            legListJoint.append(
                mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n=('foot' + str(i + 1) + '_L_jnt')))
        elif len(legPosition) - 2 == i:
            legListJoint.append(mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]),
                                         n=('midFoot' + str(i + 1) + '_L_jnt')))
        elif len(legPosition) - 1 == i:
            legListJoint.append(
                mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n=('toe' + str(i + 1) + '_L_jnt')))
        else:
            legListJoint.append(
                mc.joint(p=(legPosition[i][0], legPosition[i][1], legPosition[i][2]), n=('leg' + str(i) + '_L_jnt')))
    mc.select(clear=True)

    for i in range(0, len(handPosition)):
        handListJoint.append(
            mc.joint(p=(handPosition[i][0], handPosition[i][1], handPosition[i][2]), n=('hand' + str(i + 1) + '_L_jnt')))
    mc.select(clear=True)

    for i in range(0, len(middleFinger)):
        middleFingerListJoint.append(mc.joint(p=(middleFinger[i][0], middleFinger[i][1], middleFinger[i][2]),
                                              n=('middleFinger' + str(i + 1) + '_L_jnt')))
    mc.select(clear=True)

    for i in range(0, len(indexFinger)):
        indexFingerList.append(mc.joint(p=(indexFinger[i][0], indexFinger[i][1], indexFinger[i][2]),
                                        n=('indexFinger' + str(i + 1) + '_L_jnt')))
    mc.select(clear=True)

    for i in range(0, len(thumb)):
        thumbListJoint.append(mc.joint(
            p=(thumb[i][0], thumb[i][1], thumb[i][2]), n=('thumb' + str(i + 1) + '_L_jnt')))
    mc.select(clear=True)

    mc.parent('middleFinger1_L_jnt', handListJoint[-1])
    mc.parent('indexFinger1_L_jnt', handListJoint[-1])
    mc.parent('thumb1_L_jnt', handListJoint[-1])
    mc.parent(handListJoint[0], 'body3_C_jnt')
    mc.parent('upperLeg_L_jnt', 'pelvis_C_jnt')
    mc.parent('pelvis_C_jnt', 'root_C_jnt')

    allListJoint.extend(bodyListJoint)
    allListJoint.extend(legListJoint)
    allListJoint.extend(handListJoint)
    allListJoint.extend(middleFingerListJoint)
    allListJoint.extend(indexFingerList)
    allListJoint.extend(thumbListJoint)

    for i in range(0, len(allListJoint)):
        print i
        makeAxis(allListJoint[i])

    mc.mirrorJoint(handListJoint[0], mirrorYZ=True, mb=True, searchReplace=("L", "R"))
    mc.mirrorJoint('upperLeg_L_jnt', mirrorYZ=True, mb=True, searchReplace=("L", "R"))

    mc.select(clear=True)

    allObjectList.extend(mc.ls(dag=True))

    # stored joint name in list
    for i in range(0, len(allObjectList)):
        if mc.objectType(allObjectList[i]) == 'joint':
            jointNameList.append(allObjectList[i])


def createZeroGrp():
    # create zGrp parentCon joint to the zGrp and delete it
    handListJoint.extend(middleFingerListJoint)
    handListJoint.extend(indexFingerList)
    handListJoint.extend(thumbListJoint)

    for i in range(0, len(handListJoint)):
        handRListJoint.append(handListJoint[i].replace("L", "R"))

    for i in range(0, len(handListJoint) - 1):
        zGrpName = handListJoint[i].replace("jnt", "zGrp")
        zGrpNameR = zGrpName.replace("L", "R")
        # mc.circle(n = 'C_ctrl')
        mc.group(em=True, n=zGrpName)
        mc.group(em=True, n=zGrpNameR)
        mc.parentConstraint(handListJoint[i], zGrpName, w=1)
        mc.parentConstraint(handListJoint[i], mc.circle(n='C_ctrl'), w=1)
        mc.parentConstraint(handRListJoint[i], zGrpNameR, w=1)

    for i in range(0, len(legListJoint)):
        legRListJoint.append(legListJoint[i].replace("L", "R"))

    for i in range(0, len(legListJoint)):
        zGrpName = legListJoint[i].replace("jnt", "zGrp")
        zGrpNameR = zGrpName.replace("L", "R")
        # mc.group(em=True, n=zGrpName)
        # mc.group(em=True, n=zGrpNameR)
        if i == 0:
            mc.group(em=True, n=zGrpName)
            mc.group(em=True, n=zGrpNameR)
            mc.parentConstraint(legListJoint[i], zGrpName, w=1)
            mc.parentConstraint(legRListJoint[i], zGrpNameR, w=1)
        elif i == len(legListJoint)-1 or i == len(legListJoint)-2 or i == len(legListJoint)-3:
            mc.group(em=True, n=zGrpName)
            mc.group(em=True, n=zGrpNameR)
            mc.parentConstraint(legListJoint[i], zGrpName, w=1)
            mc.parentConstraint(legRListJoint[i], zGrpNameR, w=1)
            print legListJoint
    for i in range(0, len(bodyListJoint)):
        zGrpName = bodyListJoint[i].replace("jnt", "zGrp")
        if i == 0:
            mc.group(em=True, n=zGrpName)
            mc.parentConstraint(bodyListJoint[i], zGrpName, w=1)
        elif i == len(legListJoint)-2 or i == len(legListJoint)-3:
            mc.group(em=True, n=zGrpName)
            mc.parentConstraint(bodyListJoint[i], zGrpName, w=1)

def makeAxis(jntName):
    mc.select(jntName)
    mc.joint(edit=True, zso=True, n=(jntName), oj='yxz', sao='xdown')
    mc.select(clear=True)
    print jntName + ' makeAxis Done'

# allListJoint.extend(bodyListJoint)
# allListJoint.extend(legListJoint)
# allListJoint.extend(handListJoint)
# allListJoint.extend(middleFingerListJoint)
# allListJoint.extend(indexFingerList)
# allListJoint.extend(thumbListJoint)

# for i in range(0, len(allObjectList)):
#         makeAxis(allObjectList[i])