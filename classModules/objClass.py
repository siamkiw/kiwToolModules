import maya.cmds as mc

class Obj:
    def __init__(self, name, side='', tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sX=0, sY=0, sZ=0, v = True):
        self.name = name
        self.side = side
        self.desc = self.name.split('_')[1]
        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.rx = rx
        self.ry = rz
        self.rz = rz
        self.sX = sX
        self.sY = sY
        self.sZ = sZ
        self.v = v

    def __str__(self):
        return self.name

    # name
    def setName(self, name=str):
        self.name = name
        mc.rename(self.name , name)
        return self.name

    def getName(self):
        return str(self.name)

    # desc
    def setDesc(self, desc=str):
        self.desc = desc
        nameAmp = self.name.split('_')[0] + '_' + desc + '_' + self.name.split('_')[2]
        mc.rename(self.name , nameAmp)
        self.name = nameAmp
        return self.desc

    def getDesc(self):
        return self.desc

    # side
    def setSide(self, side=str):
        self.side = side
        return self.side

    def getSide(self):
        return self.side

    # vis
    def setV(self, vis = bool):
        self.v = vis
        mc.setAttr(self.name + '.v', vis)
        return self.v

    def getV(self):
        return mc.getAttr(self.name + '.v')

    # Tx
    def setTx(self, tx=float):
        self.tx = tx
        mc.setAttr(self.name + '.tx', tx)
        return self.tx

    def getTx(self):
        return mc.getAttr(self.name + '.tx')

    # Ty
    def setTy(self, ty=float):
        self.ty = ty
        mc.setAttr(self.name + '.ty', ty)
        return self.ty

    def getTy(self):
        return mc.getAttr(self.name + '.ty')

    # Tz
    def setTz(self, tz=float):
        self.tz = tz
        mc.setAttr(self.name + '.tz', tz)
        return self.tz

    def getTz(self):
        return mc.getAttr(self.name + '.tz')

    #setT
    def setT(self, x, y, z):
        return (self.setTx(x), self.setTy(y), self.setTz(z))

    def getT(self):
        return [self.getTx(), self.getTy(), self.getTz()]
        
    # Rx
    def setRx(self, rx=float):
        self.rx = rx
        mc.setAttr(self.name + '.rx', rx)
        return self.rx

    def getRx(self):
        return mc.getAttr(self.name + '.rx')

    # Ry
    def setRy(self, ry=float):
        self.ry = ry
        mc.setAttr(self.name + '.ry', ry)
        return self.ry

    def getRy(self):
        return mc.getAttr(self.name + '.ry')

    # Rz
    def setRz(self, rz=float):
        self.rz = rz
        mc.setAttr(self.name + '.rz', rz)
        return self.rz

    def getRz(self):
        return mc.getAttr(self.name + '.rz')

    #setR
    def setR(self, x, y, z):
        return (self.setRx(x), self.setRy(y), self.setRz(z))

    def getR(self):
        return (self.getRx(), self.getRy(), self.getRz())

    # Sx
    def setSx(self, sx=float):
        self.sx = sx
        mc.setAttr(self.name + '.sx', sx)
        return self.rz

    def getSx(self):
        return mc.getAttr(self.name + '.sx')

    # Sy
    def setSy(self, sy=float):
        self.sy = sy
        mc.setAttr(self.name + '.sy', sy)
        return self.ry

    def getSy(self):
        return mc.getAttr(self.name + '.sy')

    # Sz
    def setSz(self, sz=float):
        self.sz = sz
        mc.setAttr(self.name + '.sz', sz)
        return self.sz

    #setS
    def setS(self, x, y, z):
        return (self.setSx(x), self.setSy(y), self.setSz(z))

    def getS(self):
        return (self.getSx(), self.getSy(), self.getSz())

    def getSz(self):
        return mc.getAttr(self.name + '.sz')

    def objectType(self):
        return mc.objectType(self.name)

    def cleanObj(self):
            mc.select(self.name)
            mc.makeIdentity(self.name, apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)
            mc.delete(self.name, ch = 1)
    
    def delete(self):
        mc.delete(self.name)

class Joint(Obj):
    
    def __init__(self, name):
        Obj.__init__(self, name)

        if mc.objExists(self.name) == False:
            mc.joint(n = self.name)
            # mc.joint(n = self.name, edit = True, zso = True, oj = 'yxz', sao = 'xdown')
            print 'create Joint'
        else:
            print 'map Joint'
    
    def findRel(self):
        return mc.listRelatives(self.name, p = True)
        


class Ctrl(Obj):

    def __init__(self, name, shapeCtrl):

        shape = {
        'square': [[(-1, 0, -1), (-1, 0, 1), (1, 0, 1), (1, 0, -1), (-1, 0, -1)], [0, 1, 2, 3, 4]],
        'box': [[(-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5)], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
        'FourDir': [[(-1.009675, 0, -0.977991), (-1.009675, 0, -3.017713), (-1.009675, 0, -3.017713), (-2, 0, -3), (0, 0, -5), (2, 0, -3), (1, 0, -3), (1, 0, -1), (3, 0, -1), (3, 0, -2), (5, 0, 0), (3, 0, 2), (3, 0, 1), (1, 0, 1), (1, 0, 3), (2, 0, 3), (0, 0, 5), (-2, 0, 3), (-1, 0, 3), (-1, 0, 1), (-3, 0, 1), (-3, 0, 2), (-5, 0, 0), (-3, 0, -2), (-3, 0, -1), (-1, 0, -1)], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]],
        'twoDri': [[(-1, 0, -2), (-2, 0, -2), (0, 0, -4), (2, 0, -2), (1, 0, -2), (1, 0, 1), (2, 0, 1), (0, 0, 3), (-2, 0, 1), (-1, 0, 1), (-1, 0, -2)], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
        'stick': [[(0, 0, 0), (0, 3, 0), (-1,  5, 0), (1,  5, 0), (0, 3, 0)], [0, 1, 2, 3, 4]]
        }

        Obj.__init__(self, name)
        self.shape = shapeCtrl

        if mc.objExists(self.name) == False:
            mc.curve(d = 1, p = shape[self.shape][0], k = shape[self.shape][1], n = self.name)
            mc.rename('curveShape1', self.name + 'Shape')
            print 'create Ctrl'
        else:
            print 'map Ctrl'

class Group(Obj):
    
    def __init__(self, name):
        Obj.__init__(self, name)

        if mc.objExists(self.name) == False:
            mc.joint(n = self.name)
            # mc.joint(n = self.name, edit = True, zso = True, oj = 'yxz', sao = 'xdown')
            print 'create Group'
        else:
            print 'map Group'
# global proc BallProcedure()
# {
# curve 	-d 1
# 	-p 0 0 0
# 	-p -1 0 0
# 	-p -0.665474 0 0
# 	-p -0.642798 0.172237 0
# 	-p -0.576317 0.332738 0
# 	-p -0.470563 0.470563 0
# 	-p -0.332738 0.576317 0
# 	-p -0.172237 0.642798 0
# 	-p 0 0.665474 0
# 	-p 0 1 0
# 	-p 0 0.665474 0
# 	-p 0.172237 0.642798 0
# 	-p 0.332738 0.576317 0
# 	-p 0.470563 0.470563 0
# 	-p 0.576317 0.332738 0
# 	-p 0.642798 0.172237 0
# 	-p 0.665474 0 0
# 	-p 1 0 0
# 	-p 0 0 0
# 	-p 0 0 1
# 	-p 0 0 0.665474
# 	-p 0 0.205643 0.632905
# 	-p 0 0.391156 0.538379
# 	-p 0 0.538379 0.391156
# 	-p 0 0.632905 0.205643
# 	-p 0 0.665474 0
# 	-p 0 0.632905 -0.205643
# 	-p 0 0.538381 -0.391156
# 	-p 0 0.391156 -0.538379
# 	-p 0 0.205643 -0.632905
# 	-p 0 0 -0.665474
# 	-p 0 0 -1
# 	-p 0 0 -0.665474
# 	-p -0.172237 0 -0.642798
# 	-p -0.332738 0 -0.576317
# 	-p -0.470563 0 -0.470563
# 	-p -0.576317 0 -0.332738
# 	-p -0.642798 0 -0.172237
# 	-p -0.665474 0 0
# 	-p -0.642798 0 0.172237
# 	-p -0.576317 0 0.332738
# 	-p -0.470563 0 0.470563
# 	-p -0.332738 0 0.576317
# 	-p -0.172237 0 0.642798
# 	-p 0 0 0.665474
# 	-p 0.172237 0 0.642798
# 	-p 0.332738 0 0.576317 
# 	-p 0.470563 0 0.470563
# 	-p 0.576317 0 0.332738
# 	-p 0.642798 0 0.172237
# 	-p 0.665474 0 0
# 	-p 0.642798 0 -0.172237
# 	-p 0.576317 0 -0.332738
# 	-p 0.470563 0 -0.470563
# 	-p 0.332738 0 -0.576317
# 	-p 0.172237 0 -0.642798
# 	-p 0 0 -0.665474
# 	-p 0 0 0
# 	-k 0 -k 1 -k 2 -k 3 -k 4
# 	-k 5 -k 6 -k 7 -k 8 -k 9
# 	-k 10 -k 11 -k 12 -k 13
# 	-k 14 -k 15 -k 16 -k 17
# 	-k 18 -k 19 -k 20 -k 21
# 	-k 22 -k 23 -k 24 -k 25
# 	-k 26 -k 27 -k 28 -k 29
# 	-k 30 -k 31 -k 32 -k 33
# 	-k 34 -k 35 -k 36 -k 37
# 	-k 38 -k 39 -k 40 -k 41
# 	-k 42 -k 43 -k 44 -k 45
# 	-k 46 -k 47 -k 48 -k 49
# 	-k 50 -k 51 -k 52 -k 53
# 	-k 54 -k 55 -k 56 -k 57;
# }