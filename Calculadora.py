
import tkinter
valor1 = []
valor2 = []
valor3 = ['a']
operador = []
ultimo_resultado = []
resultado_final = []
ordem_valores = ['']
ordem_valores2 = ['']
operador_teste = ['1']
parametro = ''
operador1 = ''
limpar_numeros = 'false'
operador2 = []

def botao_igual():
    if len(valor1) == 0 or len(valor2) == 0 or len(operador) == 0:
        print('Insira os valores corretamente')
        return False

    if ordem_valores2[-1] in ['/', '*', '-', '+']:
        print('Insira mais um valor')
        return False

    resultado = ''
    numero1 = ''.join(valor1)
    numero2 = ''.join(valor2)
    operado = operador[-1]
    parametro = 'false'
    if len(ultimo_resultado) != 0: resultado = ultimo_resultado[-1]
    if len(valor3) > 1:
        numero3 = ''.join(valor3[1:])
        if operado == '+':
            somar(resultado, numero3,parametro)
        elif operado == '-':
            subtracao(resultado,numero3,parametro)
        elif operado == '/':
            divisao(resultado, numero3,parametro)
        elif operado == '*':
            multiplicacao(resultado, numero3,parametro)
    else:
        if operado == '+':
            somar(numero1, numero2,parametro)
        elif operado == '-':
            subtracao(numero1,numero2,parametro )
        elif operado == '/':
            divisao(numero1, numero2,parametro)
        elif operado == '*':
            multiplicacao(numero1, numero2,parametro)

def limpar_tudo():
    mostrar_valor.config(state='normal')
    mostrar_valor.delete(0,tkinter.END)
    mostrar_valor.config(state='disabled')
    valor3.clear()
    valor3.append('a')
    valor1.clear()
    valor2.clear()
    operador.clear()
    ordem_valores.clear()
    ultimo_resultado.clear()


def exibir_valores(numero):
    mostrar_valor.config(state='normal')
    numero = str(numero)

    if ordem_valores and ordem_valores[-1] == '.' and numero == '.':

        print('Não é possivel inserir dois pontos seguidos')
        return False

    if numero == '.' and len(operador) == 2:
        print('Não é possivel inserir um ponto apos um operador')
        return False

    if len(ordem_valores) == 1  and numero == '.' and len(valor2) == 0 and len(operador) == 0 and len(valor1) == 0:
        print('O primeiro valor não pode ser um ponto')
        return False

    if len(ordem_valores) > 1 and numero == '0' and valor1[0] == '0' and len(valor2) == 0:
        print('Não é possivel inserir dois numeros zeros no inicio')
        return False

    if ordem_valores2[-1] in ['/','*','-','+'] and numero == '.':
        print('Não é possivel inserir um ponto apos um operador')
        return False

    if ordem_valores2[-1] in ['/', '*', '-', '+'] and numero in ['/', '*', '-', '+']:
        print('Não é possivel inserir dois operadores seguidos')
        return False

    #primeiro valor
    if numero not in ['/','*','-','+'] and len(valor2) == 0 and len(operador) == 0:
        if '.' in valor1 and numero == '.':
            print('Nao é possivel adicionar mais de um ponto em um valor')
            return False
        valor1.append(numero)
        ordem_valores.append(numero)
        ordem_valores2.append(numero)
        valor_formatado = str(ordem_valores[-1:]).strip("[]'")
        mostrar_valor.insert(tkinter.END, f'{valor_formatado}')


    elif numero in ['/','*','-','+'] and ordem_valores[-1] in ['/','*','-','+']:
        print('Não é possivel inserir dois operadores seguidos')
        return False


    elif numero in ['/','*','-','+'] and len(valor1) != 0 and len(valor2) == 0:
        operador.append(numero)
        ordem_valores.append(numero)
        ordem_valores2.append(numero)
        mostrar_valor.insert(tkinter.END, f'{operador[-1]}')


    elif numero not in ['/','*','-','+'] and len(operador) != 0 and len(valor1) != 0 and valor3[0] == 'a':
        if '.' in valor2 and numero == '.':
            print('Nao é possivel adicionar mais de um ponto em um valor')
            return False
        valor2.append(numero)
        ordem_valores.append(numero)
        ordem_valores2.append(numero)
        mostrar_valor.insert(tkinter.END, f'{numero}')


    elif numero in ['/','*','-','+'] and len(operador) != 0 and len(valor1) != 0 and len(valor2) != 0 and valor3[0] == 'a' or valor3[0] == 'b' and operador_teste[0] == '1':
        global operador1
        operador1 = numero
        parametro = 'true' # essa variavel vai definir se o operador vai aparecer junto com o resultado ou nao
        numero1 = ''.join(valor1)
        numero2 = ''.join(valor2)
        operado = operador[-1]
        operador2.append(numero)
        if operado == '+':
            somar(numero1,numero2,parametro)
        elif operado == '-':
            subtracao(numero1,numero2,parametro)
        elif operado == '/':
            divisao(numero1,numero2,parametro)
        elif operado == '*':
            multiplicacao(numero1,numero2,parametro)

        mostrar_valor.insert(tkinter.END, f'{numero}')
        parametro = 'false'
        ordem_valores2.append(numero)


    elif numero not in ['/','*','-','+'] and len(valor1) != 0 and len(valor2) != 0 and len(operador) != 0 and valor3[0] == 'b' :
        if '.' in valor3 and numero == '.':
            print('Nao é possivel adicionar mais de um ponto em um valor')
            return False
        valor3.append(numero)
        ordem_valores.append(numero)
        ordem_valores2.append(numero)
        valor_formatado = str(ordem_valores[-1:]).strip("[]'")
        mostrar_valor.insert(tkinter.END, f'{valor_formatado}')
        operador_teste[0] = '10'

    elif numero in ['/','*','-','+'] and len(valor1) != '' and len(valor2) != '' and len(valor3) != '' and valor3[0] == 'b' and operador_teste[0] == '10':
        operador1 = numero
        parametro = 'true'
        resultado = ultimo_resultado[-1]
        operado = operador2[-1]
        numero1 = ''.join(valor3[1:])
        if operado == '+':
            somar(numero1,resultado,parametro)
        elif operado == '-':
            subtracao(resultado,numero1,parametro)
        elif operado == '/':
            divisao(resultado,numero1,parametro)
        elif operado == '*':
            multiplicacao(numero1,resultado,parametro)
        parametro = 'false'
        valor3[1:].clear()
        ordem_valores2.append(numero)
        operador2.append(numero)
    mostrar_valor.config(state='disabled')


def somar(num1,num2,parametro):
    soma = float(num1)+float(num2)
    operador_teste[0] = '5'
    mostrar_valor.config(state='normal')
    mostrar_valor.delete(0,tkinter.END)
    if parametro == 'true':
        mostrar_valor.insert(tkinter.END,f'{soma:.2f}{operador1}')
        #operador.append(operador1)
    else:
        mostrar_valor.insert(tkinter.END,f'{soma:.2f}')
    mostrar_valor.config(state='disabled')
    ultimo_resultado.append(str(soma))
    valor3.clear()
    valor3.append('b')
    resultado_final.clear()
    resultado_final.append(soma)
    return print(f'{soma:.2f}')

def subtracao(num1,num2,parametro):
    subtrair = float(num1)-float(num2)
    operador_teste[0] = '5'
    mostrar_valor.config(state='normal')
    mostrar_valor.delete(0, tkinter.END)
    if parametro == 'true':
        mostrar_valor.insert(tkinter.END, f'{subtrair:.2f}{operador1}')
        #operador.append(operador1)
    else:
        mostrar_valor.insert(tkinter.END, f'{subtrair:.2f}')
    mostrar_valor.config(state='disabled')
    valor3.clear()
    valor3.append('b')
    resultado_final.clear()
    resultado_final.append(subtrair)
    ultimo_resultado.append(str(subtrair))
    return print(f'{subtrair:.2f}')

def divisao(num1,num2,parametro):
    dividir = float(num1)/float(num2)
    operador_teste[0] = '5'
    mostrar_valor.config(state='normal')
    mostrar_valor.delete(0, tkinter.END)
    if parametro == 'true':
        mostrar_valor.insert(tkinter.END, f'{dividir:.2f}{operador1}')
    else:
        mostrar_valor.insert(tkinter.END, f'{dividir:.2f}')
    mostrar_valor.config(state='disabled')
    resultado_final.clear()
    resultado_final.append(dividir)
    valor3.clear()
    valor3.append('b')
    ultimo_resultado.append(str(dividir))
    return print(f'{dividir:.2f}')

def multiplicacao(num1,num2,parametro):
    multiplicar = float(num1)*float(num2)
    operador_teste[0] = '5'
    mostrar_valor.config(state='normal')
    mostrar_valor.delete(0, tkinter.END)
    if parametro == 'true':
        mostrar_valor.insert(tkinter.END, f'{multiplicar:.2f}{operador1}')
    else:
        mostrar_valor.insert(tkinter.END, f'{multiplicar:.2f}')
    mostrar_valor.config(state='disabled')
    valor3.clear()
    valor3.append('b')
    resultado_final.clear()
    resultado_final.append(multiplicar)
    ultimo_resultado.append(str(multiplicar))
    return print(f'{multiplicar:.2f}')

def mostrar(numero):
    mostrar_valor.config(state='normal')
    mostrar_valor.delete(0,tkinter.END)
    mostrar_valor.insert(tkinter.END, f'{numero:.2f}')
    mostrar_valor.config(state='disabled')


janela = tkinter.Tk()
janela.geometry('320x320')
janela.minsize(320,320)
janela.maxsize(320,320)
janela.title('Calculadora')


mostrar_valor = tkinter.Entry(janela,font=('Arial',24),justify='right')
mostrar_valor.pack()
mostrar_valor.config(state='disabled')
cor1 = '#DB0000'
cor = '#C8C4C4'
botao1 = tkinter.Button(janela,text='1',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('1'))
botao1.place(x=1,y=90)

botao2 = tkinter.Button(janela,text='2',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('2'))
botao2.place(x=81,y=90)

botao3 = tkinter.Button(janela,text='3',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('3'))
botao3.place(x=161,y=90)

botao4 = tkinter.Button(janela,text='4',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('4'))
botao4.place(x=1,y=148)

botao5 = tkinter.Button(janela,text='5',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('5'))
botao5.place(x=81,y=148)

botao6 = tkinter.Button(janela,text='6',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('6'))
botao6.place(x=161,y=148)

botao7 = tkinter.Button(janela,text='7',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('7'))
botao7.place(x=1,y=206)

botao8 = tkinter.Button(janela,text='8',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('8'))
botao8.place(x=81,y=206)

botao9 = tkinter.Button(janela,text='9',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('9'))
botao9.place(x=161,y=206)

botao0 = tkinter.Button(janela,text='0',font=('Calibri',20),background=cor,width=11,command= lambda:exibir_valores('0'))
botao0.place(x=1,y=264)

ponto = tkinter.Button(janela,text='.',font=('Calibri',20),background=cor,width=5,command= lambda:exibir_valores('.'))
ponto.place(x=160,y=264)

sinal_mais = tkinter.Button(janela, text='+',font=('Calibri',18),background=cor1,width=6,command= lambda:exibir_valores('+'))
sinal_mais.place(x=239,y=40)

sinal_menos = tkinter.Button(janela, text='-',font=('Calibri',20),background=cor1,width=5,command= lambda:exibir_valores('-'))
sinal_menos.place(x=241,y=90)

sinal_dividir = tkinter.Button(janela, text='/',font=('Calibri',20),background=cor1,width=5,command= lambda:exibir_valores('/'))
sinal_dividir.place(x=241,y=148)

sinal_multiplicar = tkinter.Button(janela, text='*',font=('Calibri',20),background=cor1,width=5,command= lambda:exibir_valores('*'))
sinal_multiplicar.place(x=241,y=206)

sinal_igual = tkinter.Button(janela, text='=',font=('Calibri',20),background=cor1,width=5,command= botao_igual)
sinal_igual.place(x=240,y=264)

limpar = tkinter.Button(janela,text='C',font=('Calibri',17),background=cor1,width=19,command= limpar_tudo)
limpar.place(x=1,y=41)

frame = tkinter.Frame(janela,background=cor1,height=49,width=2)
frame.place(x=131,y=41)
janela.mainloop()

