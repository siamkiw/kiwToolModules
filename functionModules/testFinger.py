import maya.cmds as mc
elemList = ['thumb','index','middle','ring','pinky']
sideList = ['LFT','RGT']

for side in sideList:    
    for elem in elemList:
         if elem == 'thumb':
               num = 3 
         else :
               num = 4
         ctrlList = []
         for i in range (0,num):
               ctrlfkik  = 'arm'+ '_' + side + '_' + 'ctrl'
               ctrlShape = 'arm'+ '_' + side + '_' + 'ctrlShape'
               if elem == 'thumb' :
                  if i == 0 : 
                     fist1 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rx' + side , at="double", dv=0, k=True)
                     fist2 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Ry' + side , at="double", dv=0, k=True)
                     fist3 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rz' + side , at="double", dv=0, k=True)
                  if i == 1 :
                     fist4 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rx' + side , at="double", dv=0, k=True)
                     fist5 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Ry' + side , at="double", dv=0, k=True)
                     fist6 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rz' + side , at="double", dv=0, k=True)   
                  if i == 2 :   
                     fist7 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rx' + side , at="double", dv=0, k=True)
                     fist8 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Ry' + side , at="double", dv=0, k=True)
                     fist9 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rz' + side , at="double", dv=0, k=True)
                     cup1 = mc.addAttr(ctrlShape, ln= elem + str(i-1)+ '_Cup_'+ side, at="double", dv=0, k=True)
                     cup2 = mc.addAttr(ctrlShape, ln= elem + str(i)  +'_Cup_'+ side, at="double", dv=0, k=True)  
                     cup3 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_Cup_'+ side, at="double", dv=0, k=True)
                     spread = mc.addAttr(ctrlShape, ln= elem + 'Spread'+side , at="double", dv=0, k=True)
                     bastSpread = mc.addAttr(ctrlShape, ln= elem + 'BastSpread'+side, at="double", dv=0, k=True)      
               else :
                     if i == 0 :
                        fist1 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rx' + side , at="double", dv=0, k=True)
                        fist2 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Ry' + side , at="double", dv=0, k=True)
                        fist3 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rz' + side , at="double", dv=0, k=True)
                     if i == 1 :
                        fist4 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rx' + side , at="double", dv=0, k=True)
                        fist5 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Ry' + side , at="double", dv=0, k=True)
                        fist6 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rz' + side , at="double", dv=0, k=True) 
                     if i == 2 :
                        fist7 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rx' + side , at="double", dv=0, k=True)
                        fist8 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Ry' + side , at="double", dv=0, k=True)
                        fist9 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rz' + side , at="double", dv=0, k=True) 
                     if i == 3 :
                        fist10 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rx' + side , at="double", dv=0, k=True)
                        fist11 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Ry' + side , at="double", dv=0, k=True)
                        fist12 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_fist_Rz' + side , at="double", dv=0, k=True)
                        cup1 = mc.addAttr(ctrlShape, ln= elem + str(i-2)+ '_Cup_'+ side, at="double", dv=0, k=True)
                        cup2 = mc.addAttr(ctrlShape, ln= elem + str(i-1)+ '_Cup_'+ side, at="double", dv=0, k=True)
                        cup3 = mc.addAttr(ctrlShape, ln= elem + str(i)  +'_Cup_'+ side, at="double", dv=0, k=True)  
                        cup4 = mc.addAttr(ctrlShape, ln= elem + str(i+1)+'_Cup_'+ side, at="double", dv=0, k=True)
                        spread = mc.addAttr(ctrlShape, ln= elem + 'Spread'+side , at="double", dv=0, k=True)
                        bastSpread = mc.addAttr(ctrlShape, ln= elem + 'BastSpread'+side, at="double", dv=0, k=True)                    
               
               ctrl  = elem + str(i+1)+ '_' + side 
               mdb   = elem + str(i+1) + '_fistAmp' + side + '_mdb'
               mult1 = elem + str(i+1) + '_cupAmp' + side + '_mult'
               if i == 0 :
                  mult2 = elem  + '_bastSpreadAmp' + side + '_mult'
                  mult3 = elem  + '_spreadAmp' + side + '_mult'
                  mc.createNode('multDoubleLinear',n= mult2)
                  mc.createNode('multDoubleLinear',n= mult3)    
               pma   = elem + str(i+1) + '_rotate' + side + '_pma'
               zGrpSide  = elem + str(i+1) +'_'+  side + '_zGrp'
               zGrp   = elem + str(i+1) + '_rotate' + side + '_zGrp'
               mc.duplicate (zGrpSide,n=zGrp,po=True)
               mc.parent(zGrp,zGrpSide)
               mc.parent(ctrl,zGrp)
               mc.createNode('plusMinusAverage',n= pma)
               mc.connectAttr(pma +'.output3D',  zGrp + '.rotate' )
               mc.createNode('multiplyDivide',n= mdb)
               mc.connectAttr(mdb +'.output',  pma + '.input3D[0]' )
               mc.createNode('multDoubleLinear',n= mult1)
               mc.connectAttr(mult1 +'.output',  pma + '.input3D[1].input3Dx')
               if i == 0 :
                  mc.connectAttr(mult2 +'.output',  pma + '.input3D[2].input3Dz')
               if i == 1 :
                  mc.connectAttr(mult3 +'.output',  pma + '.input3D[2].input3Dz')
                  
               if elem == 'thumb' :
                  if i == 0 :
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                     mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                     mc.connectAttr(ctrlfkik + '.bastSpread',   mult2 + '.input1')
                     mc.connectAttr(ctrlfkik + '.spread',   mult3 + '.input1')
                  if i == 1 :
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                     mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                     
                  if i == 2 :
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                     mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i-1)+ '_Cup_'+ side,   elem + str(i-1) + '_cupAmp' + side + '_mult' + '.input2')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i)+ '_Cup_'+ side,   elem + str(i) + '_cupAmp' + side + '_mult' + '.input2') 
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+ '_Cup_'+ side,   elem + str(i+1) + '_cupAmp' + side + '_mult' + '.input2')
                     mc.connectAttr(ctrlShape+ '.'+ elem + 'Spread'+  side,   elem  + '_spreadAmp' + side + '_mult' + '.input2')
                     mc.connectAttr(ctrlShape+ '.'+ elem + 'BastSpread'+  side,   elem  + '_bastSpreadAmp' + side + '_mult' + '.input2')   
                  if i == 3 :
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                     mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                     mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                     mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')

                     

               else :
                     if i == 0 :
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                        mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                        mc.connectAttr(ctrlfkik + '.bastSpread',   mult2 + '.input1')
                        mc.connectAttr(ctrlfkik + '.spread',   mult3 + '.input1')
                     if i == 1 :
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                        mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                        
                     if i == 2 :
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                        mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                         
                     if i == 3 :
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                        mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i-2)+ '_Cup_'+ side,   elem + str(i-2) + '_cupAmp' + side + '_mult' + '.input2')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i-1)+ '_Cup_'+ side,   elem + str(i-1) + '_cupAmp' + side + '_mult' + '.input2')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i)+ '_Cup_'+ side,   elem + str(i) + '_cupAmp' + side + '_mult' + '.input2') 
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+ '_Cup_'+ side,   elem + str(i+1) + '_cupAmp' + side + '_mult' + '.input2')
                        mc.connectAttr(ctrlShape+ '.'+ elem + 'Spread'+  side,   elem  + '_spreadAmp' + side + '_mult' + '.input2')
                        mc.connectAttr(ctrlShape+ '.'+ elem + 'BastSpread'+  side,   elem  + '_bastSpreadAmp' + side + '_mult' + '.input2')  
                        
                     if i == 4 :
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1X')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Y')
                        mc.connectAttr(ctrlfkik + '.fist',  mdb + '.input1Z')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rx'+ side, mdb +'.input2X')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Ry'+ side, mdb +'.input2Y')
                        mc.connectAttr(ctrlShape+ '.'+ elem + str(i+1)+'_fist_Rz'+ side, mdb +'.input2Z')
                        mc.connectAttr(ctrlfkik + '.cup',   mult1 + '.input1')
                        
                        
                                           