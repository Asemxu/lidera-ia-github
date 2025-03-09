def GETPROMPTBOT(context):
    return f""" Eres LideraBot, un asistente para estudiantes de la universidad Lidera University. Si el usuario te saluda, responde amistosamente al saludo. Si no te saluda, no lo saludes. Responde sin mencionar que has tenido que obtener algun contexto y hazlo amigablemente.Debes responder a las consultas de los estudiantes unicamente con el siguiente contexto. Si no tienes el contexto necesario, debes decir que no la sabes. Contexto: {context}"""

def GETPROMPTMULTIPECHOICEQUESTION(num_of_questions,story):
    # old text promt generator
    # text = (
    #     f"Porfavor genera {num_of_questions} preguntas de opcion multiple con el siguiente formato: "
    #     "'::TEXTO_PREGUNTA { =ALTERNATIVA_CORRECTA ~ALTERNATIVA_INCORRECTA ~ALTERNATIVA_INCORRECTA ~ALTERNATIVA_INCORRECTA }' "
    #     "Las preguntas y opciones deben ser basadas en el texto que envie el usuario. Recuerda que cada pregunta debe tener una respuesta correcta y tres incorrectas. "
    #     "Sin agregar espacios en blanco según el formato indicado. Ejemplo con una sola pregunta: ::Quíen es el presidente de los estados unidos { =yo ~richard ~gustavo ~peter }.  Ejemplo con más de una sola pregunta: ::Quíen es el presidente de los estados unidos { =yo ~richard ~gustavo ~peter } \n::Cual es la capital de Francia { =Paris ~Londres ~Madrid ~Berlin }"
    #     "Sigue al pie de la letra las indicaciones que se te indica"
    #     "No me agreges ningun salto de linea '\n' entre la pregunta y la respuesta"
    #     "Por favor, deje una línea en blanco entre las preguntas. No olvides ningún signo igual o tilde!. Usa el siguiente texto: "
    #     + story
    # )
    # new text promt better generator
    text = (
        f"Genera exactamente {num_of_questions} preguntas de opción múltiple basadas únicamente en el texto proporcionado por el usuario. "
        f"Cada pregunta debe seguir este formato exacto: '::TEXTO_PREGUNTA {{ =ALTERNATIVA_CORRECTA ~ALTERNATIVA_INCORRECTA ~ALTERNATIVA_INCORRECTA ~ALTERNATIVA_INCORRECTA }}'. "
        f"Reglas estrictas: "
        f"1. No agregues ningún espacio en blanco ni salto de línea entre la pregunta y las opciones (dentro de cada pregunta). "
        f"2. Separa cada pregunta con exactamente un salto de línea ('\n'), incluso si es la última pregunta, y no incluyas líneas vacías adicionales. "
        f"3. Cada pregunta debe tener exactamente 1 alternativa correcta (precedida por '=') y 3 alternativas incorrectas (precedidas por '~'). "
        f"4. No omitas ningún signo ('=', '~', '{{', '}}') ni tildes en las palabras en español. "
        f"5. Las preguntas y opciones deben estar basadas únicamente en el texto proporcionado, sin inventar información externa. "
        f"6. No devuelvas el resultado como una lista o en formato JSON; devuélvelo como un string con las preguntas separadas por '\n'. "
        f"Ejemplos: "
        f"- Si num_of_questions = 1: ::¿Quién es el presidente de los Estados Unidos? {{ =Yo ~Richard ~Gustavo ~Peter }}\n "
        f"- Si num_of_questions = 2: ::¿Quién es el presidente de los Estados Unidos? {{ =Yo ~Richard ~Gustavo ~Peter }}\n::¿Cuál es la capital de Francia? {{ =París ~Londres ~Madrid ~Berlín }}\n "
        f"- Si num_of_questions = 3: ::¿Quién es el presidente de los Estados Unidos? {{ =Yo ~Richard ~Gustavo ~Peter }}\n::¿Cuál es la capital de Francia? {{ =París ~Londres ~Madrid ~Berlín }}\n::¿Qué color es el cielo? {{ =Azul ~Verde ~Rojo ~Amarillo }}\n "
        f"- Si num_of_questions = 4: ::¿Quién descubrió América? {{ =Colón ~Magallanes ~Vespuccio ~Pizarro }}\n::¿En qué año ocurrió? {{ =1492 ~1500 ~1453 ~1600 }}\n::¿Qué océano cruzó? {{ =Atlántico ~Pacífico ~Índico ~Ártico }}\n::¿Cuál era su nacionalidad? {{ =Italiana ~Española ~Portuguesa ~Francesa }}\n "
        f"- Si num_of_questions = 5: ::¿Cuál es el planeta más grande? {{ =Júpiter ~Saturno ~Tierra ~Marte }}\n::¿Qué elemento es el más abundante en la Tierra? {{ =Oxígeno ~Hierro ~Carbono ~Hidrógeno }}\n::¿Quién escribió El Quijote? {{ =Cervantes ~Lope de Vega ~Quevedo ~Góngora }}\n::¿En qué siglo vivió? {{ =XVI ~XV ~XVII ~XVIII }}\n::¿Cuál es la capital de Brasil? {{ =Brasilia ~Río de Janeiro ~São Paulo ~Salvador }}\n "
        f"- Si num_of_questions = 6: ::¿Quién pintó la Mona Lisa? {{ =Da Vinci ~Michelangelo ~Rafael ~Tiziano }}\n::¿En qué ciudad está el Louvre? {{ =París ~Roma ~Madrid ~Londres }}\n::¿Qué río pasa por Egipto? {{ =Nilo ~Amazonas ~Misisipi ~Danubio }}\n::¿Cuál es el metal más conductor? {{ =Cobre ~Plata ~Oro ~Hierro }}\n::¿Quién inventó la bombilla? {{ =Edison ~Tesla ~Franklin ~Watt }}\n::¿En qué año fue la Revolución Francesa? {{ =1789 ~1815 ~1776 ~1848 }}\n "
        f"- Si num_of_questions = 7: ::¿Cuál es el continente más grande? {{ =Asia ~África ~América ~Europa }}\n::¿Qué país tiene más población? {{ =China ~India ~EEUU ~Rusia }}\n::¿Quién fue el primer hombre en la Luna? {{ =Armstrong ~Aldrin ~Gagarin ~Shepard }}\n::¿En qué año llegó? {{ =1969 ~1971 ~1965 ~1980 }}\n::¿Qué gas compone la mayor parte del aire? {{ =Nitrógeno ~Oxígeno ~Dióxido de carbono ~Argón }}\n::¿Cuál es la montaña más alta? {{ =Everest ~K2 ~Kangchenjunga ~Aconcagua }}\n::¿En qué país está? {{ =Nepal ~India ~China ~Pakistán }}\n "
        f"- Si num_of_questions = 8: ::¿Quién escribió Romeo y Julieta? {{ =Shakespeare ~Marlowe ~Chaucer ~Milton }}\n::¿En qué idioma lo escribió? {{ =Inglés ~Francés ~Latín ~Italiano }}\n::¿Cuál es el país más pequeño del mundo? {{ =Vaticano ~Mónaco ~San Marino ~Liechtenstein }}\n::¿Qué océano es el más grande? {{ =Pacífico ~Atlántico ~Índico ~Ártico }}\n::¿Quién fue el primer presidente de EE.UU.? {{ =Washington ~Adams ~Jefferson ~Lincoln }}\n::¿En qué año asumió? {{ =1789 ~1776 ~1801 ~1861 }}\n::¿Qué animal es el más rápido? {{ =Guepardo ~León ~Águila ~Caballo }}\n::¿Cuál es la capital de Japón? {{ =Tokio ~Osaka ~Kioto ~Hiroshima }}\n "
        f"- Si num_of_questions = 9: ::¿Qué planeta es el más cercano al Sol? {{ =Mercurio ~Venus ~Tierra ~Marte }}\n::¿Quién descubrió la penicilina? {{ =Fleming ~Pasteur ~Koch ~Lister }}\n::¿En qué año fue descubierta? {{ =1928 ~1900 ~1945 ~1870 }}\n::¿Cuál es el desierto más grande? {{ =Sahara ~Gobi ~Atacama ~Antártico }}\n::¿En qué continente está? {{ =África ~Asia ~América ~Australia }}\n::¿Qué instrumento mide la presión atmosférica? {{ =Barómetro ~Termómetro ~Higrómetro ~Anemómetro }}\n::¿Quién compuso la Quinta Sinfonía? {{ =Beethoven ~Mozart ~Bach ~Chopin }}\n::¿En qué siglo vivió? {{ =XIX ~XVIII ~XVII ~XX }}\n::¿Cuál es la capital de Rusia? {{ =Moscú ~San Petersburgo ~Kiev ~Vladivostok }}\n "
        f"- Si num_of_questions = 10: ::¿Qué gas es esencial para la respiración? {{ =Oxígeno ~Nitrógeno ~Helio ~Dióxido de carbono }}\n::¿Quién descubrió la teoría de la relatividad? {{ =Einstein ~Newton ~Galileo ~Hawking }}\n::¿En qué año la publicó? {{ =1905 ~1890 ~1920 ~1875 }}\n::¿Cuál es el río más largo del mundo? {{ =Amazonas ~Nilo ~Yangtsé ~Misisipi }}\n::¿En qué continente fluye principalmente? {{ =América ~África ~Asia ~Europa }}\n::¿Qué país ganó el primer Mundial de fútbol? {{ =Uruguay ~Brasil ~Argentina ~Alemania }}\n::¿En qué año fue? {{ =1930 ~1950 ~1920 ~1940 }}\n::¿Cuál es la capital de Italia? {{ =Roma ~Milán ~Venecia ~Florencia }}\n::¿Qué elemento químico tiene el símbolo H? {{ =Hidrógeno ~Helio ~Hierro ~Hafnio }}\n::¿Quién pintó el techo de la Capilla Sixtina? {{ =Michelangelo ~Da Vinci ~Rafael ~Botticelli }}\n "
        f"Usa el siguiente texto para generar las preguntas: {story}"
    )
    
    return text

MIN_WORDS_STORY = 10

MIN_WORDS_STORY_MESSAGE = 'El story es demasiado corta para generar preguntas. Debe tener al menos 10 palabras.'