#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os  

def readFile(enPath, cnPath):
    #Read File to pairs  
    with open(enPath,'r',encoding='utf8') as fp_en:
        with open(cnPath,'r',encoding='utf8') as fp_cn: 
            iters = 1  
            pairDic = {}  
            
            #生成原始序对字典  
            countPair = 0  
            for line_cn,line_en in zip(fp_cn,fp_en):  
                f = line_cn.split()  
                e = line_en.split()  
                for word1 in f:  
                    for word2 in e:  
                        pairDic[countPair] = (word1,word2)  
                        countPair += 1  
                iters += 1 
            return pairDic

def getDict(pairDic):
    #先将序对字典一次性去重  
    lst = list(set(pairDic.values()))   
    NewpairDic = {}  
    i = 0  
    foreign,english = [],[]  
    for _tuple in lst:  
        #生成新的序对字典  
        NewpairDic[i] = _tuple  
        i += 1  
    print("get pairs...")  
    return NewpairDic

def IBMmodel1(NewpairDic, enPath, cnPath, outPath):
    # run ibm-model-1(EM)
    with open(outPath, 'w', encoding='utf8') as outFile:  
        t = {}  
        for key in NewpairDic.values():  
            t[key]=1.0/len(NewpairDic)  #initialize t(e|f) uniformly  
        outFile.write("t0=\n"+str(t)+'\n')
        
        K = 0  
        while K<=2: #while not converged  
            with open(enPath,'r',encoding='utf8') as fp_en:
                with open(cnPath,'r',encoding='utf8') as fp_cn: 
                    count,total = {},{}  
                    for key in NewpairDic.values():  
                        count[key] = 0  
                    for _tuple in NewpairDic.values():  
                        total[_tuple[0]] = 0  
                    s_total = {}  
                    for ee,ff in zip(fp_en,fp_cn):  
                        #compute normalization  
                        for e in ee.split():  
                            s_total[e] = 0  
                            for f in ff.split():  
                                s_total[e] += t[(f,e)]  
                        #collect counts  
                        for e in ee.split():  
                            for f in ff.split():  
                                count[(f,e)] += t[(f,e)]/s_total[e]  
                                total[f] += t[(f,e)]/s_total[e]  
                    #estimate probabilities  
                    for f,e in NewpairDic.values():  
                        t[(f,e)] = count[(f,e)]/total[f]  
                    #end of while     
                    K += 1  
                
                    outFile.write("t%d=\n" %K)
                    print("t%d processing..." %K)  
                    for it in t.items():  
                        outFile.write(str(it)+'\n')

if __name__ == "__main__":
    enPath = input('Please input source language text file path:')
    cnPath = input('Please input target language text file path:')
    outPath = input('Please input output text file path:')
    pairDic = readFile(enPath, cnPath)
    NewpairDic = getDict(pairDic)
    IBMmodel1(NewpairDic, enPath, cnPath, outPath)
    print('processing over!\nOutput file in '+outPath)
    input('Press any key to continue...')