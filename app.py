import streamlit as st

# Configuración visual de la página web
st.set_page_config(page_title="Tu Novio Literario", page_icon="📚", layout="centered")

# CARACTERISTICAS DE LOS PERSONAJES (Diccionarios de opciones)
color_ojos = {"marron": 1, "negro": 2, "azul": 3, "verde": 4, "miel": 5}
color_cabello = {"marron": 1, "negro": 2, "rubio": 3, "azabache": 4}
vestimenta = {"casual": 1, "elegante": 2, "motorizado": 3, "colegial": 4}
caracter = {"calido": 1, "frio": 2}
energia_visual = {"golden": 1, "bad boy": 2, "dark academia": 3, "soft boy": 4, "principe": 5, "chico problematico": 6}
personalidad = {"extrovertido": 1, "introvertido": 2}
celos = {"si": 1, "no": 2}
tropo = {"enemies to lovers": 1, "friends to lovers": 2, "strangers to lovers": 3, "fake dating": 4, "slow burn": 5}
relacion = {"publico": 1, "secreto": 2}
dulzura = {"dulce": 1, "misterioso": 2}
escenario = {"castillo": 1, "academico": 2, "ciudad": 3, "fantasia": 4, "epoca": 5}
humor = {"tiene humor": 1, "no tiene humor": 2}

# BASE DE DATOS DE PERSONAJES
personajes = [
    {
        "nombre": "Jack Ross",
        "libro": "Antes de diciembre",
        "ojos": color_ojos["marron"],
        "cabello": color_cabello["marron"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["calido"],
        "energia": energia_visual["golden"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["friends to lovers"],
        "romance": relacion["publico"],
        "dulzura": dulzura["dulce"],
        "escenario": escenario["academico"],
        "humor": humor["tiene humor"],
        "sinopsis" : "🤍 El green flag que restaura tu fe en los hombres. Jack no necesita presumir para llamar la atención; su tranquilidad, inteligencia y pequeños gestos hablan por él. Es el tipo de chico que recordaría cómo te gusta el café ☕, te prestaría su sudadera sin que se la pidieras 🧥 y se aseguraría de que llegaras bien a casa 🌙. Puede parecer reservado, pero cuando ama... ama con todo el corazón. Si buscas un novio estable, atento y de esos que dicen \"te quiero\" con acciones, Jack es tu hombre. 🫶"
    },
    {
        "nombre": "Darcy",
        "libro": "Orgullo y prejuicio",
        "ojos": color_ojos["negro"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["elegante"],
        "caracter": caracter["frio"],
        "energia": energia_visual["principe"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["publico"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["epoca"],
        "humor": humor["no tiene humor"],
        "sinopsis": "✨ El fundador oficial del \"parece un red flag, pero solo es pésimo expresando emociones\". Darcy es elegante, reservado y orgulloso 👑. Parece juzgar a todo el mundo, pero cuando se enamora literalmente cambia como persona. Es el tipo de hombre que resolvería todos tus problemas en silencio 🤍 sin esperar nada a cambio. Cuidado... porque termina enamorando a cualquiera. 🌹"
    },
    {
        "nombre": "Nick Leister",
        "libro": "Culpa mía",
        "ojos": color_ojos["azul"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["motorizado"],
        "caracter": caracter["frio"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["ciudad"],
        "humor": humor["no tiene humor"],
        "sinopsis": "La definición de \"bad boy\". Carreras 🏍️, peleas 🥊, celos 😤 y muchísima tensión romántica. Nick parece un caos andante, pero cuando ama es increíblemente protector. Es impulsivo y comete errores... aunque siempre intenta arreglarlos. Si te gustan los chicos malos de Wattpad, él es un clásico. 😮‍💨"
    },
    {
        "nombre": "Logan Turner",
        "libro": "El arte de ser nosotros",
        "ojos": color_ojos["marron"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["motorizado"],
        "caracter": caracter["frio"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["academico"],
        "humor": humor["no tiene humor"],
        "sinopsis": "El golden retriever boyfriend definitivo. Logan es divertido, impulsivo y el rey de hacerte reír hasta que te duela el estómago 😂. Siempre parece meterse en problemas, pero también sería el primero en aparecer cuando más lo necesites ❤️‍🩹. Vive improvisando, habla sin pensar y convierte cualquier momento aburrido en una aventura. Eso sí... también es experto en esconder sus sentimientos detrás de una sonrisa 🥹"
    },
    {
        "nombre": "Adam Carlsen",
        "libro": "La hipótesis del amor",
        "ojos": color_ojos["marron"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["elegante"],
        "caracter": caracter["frio"],
        "energia": energia_visual["dark academia"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["fake dating"],
        "romance": relacion["publico"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["academico"],
        "humor": humor["no tiene humor"],
        "sinopsis": "El profesor que intimida a todos... menos a ti. Adam parece serio, frío e imposible de impresionar 😶, pero en realidad es el novio que movería cielo y tierra para verte feliz. Recordaría cada pequeño detalle que mencionaste meses atrás 📝, te prepararía comida cuando olvidaras comer 🍱 y jamás dejaría que nadie te faltara el respeto. Es la definición de grumpy por fuera, softie por dentro 🖤➡️🤍"
    },
    {
        "nombre": "Rhys Baker",
        "libro": "Nosotros en la luna",
        "ojos": color_ojos["verde"],
        "cabello": color_cabello["rubio"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["calido"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["friends to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["ciudad"],
        "humor": humor["tiene humor"],
        "sinopsis": "El chico que te haría querer comprar un boleto de avión solo para verlo otra vez. Aventurero, romántico y con alma de poeta 🌙📖, Rhys convierte cualquier conversación en un recuerdo inolvidable. Es de esos que te mandarían fotos del amanecer desde otro continente 📸 y te escribirían mensajes que releerías mil veces. Amar a Rhys es bonito... pero también duele. 💙"
    },
    {
        "nombre": "Damian",
        "libro": "Damian: un secreto oscuro y perverso",
        "ojos": color_ojos["negro"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["motorizado"],
        "caracter": caracter["frio"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["slow burn"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["fantasia"],
        "humor": humor["no tiene humor"],
        "sinopsis": "El chico misterioso que sabes que es peligroso, pero igual te atrae 😈 Damian es inteligente, frío y demasiado encantador para su propio bien. Siempre parece esconder algo detrás de su actitud segura y calculadora 🖤 Tiene una personalidad intensa, protectora y llena de secretos, con esa energía de soy un problema, pero contigo sería diferente. Si te gustan los personajes oscuros, misteriosos y moralmente grises... Damian es tu obsesión asegurada 🥀✨"
    },
    {
        "nombre": "Darian",
        "libro": "Vampire",
        "ojos": color_ojos["miel"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["elegante"],
        "caracter": caracter["frio"],
        "energia": energia_visual["dark academia"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["fantasia"],
        "humor": humor["tiene humor"],
        "sinopsis": "El vampiro que todas juran poder arreglar. Misterioso, dominante y peligrosamente atractivo 😮‍💨. Parece completamente inalcanzable, pero cuando alguien logra entrar en su corazón se vuelve ferozmente protector 🖤. Si te gustan los hombres con energía de moriría por ti... Darian está en tu lista."
    },
    {
        "nombre": "Ricardito Somocurcio",
        "libro": "Travesuras de la niña mala",
        "ojos": color_ojos["marron"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["elegante"],
        "caracter": caracter["calido"],
        "energia": energia_visual["golden"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["fake dating"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["dulce"],
        "escenario": escenario["epoca"],
        "humor": humor["tiene humor"],
        "sinopsis" : "El romántico que jamás dejó de creer en el amor. Inteligente, tranquilo y completamente enamorado ❤️. Cruzaría océanos solo para volver a ver a la mujer que ama 🌍. Es el ejemplo perfecto de que algunas personas aman con tanta intensidad que cambian el rumbo de toda su vida."
    },
    {
        "nombre": "Tomás",
        "libro": "Una perfecta confusión",
        "ojos": color_ojos["azul"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["calido"],
        "energia": energia_visual["chico problematico"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["academico"],
        "humor": humor["tiene humor"],
        "sinopsis": "El novio aprobado por absolutamente todo el mundo. Amable, paciente y protector 🤍. Es quien siempre preguntará si ya comiste 🍜, si llegaste bien 🚗 y cómo estuvo tu día 🌻. Tal vez no sea el más escandaloso... pero sí el que te haría sentir más segura."
    },
    {
        "nombre": "Andrew Minyard",
        "libro": "All for the game",
        "ojos": color_ojos["miel"],
        "cabello": color_cabello["rubio"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["frio"],
        "energia": energia_visual["chico problematico"],
        "celoso": celos["no"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["slow burn"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["academico"],
        "humor": humor["tiene humor"],
        "sinopsis": "No me hables... y cinco minutos después ya estás obsesionada. Andrew parece incapaz de demostrar cariño 😐. Es sarcástico, frío y levanta muros enormes alrededor de sí mismo. Pero cuando decide que alguien es importante para él... su lealtad es inquebrantable 🔒. No sonríe mucho, pero cuando lo hace sientes que ganaste la lotería. 😭"
    },
    {
        "nombre": "Gerdad Gibson",
        "libro": "Tamming 7",
        "ojos": color_ojos["azul"],
        "cabello": color_cabello["marron"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["calido"],
        "energia": energia_visual["golden"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["friends to lovers"],
        "romance": relacion["publico"],
        "dulzura": dulzura["dulce"],
        "escenario": escenario["ciudad"],
        "humor": humor["tiene humor"],
        "sinopsis": "El papá que haría cualquier cosa por su familia. Fuerte, trabajador y protector 💙. Siempre intenta mantener todo bajo control y hacer lo correcto, incluso cuando eso implique sacrificarse. Es uno de esos personajes que inspiran muchísimo respeto."
    },
    {
        "nombre": "Hua Cheng",
        "libro": "La bendición del oficial celestial",
        "ojos": color_ojos["negro"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["elegante"],
        "caracter": caracter["calido"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["no"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["friends to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["dulce"],
        "escenario": escenario["epoca"],
        "humor": humor["tiene humor"],
        "sinopsis": "El estándar masculino quedó arruinado gracias a este hombre. Rico 💎, poderoso ⚔️, elegante 🖤 y completamente obsesionado con la persona que ama ❤️. Hua Cheng literalmente esperaría cientos de años por ti si fuera necesario. Su devoción es tan enorme que hace parecer mediocres a casi todos los demás intereses románticos. 😭✨"
    },
    {
        "nombre": "Luke Howland",
        "libro": "Boulevard",
        "ojos": color_ojos["azul"],
        "cabello": color_cabello["rubio"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["frio"],
        "energia": energia_visual["chico problematico"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["friends to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["ciudad"],
        "humor": humor["tiene humor"],
        "sinopsis": "🥀 El chico roto que solo quería que alguien lo quisiera. Rebelde, impulsivo y autodestructivo 💔. Siempre intenta alejar a quienes se preocupan por él, aunque en el fondo solo desea dejar de sentirse solo 🤍. Es uno de esos personajes que te hacen llorar página tras página."
    },
    {
        "nombre": "Cameron Parker",
        "libro": "Bad Ash",
        "ojos": color_ojos["marron"],
        "cabello": color_cabello["marron"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["calido"],
        "energia": energia_visual["golden"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["friends to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["dulce"],
        "escenario": escenario["academico"],
        "humor": humor["tiene humor"],
        "sinopsis": "😏 El deportista que sabe perfectamente que es guapo. Seguro de sí mismo, competitivo y protector 🏆. Parece el típico popular del instituto, pero debajo de toda esa confianza hay alguien mucho más sensible de lo que deja ver 💙."
    },
    {
        "nombre": "Simon Lewis",
        "libro": "Cazadores de sombras",
        "ojos": color_ojos["marron"],
        "cabello": color_cabello["marron"],
        "vestimenta": vestimenta["casual"],
        "caracter": caracter["calido"],
        "energia": energia_visual["soft boy"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["strangers to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["dulce"],
        "escenario": escenario["ciudad"],
        "humor": humor["tiene humor"],
        "sinopsis": "😂 El mejor amigo que todos querríamos tener. Divertido, leal y adorablemente torpe 🤓. Siempre está dispuesto a ayudarte aunque eso signifique meterse en problemas. Su evolución es de las más bonitas porque nunca deja de ser buena persona. 🌟"
    },
    {
        "nombre": "Jax",
        "libro": "Una perfecta equivocación",
        "ojos": color_ojos["negro"],
        "cabello": color_cabello["marron"],
        "vestimenta": vestimenta["motorizado"],
        "caracter": caracter["frio"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["si"],
        "personalidad": personalidad["introvertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["academico"],
        "humor": humor["tiene humor"],
        "sinopsis": "😎 Problemas con patas... pero qué problemas tan lindos. Bromista, impulsivo y encantador 😮‍💨. Tiene una facilidad increíble para sacar de quicio a cualquiera, pero también sería el primero en defenderte 💥. Es imposible no terminar enamorándose de él."
    },
    {
        "nombre": "Cardan Greenbriar",
        "libro": "Príncipe Cruel",
        "ojos": color_ojos["negro"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["elegante"],
        "caracter": caracter["calido"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["no"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["castillo"],
        "humor": humor["tiene humor"],
        "sinopsis" : "🖤 El príncipe que nació para hacerte sufrir... y enamorarte. Sarcástico, arrogante y absolutamente precioso ✨. Al principio parece insufrible 😤, pero poco a poco descubres que detrás de toda esa actitud hay alguien mucho más vulnerable. Enemies to lovers en su máxima expresión. 🥀👑"
    },
    {
        "nombre": "Johnny Kavanagh",
        "libro": "Blinding 13",
        "ojos": color_ojos["azul"],
        "cabello": color_cabello["marron"],
        "vestimenta": vestimenta["colegial"],
        "caracter": caracter["calido"],
        "energia": energia_visual["golden"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["friends to lovers"],
        "romance": relacion["publico"],
        "dulzura": dulzura["dulce"],
        "escenario": escenario["academico"],
        "humor": humor["tiene humor"],
        "sinopsis": "💚 El capitán perfecto con corazón de osito de peluche. Talentoso, popular y extremadamente protector 🫶. Es el chico que te animaría antes de un examen 📚, te abrazaría cuando todo salga mal 🤍 y presumiría de ti frente a todo el mundo. Un green flag enorme. 🌿"
    },
    {
        "nombre": "Noah Flynn",
        "libro": "El stand de los besos",
        "ojos": color_ojos["marron"],
        "cabello": color_cabello["marron"],
        "vestimenta": vestimenta["motorizado"],
        "caracter": caracter["frio"],
        "energia": energia_visual["bad boy"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["fake dating"],
        "romance": relacion["publico"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["ciudad"],
        "humor": humor["tiene humor"],
        "sinopsis": "✨ El crush de todo el instituto. Guapo, popular y con un carisma imposible de ignorar 😌. Todo el mundo quiere estar cerca de Noah, pero detrás de esa imagen perfecta también hay inseguridades y presión. Es el típico chico que parece inalcanzable... hasta que te sonríe. 💙"
    },
    {
        "nombre": "Owen",
        "libro": "Doberman",
        "ojos": color_ojos["miel"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["elegante"],
        "caracter": caracter["frio"],
        "energia": energia_visual["dark academia"],
        "celoso": celos["si"],
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["publico"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["ciudad"],
        "humor": humor["tiene humor"],
        "sinopsis": "⚠️ PELIGRO: altamente adictivo. Owen no entra en una habitación... la domina. Inteligente, dominante y con una presencia que intimida incluso cuando permanece en silencio. Es el tipo de personaje que sabes que es una pésima decisión... pero aun así no puedes dejar de leer cada escena en la que aparece. Oscuro, intenso y completamente obsesivo. 🖤🥀🩸"
    },
    {
        "nombre": "Aegan Cash",
        "libro": "Perfectos mentirosos",
        "ojos": color_ojos["negro"],
        "cabello": color_cabello["negro"],
        "vestimenta": vestimenta["motorizado"],
        "caracter": caracter["frio"],
        "energia": energia_visual["chico problematico"],
        "celoso": celos["si"],
        "personalidad": presidential = 1, # Compatible con el for original
        "personalidad": personalidad["extrovertido"],
        "trope1": tropo["enemies to lovers"],
        "romance": relacion["secreto"],
        "dulzura": dulzura["misterioso"],
        "escenario": escenario["academico"],
        "humor": humor["tiene humor"],
        "sinopsis": "♟️ El chico que nunca sabes si está coqueteando contigo... o manipulándote. Inteligente, misterioso y absurdamente encantador 🖤. Siempre parece ir diez pasos por delante de todos ♟️. Jamás sabes qué está pensando, y justamente eso hace que quieras descubrirlo. Es el rey del confía en mí... cuando claramente no deberías. 😮‍💨✨ "
    }
]

# PASO 1: Modificar pedir_opcion para usar un componente web (st.selectbox) en lugar de print() e input()
def pedir_opcion(pregunta, diccionario):
    # Retornamos el valor numérico directamente según la llave seleccionada por el usuario
    opcion_seleccionada = st.selectbox(pregunta, list(diccionario.keys()))
    return diccionario[opcion_seleccionada]

# PASO 4: Cambiar los print() de la cabecera por bloques de texto estéticos de Streamlit
st.title("📚 QUIEN ES TU NOVIO LITERARIO")
st.write("Responde al quiz dentro del formulario de abajo y descubre qué personaje es tu pareja ideal.")

# PASO 2: Encapsular el bloque de las 12 preguntas dentro de la estructura de un formulario web (st.form)
with st.form("quiz_novio_literario"):
    st.write("### 📝 Selecciona tus preferencias:")
    
    # Creamos un diseño ordenado en dos columnas dentro del formulario
    col1, col2 = st.columns(2)
    
    with col1:
        respuestadeojos = pedir_opcion("¿Qué color de ojos te gusta más?", color_ojos)
        respuestadecabello = pedir_opcion("¿Qué color de cabello te gusta más?", color_cabello)
        respuestadevestimenta = pedir_opcion("¿Qué vestimenta te gusta más?", vestimenta)
        respuestadecaracter = pedir_opcion("¿Qué carácter prefieres?", caracter)
        respuestadeenergia = pedir_opcion("¿Qué energía visual prefieres?", energia_visual)
        respuestadeceloso = pedir_opcion("¿Te gusta que sea celoso?", celos)
        
    with col2:
        respuestadepersonalidad = pedir_opcion("¿Lo prefieres extrovertido o introvertido?", personalidad)
        respuestadetrope1 = pedir_opcion("¿Qué tropo prefieres?", tropo)
        respuestaderomance = pedir_opcion("¿Prefieres romance público o secreto?", relacion)
        respuestadedulzura = pedir_opcion("¿Te atrae más alguien dulce o misterioso?", dulzura)
        respuestadeescenario = pedir_opcion("¿Qué escenario prefieres?", escenario)
        respuestadehumor = pedir_opcion("¿Debe tener sentido del humor?", humor)
        
    # El botón de envío obligatorio para cerrar el st.form
    boton_enviar = st.form_submit_button("✨ Calcular mi novio literario ✨", use_container_width=True)

# PASO 3: Condicionar la lógica del ciclo for para que se ejecute ÚNICAMENTE cuando se presione el botón
if boton_enviar:
    mejorpersonaje = None
    mayorpuntaje = -1

    for personaje in personajes:
        puntaje = 0

        if respuestadeojos == personaje["ojos"]: puntaje += 1
        if respuestadecabello == personaje["cabello"]: puntaje += 1
        if respuestadevestimenta == personaje["vestimenta"]: puntaje += 1
        if respuestadecaracter == personaje["caracter"]: puntaje += 1
        if respuestadeenergia == personaje["energia"]: puntaje += 1
        if respuestadeceloso == personaje["celoso"]: puntaje += 1
        if respuestadepersonalidad == personaje["personalidad"]: puntaje += 1
        if respuestadetrope1 == personaje["trope1"]: puntaje += 1
        if respuestaderomance == personaje["romance"]: puntaje += 1
        if respuestadedulzura == personaje["dulzura"]: puntaje += 1
        if respuestadeescenario == personaje["escenario"]: puntaje += 1
        if respuestadehumor == personaje["humor"]: puntaje += 1

        if puntaje > mayorpuntaje:
            mayorpuntaje = puntaje
            mejorpersonaje = personaje

    # PASO 4 (Continuación): Cambiar los print() del resultado final por bloques de texto estéticos (widgets)
    st.balloons() # Efecto visual interactivo de celebración 🎉
    
    st.success(f"## Tu novio literario es: **{mejorpersonaje['nombre']}**")
    st.subheader(f"📖 Libro: *{mejorpersonaje['libro']}*")
    st.write(f"🎯 **Puntaje de coincidencia:** {mayorpuntaje} de 12 puntos posibles.")
    
    st.markdown("---")
    st.info("### 📝 Aquí está la sinopsis de tu novio literario:")
    st.write(mejorpersonaje["sinopsis"])
    st.write("¿Ya lo leíste? Si no lo has leído aún, ¡hazlo ya! ¡Tu novio literario te espera! 🥰")
