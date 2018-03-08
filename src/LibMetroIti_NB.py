# -*- coding: utf-8 -*-

############ Import & Define ############

from LibMetroCsv_NB import *

L=listeMetroCsv(".\\data\\liste stations.csv")
Lex=listeMetroCsvStation(".\\data\\liste stations exceptions-fourche2.csv")
Lf=listeMetroCsvStation(".\\data\\liste stations fourche1.csv")
Linfos=listeMetroCsvInfos(".\\data\\infos_metro.csv")

############ Fonctions ############

def itineraire(station_depart,ligne_depart,station_arrive,ligne_arrive):
    """ Str or Int -> Str
    Transforme le code recu de la fonction
    calcul_itineraire en un str lisible et compréhensible par tous."""
    
    code=calcul_itineraire(station_depart,ligne_depart,station_arrive,ligne_arrive)
    if code=="Vous êtes déjà arrivé.":
        return code
    elif type(code)==type(0):
        return ("Entre "+station_depart+" à "+station_arrive+", il y a "+str(code)+" stations.") 
    else:
        l=code.split(".")
        if l[4]=="":
            return ("Pour aller de "+station_depart+" ligne "+ligne_depart+" à "+station_arrive+" ligne "+ligne_arrive+" en "+str(l[0])+" stations, \nil vous faut changer à "+str(l[1])+".")
        elif str(l[1])==station_depart:
            return ("Pour aller de "+station_depart+" ligne "+ligne_depart+" à "+station_arrive+" ligne "+ligne_arrive+" en "+str(l[0])+" stations, \nil vous faut changer à "+str(l[3])+".")
        else:
            return ("Pour aller de "+station_depart+" ligne "+ligne_depart+" à "+station_arrive+" ligne "+ligne_arrive+" en "+str(l[0])+" stations, \nil vous faut changer à "+str(l[1])+" pour prendre la ligne "+str(l[4])+" puis changer à "+str(l[3])+".")
            
def infos_station(station):
    """
    Fonction qui retourne sous str les informations (ligne et place) de la station donnée.
    """
    LM, Lp = [], []
    ans=(station+" : ")
    for var in L:
        if station in var:
            LM.append(var[0])
            Lp.append(var[2])
    for i in range (0,len(LM)):
        ans+=("est la station numéro "+str(Lp[i])+" de la ligne "+ str(LM[i])+".\n")
    return ans

def calcul_itineraire(station_depart,ligne_depart,station_arrive,ligne_arrive):
    """
    Fonction qui retourne le chemin le plus court entre les deux stations renseignées par l'utulisateur.
    """
    
    L1corres=list()
    L2corres=list()
    trajet=100
    memtrajet=99
    corres=""
    corres2=""
    lignecorres=""
    lignecorres2=""
    
    if station_depart == station_arrive:
        return "Vous êtes déjà arrivé."
    elif ligne_depart == ligne_arrive:
        return calcul_distance(station_depart,ligne_depart,station_arrive,ligne_arrive)
    elif ligne_depart != ligne_arrive:
        for var in L:
          if var[0]==ligne_depart:
              if ligne_arrive in correspondance(var[1],var[0]):
                  L1corres.append([var[0],var[1]])
              for var2 in correspondance(var[1],var[0]):
                  for var3 in L:
                      if var2 == var3[0]:
                          if ligne_arrive in correspondance(var3[1],var2):
                              L2corres.append([var2,var3[1]])
                              
        if station_depart in L1corres:
            return calcul_distance(station_depart,ligne_arrive,station_arrive,ligne_arrive)
        else:
            for var in L1corres:
                if var[0] == ligne_depart:
                    trajet=calcul_distance(station_depart,ligne_depart,var[1],var[0])+calcul_distance(var[1],ligne_arrive,station_arrive,ligne_arrive)
                if trajet < memtrajet:
                    memtrajet=trajet
                    corres=var[1]
                    lignecorres=var[0]
        
        for var2 in L2corres:
            for var in L:
                if var[0]==ligne_depart:
                    if var2[0] in correspondance(var[1],var[0]):
                        trajet=calcul_distance(station_depart,ligne_depart,var[1],var[0])+calcul_distance(var[1],var2[0],var2[1],var2[0])+calcul_distance(var2[1],ligne_arrive,station_arrive,ligne_arrive)
                    if trajet < memtrajet:
                        memtrajet=trajet
                        corres=var[1]
                        lignecorres=var[0]
                        corres2=var2[1]
                        lignecorres2=var2[0]


    return (str(memtrajet)+"."+corres+"."+lignecorres+"."+corres2+"."+lignecorres2)

def listage_stations_itineraire(station_depart,ligne_depart,station_arrive,ligne_arrive):
    """Fonction qui liste toutes les stations de l'itinéraire."""
        
    code=calcul_itineraire(station_depart,ligne_depart,station_arrive,ligne_arrive)
    compteur_index=0
    sens=1 #vers la fin
    Lr=list()
    
    if code=="Vous êtes déjà arrivé.":
        return code
    
    while(L[compteur_index][0]!=ligne_depart or L[compteur_index][1]!=station_depart):
        compteur_index+=1  
            
    if type(code)==type(0):
        for var in Linfos:
            if var[0]==ligne_depart:
                temps_moyen=var[1]
                capacite=var[2]
        for var in L:
            if (var[0]==ligne_arrive and var[1]==station_arrive):
                if (int(var[2])-int(L[compteur_index][2])<0):
                    sens=0 #vers le début
            

        for i in range(0,int(code),1):
            if sens:
                Lr.append([L[compteur_index+i][1],L[compteur_index+i+1][1],L[compteur_index][0],temps_moyen,capacite])
            else:
                Lr.append([L[compteur_index-i][1],L[compteur_index-i-1][1],L[compteur_index][0],temps_moyen,capacite])
        return Lr
    else:
        l=code.split(".")
        if l[4]=="":
            return listage_stations_itineraire(station_depart,ligne_depart,str(l[1]),ligne_depart)+listage_stations_itineraire(str(l[1]),ligne_arrive,station_arrive,ligne_arrive)
        elif str(l[1])==station_depart:
            return listage_stations_itineraire(station_depart,ligne_depart,str(l[3]),ligne_depart)+listage_stations_itineraire(str([3]),ligne_depart,station_arrive,ligne_arrive)
        else:
            return listage_stations_itineraire(station_depart,ligne_depart,str(l[1]),ligne_depart)+listage_stations_itineraire(str(l[1]),str(l[4]),str(l[3]),str(l[4]))+listage_stations_itineraire(str(l[3]),ligne_arrive,station_arrive,ligne_arrive)

            
    
def calcul_distance(station_depart,ligne_depart,station_arrive,ligne_arrive):
    """
    Fonction qui retourne le nombre de station à faire pour arriver à l'arrivé.
    """
    nb_station=0
    
    if ligne_depart == ligne_arrive:
        if ligne_depart == "M7":
            if station_depart in Lex and station_arrive in Lex:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
            elif station_depart in Lex and station_arrive in Lf:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])-29
                        if var[1] == station_arrive:
                            nb_station+=int(var[2])-34
            else :
                if station_depart in Lex:
                    nb_station-=5
                if station_arrive in Lex:
                    nb_station+=5
                for var in L:
                        if var[0] == ligne_depart:
                            if var[1] == station_depart:
                                nb_station+=int(var[2])
                            if var[1] == station_arrive:
                                nb_station-=int(var[2])
                       
                                
        elif ligne_depart == "M7b":
            if station_depart == "PLACE DES FETES" and station_arrive == "DANUBE":
                nb_station=2
            elif station_depart == "PLACE DES FETES" and station_arrive == "PRE SAINT-GERVAIS":
                nb_station=1
            elif station_depart == "DANUBE" and station_arrive == "PLACE DES FETES":
                nb_station=2
            elif station_depart == "DANUBE" and station_arrive == "PRE SAINT-GERVAIS":
                nb_station=3
            elif station_depart == "PRE SAINT-GERVAIS" and station_arrive == "PLACE DES FETES":
                nb_station=3
            elif station_depart == "PRE SAINT-GERVAIS" and station_arrive == "DANUBE":
                nb_station=1
            else:
                if station_depart == "PLACE DES FETES":
                    nb_station+=2
                elif station_depart == "PRE SAINT-GERVAIS":
                    nb_station-1
                elif station_depart == "DANUBE":
                    nb_station-=1
                if station_arrive == "DANUBE":
                    nb_station+=1
                elif station_arrive == "PRE SAINT-GERVAIS":
                    nb_station-=1
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
                            
                            
        elif ligne_depart == "M10":
            if (station_depart == "BOULOGNE-PONT DE SAINT CLOUD" and station_arrive == "BOULOGNE-JEAN JAURES") or (station_arrive == "BOULOGNE-PONT DE SAINT CLOUD" and station_depart == "BOULOGNE-JEAN JAURES") :
                nb_station=1
            elif (station_depart == "BOULOGNE-PONT DE SAINT CLOUD" or station_depart == "BOULOGNE-JEAN JAURES") and station_arrive in Lf:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
            elif (station_arrive == "BOULOGNE-PONT DE SAINT CLOUD" or station_arrive == "BOULOGNE-JEAN JAURES") and station_depart in Lf:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=(9-(int(var[2])+3))
                        if var[1] == station_arrive:
                            nb_station-=(9-int(var[2])-3)
            elif (station_depart == "BOULOGNE-PONT DE SAINT CLOUD" or station_depart == "BOULOGNE-JEAN JAURES" or station_depart in Lf) and station_arrive in Lex:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=(9-(int(var[2])+3))
                        if var[1] == station_arrive:
                            nb_station+=(9-int(var[2]))
            elif (station_arrive == "BOULOGNE-PONT DE SAINT CLOUD" or station_arrive == "BOULOGNE-JEAN JAURES") and (station_depart in Lex or not(station_depart in Lf)):
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])-3
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])            
            elif (station_depart == "BOULOGNE-PONT DE SAINT CLOUD" or station_depart == "BOULOGNE-JEAN JAURES" or station_depart in Lf) and (not station_arrive in Lex and not station_arrive in Lf and station_arrive != "BOULOGNE-PONT DE SAINT CLOUD" and station_arrive != "BOULOGNE-JEAN JAURES"):
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])+3
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
            elif station_depart in Lex and (not station_arrive in Lf and not station_arrive in Lex and station_arrive != "BOULOGNE-PONT DE SAINT CLOUD" and station_arrive != "BOULOGNE-JEAN JAURES"):
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=(2-(int(var[2])-5))
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])-3
            elif (station_depart in Lex or (not station_depart in Lf and not station_depart in Lex and station_depart != "BOULOGNE-PONT DE SAINT CLOUD" and station_depart != "BOULOGNE-JEAN JAURES")) and station_arrive in Lf:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=(2-(int(var[2])-5))
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
            elif (station_depart in Lf and station_arrive in Lf) or (station_depart in Lex and station_arrive in Lex):
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
                if nb_station == 1 or nb_station == (-1):
                    nb_station=7
                elif nb_station == 2 or nb_station == (-2):
                    nb_station=6
            else:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])      
                            
                            
        elif ligne_depart == "M13":
            if (station_depart in Lf and station_arrive in Lf) or (station_depart in Lex and station_arrive in Lex):
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
            elif (station_depart in Lex and not station_arrive in Lf) or (station_arrive in Lex and not station_depart in Lf):
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
            elif station_depart in Lf and not station_arrive in Lex:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])+6
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
            elif station_arrive in Lf and not station_depart in Lex:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])+6
            elif station_depart in Lf and station_arrive in Lex:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=(15-(int(var[2])+6))
                        if var[1] == station_arrive:
                            nb_station+=(15-int(var[2]))
            elif station_depart in Lex and station_arrive in Lf:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=(15-int(var[2]))
                        if var[1] == station_arrive:
                            nb_station+=(15-(int(var[2])+6))
            else:
                for var in L:
                    if var[0] == ligne_depart:
                        if var[1] == station_depart:
                            nb_station+=int(var[2])
                        if var[1] == station_arrive:
                            nb_station-=int(var[2])
        elif ligne_depart!="M7" or ligne_depart!="M7b" or ligne_depart!="M10" or ligne_depart!="M13":
            for var in L:
                if var[0] == ligne_depart:
                    if var[1] == station_depart:
                        nb_station+=int(var[2])
                    if var[1] == station_arrive:
                        nb_station-=int(var[2])    
    return abs(nb_station)


def correspondance(station,ligne):
    """
    Fonction qui retourne les correspondance possibles de la station donnée sous forme de liste.
    """
    
    Lcorres=list()
    
    for var in L:
        if var[1]==station:
            if var[0]!=ligne:
                Lcorres.append(var[0])
    return Lcorres