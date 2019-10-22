import objClass as oc
import maya.cmds as mc

class Joint(oc.Obj):
    
    def __init__(self, name):
        oc.Obj.__init__(self, name)

        if mc.objExists(self.name) == False:
            mc.joint(n = self.name)
            mc.joint(n = self.name, edit = True, zso = True, oj = 'yxz', sao = 'xdown')
            print 'create Joint'
        else:
            print 'map Joint'




