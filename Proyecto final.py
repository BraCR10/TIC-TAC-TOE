import random

'''def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print('+-','-'*28,'+',sep='')
    print('|',' '*7,'TIC-TAC-TOE',' '*7,'|')
    cont=0
    while cont<3:#Repite la tarea 3 veces
        #Linea horizontal 
        for i in range(30):
            if(i%10==0):
                print('+',end='')
                continue
            print('-',end='')
        else:
            print('+\n',end='')
        
        #Linea verticales vacias
        for i in range(30):
            if(i%10==0):
                print('|',end='         ')
        else:
            print('|',end='')
        
        #Linea verticales con datos
        row=0
        if cont==1:
            row=1
        elif cont==2:
            row=2
        colum=0
        print('')
        for i in range(30):
            if(i%10==0):
                print('|',end='    ')
                print(board[row][colum],end='    ')
                colum+=1
        else:
            print('|')
                
        #Linea vertical vacia
        for i in range(30):
            if(i%10==0):
                print('|',end='         ')
        else:
            print('|')    
        cont+=1
    else:
        #Linea horizontal arriba
        for i in range(30):
            if(i%10==0):
                print('+',end='')
                continue
            print('-',end='')
        else:
            print('+\n',end='')'''

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print('+-','-'*28,'+',sep='')
    print('|',' '*7,'TIC-TAC-TOE',' '*7,'|')
    print('+-','-'*8,'+','-'*9,'+','-'*9,'+',sep='')   
    for row in range(3):
        print('|         '*4)
        for colum in range(3):
            print('|    ',end='')
            print(board[row][colum],end='    ')
        print('|')
        print('|         '*4)
        print('+-','-'*8,'+','-'*9,'+','-'*9,'+',sep='')
        
def enter_move(board,checkS,dicc):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        num=int(input('Ingrese un numero para insertar la figura: '))
        if num<=0 or num>9:#Evitar un numero no valido
            print('Esa casilla no existe! ')
            continue
        if num in checkS:#Verifica que el numero no este ya usado
            print('Ya esa casilla no esta disponible, ingrese otra: ')
            continue
        checkS.append(num)
        break 
    if num in dicc:#Insertar el valor en el tablero
        board[dicc[num][0]][dicc[num][1]]='O'
    del dicc[num]
    
def draw_move(board,checkS,dicc):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    print('\n --Ahora es turno de la maquina!:')
    while True:
        numMachine=random.randrange(10)#Escoje un numero random del 1 al 9
        checkS.append(numMachine)
        if numMachine in dicc:#Insertar el valor en el tablero
            board[dicc[numMachine][0]][dicc[numMachine][1]]='X'
            break
        elif len(dicc)==0:
            break
    if (len(dicc)>0):#Verifica que aun hay numero para jugar.
        del dicc[numMachine]
    
def victory_for(board, dicc):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    global win
    win = False
    #Verifica toda las horizontales
    if board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O'or board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O' or board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O':
        print('\n--Has ganado, felicidades!')    
        dicc.clear()
        win=True
    elif board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X' or board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X' or board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X':
        print('\n--He ganado yo!, suerte en la proxima')    
        dicc.clear()
        win=True
    #Verifica toda las verticales
    if board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O'or board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O' or board[2][2]=='O' and board[1][2]=='O' and board[0][2]=='O':
        print('\n--Has ganado, felicidades!')    
        dicc.clear()
        win=True
    elif board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X'or board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X' or board[2][2]=='X' and board[1][2]=='X' and board[0][2]=='X':
        print('\n--He ganado yo!, suerte en la proxima')    
        dicc.clear()  
        win=True     
    #Verifica toda las diagonales
    if board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O':
        print('\n--Has ganado, felicidades!')    
        dicc.clear()
        win=True
    elif board[0][2]=='O' and board[1][1]=='O' and board[2][1]=='O':
        print('\n--He ganado yo!, suerte en la proxima')    
        dicc.clear() 
        win=True

'''
def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
'''

#Main
try:
    board=[
            [1,2,3],
            [4,5,6],
            [7,8,9]]
    checker=[]#Para evitar datos repetidos
    dicc={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}#Se utiliza como clave para cada casilla
    while True:
        display_board(board)
        enter_move(board,checker,dicc)
        draw_move(board,checker,dicc)
        victory_for(board, dicc)
        if len(dicc)==0:break
    display_board(board)
    if win==False:
        print('\n --Ha terminado el juego, no hubo un ganador!')
except ValueError:
    print('Algo salio mal!, reinicia el programa')
except TypeError:
    print('Algo salio mal!, reinicia el programa')
except SyntaxError:
    print('Algo salio mal!, reinicia el programa')
except AttributeError:
    print('Algo salio mal!, reinicia el programa')
