import pandas as pd
import numpy as np
from scripts.constants_Exp2 import *
from IPython.display import display


def tablaPreprocesada (data, name):

    resumen = pd.DataFrame(index = data.index)

    for pregunta, dic in preguntasUnicas.items():
        subset = data[list(dic.keys())]
        if len(dic.keys()) > 1 :
            subset['RtaInvalida'] = pd.Series(subset.sum(axis=1)!=1)
            subset.loc[subset['RtaInvalida'], list(dic.keys())] = 0
            subset = subset.stack()
            subset = subset[subset==1]
            subset = subset.reset_index()
            subset = subset.rename (columns = {'level_0':'IdSujeto','level_1':pregunta})
            subset[pregunta] = subset[pregunta].map(dic)
            #subset = subset.replace({pregunta:{'RtaInvalida':np.nan}})
            resumen[pregunta] = subset[pregunta]
        else:
            resumen[pregunta] = subset

    for pregunta, dic in preguntasMultiples.items():
        subset = data[list(dic.keys())]
        if len(dic.keys()) > 1 :
            subsetOriginal = subset
            subset = subset.stack()
            subset = subset[subset==1]
            subset = subset.reset_index()
            subset = subset.rename (columns = {'level_0':'IdSujeto','level_1':pregunta})
            subset[pregunta] = subset[pregunta].map(dic)
            #subset = subset.replace({pregunta:{'RtaInvalida':np.nan}})
            subset = subset.drop(0,1)
            grouped = subset.groupby("IdSujeto")
            subsetOriginal[pregunta] = grouped[pregunta].apply(lambda x: list(x))
            resumen[pregunta] = grouped[pregunta].apply(lambda x: list(x))
        else:
            resumen[pregunta] = subset

    resumen['IdExp'] = data['global_id']
    resumen['IdForm'] = data['questionnaire_id']
    resumen['IdSubset'] = name

    return resumen
