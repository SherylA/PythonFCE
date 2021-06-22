import pandas as pd
import numpy as np
from inspect import isfunction
from IPython.core.display import display, HTML

m = [ 0.13990557,  0.9871224 , 50.03588815, 47.06105197, 33.87407988, 49.82422904]
b = [19.01972647, 13.2165551 , 38.10707111, 62.86886669, 66.21730317, 13.06513052]

INIT_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

</style>
</head>
<body>

<h2>RESULTADOS</h2>

<table>
  <tr>
    <th>Prueba</th>
    <th>Resultado</th>
  </tr>
"""

END_HTML = """
</table>
</body>
</html>
"""

class Exercise:
    def __init__(self,number, Group=1, Id='123456789'):
        self.root = 'https://raw.githubusercontent.com/SherylA/PythonFCE/master/Datos/Datos_Ejercicio0/' 
        self.Group = Group
        self.Id = Id
        self.number = number
    
    def _lineHTML(self,test,result):
            if result == 'Failed':
                color = '#ff6666'
            elif result == 'Success':
                color = '#03AC13'
            elif result == 'Skipped':
                color = '#ED820E'

            line = f"""
            <tr>
            <td>{test}</td>
            <td style="background-color:{color};">{result} </td>
            </tr>"""

            return line

    def _checkEx0(self):
        self.failed = False
        self.success = False
        try:
            self.slope = m[self.Group]
            self.intercept = b[self.Group]
        except Exception as err:
            print(err)

    def _checkForNumber(self):
        if self.number == 0: 
            self._checkEx0()    
        elif self.number == 1:
            pass
    
    def chargeData_ej0(self):
        try:
            self._checkForNumber()
            path = self.root + f'grupo_{self.Group}.txt'
            print(f"Cargando archivo ubicado en {path}")
            data = pd.read_csv(path, sep=' ',header=None)
            data.columns = ['Y','X']
            self.dataY = data['Y'].values
            self.dataX = data['X'].values
            return data['Y'].values,data['X'].values
        except Exception as err:
            print(f"Estudiante {self.Id} ha sucedido un error en la lectura de los datos:")
            print(err)

    def _check_function(self, func):
        if not isfunction(func):
            self.failed = True
    
    def _check_slope_ej0(self, func):
        try:
            m, _ = func(self.dataY,self.dataX)
            if abs(m - self.slope) > 0.001:
                self.failed = True
        except Exception as err:
            self.failed = True

    def _check_intercept_ej0(self, func):
        try:
            _, b = func(self.dataY,self.dataX)
            if abs(b - self.intercept)>0.001:
                self.failed = True
        except Exception as err:
            self.failed = True

    def check_exercise(self, func):
        nameTest = ["Haz ingresado una función",
                     f"La pendiente es correcta, m = {self.slope}",
                     f"El intercepto con el eje y es correcto, b = {self.intercept}"
                    ]
        test = [self._check_function, self._check_slope_ej0, self._check_intercept_ej0]
        testResult = ['Skipped']*len(test)
        for i,t in enumerate(test):
            t(func)
            if self.failed:
                testResult[i] = 'Failed' 
                break
            testResult[i] = 'Success' 
        self.success = all([t=='Success' for t in testResult])
        middle_HTML = ""
        for i in range(len(test)):
            middle_HTML += self._lineHTML(nameTest[i],testResult[i]) + '\n'

        display(HTML(INIT_HTML + middle_HTML + END_HTML))

        
        



