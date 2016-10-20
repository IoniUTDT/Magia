C_Edades = {'1_1_0':'Menos 5',
                  '1_1_1':'5 a 12',
                  '1_1_2':'13 a 17',
                  '1_1_3':'18 a 24',
                  '1_1_4':'25 a 40',
                  '1_1_5':'40 Mas'
            }
C_Profesion = {'1_2_0':'Psicologia',
                  '1_2_1':'Bio/Qui/Geo/Paleo',
                  '1_2_2':'Prof/Docencia',
                  '1_2_3':'Medicas',
                  '1_2_4':'Arq/Diseño',
                  '1_2_5':'Fisica',
                  '1_2_6':'Musica',
                  '1_2_7':'Turismo',
                  '1_2_8':'Derecho',
                  '1_2_9':'Mate/Comp/Sistemas',
                  '1_2_10':'Farm. y Bioq.',
                  '1_2_11':'Artes Plasticas',
                  '1_2_12':'Letras',
                  '1_2_13':'Agro./Vet.',
                  '1_2_14':'Danzas/Deportes',
                  '1_2_15':'Ingenierias',
                  '1_2_16':'Cs. Sociales',
                  '1_2_17':'Gastronomia',
                  '1_2_18':'Marketing/Publicidad',
                  '1_2_19':'Cs. Economicas',
                  '1_2_20':'OpcionLibre'
                    }

C_Exactas = ['1_2_1','1_2_5','1_2_9','1_2_15']
C_Afines = ['1_2_3','1_2_4','1_2_10','1_2_13','1_2_2']
C_NoAfines = ['1_2_0','1_2_6','1_2_7','1_2_8','1_2_11','1_2_12',
                    '1_2_14','1_2_16','1_2_17','1_2_18','1_2_19','1_2_20']

C_NivelFormacion = {'1_3_0':'Primaria','1_3_1':'Secundaria','1_3_2':'Terciario',
                          '1_3_3':'UniversidadCompleta','1_3_4':'UniversidadCurso','1_3_5':'Posgrado'}

C_Mecanismo_Q1 = {'2_1_0':'Calor','2_1_1':'Telekinesis','2_1_2':'Magnetismo','2_1_3':'EnergiaCosmica',
                     '2_1_4':'FisicaCuantica','2_1_5':'Presion','2_1_6':'Aura Corporal','2_1_7':'Electricidad',
                     '2_1_8':'No lo se'}

C_Confianza = {'2_2':'Confianza'}

C_Mecanismo_Q2 = {'2_3_0':'Calor','2_3_1':'Telekinesis','2_3_2':'Magnetismo','2_3_3':'EnergiaCosmica',
                     '2_3_4':'FisicaCuantica','2_3_5':'Presion','2_3_6':'Aura Corporal','2_3_7':'Electricidad',
                     '2_3_8':'CampoLibre'}

C_RelevanciaMano = {'2_4':'Relevancia Mano'}

C_Mecanismo_Q3 = {'3_1_0':'Calor','3_1_1':'Telekinesis','3_1_2':'Magnetismo','3_1_3':'EnergiaCosmica',
                     '3_1_4':'FisicaCuantica','3_1_5':'Presion','3_1_6':'Aura Corporal','3_1_7':'Electricidad',
                     '3_1_8':'No lo se'}

C_Confianza_Q3 = {'3_2':'Confianza'}

C_Truco = {'3_3_0' : 'Si', '3_3_1' : 'No', '3_3_2' : 'No se'}

C_Intereses = {'4_1_1' : 'Bailar', '4_1_2' : 'Cocinar', '4_1_3' : 'Matematica', '4_1_4' : 'PelisSeries',
                    '4_1_5' : 'Construir', '4_1_6' : 'Oficina', '4_1_7' : 'Tarot', '4_1_8' : 'Literatura',
                    '4_1_9' : 'Religion', '4_1_10' : 'Reparar', '4_1_11' : 'Programar' , '4_1_12' : 'Correr',
                    '4_1_13' : 'Acertijos', '4_1_14' : 'Astrologia', '4_1_15' : 'DeportesEquipo', '4_1_16' : 'Debatir',
                    '4_1_17' : 'Magia', '4_1_18' : 'Electronica'}

EscalaIntereses = [0,1,2,3,4]

preguntasAnidadas = {}

for key, value in C_Intereses.items():
    dic = {}
    for escala in EscalaIntereses:
        dic.update({key+'_'+str(escala):escala})
    preguntasAnidadas.update({'Interes_' + value:dic})

preguntasUnicas = {'Edad' : C_Edades,
            'Profesion' : C_Profesion,
            'Formacion' : C_NivelFormacion,
            'MecanismoInicial': C_Mecanismo_Q1,
            'ConfianzaInicial' : C_Confianza,
            'RelevanciaMano' : C_RelevanciaMano,
            'MecanismoPost' : C_Mecanismo_Q3,
            'ConfianzaPost' : C_Confianza_Q3,
            'HayTruco' : C_Truco
            }

#preguntasUnicas.update (preguntasAnidadas)

preguntasMultiples = {
            'MecanismoInicialOtros' : C_Mecanismo_Q2
            }
