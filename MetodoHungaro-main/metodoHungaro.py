import pandas as pd
from scipy.optimize import linear_sum_assignment

def intersection(df,valor_min,cant_inter):
    
    for i in range(cant_inter):
        fila = input("Ingresa el nombre de la fila en la que hay una intersección: ")
        columna = input("Ingresa el nombre de la columna en la que hay una intersección: ")
        if cant_inter == 1:
            df.at[fila, columna] = df.at[fila, columna] + valor_min
        else:
            df.at[fila, columna] = df.at[fila, columna] + (valor_min/cant_inter)
    return df
    
    

def hayarMenor(df,isMenor):
    band = 0
    ind = None
    col = None
    for index, fila in df.iterrows():
        for columna, valor in fila.items():
            # Ahora tienes el índice de la fila en 'index' y el nombre de la columna en 'columna'
            if valor > 0 and index != "X":
                if band == 0:
                    isMenor = valor
                    ind = index
                    col = columna
                    band = 1
                else:
                    if valor < isMenor:
                        isMenor = valor
                        ind = index
                        col = columna

    print(f"el menor valor es:{isMenor} en la fila:{ind} y columna:{col} ")
    return isMenor

def restarMenorRestantes(df,isMenor):
    for index, fila in df.iterrows():
        for columna, valor in fila.items():
            # Ahora tienes el índice de la fila en 'index' y el nombre de la columna en 'columna'
            if valor > 0 and index != "X":
                df.at[index, columna] = df.at[index, columna] - isMenor
    print("---------------------Resultado Final-----------------------")
    print()
    return df
def funcionCompletaMax(df,filas,columnas,data_original):
    #Encontramos el menor valor de cada una de las filas dentro del dataFrame y lo asignamos a una nueva columna
                print("-----------------------Data Original----------------------")
                df['Min'] = df.min(axis=1)
                print(df)
                print()
                df_original = data_original
                #Restamos el valor mínimo de cada fila del dataFrame
                print("-----------------------Primera Iteración por Filas----------------------")
                df = df.apply(lambda row: row - row.min(), axis=1)
                print(df)
                print()
                #Arrancamos sacando el valor mínimo de las columnas
                df.loc['Min_Col'] = df.min()
                print(df)
                print()
                # Encontrar el valor mínimo en cada columna y restar este valor mínimo a todos los elementos de esa columna
                print("-----------------------Segunda Iteración por Columnas----------------------")
                df = df.apply(lambda col: col - col.min(), axis=0)
                print(df)

                #Evaluamos la cantidad de ceros que hay por filas y por columnas para proceseder a tachar

                #Calculamos la cantidad de 0 que hay dentro de cada fila 
                ceros_in_filas = df.apply(lambda x: (x == 0).sum()-1, axis=1)

                #Calculamos la cantidad de 0 que hay dentro de cada columna 
                ceros_in_columns = df.apply(lambda x: (x == 0).sum()-1, axis=0)

                 # Filtrar las filas y columnas que contienen más de un cero
                filas_a_tachar = ceros_in_filas[ceros_in_filas > 1].index
                columnas_a_tachar = ceros_in_columns[ceros_in_columns > 1].index
                df = df.drop(columns=['Min'])
                df = df.drop(index='Min_Col')
                # Marcar las filas y columnas a tachar (por ejemplo, cambiando su nombre)
                df.rename(index={fila: "X" for fila in filas_a_tachar}, inplace=True)
                df.rename(columns={columna:"X" for columna in columnas_a_tachar}, inplace=True)
                
                print("DataFrame con filas y columnas tachadas:")
                print()
                print(df)
                print()

                filas_filtradas = df.filter(like="X", axis=0)
                num_filas_filtradas = filas_filtradas.shape[0]

                columnas_filtradas = df.filter(like="X", axis=1)
                num_columnas_filtradas = columnas_filtradas.shape[1]

                # Verificamos si la cantidad de filas y columnas que se tacharon son mayores o iguales a las dimensiones del DataFrame
                cant_tach = num_filas_filtradas + num_columnas_filtradas
            
                isMenor= 0
                
                if cant_tach >= df.shape[1]:
                    # Renombrar las filas
                    df.index = filas
                    # Renombrar las columnas
                    df.columns = columnas
                    print()
                    #Imprimimos el resultado Final
                    print(df)
                    print()
                    df = df.astype(float)
                    #Imprimimos la asignación
                    resolver_asignacion(df,df_original)
                else:
                    cant_inter = int(input("¿Cuántas intersecciones hay en la matriz? : "))
                    #Se encuentra el menor de los que quedaron sin tachar
                    if cant_inter > 0:
                        menor = hayarMenor(df, isMenor)
                         #Imprimimos el resultado final

                        print(restarMenorRestantes(intersection(df,menor,cant_inter),menor))
                        # Renombrar las filas
                        df.index = filas

                        # Renombrar las columnas
                        df.columns = columnas
                        print()
                        #Imprimimos el resultado Final
                        print(df)
                        print()
                        df = df.astype(float)
                        #Imprimimos la asignación
                        resolver_asignacion(df,df_original)
                    else:
                        # Renombrar las filas
                        df.index = filas

                        # Renombrar las columnas
                        df.columns = columnas
                        print()
                        #Imprimimos el resultado Final
                        print(df)
                        print()
                        df = df.astype(float)
                        #Imprimimos la asignación
                        resolver_asignacion(df,df_original)

def funcionCompleta(df,filas,columnas):
    #Encontramos el menor valor de cada una de las filas dentro del dataFrame y lo asignamos a una nueva columna
                print("-----------------------Data Original----------------------")
                df['Min'] = df.min(axis=1)
                print(df)
                print()
                df_original = df
                #Restamos el valor mínimo de cada fila del dataFrame
                print("-----------------------Primera Iteración por Filas----------------------")
                df = df.apply(lambda row: row - row.min(), axis=1)
                print(df)
                print()
                #Arrancamos sacando el valor mínimo de las columnas
                df.loc['Min_Col'] = df.min()
                print(df)
                print()
                # Encontrar el valor mínimo en cada columna y restar este valor mínimo a todos los elementos de esa columna
                print("-----------------------Segunda Iteración por Columnas----------------------")
                df = df.apply(lambda col: col - col.min(), axis=0)
                print(df)

                #Evaluamos la cantidad de ceros que hay por filas y por columnas para proceseder a tachar

                #Calculamos la cantidad de 0 que hay dentro de cada fila 
                ceros_in_filas = df.apply(lambda x: (x == 0).sum()-1, axis=1)

                #Calculamos la cantidad de 0 que hay dentro de cada columna 
                ceros_in_columns = df.apply(lambda x: (x == 0).sum()-1, axis=0)

                 # Filtrar las filas y columnas que contienen más de un cero
                filas_a_tachar = ceros_in_filas[ceros_in_filas > 1].index
                columnas_a_tachar = ceros_in_columns[ceros_in_columns > 1].index
                df = df.drop(columns=['Min'])
                df = df.drop(index='Min_Col')
                # Marcar las filas y columnas a tachar (por ejemplo, cambiando su nombre)
                df.rename(index={fila: "X" for fila in filas_a_tachar}, inplace=True)
                df.rename(columns={columna:"X" for columna in columnas_a_tachar}, inplace=True)
                
                print("DataFrame con filas y columnas tachadas:")
                print()
                print(df)
                print()

                filas_filtradas = df.filter(like="X", axis=0)
                num_filas_filtradas = filas_filtradas.shape[0]

                columnas_filtradas = df.filter(like="X", axis=1)
                num_columnas_filtradas = columnas_filtradas.shape[1]

                # Verificamos si la cantidad de filas y columnas que se tacharon son mayores o iguales a las dimensiones del DataFrame
                cant_tach = num_filas_filtradas + num_columnas_filtradas
            
                isMenor= 0
                
                if cant_tach >= df.shape[1]:
                    # Renombrar las filas
                    df.index = filas
                    # Renombrar las columnas
                    df.columns = columnas
                    print()
                    #Imprimimos el resultado Final
                    print(df)
                    print()
                    df = df.astype(float)
                    #Imprimimos la asignación
                    resolver_asignacion(df,df_original)
                else:
                    cant_inter = int(input("¿Cuántas intersecciones hay en la matriz? : "))
                    #Se encuentra el menor de los que quedaron sin tachar
                    if cant_inter > 0:
                        menor = hayarMenor(df, isMenor)
                         #Imprimimos el resultado final

                        print(restarMenorRestantes(intersection(df,menor,cant_inter),menor))
                        # Renombrar las filas
                        df.index = filas

                        # Renombrar las columnas
                        df.columns = columnas
                        print()
                        #Imprimimos el resultado Final
                        print(df)
                        print()
                        df = df.astype(float)
                        #Imprimimos la asignación
                        resolver_asignacion(df,df_original)
                    else:
                        # Renombrar las filas
                        df.index = filas

                        # Renombrar las columnas
                        df.columns = columnas
                        print()
                        #Imprimimos el resultado Final
                        print(df)
                        print()
                        df = df.astype(float)
                        #Imprimimos la asignación
                        resolver_asignacion(df,df_original)

                   
                        

def funcionSoloFilas(df,filas,columnas):
    print("-----------------------Matriz Inicial del problema----------------------")
    df['Min'] = df.min(axis=1)
    print(df)
    print()
    df_original = df
    #Restamos el valor mínimo de cada fila del dataFrame
    print("-----------------------Primera Iteración por Filas----------------------")
    df = df.apply(lambda row: row - row.min(), axis=1)
    print(df)
    print()
    #Evaluamos la cantidad de ceros que hay por filas y por columnas para proceseder a tachar
    #Calculamos la cantidad de 0 que hay dentro de cada fila 
    ceros_in_filas = df.apply(lambda x: (x == 0).sum()-1, axis=1)
    #Calculamos la cantidad de 0 que hay dentro de cada columna 
    ceros_in_columns = df.apply(lambda x: (x == 0).sum()-1, axis=0)

     # Filtrar las filas y columnas que contienen más de un cero
    filas_a_tachar = ceros_in_filas[ceros_in_filas > 1].index
    columnas_a_tachar = ceros_in_columns[ceros_in_columns > 1].index

    df = df.drop(columns=['Min'])
    # Marcar las filas y columnas a tachar (por ejemplo, cambiando su nombre)
    df.rename(index={fila: "X" for fila in filas_a_tachar}, inplace=True)
    df.rename(columns={columna:"X" for columna in columnas_a_tachar}, inplace=True)
    
    print("DataFrame con filas y columnas tachadas:")
    print()
    print(df)
    print()
    filas_filtradas = df.filter(like="X", axis=0)
    num_filas_filtradas = filas_filtradas.shape[0]
    columnas_filtradas = df.filter(like="X", axis=1)
    num_columnas_filtradas = columnas_filtradas.shape[1]
    # Verificamos si la cantidad de filas y columnas que se tacharon son mayores o iguales a las dimensiones del DataFrame
    cant_tach = num_filas_filtradas + num_columnas_filtradas

    isMenor= 0
    
    if cant_tach >= df.shape[1]:
        # Renombrar las filas
        filas.append("Ficticia")
        df.index = filas
        # Renombrar las columnas
        df.columns = columnas
        print()
        #Imprimimos el resultado Final
        print(df)
        print()
        df = df.astype(float)
        #Imprimimos la asignación
        resolver_asignacion(df,df_original)
    else:
        cant_inter = int(input("¿Cuántas intersecciones hay en la matriz? : "))
        #Se encuentra el menor de los que quedaron sin tachar
        if cant_inter > 0:
            menor = hayarMenor(df, isMenor)
             #Imprimimos el resultado fin
            print(restarMenorRestantes(intersection(df,menor,cant_inter),menor))
            # Renombrar las filas
            filas.append("Ficticia")
            df.index = filas
            # Renombrar las columnas
            df.columns = columnas
            print()
            #Imprimimos el resultado Final
            print(df)
            print()
            df = df.astype(float)
            #Imprimimos la asignación
            resolver_asignacion(df,df_original)
        else:
            # Renombrar las filas
            filas.append("Ficticia")
            df.index = filas
            # Renombrar las columnas
            df.columns = columnas
            print()
            #Imprimimos el resultado Final
            print(df)
            print()
            df = df.astype(float)
            #Imprimimos la asignación
            resolver_asignacion(df,df_original)

def funcionSoloColumnas(df,filas,columnas):
    print("-----------------------Data Original----------------------")
    df['Min'] = df.min(axis=1)
    print(df)
    print()
    df_original = df
     # Encontrar el valor mínimo en cada columna y restar este valor mínimo a todos los elementos de esa columna
    print("-----------------------Segunda Iteración por Columnas----------------------")
    df = df.apply(lambda col: col - col.min(), axis=0)
    print(df)
    #Evaluamos la cantidad de ceros que hay por filas y por columnas para proceseder a tachar
    #Calculamos la cantidad de 0 que hay dentro de cada fila 
    ceros_in_filas = df.apply(lambda x: (x == 0).sum()-1, axis=1)
    #Calculamos la cantidad de 0 que hay dentro de cada columna 
    ceros_in_columns = df.apply(lambda x: (x == 0).sum()-1, axis=0)
     # Filtrar las filas y columnas que contienen más de un cero
    filas_a_tachar = ceros_in_filas[ceros_in_filas > 1].index
    columnas_a_tachar = ceros_in_columns[ceros_in_columns > 1].index
    df = df.drop(columns=['Min'])
    # Marcar las filas y columnas a tachar (por ejemplo, cambiando su nombre)
    df.rename(index={fila: "X" for fila in filas_a_tachar}, inplace=True)
    df.rename(columns={columna:"X" for columna in columnas_a_tachar}, inplace=True)
    
    print("DataFrame con filas y columnas tachadas:")
    print()
    print(df)
    print()
    filas_filtradas = df.filter(like="X", axis=0)
    num_filas_filtradas = filas_filtradas.shape[0]
    columnas_filtradas = df.filter(like="X", axis=1)
    num_columnas_filtradas = columnas_filtradas.shape[1]
    # Verificamos si la cantidad de filas y columnas que se tacharon son mayores o iguales a las dimensiones del DataFrame
    cant_tach = num_filas_filtradas + num_columnas_filtradas    
    isMenor= 0
    
    if cant_tach >= df.shape[1]:
        # Renombrar las filas
        columnas.append("Ficticia")
        df.index = filas
        # Renombrar las columnas
        df.columns = columnas
        print()
        #Imprimimos el resultado Final
        print(df)
        print()
        df = df.astype(float)
        #Imprimimos la asignación
        resolver_asignacion(df,df_original)
    else:
        cant_inter = int(input("¿Cuántas intersecciones hay en la matriz? : "))
        #Se encuentra el menor de los que quedaron sin tachar
        if cant_inter > 0:
            menor = hayarMenor(df, isMenor)
             #Imprimimos el resultado fin
            print(restarMenorRestantes(intersection(df,menor,cant_inter),menor))

            # Renombrar las filas
            columnas.append("Ficticia")
            df.index = filas
            # Renombrar las columnas
            df.columns = columnas
            print()
            #Imprimimos el resultado Final
            print(df)
            print()
            df = df.astype(float)
            #Imprimimos la asignación
            resolver_asignacion(df,df_original)
        else:
            # Renombrar las filas
            columnas.append("Ficticia")
            df.index = filas
            # Renombrar las columnas
            df.columns = columnas
            print()
            #Imprimimos el resultado Final
            print(df)
            print()
            df = df.astype(float)
            #Imprimimos la asignación
            resolver_asignacion(df,df_original)
            

def resolver_asignacion(df,df_original):
    # Asegurarse de que el DataFrame es cuadrado
    if df.shape[0] != df.shape[1]:
        print("El DataFrame debe ser cuadrado para usar el algoritmo de Munkres.")
        return

    # Convertir el DataFrame a una matriz de costos
    costos = df.to_numpy()

    # Usar el algoritmo de Munkres para encontrar la asignación óptima
    filas_asignadas, columnas_asignadas = linear_sum_assignment(costos)

    # Imprimir la asignación óptima y calculamos la suma o costo mínimo de la asignación
    cost_sum = 0
    print("Asignación óptima encontrada por el algoritmo de Munkres:")
    print()
    for fila, columna in zip(filas_asignadas, columnas_asignadas):
        print(f"Fila {df.index[fila]}, Columna {df.columns[columna]}: {costos[fila, columna]}")
        cost_sum += df_original.at[df_original.index[fila],df_original.columns[columna]]
    print("El costo mínimo de asignación es: ",cost_sum)

def menu():

    try:
        while True:

            res = 's'
            
            if res == 's':
                nameCandidato = input("Ingrese el nombre del candidato: ")
                type_problem = input("El problema es de maximización o minimización (Max/Min): ").lower()

                if type_problem != "max" and type_problem != "min":

                    print("Seleccione una opcion valida")
                    menu()

                # Solicitar al usuario los nombres de las columnas
                columnas = input("Ingrese los nombres de las columnas separados por comas: ").split(',')

                # Solicitar al usuario los nombres de las filas
                filas = input("Ingrese los nombres de las filas separados por comas: ").split(',')
                print()

                # Crear un DataFrame vacío con los nombres de las columnas y filas proporcionados
                df = pd.DataFrame(index=filas, columns=columnas)

                # Llenar el DataFrame con valores ingresados por el usuario
                for i, fila in enumerate(filas):
                    for j, columna in enumerate(columnas):
                        valor = int(input(f"Ingrese el valor para la fila {fila}, columna {columna}: "))
                        df.at[fila, columna] = valor


                if type_problem.lower() == 'max':
                    # Encontrar el valor máximo en todo el DataFrame
                    valor_maximo_total = df.max().max()
                    data_original = df
                    # Restar el valor máximo a cada elemento del DataFrame
                    df = df.applymap(lambda x: valor_maximo_total- x )

                    funcionCompletaMax(df,filas,columnas,data_original)
                else :
                    if len(columnas) > len(filas) :
                        cantidad_ceros_fic = df.shape[1]
                        aux = []
                        for i in range(cantidad_ceros_fic):
                            aux.append(1)
                        df.loc['Ficticia'] = aux

                        funcionSoloFilas(df,filas,columnas)

                    elif len(filas) > len(columnas) :
                        cantidad_ceros_fic = df.shape[0]
                        aux = []
                        for i in range(cantidad_ceros_fic):
                            aux.append(1)
                        df['Ficticia'] = aux
                        funcionSoloColumnas(df,filas,columnas)
                    else:
                        funcionCompleta(df,filas,columnas)
            else:
                break
    except:
        print("Ha ocurrido un error en la ejecución del programa vuelva a intentarlo: ")
        print()
        menu()
menu()