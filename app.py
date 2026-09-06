import streamlit as st

st.set_page_config(
    page_title="Red de Apoyo",
    page_icon="💚",
    layout="centered"
)

# -----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------

st.title("💚 Red de Apoyo")
st.subheader("Asistente de orientación en salud mental")

st.warning(
    "Este asistente proporciona información y opciones de canalización. "
    "No sustituye la atención psicológica, médica o de emergencia."
)

st.error(
    "Si existe peligro inmediato, llama al 911 o acude al servicio "
    "de urgencias más cercano."
)

# -----------------------------
# MEMORIA TEMPORAL DEL CHAT
# -----------------------------

if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {
            "role": "assistant",
            "content": (
                "Hola. Soy un asistente digital de orientación. "
                "Puedo ayudarte a localizar información y servicios profesionales.\n\n"
                "No necesitas proporcionar tu nombre, domicilio ni otros datos personales.\n\n"
                "¿Qué necesitas en este momento?"
            )
        }
    ]

# Mostrar la conversación
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# -----------------------------
# RESPUESTAS CONTROLADAS
# -----------------------------

def generar_respuesta(texto):
    consulta = texto.lower()

    expresiones_urgentes = [
        "quiero morir",
        "me quiero morir",
        "quiero matarme",
        "voy a matarme",
        "hacerme daño",
        "lastimarme",
        "no quiero vivir",
        "peligro inmediato",
        "ya no quiero vivir"
    ]

    if any(expresion in consulta for expresion in expresiones_urgentes):
        return """
🚨 **Es importante solicitar ayuda inmediata.**

Llama al **911** o acude al servicio de urgencias más cercano.

También puedes comunicarte con:

- **Línea de la Vida:** 800 911 2000.
- **LOCATEL CDMX:** *0311 o 55 5658 1111.

Si es posible, permanece acompañado por una persona de confianza mientras
recibes ayuda. No dependas únicamente de este chatbot.
"""

    if (
        "otra persona" in consulta
        or "amigo" in consulta
        or "amiga" in consulta
        or "familiar" in consulta
        or "ayudar a alguien" in consulta
    ):
        return """
Si estás preocupado por otra persona, escucha con respeto y toma en serio
lo que expresa.

Puedes:

1. Preguntarle si acepta recibir ayuda profesional.
2. Ofrecerte a acompañarla.
3. Contactar a una persona adulta o profesional de confianza.
4. Solicitar atención urgente si existe peligro inmediato.

Si la persona expresa intención de hacerse daño, llama al **911** o a
**Línea de la Vida: 800 911 2000**.
"""

    if (
        "profesional" in consulta
        or "psicólogo" in consulta
        or "psicologa" in consulta
        or "ayuda" in consulta
        or "contactar" in consulta
    ):
        return """
Puedes solicitar orientación profesional mediante:

☎️ **Línea de la Vida:** 800 911 2000.

En la Ciudad de México también puedes solicitar servicio psicológico en:

☎️ **LOCATEL:** *0311 o 55 5658 1111.

Si existe peligro inmediato, llama al **911** o acude a urgencias.
"""

    if (
        "señales" in consulta
        or "síntomas" in consulta
        or "información" in consulta
        or "salud mental" in consulta
    ):
        return """
Algunas expresiones de desesperanza, aislamiento o cambios importantes de
comportamiento pueden indicar que una persona necesita apoyo.

Estas señales no permiten realizar un diagnóstico. La valoración debe hacerla
personal especializado.

Puedes comunicarte con **Línea de la Vida: 800 911 2000** para recibir
orientación.
"""

    return """
Gracias por escribir. Este prototipo no puede realizar una valoración
psicológica ni interpretar clínicamente tu situación.

Puedo ayudarte con alguno de estos temas:

- Información general sobre salud mental.
- Cómo acompañar a otra persona.
- Cómo contactar a un profesional.
- Qué hacer ante una situación de peligro inmediato.

Escribe el tema sobre el que necesitas información.
"""

# -----------------------------
# CAMPO PARA ESCRIBIR
# -----------------------------

consulta = st.chat_input("Escribe aquí tu consulta, sin proporcionar datos personales")

if consulta:
    st.session_state.mensajes.append(
        {"role": "user", "content": consulta}
    )

    with st.chat_message("user"):
        st.markdown(consulta)

    respuesta = generar_respuesta(consulta)

    st.session_state.mensajes.append(
        {"role": "assistant", "content": respuesta}
    )

    with st.chat_message("assistant"):
        st.markdown(respuesta)

# -----------------------------
# INFORMACIÓN ADICIONAL
# -----------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "☎️ Línea de la Vida",
        "https://www.gob.mx/lineadelavida",
        use_container_width=True
    )

with col2:
    st.link_button(
        "🚨 Información del 911",
        "https://www.gob.mx/911",
        use_container_width=True
    )

if st.button("🗑️ Borrar conversación"):
    st.session_state.mensajes = [
        {
            "role": "assistant",
            "content": (
                "Hola. Soy un asistente digital de orientación. "
                "¿Qué información necesitas?"
            )
        }
    ]
    st.rerun()

with st.expander("Privacidad y límites del asistente"):
    st.write(
        """
        Este prototipo no realiza diagnósticos, no determina clínicamente el
        nivel de riesgo y no sustituye una valoración profesional.

        La identificación de determinadas expresiones solamente activa una
        ruta preventiva. No constituye una evaluación psicológica y puede
        cometer errores.

        No proporciones nombres, domicilios, teléfonos, expedientes clínicos
        ni otra información personal.
        """
    )

st.caption(
    "Prototipo académico. Los contenidos y directorios deben ser revisados "
    "por profesionales e instituciones competentes antes de su publicación. "
    "Última actualización: septiembre de 2026."
)
