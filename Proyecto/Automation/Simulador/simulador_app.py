import streamlit as st
import requests

# 1. LAYOUT Y CONFIGURACIÓN
st.set_page_config(
    page_title="Calculadora de Capacidad Varada",
    layout="wide"
)

# Webhook para la automatización
WEBHOOK_URL = "https://hook.us2.make.com/bz3tnotc4ucz12chy1hwhrrpg48tl9ah"

# 2. CSS CORPORATIVO
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 2rem 3rem; }
    
    /* Adaptación de textos para fondo oscuro */
    h1, h2, h3 { color: #F8FAFC !important; font-family: 'Segoe UI', Tahoma, sans-serif; }
    
    /* Título principal */
    .main-title { text-align: left; font-size: 3rem; font-weight: 800; color: #FFFFFF; margin-bottom: 5px; line-height: 1.2; }
    .subtitle { color: #94A3B8; font-size: 1.1rem; margin-bottom: 20px; }
    
    /* Caja de texto promocional */
    .promo-box { background-color: #1E293B; padding: 40px; border-radius: 8px; border: 1px solid #334155; border-left: 6px solid #CB9F2E; width: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin-top: 10px;}
    .promo-title { font-size: 1.8rem; font-weight: 700; color: #F8FAFC; margin-bottom: 15px; line-height: 1.3;}
    .promo-text { font-size: 1.1rem; color: #CBD5E1; line-height: 1.6; margin-bottom: 20px;}
    .promo-highlight { color: #CB9F2E; font-weight: 700; }
    
    /* Botón ENVIAR del Formulario */
    .stButton>button, .stFormSubmitButton>button { background-color: #35664C !important; color: #FFFFFF !important; border-radius: 6px !important; border: none !important; padding: 10px 24px !important; font-size: 1.1rem !important; font-weight: 700 !important; width: 100% !important; margin-top: 15px; transition: 0.3s; }
    .stButton>button:hover, .stFormSubmitButton>button:hover { background-color: #CB9F2E !important; color: #1E293B !important; }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO Y AVISO
st.markdown("<div class='main-title'>Simulador de Capacidad Varada</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Evaluación del costo de oportunidad financiero por demoras en la red de interconexión.</div>", unsafe_allow_html=True)

st.warning("⚠️ **Entorno de Simulación:** Esta interfaz es una demostración técnica. Los datos ingresados aquí se utilizan exclusivamente para validar el flujo de ingesta de datos y disparar el proceso de automatización en el backend.")
st.markdown("<br>", unsafe_allow_html=True)

# 4. ESTRUCTURA DE COLUMNAS
col_left, col_right = st.columns([1, 1.2], gap="large")

with col_left:
    st.subheader("Datos del Operador")
    
    # st.form es la clave: agrupa todo y clear_on_submit lo vacía al final
    with st.form("formulario_operador", clear_on_submit=True):
        nombre = st.text_input("Nombre Completo")
        email = st.text_input("Correo Electrónico Corporativo")
        
        col_form1, col_form2 = st.columns(2)
        with col_form1:
            cargo = st.selectbox("Cargo del Usuario", ["Seleccionar...", "CTO", "Facility Manager", "Infrastructure Director", "Operations Director", "No Especificado"])
            tamano_empresa = st.selectbox("Tamaño de Empresa", ["Seleccionar...", "100-500", "500-1000", "1000+", "No Especificado"])
        with col_form2:
            tipo_empresa = st.selectbox("Tipo de Empresa", ["Seleccionar...", "Colocation", "Edge", "Enterprise", "Hyperscaler", "No Especificado"])
            industria = st.selectbox("Industria", ["Seleccionar...", "Cloud", "Financial", "Telecommunications", "No Especificado"])

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Parámetros del Simulador")
        resultado_mw = st.slider("Capacidad Varada Detectada (MW)", 0.1, 50.0, 5.0, 0.1)
        
        # El botón ahora pertenece al formulario
        submit_btn = st.form_submit_button("ENVIAR")
        
        if submit_btn:
            # 1. Validación de campos vacíos o no seleccionados
            if not nombre or not email:
                st.error("Por favor, complete los campos obligatorios (Nombre y Correo).")
            elif cargo == "Seleccionar..." or tamano_empresa == "Seleccionar..." or tipo_empresa == "Seleccionar..." or industria == "Seleccionar...":
                st.error("Por favor, seleccioná una opción válida en todos los menús desplegables.")
            else:
                # 2. Si pasa la validación, armamos los datos
                payload = {
                    "nombre": nombre,
                    "email": email,
                    "cargo_usuario": cargo,
                    "tipo_empresa": tipo_empresa,
                    "tamano_empresa": tamano_empresa,
                    "industria": industria,
                    "resultado_mw": resultado_mw
                }
                
                # 3. Envío al Webhook
                with st.spinner("Procesando datos y enviando reporte..."):
                    try:
                        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
                        if response.status_code == 200:
                            st.success("¡Datos enviados con éxito! Revisá tu casilla de correo para ver el reporte financiero.")
                        else:
                            st.error(f"Error de conexión. Código {response.status_code}.")
                    except Exception as e:
                        st.error("Error en la conexión con el Webhook.")

with col_right:
    # Bloque de texto promocional / Copywriting
    st.markdown(f"""
        <div class='promo-box'>
            <div class='promo-title'>¿Sabés cuánto capital estás perdiendo hoy mismo?</div>
            <div class='promo-text'>
                Cada megavatio de capacidad varada representa <span class='promo-highlight'>millones de dólares en costo de oportunidad</span> a lo largo del tiempo. No tomar decisiones basadas en datos hoy, compromete el crecimiento de tu infraestructura mañana.
            </div>
            <div class='promo-text'>
                Simulá tus parámetros en el panel y recibí de inmediato un <b>Reporte Benchmark</b> directo en tu correo electrónico con:
            </div>
            <ul style='color: #CBD5E1; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;'>
                <li>Proyección detallada de pérdidas acumuladas a 5 años.</li>
                <li>Comparativa entre un escenario conservador y uno con ajuste proyectado.</li>
                <li>Métricas ejecutivas listas para presentar a la mesa directiva.</li>
            </ul>
            <div class='promo-text' style='font-style: italic; color: #94A3B8; font-size: 0.95rem; margin-top: 30px;'>
                "Transformá la incertidumbre de la red en un caso de negocio sólido."
            </div>
        </div>
    """, unsafe_allow_html=True)