#!/bin/env python

import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import optparse

cnstfname= 'in.const.NN'
combfname= 'in.comb.NN'
paramfname= 'in.params.NN'

def comb(n,m):
    return math.factorial(n)/math.factorial(m)

def read_NN_config():
    fcnst= open(cnstfname,'r')
    buff= fcnst.readline().split()
    nl= int(buff[0])
    nhl= np.zeros((nl+1),dtype=int)
    nsp= int(buff[1])
    nhl[0]=int(buff[2])
    nhl[1]=int(buff[3])
    if nl == 2:
        nhl[2]= int(buff[4])
    print 'num of species=',nsp
    print 'num of layers =',nl
    print 'num of neurons-{0:d} ='.format(0),nhl[0]
    print 'num of neurons-{0:d} ='.format(1),nhl[1]
    if nl == 2:
        print 'num of neurons-{0:d} ='.format(2),nhl[2]
    n2=0
    n3=0
    for line in fcnst.readlines():
        buff= line.split()
        if buff[0] == '1':
            n2 += 1
        elif buff[0] == '2':
            n3 += 1
    fcnst.close()
    print 'read in.const.NN'
    print 'num of 2body terms=',n2
    print 'num of 3body terms=',n3
    
    ncmb2= nsp +comb(nsp,2)
    ncmb3= ncmb2*nsp
    print 'num of 2body pairs   =',ncmb2
    print 'num of 3body triplets=',ncmb3
    nhl[0]= n2*ncmb2 +n3*ncmb3
    print 'num of 2body and 3body inputs =',n2*ncmb2, n3*ncmb3
    if nl == 1:
        print 'num of input neurons =',nhl[0]*nhl[1] +nhl[1]
    elif nl == 2:
        print 'num of input neurons =',nhl[0]*nhl[1] +nhl[1]*nhl[2] +nhl[2]

    fcmb= open(combfname,'r')
    cmb2= np.zeros((ncmb2,2),dtype=int)
    cmb3= np.zeros((ncmb3,3),dtype=int)
    print 'pairs:'
    for i2 in range(ncmb2):
        buff= fcmb.readline().split()
        cmb2[i2,0]= int(buff[0])
        cmb2[i2,1]= int(buff[1])
        print '  ',i2,': {0:1d}-{1:1d}'.format(cmb2[i2,0],cmb2[i2,1])
    print 'triplets:'
    for i3 in range(ncmb3):
        buff= fcmb.readline().split()
        cmb3[i3,0]= int(buff[0])
        cmb3[i3,1]= int(buff[1])
        cmb3[i3,2]= int(buff[2])
        print '  ',i3,':', \
            ' {0:1d}-{1:1d}-{2:1d}'.format(cmb3[i3,0],cmb3[i3,1],cmb3[i3,2])
    fcmb.close()
    return nl,nsp,nhl,n2,n3,cmb2,cmb3
    
def read_NN_params(nl,nhl):
    #.....read in.params.NN
    fparam= open(paramfname,'r')
    buff= fparam.readline().split()
    if nl == 1:
        wgt11= np.zeros((nhl[0],nhl[1]))
        wgt12= np.zeros(nhl[1])
        for ihl0 in range(nhl[0]):
            for ihl1 in range(nhl[1]):
                buff= fparam.readline().split()
                wgt11[ihl0,ihl1]= float(buff[0])
        for ihl1 in range(nhl[1]):
            buff= fparam.readline().split()
            wgt12[ihl1]= float(buff[0])
    elif nl == 2:
        wgt21= np.zeros((nhl[0],nhl[1]))
        wgt22= np.zeros((nhl[1],nhl[2]))
        wgt23= np.zeros(nhl[2])
        for ihl0 in range(nhl[0]):
            for ihl1 in range(nhl[1]):
                buff= fparam.readline().split()
                wgt21[ihl0,ihl1]= float(buff[0])
        for ihl1 in range(nhl[1]):
            for ihl2 in range(nhl[2]):
                buff= fparam.readline().split()
                wgt22[ihl1,ihl2]= float(buff[0])
        for ihl2 in range(nhl[2]):
            buff= fparam.readline().split()
            wgt23[ihl2]= float(buff[0])
        
    
    fparam.close()
    print 'read in.params.NN'
    #for ihl0 in range(n2+n3):
    #    print ihl0,': ',wgt11[ihl0,0:nhl[1]+1]
    # for ihl1 in range(nhl[1]):
    #     print ihl1,': ',wgt12[ihl1]OB
    if nl == 1:
        return wgt11,wgt12
    elif nl == 2:
        return wgt21,wgt22,wgt23

if __name__ == '__main__':

    usage= '%prog [options]'

    parser= optparse.OptionParser(usage=usage)
    parser.add_option("-w",action="store_true",
                      dest="weight",default=False,
                      help="Show weight values.")
    parser.add_option("-t",dest="threshold",type="float",default=0.01,
                      help="Threshold value multiplied to max edge for omitting criterion of edge.")
    (options,args)= parser.parse_args()

    flag_weight= options.weight
    threshold= options.threshold

    nl,nsp,nhl,n2,n3,cmb2,cmb3= read_NN_config()
    if nl == 1:
        wgt11,wgt12= read_NN_params(nl,nhl)
    elif nl == 2:
        wgt21,wgt22,wgt23= read_NN_params(nl,nhl)
    
    g= nx.Graph()
    pos= {}
    dy=-1.0
    for ihl0 in range(nhl[0]):
        g.add_node('0-{0:03d}'.format(ihl0))
        pos['0-{0:03d}'.format(ihl0)]= [0,ihl0*dy]
    dy= -float(nhl[0]-1)/(nhl[1]-1)
    for ihl1 in range(nhl[1]):
        g.add_node('1-{0:03d}'.format(ihl1))
        pos['1-{0:03d}'.format(ihl1)]= [1,ihl1*dy]
    if nl == 1:
        dy= -float(nhl[0])/2
        g.add_node('2')
        pos['2']= [2,dy]
    elif nl == 2:
        dy= -float(nhl[0]-1)/(nhl[2]-1)
        for ihl2 in range(nhl[2]):
            g.add_node('2-{0:03d}'.format(ihl2))
            pos['2-{0:03d}'.format(ihl2)]= [2,ihl2*dy]
        dy= -float(nhl[0])/2
        g.add_node('3')
        pos['3']= [3,dy]

    n= 0
    nlabel= {}
    for key in pos:
        # print key,pos[key]
        if key[0] != '0':
            nlabel[key]= ''
        else:
            ineuron= int(key[2:5])
            # print 'ineuron=',ineuron
            if ineuron < n2*len(cmb2):
                pair= ineuron / n2
                isf2= ineuron % n2
                nlabel[key]= '{0:1d}-'.format(cmb2[pair,0]) \
                             +'{0:1d}:'.format(cmb2[pair,1]) \
                             +' {0:02d}'.format(isf2)
            else:
                ine= ineuron -n2*len(cmb2)
                triplet= ine / n3
                isf3   = ine % n3
                # print ' n3,triplet,isf3=',n3,triplet,isf3
                nlabel[key]= '{0:1d}-'.format(cmb3[triplet,0]) \
                             +'{0:1d}-'.format(cmb3[triplet,1]) \
                             +'{0:1d}:'.format(cmb3[triplet,2]) \
                             +' {0:02d}'.format(isf3)
        # print n,nlabel[n]
        n += 1
    # exit()
    
    maxedge=0.0
    if nl == 1:
        for ihl0 in range(nhl[0]):
            for ihl1 in range(nhl[1]):
                maxedge= max(maxedge,np.abs(wgt11[ihl0,ihl1]))
        for ihl1 in range(nhl[1]):
            maxedge= max(maxedge,np.abs(wgt12[ihl1]))
    elif nl == 2:
        for ihl0 in range(nhl[0]):
            for ihl1 in range(nhl[1]):
                maxedge= max(maxedge,np.abs(wgt21[ihl0,ihl1]))
        for ihl1 in range(nhl[1]):
            for ihl2 in range(nhl[2]):
                maxedge= max(maxedge,np.abs(wgt22[ihl1,ihl2]))
        for ihl2 in range(nhl[2]):
            maxedge= max(maxedge,np.abs(wgt23[ihl2]))
    print 'max of edge value= ',maxedge
        
    colors= []
    elabels= {}
    ic= 0
    if nl == 1:
        for ihl0 in range(nhl[0]):
            for ihl1 in range(nhl[1]):
                if np.abs(wgt11[ihl0,ihl1]) > threshold*maxedge:
                    val= wgt11[ihl0,ihl1]
                    g.add_edge('0-{0:03d}'.format(ihl0),'1-{0:03d}'.format(ihl1))
                    elabels[('0-{0:03d}'.format(ihl0),'1-{0:03d}'.format(ihl1))]='{0:7.4f}'.format(val)
        for ihl1 in range(nhl[1]):
            if np.abs(wgt12[ihl1]) > threshold*maxedge:
                val= wgt12[ihl1]
                g.add_edge('1-{0:03d}'.format(ihl1), '2')
                elabels[('1-{0:03d}'.format(ihl1),'2')]= '{0:7.4f}'.format(val)
    elif nl == 2:
        for ihl0 in range(nhl[0]):
            for ihl1 in range(nhl[1]):
                if np.abs(wgt21[ihl0,ihl1]) > threshold*maxedge:
                    val= wgt21[ihl0,ihl1]
                    g.add_edge('0-{0:03d}'.format(ihl0),'1-{0:03d}'.format(ihl1))
                    elabels[('0-{0:03d}'.format(ihl0),'1-{0:03d}'.format(ihl1))]='{0:7.4f}'.format(val)
        for ihl1 in range(nhl[1]):
            for ihl2 in range(nhl[2]):
                if np.abs(wgt22[ihl1,ihl2]) > threshold*maxedge:
                    val= wgt22[ihl1,ihl2]
                    g.add_edge('1-{0:03d}'.format(ihl1), '2-{0:03d}'.format(ihl2))
                    elabels[('1-{0:03d}'.format(ihl1),'2-{0:03d}'.format(ihl2))]= '{0:7.4f}'.format(val)
        for ihl2 in range(nhl[2]):
            if np.abs(wgt23[ihl2]) > threshold*maxedge:
                val= wgt23[ihl2]
                g.add_edge('2-{0:03d}'.format(ihl2), '3')
                elabels[('2-{0:03d}'.format(ihl2),'3')]= '{0:7.4f}'.format(val)

    for e in g.edges():
        e1= e[0]
        e2= e[1]
        for l in elabels.keys():
            if e1 in l and e2 in l:
                colors.append(np.sqrt(np.abs(float(elabels[l]))))

    # print 'len(edges)=',len(g.edges())
    # print g.edges()
    # print 'len(colors)=',len(colors)
    # print colors
    #exit()
            
    #nx.draw_networkx_nodes(g,pos,node_size=30,node_color='b',node_shape='o')
    #nx.draw_networkx_edges(g,pos)
    nodes= nx.draw_networkx_nodes(g,pos,node_size=30,node_color='b')
    edges= nx.draw_networkx_edges(g,pos,edge_color=colors,edge_cmap=plt.get_cmap('jet'))
    if flag_weight:
        nx.draw_networkx_edge_labels(g,pos,alpha=1.0,edge_labels=elabels,label_pos=0.5)
    for key in pos:
        pos[key][0] -= 0.2
    nx.draw_networkx_labels(g,pos,nlabel,font_size=8)
    
    plt.colorbar(edges)
    plt.tick_params(axis='x',bottom='off',top='off',labelbottom='off')
    plt.tick_params(axis='y',bottom='off',top='off',labelleft='off')
    plt.show()
