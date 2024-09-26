import logging


from besser.bot.core.bot import Bot
from besser.bot.core.session import Session

from besser.bot.library.entity.base_entities import number_entity
from besser.bot.nlp.intent_classifier.intent_classifier_prediction import IntentClassifierPrediction

# Configuración del módulo logging, para ver las acciones del bot en la terminal
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')

# Creación del chatbot
bot = Bot('chatbot_tg')

# Cargar las propiedades del bot almacenadas en el archivo config.ini
bot.load_properties('config.ini')

# Definir que plataforma va a utilizar el chatbot (websocket_platform)
websocket_platform = bot.use_websocket_platform(use_ui=True)

# Añade la entidad 'number_entity'
bot.add_entity(number_entity)

# STATES - ESTADOS

initial_state = bot.new_state('initial_state', initial=True)

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
pregunta18_state = bot.new_state('pregunta18_state')
pregunta19_state = bot.new_state('pregunta19_state')
pregunta20_state = bot.new_state('pregunta20_state')
pregunta21_state = bot.new_state('pregunta21_state')
pregunta22_state = bot.new_state('pregunta22_state')
pregunta23_state = bot.new_state('pregunta23_state')

hello_state = bot.new_state('hello_state')
good_state = bot.new_state('good_state')
bad_state = bot.new_state('bad_state')
mensaje_por_defecto_state = bot.new_state('mensaje_por_defecto_state')

# Estados para obtener las variables para calcular la fórmula
get_pasivo_state = bot.new_state('get_pasivo_state')
get_activo_state = bot.new_state('get_activo_state')

# Estado para mostrar el resultado
pregunta4_result_state = bot.new_state('pregunta4_result_state')

# Estado para capturar números
pre4_calculo_state = bot.new_state('pre4_calculo_state')

# Función para capturar variables y calcular
def capture_variables_and_calculate(session: Session, variable_names: list, calculation_function):
    current_var_index = session.get('current_var_index') or 0
    current_var_name = variable_names[current_var_index]

    # Capturar el valor de la variable actual
    # predicted_intent: IntentClassifierPrediction = session.predicted_intent
    # number_value = predicted_intent.get_parameter('value').value
    # session.set(current_var_name, number_value)
    # session.reply(f"El valor ingresado para {current_var_name} es {number_value}")
    
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
        #session.move(pre4_calculo_state)
    else:
        # Realizar el cálculo si todas las variables han sido capturadas
        result, interpretacion = calculation_function(session)
        #session.set('resultado', f"El resultado es {result:.3f}. \n{interpretacion}")
        session.reply(f"""
                El resultado es {result:.3f}. 
                \n{interpretacion}
        """)
        session.delete('current_var_index')
        for var_name in variable_names:
            session.delete(var_name)
        session.set('calculo_completado', True) # Marca el flujo de la funcion como completado en la variable calculo_completado
        return True # Indicar que la captura y calculo estan completos

# Función para calcular el índice de endeudamiento
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

# INTENTS - INTENCIONES

# Inputs de usuario para las preguntas

# Crear intents que capturan números
number_intent = bot.new_intent('number_intent', [
    '{number:number_entity}'
])
number_intent.parameter('value', 'number', number_entity)

# PREGUNTA #1 - ¿Qué son las razones financieras?
pregunta1_intent = bot.new_intent('pregunta1_intent', [
    'qué son las razones financieras',
    'qué significa razones financieras',
    'a qué se refiere las razones financieras',
    'qué significa razones financieras',    
    'what are the financial ratios',
])

# PREGUNTA #2 - ¿Cuáles son las razones financieras?
pregunta2_intent = bot.new_intent('pregunta2_intent', [
    'cuáles son las razones financieras',
    'cuántas razones financieras',
    'dime las razones financieras que hay',
    'qué factores financieros se consideran',
    'necesito conocer las razones financieras',
    'cuántas razones financieras existen',
    'por favor, enumera las razones financieras',
    'cuáles son algunas de las razones financieras más importantes',
    'dime sobre los indicadores financieros relevantes',
])

# PREGUNTA #3 - ¿Qué son las razones de endeudamiento o apalancamiento?
pregunta3_intent = bot.new_intent('pregunta3_intent',[
    'qué son las razones de endeudamiento o apalancamiento',
    'qué son las razones de endeudamiento',
    'qué son las razones de apalancamiento',
    'qué es razón de endeudamiento',
    'qué es razón de apalancamiento',
    'cómo se calcula la razón de endeudamiento',
    'cómo se calcula la razón de apalancamiento',
])

# PREGUNTA #4 - ¿Qué es el índice de endeudamiento y cómo se calcula?
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

# PREGUNTA #5 - ¿Qué son las razones de liquidez?
pregunta5_intent = bot.new_intent('pregunta5_intent', [
    'qué son las razones de liquidez',
    'razones de liquidez',
    'necesito entender las razones de liquidez',
    'dime sobre las razones de liquidez',
    'podrías explicar las razones de liquidez',
    'qué implica el concepto de razones de liquidez',
    'cuáles son las razones de liquidez',
    'quiero saber más acerca de las razones de liquidez',
    'cuál es la importancia de las razones de liquidez',
])

# PREGUNTA #6 - ¿Qué es la razón corriente y cómo se calcula?
pregunta6_intent = bot.new_intent('pregunta6_intent', [
    'qué es la razón corriente y cómo se calcula',
    'qué es la razón corriente',
    'cómo se calcula la razón corriente',
    'necesito entender la razón corriente y su cálculo',
    'dime sobre la razón corriente y su fórmula',
    'podrías explicar la razón corriente y su cálculo',
    'qué implica el concepto de razón corriente',
    'quiero saber más sobre la razón corriente y su cálculo',
    'cuál es la importancia de la razón corriente en finanzas',
])

# PREGUNTA #7 - ¿Qué es la prueba ácida y cómo se calcula?
pregunta7_intent = bot.new_intent('pregunta7_intent', [
    'qué es la prueba ácida y cómo se calcula',
    'qué es la prueba ácida',
    'cómo se calcula la prueba ácida',
    'a qué se refiere la prueba ácida y cómo se calcula',
    'necesito entender la prueba ácida y su cálculo',
    'dime sobre la prueba ácida y su fórmula',
    'podrías explicar la prueba ácida y su cálculo',
    'qué implica el concepto de prueba ácida',
    'quiero saber más sobre la prueba ácida y su cálculo',
])

# Otros intents siguen la misma estructura

resp_si_intent = bot.new_intent('resp_si_intent', ['SI'])
resp_no_intent = bot.new_intent('resp_no_intent', ['NO'])

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


###########################################################################################

def initial_state_body(session: Session):
    session.set('calculo_completado', False)

initial_state.set_body(initial_state_body)

# Respuestas para las preguntas

# RESPUESTA #1 - ¿Qué son las razones financieras?
initial_state.when_intent_matched_go_to(pregunta1_intent, pregunta1_state)

def pregunta1_body(session: Session):
    session.reply('Las razones financieras son herramientas utilizadas para analizar y evaluar la salud financiera de una empresa...')
pregunta1_state.set_body(pregunta1_body)
pregunta1_state.go_to(initial_state)

# RESPUESTA #2 - ¿Cuáles son las razones financieras?
initial_state.when_intent_matched_go_to(pregunta2_intent, pregunta2_state)

def pregunta2_body(session: Session):
    session.reply("""
        **Razones de liquidez:** Mide la disponibilidad de recursos de corto plazo para atender sus obligaciones más próximas
        \n**Razones de endeudamiento o apalancamiento:** Mide el nivel de endeudamiento y la capacidad para asumir nuevos pasivos.
        \n**Razones de rentabilidad:** Permite evaluar qué tan rentable son las diferentes etapas del negocio así como la empresa.
        \n**Razones de cobertura:** Identifican la capacidad de la empresa para cubrir con diferentes tipos de obligaciones, en especial las financieras.
    """)
pregunta2_state.set_body(pregunta2_body)
pregunta2_state.go_to(initial_state)

# RESPUESTA #3 - ¿Qué son las razones de endeudamiento o apalancamiento?
initial_state.when_intent_matched_go_to(pregunta3_intent, pregunta3_state)

def pregunta3_body(session: Session):
    session.reply("""
        Las **razones de apalancamiento** permiten medir el nivel de endeudamiento de la empresa en la que se va a invertir...
    """)
    websocket_platform.reply(session, '¿Deseas realizar el cálculo de **Apalancamiento de la empresa**?')
    websocket_platform.reply_options(session, ['SI', 'NO'])

pregunta3_state.set_body(pregunta3_body)
pregunta3_state.when_intent_matched_go_to(resp_si_intent, pre4_calculo_state)
pregunta3_state.when_intent_matched_go_to(resp_no_intent, initial_state)
pregunta3_state.when_no_intent_matched_go_to(initial_state)

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
    #session.set('current_var_index', 0)
    #session.reply("Por favor, ingresa el valor del **pasivo total**.")

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






# RESPUESTA #5 - ¿Qué son las razones de liquidez?
initial_state.when_intent_matched_go_to(pregunta5_intent, pregunta5_state)

def pregunta5_body(session: Session):
    session.reply('Son las que permiten evaluar la capacidad de la empresa para atender sus obligaciones de corto plazo y por lo tanto su estabilidad en el corto plazo.')
pregunta5_state.set_body(pregunta5_body)
pregunta5_state.go_to(initial_state)

# RESPUESTA #6 - ¿Qué es la razón corriente y cómo se calcula?
initial_state.when_intent_matched_go_to(pregunta6_intent, pregunta6_state)

def pregunta6_body(session: Session):
    session.reply("""
        La **razón corriente** determina las veces que una empresa paga sus deudas de corto plazo con sus activos de corto plazo
        \n**Fórmula:**
        \n**Razón corriente =** Activo corriente / Pasivo corriente
    """)
    session.set('current_var_index', 0)
    capture_variables_and_calculate(session, ['activo_corriente', 'pasivo_corriente'], calculate_endeudamiento)

pregunta6_state.set_body(pregunta6_body)
pregunta6_state.go_to(initial_state)

# Otros estados de respuesta siguen la misma estructura

###########################################################################################å

initial_state.when_intent_matched_go_to(hello_intent, hello_state)

def hello_body(session: Session):
    session.reply('¡Hola!, mucho gusto mi nombre es Chatbot Financiero, ¿cómo estás?')

hello_state.set_body(hello_body)
hello_state.when_intent_matched_go_to(good_intent, good_state)
hello_state.when_intent_matched_go_to(bad_intent, bad_state)
hello_state.when_no_intent_matched_go_to(initial_state)

def good_body(session: Session):
    session.reply('Me alegra que estés bien, dime en qué te puedo ayudar')

good_state.set_body(good_body)
good_state.go_to(initial_state)

def bad_body(session: Session):
    session.reply('Ojalá que pronto te puedas sentir mejor')

bad_state.set_body(bad_body)
bad_state.go_to(initial_state)

###########################################################################################

# Mensaje por defecto cuando el bot no reconoce la intención del usuario
def mensaje_por_defecto_body(session: Session):
    session.reply("Lo siento, no entiendo a qué te refieres, inténtalo de nuevo.")

bot.set_global_fallback_body(mensaje_por_defecto_body)

# RUN APPLICATION
if __name__ == '__main__':
    bot.run()
