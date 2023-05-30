import requests
import streamlit as st
from streamlit_lottie import st_lottie 
from moviepy.editor import * 
import tempfile
st.set_page_config(page_title="Ricardo Gomez", page_icon=":tada:", layout="wide")

def ll(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load assets
lc = ll("https://assets1.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
# Header
with st.container():
    st.subheader("Hola soy Ricardo :wave:")
    st.title("Soy ingeniero en TIC's")
    st.write("Me gusta mucho la tecnología, soy una persona dedicada y constante")

with st.container():
    st.write("----")
    left_column, right_column  = st.columns(2)
    with left_column:
        st.header("¿Que hago?")
        st.write("##")
        st.write(
            """
            - Tengo logica de programacion 
            - Estoy trabajando con IA (TensorFlow)
            """)
    with right_column:
        st_lottie(lc, height=300, key="coding")
with st.container():
    st.title("Convertidor mp4 a mp3")
with st.container():
    uploaded_files = st.file_uploader("Seleccione el video a convertir", accept_multiple_files=False)
    if uploaded_files is not None:
        # Crear un archivo temporal
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        # Guardar el contenido del archivo cargado en el archivo temporal
        temp_file.write(uploaded_files.read())
        # Obtener la ruta del archivo temporal
        file_path = temp_file.name
        st.write("Archivo guardado en:", file_path)
        st.write("Nombre del archivo:", uploaded_files.name)
        if st.button('Convertir video'):
            # Load the mp4 file
            video = VideoFileClip(file_path)
            D = uploaded_files.name+".mp3"
            video.audio.write_audiofile(D)
            with open(D, "rb") as file:
                    btn = st.download_button(
                    label="Descargar archivo",
                    data=file,
                    file_name=D,
                    mime="mp3"
                    )

