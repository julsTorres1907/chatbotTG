import logging

from besser.bot.nlp.intent_classifier.intent_classifier_prediction import IntentClassifierPrediction
from besser.bot.core.bot import Bot
from besser.bot.core.session import Session
from besser.bot.library.entity.base_entities import number_entity

# Configuracion del modulo logging, para ver las acciones del bot en la terminal
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')

# Creacion del chatbot
bot = Bot('chatbot_project')

# Cargar las propiedades del bot almacenadas en el archivo config.ini
bot.load_properties('config.ini')

# Definir que plataforma va a utilizar el chatbot (websocket_platform)
websocket_platform = bot.use_websocket_platform(use_ui=True)

# ENTITIES - ENTIDADES

# Añade la entidad 'number_entity'
bot.add_entity(number_entity)

# STATES - ESTADOS
# Estado Inicial
initial_state = bot.new_state('initial_state', initial=True)

# Estados de las preguntas asociados con la base de conocimiento
pregunta1_state = bot.new_state('pregunta1_state')
pregunta2_state = bot.new_state('pregunta2_state')
pregunta3_state = bot.new_state('pregunta3_state')
pregunta4_state = bot.new_state('pregunta4_state')
pregunta5_state = bot.new_state('pregunta5_state')
pregunta6_state = bot.new_state('pregunta6_state')
pregunta7_state = bot.new_state('pregunta7_state')
pregunta8_state = bot.new_state('pregunta8_state')
pregunta9_state = bot.new_state('pregunta9_state')
pregunta10_state = bot.new_state('pregunta10_state')
pregunta11_state = bot.new_state('pregunta11_state')
pregunta12_state = bot.new_state('pregunta12_state')
pregunta13_state = bot.new_state('pregunta13_state')
pregunta14_state = bot.new_state('pregunta14_state')
pregunta15_state = bot.new_state('pregunta15_state')
pregunta16_state = bot.new_state('pregunta16_state')
pregunta17_state = bot.new_state('pregunta17_state')
pregunta19_state = bot.new_state('pregunta19_state')
pregunta20_state = bot.new_state('pregunta20_state')
pregunta21_state = bot.new_state('pregunta21_state')
pregunta22_state = bot.new_state('pregunta22_state')
pregunta23_state = bot.new_state('pregunta23_state')

# Estados para las preguntas que requieren hacer algun calculo
pre3_calculo_state = bot.new_state('pre3_calculo_state')
pre4_calculo_state = bot.new_state('pre4_calculo_state')
pre6_calculo_state = bot.new_state('pre6_calculo_state')
pre7_calculo_state = bot.new_state('pre7_calculo_state')
pre8_calculo_state = bot.new_state('pre8_calculo_state')
pre10_calculo_state = bot.new_state('pre10_calculo_state')
pre11_calculo_state = bot.new_state('pre11_calculo_state')
pre13_calculo_state = bot.new_state('pre13_calculo_state')
pre14_calculo_state = bot.new_state('pre14_calculo_state')
pre15_calculo_state = bot.new_state('pre15_calculo_state')
pre16_calculo_state = bot.new_state('pre16_calculo_state')
pre17_calculo_state = bot.new_state('pre17_calculo_state')
pre19_calculo_state = bot.new_state('pre19_calculo_state')
pre20_calculo_state = bot.new_state('pre20_calculo_state')
pre21_calculo_state = bot.new_state('pre21_calculo_state')
pre22_calculo_state = bot.new_state('pre22_calculo_state')
pre23_calculo_state = bot.new_state('pre23_calculo_state')

hello_state = bot.new_state('hello_state')
good_state = bot.new_state('good_state')
bad_state = bot.new_state('bad_state')
mensaje_por_defecto_state = bot.new_state('mensaje_por_defecto_state')

###########################################################################################
# INTENTS - INTENCIONES

# Inputs de usuario para las preguntas

#Crear intents que capturan numeros
number_intent = bot.new_intent('number_intent', [
    '{number:number_entity}'
])
# Definicion de parametros para capturar numeros
number_intent.parameter('value', 'number', number_entity)

# PREGUNTA #1 - ¿Que son las razones financieras?

pregunta1_intent = bot.new_intent('pregunta1_intent', [
    'que son las razones financieras',
    'que significa razones financieras',
    'a que se refiere las razones financieras',  
    'what are the financial ratios',
])

# PREGUNTA #2 - ¿Cuales son las razones financieras?
pregunta2_intent = bot.new_intent('pregunta2_intent', [
    'cuales son las razones financieras',
    'cuantas razones financieras',
    'dime las razones financieras que hay',
    'que factores financieros se consideran',
    'necesito conocer las razones financieras',
    'cuantas razones financieras existen',
    'por favor, enumera las razones financieras',
    'cuales son algunas de las razones financieras mas importantes',
    'dime sobre los indicadores financieros relevantes',
])

# PREGUNTA #3 - ¿Que son las razones de endeudamiento o apalancamiento?

pregunta3_intent = bot.new_intent('pregunta3_intent',[
    'que son las razones de endeudamiento o apalancamiento',
    'que son las razones de endeudamiento',
    'que son las razones de apalancamiento',
    'que es razon de endeudamiento',
    'que es razon de apalancamiento',
    'como se calcula la razon de endeudamiento',
    'como se calcula la razon de apalancamiento',
])

# PREGUNTA #4 - ¿Que es el indice de endeudamiento y como se calcula?

pregunta4_intent = bot.new_intent('pregunta4_intent', [
    'que es el indice de endeudamiento y como se calcula',
    'a que se refiere el indice de endeudamiento',
    'como se calcula el indice de endeudamiento',
    'explicame que significa el indice de endeudamiento y como se determina',
    'quisiera entender el concepto de indice de endeudamiento y su calculo',
    'podrias detallar que implica el indice de endeudamiento y como se formula',
    'necesito comprender el indice de endeudamiento y su formula de calculo',
    'cual es la definicion y el proceso para calcular el indice de endeudamiento',
    'hablame sobre el indice de endeudamiento y como se realiza su calculo',
    'que implica el termino indice de endeudamiento y como se determina',
    'quiero aprender sobre el indice de endeudamiento y su metodo de calculo',
    'por favor proporciona informacion sobre el indice de endeudamiento y su formula',
])

# PREGUNTA #5 - ¿Que son las razones de liquidez?

pregunta5_intent = bot.new_intent('pregunta5_intent', [
    'que son las razones de liquidez',
    'razones de liquidez',
    'necesito entender las razones de liquidez',
    'dime sobre las razones de liquidez',
    'podrias explicar las razones de liquidez',
    'que implica el concepto de razones de liquidez',
    'cuales son las razones de liquidez',
    'quiero saber mas acerca de las razones de liquidez',
    'cual es la importancia de las razones de liquidez',
])

# PREGUNTA #6 - ¿Que es la razon corriente y como se cálcula?

pregunta6_intent = bot.new_intent('pregunta6_intent', [
    'que es la razon corriente y como se calcula',
    'que es la razon corriente',
    'como se calcula la razon corriente',
    'necesito entender la razon corriente y su calculo',
    'dime sobre la razon corriente y su formula',
    'podrias explicar la razon corriente y su calculo',
    'que implica el concepto de razon corriente',
    'quiero saber mas sobre la razon corriente y su calculo',
    'cual es la importancia de la razon corriente en finanzas',
])

# PREGUNTA #7 - ¿Que es la prueba ácida y como se cálcula?

pregunta7_intent = bot.new_intent('pregunta7_intent', [
    'que es la prueba acida y como se calcula',
    'que es la prueba acida',
    'como se calcula la prueba acida',
    'a que se refiere la prueba acida y como se calcula',
    'necesito entender la prueba acida y su calculo',
    'dime sobre la prueba acida y su formula',
    'podrias explicar la prueba acida y su calculo',
    'que implica el concepto de prueba acida',
    'quiero saber mas sobre la prueba acida y su calculo',
])

# PREGUNTA #8 - ¿Que es la prueba de efectivo y como se cálcula?

pregunta8_intent = bot.new_intent('pregunta8_intent', [
    'que es la prueba de efectivo y como se calcula',
    'que es la prueba de efectivo',
    'como se calcula la prueba de efectivo',
    'a que se refiere la prueba de efectivo y como se calcula',
    'necesito entender la prueba de efectivo y su calculo',
    'dime sobre la prueba de efectivo y su formula',
    'podrias explicar la prueba de efectivo y su calculo',
    'que implica el concepto de prueba de efectivo',
    'quiero saber mas sobre la prueba de efectivo y su calculo',
])

# PREGUNTA #9 - ¿Que son las razones de Rentabilidad?

pregunta9_intent = bot.new_intent('pregunta9_intent', [
    'que son las razones de rentabilidad',
    'que es razon de rentabilidad',
    'a que se refiere la razon de rentabilidad',
    'razon de rentabilidad',
    'necesito entender las razones de rentabilidad',
    'dime sobre las razones de rentabilidad',
    'podrias explicar las razones de rentabilidad',
    'que implica el concepto de razones de rentabilidad',
    'quiero saber mas acerca de las razones de rentabilidad',
])

# PREGUNTA #10 - ¿Que es el ROE o Retorno sobre el Patrimonio Neto y como se cálcula?

pregunta10_intent = bot.new_intent('pregunta10_intent', [
    'que es el roe y como se calcula',
    'que es el roe o retorno sobre el patrimonio neto y como se calcula',
    'retorno sobre el patrimonio neto',
    'RPN',
    'que es ROE',
    'que es RPN',
    'como se calcula el ROE',
    'como se calcula el RPN',
    'necesito entender el roe y su calculo',
    'dime sobre el roe y su formula',
    'podrias explicar el roe y su calculo',
    'que implica el concepto de roe',
    'quiero saber mas sobre el roe y su calculo',
])

# PREGUNTA #11 - ¿Que es el ROA y como se calcula?

pregunta11_intent = bot.new_intent('pregunta11_intent', [
    'que es el roa y como se calcula',
    'que es el roa o retorno sobre los activos y como se calcula',
    'retorno sobre los activos',
    'ROA',
    'que es ROA',
    'que es RSA',
    'como se calcula el ROA',
    'como se calcula el RSA',
    'necesito entender el roa y su calculo',
    'dime sobre el roa y su formula',
    'podrias explicar el roa y su calculo',
    'que implica el concepto de roa',
    'quiero saber mas sobre el roa y su calculo',
])

# PREGUNTA #12 - ¿Que es un indicador de actividad o Ratios?

pregunta12_intent = bot.new_intent('pregunta12_intent', [
    'que es un indicador de actividad o ratios',
    'que es ratios',
    'que es un indicador de actividad',
    'indicador de actividad',
    'ratios',
    'necesito entender los indicadores de actividad o ratios',
    'dime sobre los ratios y su uso',
    'podrias explicar los indicadores de actividad o ratios',
    'que implica el concepto de indicadores de actividad',
    'quiero saber mas sobre los indicadores de actividad o ratios',
])

# PREGUNTA #13 - ¿Que es la rotacion de cartera y como se cálcula?

pregunta13_intent = bot.new_intent('pregunta13_intent', [
    'que es la rotacion de cartera y como se calcula',
    'que es la rotacion de cartera',
    'que es rotacion de cartera',
    'como se calcula la rotacion de cartera',
    'rotacion de cartera que es',
    'necesito entender la rotacion de cartera y su calculo',
    'dime sobre la rotacion de cartera y su formula',
    'podrias explicar la rotacion de cartera y su calculo',
    'que implica el concepto de rotacion de cartera',
    'quiero saber mas sobre la rotacion de cartera y su calculo',
])

# PREGUNTA #14 - ¿Cual es la formula para el cálculo de los días de Cartera?

pregunta14_intent = bot.new_intent('pregunta14_intent', [
    'cual es la formula para el calculo de los dias de cartera',
    'calculo dias de cartera',
    'como se calcula los dias de cartera',
    'formula para calcular dias de cartera',
    'dias de cartera formula',
    'necesito entender la formula para calcular los dias de cartera',
    'podrias explicar la formula para calcular los dias de cartera',
    'que implica el concepto de dias de cartera',
    'quiero saber mas sobre la formula para calcular los dias de cartera',
])

# PREGUNTA #15 - ¿Que es la rotacion de inventarios y como se cálcula?

pregunta15_intent = bot.new_intent('pregunta15_intent', [
    'que es la rotacion de inventarios y como se calcula',
    'que es la rotacion de inventarios',
    'como se calcula la rotacion de inventarios',
    'necesito entender la rotacion de inventarios y su calculo',
    'dime sobre la rotacion de inventarios y su formula',
    'podrias explicar la rotacion de inventarios y su calculo',
    'que implica el concepto de rotacion de inventarios',
    'quiero saber mas sobre la rotacion de inventarios y su calculo',
])

# PREGUNTA #16 - ¿Cual es la formula para el cálculo de los días de Inventario?

pregunta16_intent = bot.new_intent('pregunta16_intent', [
    'cual es la formula para el calculo de los dias de inventario',
    'formula para el calculo de los dias de inventario',
    'formula de los dias de inventario',
    'como calcular los dias de inventario',
    'que es la formula para calcular los dias de inventario',
    'necesito saber la formula para calcular los dias de inventario',
    'podrias explicar la formula para calcular los dias de inventario',
    'quiero saber mas sobre la formula para calcular los dias de inventario',
])

# PREGUNTA #17 - ¿Que es la rotacion de proveedores o cuentas por pagar y como se cálcula?

pregunta17_intent = bot.new_intent('pregunta17_intent', [
    'que es la rotacion de proveedores o cuentas por pagar y como se calcula',
    'que es la rotacon de proveedores',
    'que son las cuentas por pagar y como se calcula',
    'que son las cuentas por pagar',
    'rotacion de proveedores o cuentas por pagar',
    'rotacion de proveedores',
    'rotacion de proveedores que es',
    'necesito entender la rotacion de proveedores o cuentas por pagar y su calculo',
    'dime sobre la rotacion de proveedores o cuentas por pagar y su formula',
    'podrias explicar la rotacion de proveedores o cuentas por pagar y su calculo',
    'que implica el concepto de rotacion de proveedores o cuentas por pagar',
    'quiero saber mas sobre la rotacion de proveedores o cuentas por pagar y su calculo',
])

# # PREGUNTA #18 - ¿Cual es la formula para el cálculo de los días de Inventario y que significa?

# pregunta18_intent = bot.new_intent('pregunta18_intent', [
#     'cual es la formula para el calculo de los dias de inventario y que significa',
#     'formula de los dias de inventario',
#     'cual es la formula para el calculo de los dias de inventario',
#     'que significa la formula de los dias de inventario',
#     'como calcular los dias de inventario y que representa',
#     'que implica la formula de los dias de inventario',
#     'podrias explicar la formula de los dias de inventario y su significado',
#     'quiero saber mas sobre la formula de los dias de inventario y su significado',
# ])

# PREGUNTA #19 - ¿Que es la rotacion de activos corrientes y como se cálcula?

pregunta19_intent = bot.new_intent('pregunta19_intent', [
    'que es la rotacion de activos corrientes y como se calcula',
    'que es la rotacion de activos corrientes',
    'como se calcula la rotación de activos corrientes',
    'como se calcula la rotacion de activos',
    'que significa la rotacion de activos corrientes',
    'podrias explicar la rotacion de activos corrientes y su calculo',
    'quiero saber mas sobre la rotacion de activos corrientes y su calculo',
])

# PREGUNTA #20 - ¿Cual es la formula para el cálculo de los días de activos corrientes?

pregunta20_intent = bot.new_intent('pregunta20_intent', [
    'cual es la formula para el calculo de los dias de activos corrientes',
    'formula para el calculo de los dias de activos corrientes',
    'como se calcula los dias de los de activos corrientes',
    'formula para calcular los dias de activos corrientes',
    'como calcular los dias de activos corrientes',
    'que implica la formula para calcular los dias de activos corrientes',
    'podrias explicar la formula para calcular los dias de activos corrientes',
    'quiero saber mas sobre la formula para calcular los dias de activos corrientes',
])

# PREGUNTA #21 - ¿Que es el Margen Bruto?

pregunta21_intent = bot.new_intent('pregunta21_intent', [
    'que es el margen bruto',
    'que significa margen bruto',
    'que quiere decir margen bruto',
    'margen bruto que es',
    'margen bruto definicion',
    'margen bruto explicacion',
    'puedes explicar el concepto de margen bruto',
    'quiero saber mas sobre el margen bruto',
])

# PREGUNTA #22 - ¿Que es el Margen Operacional?

pregunta22_intent = bot.new_intent('pregunta22_intent', [
    'que es el margen operacional',
    'que significa margen operacional',
    'que quiere decir margen operacional',
    'como se calcula el margen operacional',
    'margen operacional que es',
    'margen operacional definicion',
    'margen operacional explicacion',
    'puedes explicar el concepto de margen operacional',
    'quiero saber mas sobre el margen operacional',
])

# PREGUNTA #23 - ¿Que es el Margen Neto?

pregunta23_intent = bot.new_intent('pregunta23_intent', [
    'que es el margen neto',
    'que significa margen neto',
    'que quiere decir margen neto',
    'como se calcula el margen neto',
    'margen neto que es',
    'margen neto definicion',
    'margen neto explicacion',
    'puedes explicar el concepto de margen neto',
    'quiero saber mas sobre el margen neto',
])

###########################################################################################
# Saludo
hello_intent = bot.new_intent('hello_intent', [
    'hola',
    'hey',
    'buen dia',
    'buenos dias',
    'buenas noches',
    'que tal',
    'como va todo',
    'buenas',
    'como estas',
    'que pasa',
    'saludos',
    'hola bot',
    'que hay de nuevo',
    'que onda',
    'como te va',
    'hola amigo',
    'que cuentas',
    'hey como estas',
    'hola como te llamas',
    'hola que haces',
    'hola que pasa',
    'hola que hay',
    'hola todo bien',
    'hi',
    'hello',
    'whats up',
])

# Respuesta usuario saludo: Positivo
good_intent = bot.new_intent('good_intent', [
    'bien',
    'muy bien',
    'extremadamente bien',
    'feliz',
    'good',
])

# Respuesta usuario saludo: Negativo
bad_intent= bot.new_intent('bad_intent', [
    'mal',
    'me encuentro mal',
    'me encuentro fatal',
    'no muy bien',
])

# Intents cuando se le muestran al usuario las opciones de si desea realizar o no el cálculo
resp_si_intent = bot.new_intent('resp_si_intent', ['SI'])
resp_no_intent = bot.new_intent('resp_no_intent', ['NO'])

###########################################################################################
# FUNCIONES ADICIONALES

# Función para capturar variables y calcular
def capture_variables_and_calculate(session: Session, variable_names: list, calculation_function):
    current_var_index = session.get('current_var_index') or 0
    current_var_name = variable_names[current_var_index]
    #Verificar si el valor ya fue ingresado
    predicted_intent: IntentClassifierPrediction = session.predicted_intent
    number_param = predicted_intent.get_parameter('value')
    if number_param is None:
        # Si no se ha ingresado un valor, solicitarlo al usuario
        session.reply(f"Por favor, ingrese el valor de {current_var_name}.")
        return False
    # Capturar el valor de la variable actual
    number_value = number_param.value
    session.set(current_var_name, number_value)
    session.reply(f"El valor ingresado para {current_var_name} es {number_value}")
    # Avanzar al siguiente valor si es necesario
    if current_var_index < len(variable_names) - 1:
        session.set('current_var_index', current_var_index + 1)
        next_var_name = variable_names[current_var_index + 1]
        session.reply(f"Por favor, ingresa el valor de {next_var_name}.")
        return False # No hacer nada mas, esperar al siguiente input
    else:
        # Realizar el cálculo si todas las variables han sido capturadas
        result, interpretacion = calculation_function(session)
        # Formatear el resultado solo si es un numero
        if isinstance(result, (int,float)):
            result = f"{result:.6f}"
            
        session.reply(f"""
                El resultado es {result}. 
                \n{interpretacion}
        """)
        session.delete('current_var_index')
        for var_name in variable_names:
            session.delete(var_name)
        session.set('calculo_completado', True) # Marca el flujo de la funcion como completado en la variable calculo_completado
        return True # Indicar que la captura y calculo estan completos

# PREGUNTA #3 FUNCTION
def pre3_calculo(session: Session):
    activo = float(session.get('Activo Total'))
    patrimonio = float(session.get('Patrimonio'))
    apalancamiento = activo / patrimonio
    
    interpretacion = f"El apalancamiento calculado es {apalancamiento:.2f}. "
    
    # Interpretacion basada en el valor de endeudamiento
    if apalancamiento < 1:
        interpretacion += (
            "La empresa tiene más patrimonio que deuda, lo que significa que tiene una baja dependencia de fuentes de financiamiento externas. "
            "Esto sugiere que la empresa está en una posición financiera sólida y tiene menor riesgo de incumplimiento de pagos."
        )
    elif 1 <= apalancamiento <= 3:
        interpretacion += (
            "La empresa ha financiado sus activos tomando una cantidad moderada de deuda en comparación con su patrimonio. "
            "Este nivel de apalancamiento es considerado generalmente saludable, siempre que los retornos de la empresa superen los costos de la deuda."
        )
    else:
        interpretacion += (
            "La empresa ha financiado sus activos tomando una cantidad significativa de deuda en relación con su patrimonio, lo cual puede ser riesgoso. "
            "Si bien puede ser rentable si los retornos superan los costos de la deuda, este nivel de apalancamiento también aumenta el riesgo si los ingresos no son suficientes para cubrir los pagos de la deuda."
        )
    return apalancamiento, interpretacion


# PREGUNTA #4 FUNCTION
def calculate_endeudamiento(session: Session):
    pasivo = float(session.get('pasivo'))
    activo = float(session.get('activo'))
    endeudamiento = pasivo / activo
    
    # Interpretacion basada en el valor de endeudamiento
    if endeudamiento < 0.5:
        interpretacion = "El endeudamiento de la empresa es bajo."
    elif 0.5 <= endeudamiento <= 1:
        interpretacion = "El endeudamiento de la empresa es moderado"
    else:
        interpretacion = "El endeudamiento de la empresa es alto"
    return endeudamiento, interpretacion

# PREGUNTA #6 FUNCTION
def pre6_calculo(session: Session):
    activo = float(session.get('Activo corriente'))
    pasivo = float(session.get('Pasivo corriente'))
    razon_corriente = activo / pasivo
    
    if razon_corriente < 1:
        interpretacion = "Indica que la empresa tiene menos activos corrientes que pasivos corrientes, lo que podría ser una señal de problemas de liquidez y dificultades para cumplir con sus obligaciones a corto plazo."
    elif razon_corriente == 1:
        interpretacion = "Significa que los activos corrientes son exactamente iguales a los pasivos corrientes, lo que implica que la empresa apenas tiene lo suficiente para cubrir sus deudas a corto plazo."
    else:
        interpretacion = "Indica que la empresa tiene más activos corrientes que pasivos corrientes, lo que sugiere que está en una posición financiera cómoda para cubrir sus deudas a corto plazo."
    return razon_corriente, interpretacion

# PREGUNTA 7 FUNCTION
def pre7_calculo(session: Session):
    activo = float(session.get('Activo corriente'))
    inventario = float(session.get('Inventarios'))
    pasivo = float(session.get('Pasivo corriente'))
    prueba_acida = (activo - inventario) / pasivo
    
    if prueba_acida < 1:
        interpretacion = "Puede ser una señal de alerta, indicando que la empresa podría tener dificultades para cubrir sus obligaciones a corto plazo sin recurrir a la venta de inventarios o a otras fuentes de financiamiento."
    elif prueba_acida == 1:
        interpretacion = "Sugiere que la empresa tiene justo lo necesario en activos líquidos para cubrir sus pasivos corrientes."
    else:
        interpretacion = "Indica que la empresa tiene suficientes activos líquidos para cubrir sus pasivos corrientes, lo que sugiere una buena situación de liquidez."
    return prueba_acida, interpretacion

# PREGUNTA #8 FUNCTION
def pre8_calculo(session: Session):
    efectivo = float(session.get('Efectivo y Equivalentes de Efectivo'))
    pasivo = float(session.get('Pasivo Corriente'))
    prueba_efectivo = efectivo / pasivo
    
    if prueba_efectivo < 1:
        interpretacion = "Sugiere que la empresa no tiene suficiente efectivo disponible para pagar sus deudas a corto plazo sin recurrir a la venta de otros activos."
    elif prueba_efectivo == 1:
        interpretacion = "Significa que la empresa tiene justo suficiente efectivo para cubrir sus pasivos corrientes."
    else:
        interpretacion = "Indica que la empresa tiene más que suficiente efectivo y equivalentes de efectivo para cubrir sus deudas a corto plazo, lo que es una señal de una posición de liquidez muy sólida."
    return prueba_efectivo, interpretacion

# PREGUNTA #10 FUNCTION
def pre10_calculo(session: Session):
    utilidad = float(session.get('Utilidad Neta'))
    patrimonio = float(session.get('Patrimonio Neto'))
    roe = ((utilidad / patrimonio) * 100)
    
    if roe < 10:
        interpretacion = "Indica que la empresa tiene una baja rentabilidad sobre el patrimonio, lo que podría ser un signo de ineficiencia en la gestión del capital o de un entorno económico difícil."
    elif 10 <= roe <=20:
        interpretacion = "Sugiere que la empresa tiene una rentabilidad moderada sobre el patrimonio, lo cual es generalmente aceptable y podría indicar una gestión eficiente del capital."
    else: 
        interpretacion = "Indica que la empresa tiene una alta rentabilidad sobre el patrimonio, lo que es un signo positivo de eficiencia en la generación de beneficios para los accionistas."
        
    roe_formateado = f"{roe:.2f}%"
    return roe_formateado, interpretacion

# PREGUNTA #11 FUNCTION
def pre11_calculo(session: Session):
    utilidad = float(session.get('Utilidad Neta'))
    activo = float(session.get('Activos Totales'))
    roa = ((utilidad / activo) * 100)
    
    if roa < 5:
        interpretacion = "Indica que la empresa tiene una baja rentabilidad sobre sus activos, lo que podría ser un signo de ineficiencia en el uso de los recursos o de un entorno económico difícil."
    elif 5 <= roa <=10:
        interpretacion = "Sugiere que la empresa tiene una rentabilidad moderada sobre sus activos, lo cual es aceptable y podría indicar una gestión razonablemente eficiente."
    else: 
        interpretacion = "Indica que la empresa tiene una alta rentabilidad sobre sus activos, lo que es un signo positivo de eficiencia en la utilización de los recursos para generar beneficios."
        
    roa_formateado = f"{roa:.2f}%"
    return roa_formateado, interpretacion

# PREGUNTA #13 FUNCTION
def pre13_calculo(session: Session):
    credito = float(session.get('Ventas a Credito'))
    cuentas_cobrar = float(session.get('Promedio de Cuentas por Cobrar'))
    rotacion_cartera = credito / cuentas_cobrar
    
    interpretacion = f"Una rotación de cartera de {rotacion_cartera:.2f} indica que la empresa cobra sus cuentas por cobrar {rotacion_cartera:.2f} veces en un año, lo que es extremadamente rápido. "
    
    if rotacion_cartera > 50:
        interpretacion += (
            "Este nivel de rotación es inusualmente alto y podría interpretarse como una excelente eficiencia en la gestión del crédito. "
            "La empresa tiene una capacidad sobresaliente para convertir sus cuentas por cobrar en efectivo, lo que mejora su liquidez y reduce el riesgo de impago. "
            "Sin embargo, es importante considerar el contexto de la industria y las políticas de crédito de la empresa, ya que un valor tan alto podría también sugerir que la empresa está ofreciendo términos de crédito muy cortos a sus clientes, lo que podría afectar las relaciones comerciales a largo plazo."
        )
    else:
        interpretacion += (
            "Este nivel de rotación es típico o bajo, sugiriendo una eficiencia razonable en la gestión del crédito. "
            "La empresa tiene un ciclo de cobro que podría ser mejorado para aumentar su liquidez y reducir el riesgo de impago. "
            "Es recomendable revisar las políticas de crédito para asegurarse de que no se están dando términos demasiado largos a los clientes."
        )
    return rotacion_cartera, interpretacion

# PREGUNTA #14 FUNCTION
def pre14_calculo(session: Session):
    rotacion_cartera = float(session.get('Rotacion de Cartera'))
    dias_cartera = 365 / rotacion_cartera
    
    interpretacion = f"Los días de cartera calculados son {dias_cartera:.2f}. Esto indica que, en promedio, la empresa tarda {dias_cartera:.2f} días en cobrar sus cuentas por cobrar."
    
    if dias_cartera < 30:
        interpretacion += (
            " Un número bajo de días de cartera sugiere que la empresa cobra rápidamente a sus clientes, lo cual es positivo para la liquidez."
        )
    elif 30 <= dias_cartera <= 60:
        interpretacion += (
            " Un rango moderado de días de cartera es típico en muchas industrias y sugiere que la empresa mantiene un equilibrio razonable entre ventas y cobranzas."
        )
    else:
        interpretacion += (
            " Un número alto de días de cartera podría indicar problemas en la cobranza, lo que puede afectar la liquidez de la empresa y aumentar el riesgo de impago."
        )
    return dias_cartera, interpretacion

# PREGUNTA #15 FUNCTION
def pre15_calculo(session: Session):
    costos_ventas = float(session.get('Costos de Ventas'))
    inventario_promedio = float(session.get('Inventario Promedio'))
    rotacion_inventarios = costos_ventas / inventario_promedio
    
    interpretacion = f"La rotación de inventarios calculada es {rotacion_inventarios:.2f}. "
    
    if rotacion_inventarios > 8:
        interpretacion += (
            "Una alta rotación de inventarios indica que la empresa vende rápidamente su inventario, "
            "lo cual es positivo ya que sugiere una alta demanda de sus productos y una eficiente gestión de inventarios. "
            "Sin embargo, si la rotación es excesivamente alta, podría también indicar que la empresa está manteniendo un inventario demasiado bajo, "
            "lo que podría llevar a desabastecimientos."
        )
    elif 4 <= rotacion_inventarios <= 8:
        interpretacion += (
            "Una rotación de inventarios moderada sugiere que la empresa mantiene un buen equilibrio en la gestión de su inventario. "
            "Esto indica que la empresa tiene un flujo de inventario saludable y no está enfrentando problemas significativos en la venta de sus productos."
        )
    else:
        interpretacion += (
            "Una baja rotación de inventarios puede indicar problemas con la venta de los productos o un exceso de inventario. "
            "Esto puede resultar en mayores costos de almacenamiento y posibles pérdidas debido a la obsolescencia del inventario. "
            "Es recomendable revisar la estrategia de ventas o ajustar los niveles de inventario para mejorar esta situación."
        )
    return rotacion_inventarios, interpretacion

# PREGUNTA #16 FUNCTION
def pre16_calculo(session: Session):
    rotacion_inventarios = float(session.get('Rotacion de Inventarios'))
    dias_inventario = 365 / rotacion_inventarios

    interpretacion = f"Los días de inventario calculados son {dias_inventario:.2f}. Esto indica que, en promedio, la empresa tarda {dias_inventario:.2f} días en vender su inventario."
    
    if dias_inventario < 30:
        interpretacion += (
            " Un número bajo de días de inventario sugiere que la empresa vende rápidamente su inventario, lo cual es positivo ya que indica una alta demanda de sus productos y una eficiente gestión de inventarios."
        )
    elif 30 <= dias_inventario <= 60:
        interpretacion += (
            " Un rango moderado de días de inventario sugiere que la empresa mantiene un equilibrio adecuado en la gestión de su inventario. Esto indica que la empresa tiene un flujo de inventario saludable y está logrando vender sus productos en un plazo razonable."
        )
    else:
        interpretacion += (
            " Un número alto de días de inventario podría ser un indicio de problemas con la venta de los productos o un exceso de inventario. Esto puede generar mayores costos de almacenamiento y riesgos de obsolescencia. Es recomendable revisar la estrategia de ventas o ajustar los niveles de inventario para mejorar esta situación."
        )
    
    return dias_inventario, interpretacion

# PREGUNTA #17 FUNCTION
def pre17_calculo(session: Session):
    compras_credito = float(session.get('Compras a Credito'))
    promedio_cuentas_pagar = float(session.get('Promedio de Cuentas por Pagar'))
    rotacion_proveedores = compras_credito / promedio_cuentas_pagar
    
    interpretacion = f"La rotación de proveedores calculada es {rotacion_proveedores:.2f}. "
    
    if rotacion_proveedores > 10:
        interpretacion += (
            "Una alta rotación de proveedores indica que la empresa paga rápidamente a sus proveedores. "
            "Esto es positivo, ya que sugiere que la empresa mantiene buenas relaciones con sus proveedores y gestiona bien su flujo de caja. "
            "Sin embargo, si la rotación es excesivamente alta, podría también indicar que la empresa no está aprovechando plenamente los plazos de pago otorgados por los proveedores."
        )
    elif 5 <= rotacion_proveedores <= 10:
        interpretacion += (
            "Una rotación de proveedores moderada sugiere que la empresa gestiona sus pagos de manera equilibrada, "
            "aprovechando los plazos de pago pero sin retrasarse demasiado. Esto es generalmente un buen signo de una gestión financiera eficiente."
        )
    else:
        interpretacion += (
            "Una baja rotación de proveedores podría indicar que la empresa está tardando más en pagar a sus proveedores, "
            "lo que podría generar tensiones en las relaciones comerciales y potencialmente afectar su crédito. "
            "Es recomendable revisar la estrategia de pagos para evitar problemas a largo plazo."
        )
    
    return rotacion_proveedores, interpretacion

# PREGUNTA #18 FUNCTION
def pre19_calculo(session: Session):
    ventas = float(session.get('Ventas'))
    promedio_activos = float(session.get('Promedio de Activos Corrientes'))
    rotacion_activos = ventas / promedio_activos
    
    interpretacion = f"La rotación de activos corrientes calculada es {rotacion_activos:.2f}. "
    
    if rotacion_activos > 8:
        interpretacion += {
            "Una alta rotación de activos corrientes indica que la empresa está utilizando eficientemente sus activos corrientes para generar ventas, "
            "lo cual sugiere una buena gestión del capital de trabajo. Sin embargo, si la rotación es excesivamente alta, podría también indicar que "
            "la empresa podría estar operando con niveles demasiado bajos de activos corrientes, lo que podría poner en riesgo su liquidez."
        }
    elif 4 <= rotacion_activos <= 8:
        interpretacion += (
            "Una rotación de activos corrientes moderada sugiere que la empresa está utilizando sus activos corrientes de manera equilibrada para generar ventas. "
            "Esto indica una gestión adecuada del capital de trabajo, manteniendo un equilibrio saludable entre liquidez y eficiencia."
        )
    else:
        interpretacion += (
            "Una baja rotación de activos corrientes puede indicar que la empresa no está utilizando sus activos corrientes de manera efectiva para generar ingresos, "
            "lo que podría ser un signo de ineficiencia en la gestión del capital de trabajo. Es recomendable revisar la estrategia financiera para mejorar la utilización de estos activos."
        )
    
    return rotacion_activos, interpretacion

# PREGUNTA #20 FUNCTION
def pre20_calculo(session: Session):
    rotacion_activos = float(session.get('Rotacion de Activos Corrientes'))
    dias_activos_corrientes = 365 / rotacion_activos
    
    interpretacion = f"Los días de activos corrientes calculados son {dias_activos_corrientes:.2f}. Esto indica que, en promedio, la empresa tarda {dias_activos_corrientes:.2f} días en convertir sus activos corrientes en ventas."

    if dias_activos_corrientes < 45:
        interpretacion += (
            " Un número bajo de días de activos corrientes sugiere que la empresa está convirtiendo rápidamente sus activos en ventas, lo cual es positivo para la eficiencia operativa. "
            "Este nivel es generalmente deseable, pero es importante asegurar que no esté afectando la capacidad de la empresa para mantener una liquidez adecuada."
        )
    elif 45 <= dias_activos_corrientes <= 90:
        interpretacion += (
            " Un rango moderado de días de activos corrientes sugiere que la empresa tiene un equilibrio adecuado entre la eficiencia operativa y la liquidez. "
            "Esto indica que la empresa está manejando bien su capital de trabajo, manteniendo suficientes activos corrientes para cubrir sus necesidades operativas sin sacrificar la eficiencia."
        )
    else:
        interpretacion += (
            " Un número alto de días de activos corrientes puede indicar que la empresa está tardando demasiado en convertir sus activos en ventas, lo que podría ser un signo de ineficiencia en la gestión del capital de trabajo. "
            "Es recomendable revisar la estrategia financiera para mejorar la rotación de activos corrientes y reducir el riesgo de problemas de liquidez."
        )
    
    return dias_activos_corrientes, interpretacion

# PREGUNTA #21 FUNCTION
def pre21_calculo(session: Session):
    ingresos_netos = float(session.get('Ingresos Netos'))
    costos_ventas = float(session.get('Costos de Ventas'))
    
    # Cálculo del Margen Bruto
    margen_bruto = ((ingresos_netos - costos_ventas) / ingresos_netos) * 100
    
    # Interpretación del resultado
    interpretacion = f"El margen bruto calculado es {margen_bruto:.2f}%. "
    
    if margen_bruto > 50:
        interpretacion += (
            "Un margen bruto superior al 50% indica que la empresa tiene un alto grado de rentabilidad en la venta de sus productos o servicios, "
            "lo que sugiere una fuerte ventaja competitiva o un control eficiente sobre los costos de producción."
        )
    elif 30 <= margen_bruto <= 50:
        interpretacion += (
            "Un margen bruto entre el 30% y el 50% es común en muchas industrias y sugiere que la empresa mantiene un buen equilibrio entre ingresos y costos de producción. "
            "Este nivel de margen es saludable y permite a la empresa cubrir sus gastos operativos y generar beneficios."
        )
    else:
        interpretacion += (
            "Un margen bruto inferior al 30% puede indicar que la empresa está enfrentando desafíos en el control de sus costos de producción o en la fijación de precios. "
            "Es recomendable revisar la estrategia de costos y precios para mejorar la rentabilidad."
        )
    margen_bruto_formateado = f"{margen_bruto:.2f}%"
    return margen_bruto_formateado, interpretacion

# PREGUNTA #22 FUNCTION
def pre22_calculo(session: Session):
    utilidad_operativa = float(session.get('Utilidad Operativa'))
    ventas_netas = float(session.get('Ventas Netas'))
    margen_operacional = (utilidad_operativa / ventas_netas) * 100
    
    interpretacion = f"El margen operacional calculado es {margen_operacional:.2f}%. "
    
    if margen_operacional > 20:
        interpretacion += (
            "Un margen operacional superior al 20% indica que la empresa es altamente eficiente en sus operaciones, "
            "lo que sugiere una excelente gestión de costos y una fuerte posición competitiva en el mercado."
        )
    elif 10 <= margen_operacional <= 20:
        interpretacion += (
            "Un margen operacional entre el 10% y el 20% indica una eficiencia operativa razonable, "
            "lo que sugiere que la empresa tiene un buen control sobre sus costos y una posición competitiva aceptable."
        )
    else:
        interpretacion += (
            "Un margen operacional por debajo del 10% puede indicar que la empresa enfrenta altos costos operativos en relación con sus ventas, "
            "lo que podría ser un signo de ineficiencia en la gestión de costos o una fuerte competencia en el mercado."
        )
    margen_operacional_formateado = f"{margen_operacional:.2f}%"
    return margen_operacional_formateado, interpretacion

#PREGUNTA #23 FUNCTION
def pre23_calculo(session: Session):
    utilidad_neta = float(session.get('Utilidad Neta'))
    ventas_netas = float(session.get('Ventas Netas'))
    margen_neto = (utilidad_neta / ventas_netas) * 100
    
    interpretacion = f"El margen neto calculado es {margen_neto:.2f}%. "
    
    if margen_neto > 20:
        interpretacion += (
            "Un margen neto superior al 20% indica que la empresa tiene un alto grado de rentabilidad en la venta de sus productos o servicios, "
            "lo que sugiere una gestión muy eficiente, una sólida ventaja competitiva y un control efectivo sobre los costos."
        )
    elif 10 <= margen_neto <= 20:
        interpretacion += (
            "Un margen neto entre 10% y 20% sugiere que la empresa es razonablemente rentable, "
            "lo que indica una buena gestión de los costos y una sólida rentabilidad."
        )
    else:
        interpretacion += (
            "Un margen neto inferior al 10% puede indicar que la empresa enfrenta desafíos para controlar sus costos "
            "o que está operando en un entorno altamente competitivo, lo que reduce su capacidad para retener ganancias."
        )
    margen_neto_formateado = f"{margen_neto:.2f}%"
    return margen_neto_formateado, interpretacion

###########################################################################################
# STATES BODIES' DEFINITION + TRANSITIONS

# Cuando el flujo de conversacion vuelve a initial_state, la variable 'calculo_completado' se cambia a false para que el usuario pueda seguirle solicitando calculos al bot
def initial_state_body(session: Session):
    session.set('calculo_completado', False)
    session.set('current_var_index', 0)

initial_state.set_body(initial_state_body)

# RESPUESTAS PARA EL CHATBOT

# RESPUESTA #1 - ¿Que son las razones financieras?
initial_state.when_intent_matched_go_to(pregunta1_intent, pregunta1_state)

def pregunta1_body(session: Session):
    session.reply('Las razones financieras son herramientas utilizadas para analizar y evaluar la salud financiera de una empresa. Se calculan a partir de datos financieros de una empresa, como los estados financieros, y proporcionan información clave sobre su desempeño y solidez financiera. Estas razones se dividen en diferentes categorías, como liquidez, rentabilidad, endeudamiento y eficiencia, y ayudan a los inversionistas, analistas y gerentes a comprender mejor diversos aspectos de la situación financiera de una empresa. Ejemplos comunes de razones financieras incluyen el ratio de liquidez, el retorno sobre la inversión (ROI), el ratio de endeudamiento, entre otros.')

pregunta1_state.set_body(pregunta1_body)
pregunta1_state.go_to(initial_state)

###########################################################################################
# RESPUESTA #2 - ¿Cuales son las razones financieras?
initial_state.when_intent_matched_go_to(pregunta2_intent, pregunta2_state)

def pregunta2_body(session: Session):
    session.reply("""
            **Razones de liquidez:** Mide la disponibilidad de recursos de corto plazo para atender sus obligaciones más próximas
            \n**Razones de endeudamiento o apalancamiento:** Mide el nivel de endeudamiento y la capacidad para asumir nuevos pasivos. (apalancamiento)
            \n**Razones de rentabilidad:** Permite evaluar que tan rentable son las diferentes etapas del negocio así como la empresa.
            \n**Razones de cobertura:** Identifican la capacidad de la empresa para cubrir con diferentes tipos de obligaciones, en especial las financieras.
            """)

pregunta2_state.set_body(pregunta2_body)
pregunta2_state.go_to(initial_state)

###########################################################################################
# RESPUESTA #3 - ¿Que son las razones de endeudamiento o apalancamiento?
initial_state.when_intent_matched_go_to(pregunta3_intent, pregunta3_state)

def pregunta3_body(session: Session):
    session.reply("""
                Las **razones de apalancamiento** es una métrica que mide el grado en que una empresa utiliza deuda para financiar sus actividades y su crecimiento. Es crucial porque proporciona una idea clara del riesgo que asume la empresa al usar capital externo. Un mayor apalancamiento significa que la empresa tiene más deuda en comparación con su patrimonio, lo que puede incrementar la rentabilidad para los accionistas, pero también eleva el riesgo de insolvencia si no se genera suficiente rentabilidad para cubrir los pagos de deuda.
                \n**Fórmula:**
                \n**Apalancamiento =** Activo Total / Patrimonio
                \nEste indicador refleja la capacidad de una empresa para operar utilizando recursos financiados externamente (deuda), en lugar de depender únicamente del capital propio o patrimonio. Específicamente, el indicador de apalancamiento muestra cuántas veces la empresa toma deuda en relación con su capital propio, proporcionando una visión clara sobre su nivel de endeudamiento y la exposición al riesgo.
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Apalancamiento de la empresa**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta3_state.set_body(pregunta3_body)

pregunta3_state.when_intent_matched_go_to(resp_si_intent, pre3_calculo_state)
pregunta3_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta3_state.when_no_intent_matched_go_to(initial_state)

def pre3_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Activo Total', 'Patrimonio'], pre3_calculo)
    
pre3_calculo_state.set_body(pre3_calculo_body)

pre3_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre3_calculo_state.when_intent_matched_go_to(number_intent, pre3_calculo_state)
pre3_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #4 - ¿Qué es el índice de endeudamiento y cómo se calcula?
initial_state.when_intent_matched_go_to(pregunta4_intent, pregunta4_state)

def pregunta4_body(session: Session):
    session.reply("""
        El **índice de endeudamiento** mide qué cantidad de deuda externa utiliza una empresa para financiar sus activos en relación con su patrimonio neto.
        \n**Fórmula:**
        \n**Endeudamiento =** pasivo total / activo total
    """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Ìndice de endeudamiento**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta4_state.set_body(pregunta4_body)

# Transiciones basadas en la respuesta del usuario
pregunta4_state.when_intent_matched_go_to(resp_si_intent, pre4_calculo_state)
pregunta4_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta4_state.when_no_intent_matched_go_to(initial_state)

def pre4_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['pasivo', 'activo'], calculate_endeudamiento)

pre4_calculo_state.set_body(pre4_calculo_body)

# Configurar transiciones para capturar numeros
pre4_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre4_calculo_state.when_intent_matched_go_to(number_intent, pre4_calculo_state)
pre4_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #5 - ¿Que son las razones de liquidez?

initial_state.when_intent_matched_go_to(pregunta5_intent, pregunta5_state)

def pregunta5_body(session: Session):
    session.reply('Son las que permiten evaluar la capacidad de la empresa para atender sus obligaciones de corto plazo y por lo tanto su estabilidad en el corto plazo.')

pregunta5_state.set_body(pregunta5_body)
pregunta5_state.go_to(initial_state)

###########################################################################################
# RESPUESTA #6 - ¿Que es la razon corriente y cómo se calcula?

initial_state.when_intent_matched_go_to(pregunta6_intent, pregunta6_state)

def pregunta6_body(session: Session):
    session.reply("""
                La **razón corriente**, también conocida como índice de liquidez corriente, es un indicador financiero que mide la capacidad de una empresa para pagar sus deudas a corto plazo con sus activos a corto plazo. Es una métrica crucial en el análisis financiero, ya que ofrece una visión de la liquidez de una empresa y su capacidad para cumplir con sus obligaciones financieras inmediatas.
                \n**Fórmula:**
                \n**Razón corriente =** Activo corriente / Pasivo corriente
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Razón Corriente**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta6_state.set_body(pregunta6_body)
pregunta6_state.when_intent_matched_go_to(resp_si_intent, pre6_calculo_state)
pregunta6_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta6_state.when_no_intent_matched_go_to(initial_state)

def pre6_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Activo corriente', 'Pasivo corriente'], pre6_calculo)
    
pre6_calculo_state.set_body(pre6_calculo_body)
pre6_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre6_calculo_state.when_intent_matched_go_to(number_intent, pre6_calculo_state)
pre6_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #7 - ¿Que es la prueba acida y cómo se calcula?

initial_state.when_intent_matched_go_to(pregunta7_intent, pregunta7_state)

def pregunta7_body(session: Session):
    session.reply("""
                La **prueba ácida** también conocida como **Ratio Ácido** o **Quick Ratio**, es un indicador financiero que mide la capacidad de una empresa para cumplir con sus obligaciones a corto plazo utilizando sus activos más líquidos, excluyendo los inventarios. Es una medida más conservadora de la liquidez de la empresa en comparación con la razón corriente, ya que los inventarios pueden no ser tan fácilmente convertibles en efectivo como otros activos corrientes.
                \n**Fórmula:**
                \n**Prueba Ácida =** Activo corriente - Inventarios / Pasivo corriente
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Prueba Ácida**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta7_state.set_body(pregunta7_body)
pregunta7_state.when_intent_matched_go_to(resp_si_intent, pre7_calculo_state)
pregunta7_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta7_state.when_no_intent_matched_go_to(initial_state)

def pre7_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Activo corriente', 'Inventarios', 'Pasivo corriente'], pre7_calculo)

pre7_calculo_state.set_body(pre7_calculo_body)
pre7_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre7_calculo_state.when_intent_matched_go_to(number_intent, pre7_calculo_state)
pre7_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #8 - ¿Que es la prueba de efectivo y cómo se calcula?
initial_state.when_intent_matched_go_to(pregunta8_intent, pregunta8_state)

def pregunta8_body(session: Session):
    session.reply("""
                La **prueba de efectivo**, también conocida como **Cash Ratio** o **Ratio de Efectivo**, es un indicador financiero que mide la capacidad de una empresa para cubrir sus obligaciones a corto plazo utilizando únicamente su efectivo y equivalentes de efectivo. Es una medida extremadamente conservadora de la liquidez, ya que solo considera los activos más líquidos, excluyendo todas las cuentas por cobrar y otros activos corrientes.
                \n**Fórmula:**
                \n**Prueba de Efectivo =** Efectivo y Equivalentes de Efectivo / Pasivo Corriente
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Prueba de Efectivo**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta8_state.set_body(pregunta8_body)
pregunta8_state.when_intent_matched_go_to(resp_si_intent, pre8_calculo_state)
pregunta8_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta8_state.when_no_intent_matched_go_to(initial_state)

def pre8_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Efectivo y Equivalentes de Efectivo', 'Pasivo Corriente'], pre8_calculo)

pre8_calculo_state.set_body(pre8_calculo_body)
pre8_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre8_calculo_state.when_intent_matched_go_to(number_intent, pre8_calculo_state)
pre8_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #9 - ¿Que son las razones de rentabilidad?
initial_state.when_intent_matched_go_to(pregunta9_intent, pregunta9_state)

def pregunta9_body(session: Session):
    session.reply("Las **razones de rentabilidad** son indicadores financieros que miden la capacidad de una empresa para generar ganancias o rendimientos en relación con sus ventas, activos, capital, o patrimonio. Estas razones proporcionan una visión sobre la eficiencia de la empresa en la gestión de sus recursos y la efectividad de su estrategia para generar ingresos, lo que es crucial para evaluar la viabilidad a largo plazo de la empresa.")

pregunta9_state.set_body(pregunta9_body)
pregunta9_state.go_to(initial_state)

###########################################################################################
# RESPUESTA #10 - ¿Que es el ROE y como se calcula?

initial_state.when_intent_matched_go_to(pregunta10_intent, pregunta10_state)

def pregunta10_body(session: Session):
    session.reply("""
                El **ROE** (Return on Equity), o **Retorno sobre el Patrimonio**, es una métrica financiera que mide la rentabilidad de una empresa en relación con el capital aportado por sus accionistas. En otras palabras, indica cuánto beneficio genera una empresa con el dinero invertido por sus propietarios.
                \n**Fórmula:**
                \n**ROE =** (Utilidad Neta / Patrimonio) x 100
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **ROE**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta10_state.set_body(pregunta10_body)
pregunta10_state.when_intent_matched_go_to(resp_si_intent, pre10_calculo_state)
pregunta10_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta10_state.when_no_intent_matched_go_to(initial_state)

def pre10_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Utilidad Neta', 'Patrimonio Neto'], pre10_calculo)
    
pre10_calculo_state.set_body(pre10_calculo_body)
pre10_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre10_calculo_state.when_intent_matched_go_to(number_intent, pre10_calculo_state)
pre10_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #11 - ¿Que es el ROA y como se calcula?

initial_state.when_intent_matched_go_to(pregunta11_intent, pregunta11_state)

def pregunta11_body(session: Session):
    session.reply("""
                El **ROA**, o **Return on Assets** (Retorno sobre Activos), es un indicador financiero que mide la rentabilidad de una empresa en relación con sus activos totales. En otras palabras, el ROA indica qué tan eficientemente una empresa está utilizando sus activos para generar beneficios.
                \n**Fórmula:**
                \n**ROA =** (Utilidad Neta / Activos Totales) x 100
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **ROA**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta11_state.set_body(pregunta11_body)
pregunta11_state.when_intent_matched_go_to(resp_si_intent, pre11_calculo_state)
pregunta11_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta11_state.when_no_intent_matched_go_to(initial_state)

def pre11_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Utilidad Neta', 'Activos Totales'], pre11_calculo)
    
pre11_calculo_state.set_body(pre11_calculo_body)
pre11_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre11_calculo_state.when_intent_matched_go_to(number_intent, pre11_calculo_state)
pre11_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #12 - ¿Que es un indicador de actividad o Ratios?

initial_state.when_intent_matched_go_to(pregunta12_intent, pregunta12_state)

def pregunta12_body(session: Session):
    session.reply("""
                Son las razones financieras que permiten medir la eficiencia de una empresa en la utilización de sus activos, mediante el tiempo que tarda en recuperar la inversión realizada en ellos.
                \nEntre los indicadores de actividad estan: 
                \nRotación de cartera, Días de cartera, Rotación de invetarios, Días de inventarios, rotación de proveedores, días de proveedores
                """)

pregunta12_state.set_body(pregunta12_body)
pregunta12_state.go_to(initial_state)

###########################################################################################
# RESPUESTA #13 - ¿Que es la rotacion de cartera y como se cálcula?

initial_state.when_intent_matched_go_to(pregunta13_intent, pregunta13_state)

def pregunta13_body(session: Session):
    session.reply("""
                La **Rotación de Cartera**, también conocida como rotación de cuentas por cobrar, es un indicador financiero que mide la eficiencia con la que una empresa gestiona y cobra sus cuentas por cobrar. Específicamente, muestra cuántas veces, en promedio, una empresa cobra sus cuentas por cobrar durante un período específico, generalmente un año.
                \n**Fórmula:**
                \n**Rotación de Cartera =** Ventas a crédito / Promedio de Cuentas por Cobrar
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Rotación de Cartera**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta13_state.set_body(pregunta13_body)
pregunta13_state.when_intent_matched_go_to(resp_si_intent, pre13_calculo_state)
pregunta13_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta13_state.when_no_intent_matched_go_to(initial_state)

def pre13_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Ventas a Credito', 'Promedio de Cuentas por Cobrar'], pre13_calculo)

pre13_calculo_state.set_body(pre13_calculo_body)
pre13_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre13_calculo_state.when_intent_matched_go_to(number_intent, pre13_calculo_state)
pre13_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #14 - ¿Cual es la formula para el cálculo de los días de Cartera?
initial_state.when_intent_matched_go_to(pregunta14_intent, pregunta14_state)

def pregunta14_body(session: Session):
    session.reply("""
                Este indicador es clave para evaluar la eficiencia de una empresa en la gestión de su cartera de clientes y su capacidad para convertir las ventas a crédito en efectivo. Un número bajo de días de cartera sugiere una buena capacidad para cobrar rápidamente, mientras que un número alto podría indicar posibles problemas de liquidez.
                \n**Fórmula:**
                \n**Días de Cartera =** Días de un año (365) / Rotación de Cartera
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Días de Cartera**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta14_state.set_body(pregunta14_body)
pregunta14_state.when_intent_matched_go_to(resp_si_intent, pre14_calculo_state)
pregunta14_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta14_state.when_no_intent_matched_go_to(initial_state)

def pre14_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Rotacion de Cartera'], pre14_calculo)

pre14_calculo_state.set_body(pre14_calculo_body)
pre14_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre14_calculo_state.when_intent_matched_go_to(number_intent, pre14_calculo_state)
pre14_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #15 - ¿Que es la rotacion de inventarios y como se cálcula?
initial_state.when_intent_matched_go_to(pregunta15_intent, pregunta15_state)

def pregunta15_body(session: Session):
    session.reply("""
                La **rotación de inventarios** es un indicador financiero que mide cuántas veces una empresa ha vendido y reemplazado sus inventarios durante un período determinado, generalmente un año. Es una métrica clave en la gestión de inventarios y en la evaluación de la eficiencia operativa de una empresa.
                \n**Fórmula:**
                \n**Rotación de Inventarios =** Costos de Ventas / Inventario Promedio
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Rotación de Inventarios**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta15_state.set_body(pregunta15_body)
pregunta15_state.when_intent_matched_go_to(resp_si_intent, pre15_calculo_state)
pregunta15_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta15_state.when_no_intent_matched_go_to(initial_state)

def pre15_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Costos de Ventas', 'Inventario Promedio'], pre15_calculo)

pregunta15_state.set_body(pre15_calculo_body)
pre15_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre15_calculo_state.when_intent_matched_go_to(number_intent, pre15_calculo_state)
pre15_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #16 - ¿Cual es la formula para el cálculo de los días de Inventario?
initial_state.when_intent_matched_go_to(pregunta16_intent, pregunta16_state)

def pregunta16_body(session: Session):
    session.reply("""
                **Días de Inventario:** Este indicador muestra el número promedio de días que una empresa tarda en vender su inventario completo. Es una medida de eficiencia en la gestión del inventario.
                \n**Rotación de Inventarios:** Es el número de veces que una empresa vende y repone su inventario en un período determinado, generalmente un año.
                \nUn número bajo de días de inventario indica que la empresa vende su inventario rápidamente, lo que generalmente es una señal de eficiencia. Un número alto de días de inventario sugiere que el inventario se está quedando en los almacenes por un período más prolongado, lo que podría implicar una sobreproducción, una demanda baja o ineficiencias en la gestión del inventario.
                \n**Fórmula:**
                \n**Días de Inventario =** Dias de un año (365) / Rotación de Inventarios
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Días de Inventario**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta16_state.set_body(pregunta16_body)
pregunta16_state.when_intent_matched_go_to(resp_si_intent, pre16_calculo_state)
pregunta16_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta16_state.when_no_intent_matched_go_to(initial_state)

def pre16_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Rotacion de Inventarios'], pre16_calculo)

pre16_calculo_state.set_body(pre16_calculo_body)
pre16_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre16_calculo_state.when_intent_matched_go_to(number_intent, pre16_calculo_state)
pre16_calculo_state.when_no_intent_matched_go_to(initial_state)


###########################################################################################
# RESPUESTA #17 - ¿Que es la rotacion de proveedores o cuentas por pagar y como se cálcula?
initial_state.when_intent_matched_go_to(pregunta17_intent, pregunta17_state)

def pregunta17_body(session: Session):
    session.reply("""
                La **rotación de proveedores** o rotación de cuentas por pagar es un indicador financiero que mide la rapidez con la que una empresa paga sus obligaciones a sus proveedores. Este ratio permite evaluar la eficiencia con la que una empresa gestiona sus cuentas por pagar y su relación con los proveedores.
                \n**Fórmula:**
                \n**Rotación de Proveedores =** Compras a Crédito / Promedio de Cuentas por Pagar
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Rotación de Proveedores**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta17_state.set_body(pregunta17_body)
pregunta17_state.when_intent_matched_go_to(resp_si_intent, pre17_calculo_state)
pregunta17_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta17_state.when_no_intent_matched_go_to(initial_state)

def pre17_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Compras a Credito', 'Promedio de Cuentas por Pagar'], pre17_calculo)
    
pre17_calculo_state.set_body(pre17_calculo_body)
pre17_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre17_calculo_state.when_intent_matched_go_to(number_intent, pre17_calculo_state)
pre17_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# # RESPUESTA #18 - ¿Cual es la formula para el cálculo de los días de Inventario y que significa?
# initial_state.when_intent_matched_go_to(pregunta18_intent, pregunta18_state)

# def pregunta18_body(session: Session):
#     session.reply("""
#                 **Los días de inventario** se refiere al tiempo en que los artículos de una empresa o almacén permanecen almacenados. Con esta información podemos planificar mejor las reposiciones, identificar productos con un excesivo costo de almacenaje o comparar la rentabilidad con otros negocios similares.
#                 \n**Fórmula:**
#                 \n**Días de Proveedores =** Días del año (365) / Rotación de Proveedores
#                 """)
#     websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Días de Proveedores**?')
#     websocket_platform.reply_options(session, ['SI', 'NO'])

# pregunta18_state.set_body(pregunta18_body)
# pregunta18_state.when_intent_matched_go_to(resp_si_intent, initial_state)
# pregunta18_state.when_intent_matched_go_to(resp_no_intent, initial_state)
# pregunta18_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #19 - ¿Que es la rotacion de activos corrientes y como se cálcula?

initial_state.when_intent_matched_go_to(pregunta19_intent, pregunta19_state)

def pregunta19_body(session: Session):
    session.reply("""
                La **rotación de activos corrientes** es un indicador financiero que mide la eficiencia con la que una empresa utiliza sus activos corrientes para generar ventas o ingresos. Este ratio indica cuántas veces los activos corrientes de la empresa se han "rotado" o convertido en ventas durante un período determinado, generalmente un año.
                \n**Fórmula:**
                \n**Rotación de Activos Corrientes =** Ventas / Promedio de Activos Corrientes
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Rotación de Activos Corrientes**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta19_state.set_body(pregunta19_body)
pregunta19_state.when_intent_matched_go_to(resp_si_intent, pre19_calculo_state)
pregunta19_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta19_state.when_no_intent_matched_go_to(initial_state)

def pre19_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Ventas', 'Promedio de Activos Corrientes'], pre19_calculo)

pre19_calculo_state.set_body(pre19_calculo_body)
pre19_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre19_calculo_state.when_intent_matched_go_to(number_intent, pre19_calculo_state)
pre19_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #20 - ¿Cual es la formula para el cálculo de los días de activos corrientes?
initial_state.when_intent_matched_go_to(pregunta20_intent, pregunta20_state)

def pregunta20_body(session: Session):
    session.reply("""
                Este indicador muestra el número promedio de días que una empresa tarda en convertir sus activos corrientes en ventas. Es una medida del tiempo que le toma a la empresa recuperar su inversión en activos corrientes.
                \n**Fórmula:**
                \n**Diás de Activos Corrientes =** Días del año (365) / Rotación de Activos Corrientes
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Diás de Activos Corrientess**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta20_state.set_body(pregunta20_body)
pregunta20_state.when_intent_matched_go_to(resp_si_intent, pre20_calculo_state)
pregunta20_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta20_state.when_no_intent_matched_go_to(initial_state)

def pre20_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Rotacion de Activos Corrientes'], pre20_calculo)

pre20_calculo_state.set_body(pre20_calculo_body)
pre20_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre20_calculo_state.when_intent_matched_go_to(number_intent, pre20_calculo_state)
pre20_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #21 - ¿Que es el Margen Bruto?

initial_state.when_intent_matched_go_to(pregunta21_intent, pregunta21_state)

def pregunta21_body(session: Session):
    session.reply("""
                El **Margen Bruto** es un indicador financiero que muestra la rentabilidad de una empresa antes de deducir los gastos operativos, impuestos, intereses y otros costos. Se calcula como el porcentaje de ingresos que excede el costo de los bienes vendidos (COGS), y es una medida de la eficiencia con la que una empresa utiliza sus recursos para producir bienes o servicios.
                \nUn margen bruto alto indica que la empresa retiene una gran parte de los ingresos después de cubrir los costos directos de producción, lo cual es positivo para su rentabilidad. Un margen bruto bajo, por otro lado, podría señalar que la empresa está enfrentando altos costos de producción o está compitiendo en un mercado con precios bajos.
                \n**Fórmula:**
                \n**Margen Bruto =** (Ingresos Netos - Costos de Ventas / Ingresos Netos) x 100 
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Margen Bruto**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta21_state.set_body(pregunta21_body)
pregunta21_state.when_intent_matched_go_to(resp_si_intent, pre21_calculo_state)
pregunta21_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta21_state.when_no_intent_matched_go_to(initial_state)

def pre21_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Ingresos Netos', 'Costos de Ventas'], pre21_calculo)

pre21_calculo_state.set_body(pre21_calculo_body)
pre21_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre21_calculo_state.when_intent_matched_go_to(number_intent, pre21_calculo_state)
pre21_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #22 - ¿Que es el Margen Operacional?

initial_state.when_intent_matched_go_to(pregunta22_intent, pregunta22_state)

def pregunta22_body(session: Session):
    session.reply("""
                El **Margen Operacional** mide la rentabilidad del negocio independiente de su forma de financiación.
                \nIncluye los gastos administrativos y operativos.
                \nEl principal indicador de la viabilidad del negocio.
                \nEl margen operativo depende del sector de la empresa **(comercio - industria - servicios)** y deberá compararse con el sector.
                \n**Fórmula:**
                \n**Margen Operacional =** (Utilidad Operativa / Ventas Netas) x 100
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Margen Operacional**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta22_state.set_body(pregunta22_body)
pregunta22_state.when_intent_matched_go_to(resp_si_intent, pre22_calculo_state)
pregunta22_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta22_state.when_no_intent_matched_go_to(initial_state)

def pre22_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Utilidad Operativa', 'Ventas Netas'], pre22_calculo)

pre22_calculo_state.set_body(pre22_calculo_body)
pre22_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre22_calculo_state.when_intent_matched_go_to(number_intent, pre22_calculo_state)
pre22_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTA #23 - ¿Que es el Margen Neto?

initial_state.when_intent_matched_go_to(pregunta23_intent, pregunta23_state)

def pregunta23_body(session: Session):
    session.reply("""
                El **Margen Neto** es un indicador financiero que mide la rentabilidad de una empresa al expresar la relación entre la utilidad neta (ganancias después de impuestos, intereses y todos los costos) y las ventas netas. En otras palabras, muestra qué porcentaje de cada unidad monetaria de ventas se convierte en ganancia neta después de deducir todos los costos y gastos.
                \n**Fórmula:**
                \n**Margen Neto =** (Utilidad Neta / Ventas Netas) x 100
                """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Margen Neto**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta23_state.set_body(pregunta23_body)
pregunta23_state.when_intent_matched_go_to(resp_si_intent, pre23_calculo_state)
pregunta23_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta23_state.when_no_intent_matched_go_to(initial_state)

def pre23_calculo_body(session: Session):
    capture_variables_and_calculate(session, ['Utilidad Neta', 'Ventas Netas'], pre23_calculo)

pre23_calculo_state.set_body(pre23_calculo_body)
pre23_calculo_state.when_variable_matches_operation_go_to('calculo_completado', lambda x, y: x == y, True, initial_state)
pre23_calculo_state.when_intent_matched_go_to(number_intent, pre23_calculo_state)
pre23_calculo_state.when_no_intent_matched_go_to(initial_state)

###########################################################################################
# RESPUESTAS SALUDO
initial_state.when_intent_matched_go_to(hello_intent, hello_state)

def hello_body(session: Session):
    session.reply('Hola!, mucho gusto mi nombre es Chatbot Financiero, como estas?')

hello_state.set_body(hello_body)
hello_state.when_intent_matched_go_to(good_intent, good_state)
hello_state.when_intent_matched_go_to(bad_intent, bad_state)
hello_state.when_no_intent_matched_go_to(initial_state)

def good_body(session: Session):
    session.reply('Me alegra que estes bien. Dime en que puedo ayudarte.')

good_state.set_body(good_body)
good_state.go_to(initial_state)


def bad_body(session: Session):
    session.reply('Ojalá que pronto te puedas sentir mejor. Hazme alguna pregunta.')

bad_state.set_body(bad_body)
bad_state.go_to(initial_state)
###########################################################################################

# Mensaje por defecto cuando el bot no reconoce la intencion del usuario
def mensaje_por_defecto_body(session: Session):
    session.reply("Lo siento, no entiendo a que te refieres, intentalo de nuevo.")

bot.set_global_fallback_body(mensaje_por_defecto_body)


# def ejemplo_body(session: Session):
#     # Obtener la última predicción a un intent
#     prediction: IntentClassifierPrediction = session.predicted_intent
#     # Obtener el id de la session
#     session_id: str = session.id
#     # Enviar un mensaje al usuario
#     session.reply('Hola!')
#     # Obtener el historial del chat
#     # El entero asociado a cada mensaje identifica el remitente (0 = chatbot, 1 = usuario
#     chat_history: list[tuple[str,int]] = session.chat_history
#     # Cambiar el valor de una variable
#     session.set('variable', 30)
#     # Obtener una variable (el tipo de return puede ser cualquiera)
#     variable: int = session.get('variable')
#     # Eleminar una variable
#     session.delete('age')
#     # Los archivos recibidos también se almacenan como parte de las sesiones del usuario
#     file: File = session.file



# RUN APPLICATION

if __name__ == '__main__':
    bot.run()
    
