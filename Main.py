import streamlit as st
st.set_page_config(page_title="Tutorial Basico de Streamlit",page_icon=":shark:",layout="wide")
st.markdown('''<style>
.st-bx {
  font-size: 14px;
  text-transform: uppercase;
  background-image: linear-gradient(
    -225deg,
    #231557 0%,
    #44107a 29%,
    #ff1361 67%,
    #fff800 100%
  );
  background-size: auto auto;
  background-clip: border-box;
  background-size: 200% auto;
  color: #fff;
  background-clip: text;
  text-fill-color: transparent;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: textclip 5s linear infinite;
  display: inline-block;
}

@keyframes textclip {
  to {
    background-position: 200% center;
  }
}
</style>
''', unsafe_allow_html=True)
# Tutorial Basico de Streamlit
st.title("Tutorial Basico de Streamlit")
st.divider()
#Hola Mundo
st.write("Hola Mundo!")

st.write('Titulos y encabezados')
cols = st.columns(2)
with cols[0]:
    with st.expander('st.title()',expanded=True):
        st.title("Título de Nivel 1")
    with st.expander('docstring',expanded=False):
        st.write((st.title.__doc__))
with cols[1]:
    with st.expander('st.header()',expanded=True):
        st.header("título de Nivel 2")
    with st.expander('docstring',expanded=False):
        st.write((st.header.__doc__))

st.write('texto')
cols1 = st.columns(2)
with cols1[0]:
    with st.expander('st.write()',expanded=True):
        st.write("Este es un párrafo de texto normal. :sunglasses:")
        st.write('Puede escribir texto en color :blue[aquí]!')
        st.text('Este es un párrafo de texto normal. :sunglasses:, puedes escribir texto en color :blue[aquí]!')
    with st.expander('docstring',expanded=False):
            st.write((st.write.__doc__))

with cols1[1]:
    with st.expander('st.markdown()',expanded=True):
        st.markdown("## Título de Nivel 2 con Markdown")
        st.markdown("### Título de Nivel 3 con Markdown")
        st.markdown("Puedes **enfatizar** el texto utilizando Markdow")
        st.markdown("También puedes agregar [links](https://www.streamlit.io/) a tus textos.")
        st.markdown("Puedes escribir texto en *cursiva*")
        st.markdown("O puedes agregar imagenes\n ![Capybara](https://www.awsfzoo.com/media/capy1.png)")
        st.text('''
        raw markdown string
        ## Título de Nivel 2 con Markdown
        ### Título de Nivel 3 con Markdown
        Puedes **enfatizar** el texto utilizando Markdow
        También puedes agregar [links](https://www.streamlit.io/) a tus textos.
        Puedes escribir texto en *cursiva*
        O puedes agregar imagenes ![Capybara](https://www.awsfzoo.com/media/capy1.png)
        ''')
    with st.expander('docstring',expanded=False):
            st.markdown((st.markdown.__doc__))

cols2 = st.columns(2)

with cols2[0]:
    with st.expander('st.latex()',expanded=True):
        st.latex(r''' e^{i\pi} + 1 = 0 , \int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}''')
        st.text('''e^{i\pi} + 1 = 0 , \int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}''')
    with st.expander('docstring',expanded=False):
            st.write((st.latex.__doc__))

with cols2[1]:
    with st.expander('st.code()',expanded=True):
        st.code('''
        def hello():
            print("Hello, Streamlit!")
        ''',language='python')
    with st.expander('docstring',expanded=False):
            st.write((st.code.__doc__))
