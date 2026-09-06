import streamlit as st

st.set_page_config(
    page_title="Red de Apoyo",
    page_icon="💚",
    layout="centered"
)

st.title("💚 Red de Apoyo")
st.subheader("Orientación y canalización en salud mental")

st.warning(
    "Este prototipo proporciona información y opciones de canalización. "
    "No sustituye la atención psicológica, médica o de emergencia."
)

st.markdown(
    """
    Este espacio busca ayudarte a encontrar información y contactar servicios
    profesionales. No necesitas proporcionar tu nombre, domicilio, diagnóstico
    ni otros datos personales.
    """
)

st.divider()

st.subheader("¿Qué necesitas en este momento?")

opcion = st.radio(
    "Selecciona una opción:",
    [
        "Necesito información sobre salud mental",
        "Estoy preocupado por otra persona",
        "Quiero contactar a un profesional",
        "Existe peligro inmediato",
    ],
    index=None
)

if opcion == "Necesito información sobre salud mental":
    st.info(
        """
        Pedir ayuda es una acción válida y recomendable. Puedes hablar con una
        persona de confianza o acercarte a un servicio profesional de salud mental.
        """
    )

    tema = st.selectbox(
        "¿Sobre qué tema necesitas orientación?",
        [
            "Selecciona una opción",
            "Señales de alerta",
            "Cómo solicitar ayuda",
            "Cómo acompañar a otra persona",
            "Directorio de servicios",
        ]
    )

    if tema == "Señales de alerta":
        st.write(
            """
            Algunas señales requieren atención profesional: aislamiento,
            desesperanza intensa, cambios importantes de comportamiento o
            expresiones relacionadas con no querer continuar viviendo.

            Una señal aislada no permite realizar un diagnóstico. La valoración
            debe hacerla personal especializado.
            """
        )

    elif tema == "Cómo solicitar ayuda":
        st.write(
            """
            Puedes comunicarte con un servicio de orientación, acudir a una
            institución de salud o pedir a una persona de confianza que te
            acompañe durante la búsqueda de ayuda.
            """
        )

    elif tema == "Cómo acompañar a otra persona":
        st.write(
            """
            Escucha sin juzgar, toma en serio lo que expresa y ayúdale a contactar
            personal especializado. Si existe peligro inmediato, no dejes sola a
            la persona y solicita apoyo de emergencia.
            """
        )

    elif tema == "Directorio de servicios":
        st.success("Línea de la Vida: 800 911 2000")
        st.write("Emergencias: 911")
        st.write("LOCATEL CDMX: *0311 o 55 5658 1111")

elif opcion == "Estoy preocupado por otra persona":
    st.info(
        """
        Escucha con respeto y evita minimizar lo que la persona expresa.
        Pregunta si acepta contactar a un servicio profesional y ofrécete a
        acompañarla.
        """
    )

    st.markdown(
        """
        **Busca ayuda urgente cuando:**

        - La persona manifiesta que se encuentra en peligro inmediato.
        - Menciona una intención de hacerse daño.
        - No puede mantenerse segura.
        - Ha realizado una acción que requiere atención médica.
        """
    )

    st.error(
        "Ante peligro inmediato: llama al 911 o solicita apoyo presencial."
    )

elif opcion == "Quiero contactar a un profesional":
    st.success("Línea de la Vida: 800 911 2000")
    st.write("Servicio oficial de orientación en salud mental.")

    st.info(
        """
        En la Ciudad de México también puedes solicitar servicio psicológico
        mediante LOCATEL: *0311 o 55 5658 1111.
        """
    )

    st.link_button(
        "Consultar Línea de la Vida",
        "https://www.gob.mx/lineadelavida"
    )

elif opcion == "Existe peligro inmediato":
    st.error(
        """
        Si tú u otra persona se encuentran en peligro inmediato, llama al 911
        o acude al servicio de urgencias más cercano.
        """
    )

    st.warning(
        """
        Si es posible, permanece acompañado por una persona de confianza mientras
        llega la ayuda. No dependas únicamente de este sitio.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "Línea de la Vida",
            "https://www.gob.mx/lineadelavida"
        )

    with col2:
        st.link_button(
            "Emergencias 911",
            "https://www.gob.mx/911"
        )

st.divider()

with st.expander("Privacidad y límites del servicio"):
    st.write(
        """
        Este prototipo no realiza diagnósticos, no determina automáticamente el
        nivel de riesgo y no sustituye una valoración profesional. No debe
        solicitar ni almacenar nombres, domicilios, expedientes clínicos o
        conversaciones personales.
        """
    )

st.caption(
    "Prototipo académico. La información y los directorios deben ser revisados "
    "por profesionales e instituciones competentes antes de su publicación."
)
