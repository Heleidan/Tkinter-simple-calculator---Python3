import tkinter as tk
from tkinter import END, messagebox

root = tk.Tk()
root.title("Calculadora")
root.config(width=400, height=500)
aux = 0
signo = ""

def operador(x):
    global signo, aux
    signo = x
    aux = float(txtDisplay.get())
    txtDisplay.delete(0, END)

def operacion():
    resultado = 0
    global signo, aux
    if signo == "+":
        resultado = aux + float(txtDisplay.get())
    elif signo == "-":
        resultado = aux - float(txtDisplay.get())
    elif signo == "*":
        resultado = aux * float(txtDisplay.get())
    elif signo == "/":
        try:
            resultado = aux / float(txtDisplay.get())
        except ZeroDivisionError:
            messagebox.showerror("Error", "No puedes dividir por cero.")
            return
    elif signo == "^":
        resultado = aux ** float(txtDisplay.get())
    elif signo == "%":
        resultado = aux % float(txtDisplay.get())
    elif signo == "sqrt":
        resultado = aux ** 0.5
    elif signo == "n!":
        resultado = 1
        for i in range(1, int(aux) + 1):
            resultado *= i
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, str(resultado))

def convertir_base(base):
    try:
        valor = int(txtDisplay.get())
        if base == "Bin-Dec":
            resultado = int(str(valor), 2)
        elif base == "Oct-Dec":
            resultado = int(str(valor), 8)
        elif base == "Hex-Dec":
            resultado = int(str(valor), 16)
        elif base == "Dec-Bin":
            resultado = bin(valor).replace("0b", "")
        elif base == "Dec-Oct":
            resultado = oct(valor).replace("0o", "")
        elif base == "Dec-Hex":
            resultado = hex(valor).replace("0x", "").upper()
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Entrada no válida para la conversión de base.")

txtDisplay = tk.Entry(root)
txtDisplay.place(x=10, y=20)

tk.Label(root, text="DEC:").place(x=10, y=40)
tk.Label(root, text="OCT:").place(x=10, y=60)
tk.Label(root, text="HEX:").place(x=10, y=80)
tk.Label(root, text="BIN:").place(x=10, y=100)

btnSuma = tk.Button(root, text="+", command=lambda: operador("+"))
btnSuma.place(x=280, y=300)

btnResta = tk.Button(root, text="-", command=lambda: operador("-"))
btnResta.place(x=280, y=340)

btnMultiplicacion = tk.Button(root, text="*", command=lambda: operador("*"))
btnMultiplicacion.place(x=320, y=300)

btnDivision = tk.Button(root, text="/", command=lambda: operador("/"))
btnDivision.place(x=320, y=340)

btnIgual = tk.Button(root, text="=", command=operacion)
btnIgual.place(x=320, y=380)

btnPotencia = tk.Button(root, text="^", command=lambda: operador("^"))
btnPotencia.place(x=200, y=300)

btnPorcentaje = tk.Button(root, text="%", command=lambda: operador("%"))
btnPorcentaje.place(x=200, y=340)

btnRaiz = tk.Button(root, text="sqrt", command=lambda: operador("sqrt"))
btnRaiz.place(x=240, y=300)

btnFactorial = tk.Button(root, text="n!", command=lambda: operador("n!"))
btnFactorial.place(x=240, y=340)

btnDecBin = tk.Button(root, text="Dec-Bin", command=lambda: convertir_base("Dec-Bin"))
btnDecBin.place(x=10, y=150)

btnDecOct = tk.Button(root, text="Dec-Oct", command=lambda: convertir_base("Dec-Oct"))
btnDecOct.place(x=10, y=180)

btnDecHex = tk.Button(root, text="Dec-Hex", command=lambda: convertir_base("Dec-Hex"))
btnDecHex.place(x=10, y=210)

btnBinDec = tk.Button(root, text="Bin-Dec", command=lambda: convertir_base("Bin-Dec"))
btnBinDec.place(x=100, y=150)

btnOctDec = tk.Button(root, text="Oct-Dec", command=lambda: convertir_base("Oct-Dec"))
btnOctDec.place(x=100, y=180)

btnHexDec = tk.Button(root, text="Hex-Dec", command=lambda: convertir_base("Hex-Dec"))
btnHexDec.place(x=100, y=210)

root.mainloop()
