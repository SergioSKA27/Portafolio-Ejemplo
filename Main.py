import streamlit as st
from streamlit.components.v1 import html
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


st.markdown('''<style>
@import url("https://fonts.googleapis.com/css?family=Raleway:400");
@property --angle {
  syntax: '<angle>';
  initial-value: 90deg;
  inherits: true;
}

@property --gradX {
  syntax: '<percentage>';
  initial-value: 50%;
  inherits: true;
}

@property --gradY {
  syntax: '<percentage>';
  initial-value: 0%;
  inherits: true;
}

:root {
	--d: 2500ms;
	--angle: 90deg;
	--gradX: 100%;
	--gradY: 50%;
	--c1: rgba(168, 239, 255, 1);
	--c2: rgba(168, 239, 255, 0.1);
}

.wrapper {
	min-width: min(40rem, 100%);
}
.css-ocqkz7 {
  display: flex;
  flex-wrap: wrap;
  -moz-box-flex: 1;
  flex-grow: 1;
  -moz-box-align: stretch;
  align-items: stretch;
  gap: 1rem;
  border: solid;
    border-top-color: currentcolor;
    border-right-color: currentcolor;
    border-bottom-color: currentcolor;
    border-left-color: currentcolor;
  border-radius: 15px;
  padding: 0;

 font-size: 3vw;
	margin: max(1rem, 3vw);
	border: 0.35rem solid;
	padding: 3vw;
	border-image: conic-gradient(from var(--angle), var(--c2), var(--c1) 0.1turn, var(--c1) 0.15turn, var(--c2) 0.25turn) 30;
	animation: borderRotate var(--d) linear infinite forwards;

}


@keyframes borderRotate {
	100% {
		--angle: 420deg;
	}
}

@keyframes borderRadial {
	20% {
		--gradX: 100%;
		--gradY: 50%;
	}
	40% {
		--gradX: 100%;
		--gradY: 100%;
	}
	60% {
		--gradX: 50%;
		--gradY: 100%;
	}
	80% {
		--gradX: 0%;
		--gradY: 50%;
	}
	100% {
		--gradX: 50%;
		--gradY: 0%;
	}
}
</style>''', unsafe_allow_html=True)

# Tutorial Basico de Streamlit
st.markdown('''<style>
@import url("https://fonts.googleapis.com/css2?family=Asap&family=Roboto:ital,wght@0,500;0,900;1,500&display=swap");

.titulo {
  width: 100%;
  height: 20vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  padding-left: 0;
}
.titulo h1 {
  position: relative;
  width: 90%;
  font-size: 60px;
  font-weight: 600;
  color: transparent;
  background-image: linear-gradient(to right ,#B3EC48, #ee4b2b, #00c2cb, #ff7f50, #553c9a);
  -webkit-background-clip: text;
  background-clip: text;
  background-size: 200%;
  background-position: -200%;
  transition: all ease-in-out 2s;
  cursor: pointer;
}
.titulo h1:hover{
  background-position: 200%;
}
</style>''', unsafe_allow_html=True)




st.markdown('''<style>


@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap');
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}


.waviy {
  position: relative;
  -webkit-box-reflect: below -20px linear-gradient(transparent, rgba(0,0,0,.2));
  font-size: 40px;
}
.waviy span {
  font-family: 'Alfa Slab One', cursive;
  position: relative;
  display: inline-block;
  color: #000;
  text-transform: uppercase;
  animation: waviy 1s infinite;
  animation-delay: calc(.1s * var(--i));

}
@keyframes waviy {
  0%,40%,100% {
    transform: translateY(0)
  }
  20% {
    transform: translateY(-20px)
  }
}


/* For Android devices or smaller screens */
@media screen and (max-width: 767px) {
  .waviy {
  position: absolute;
  -webkit-box-reflect: below -20px linear-gradient(transparent, rgba(0,0,0,.2));
  font-size: 15px;
}
.waviy span {
  font-family: 'Alfa Slab One', cursive;
  position: relative;
  display: inline-block;
  color: #000;
  text-transform: uppercase;
  animation: waviy 1s infinite;
  animation-delay: calc(.1s * var(--i));

}
@keyframes waviy {
  0%,40%,100% {
    transform: translateY(0)
  }
  20% {
    transform: translateY(-20px)
  }
}

}

</style>''', unsafe_allow_html=True)

st.markdown('''<div class="titulo"><h1>Tutorial Basico de Streamlit</h1></div>''', unsafe_allow_html=True)
st.divider()
#Hola Mundo
st.write("Hola Mundo!")



html('''
<style>


@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap');
* {
  padding: 10px;
  margin: 1;
  box-sizing: border-box;
}


.waviy {
  position: relative;
  -webkit-box-reflect: below -20px linear-gradient(transparent, rgba(0,0,0,.2));
  font-size: 20px;
}
.waviy span {
  font-family: 'Alfa Slab One', cursive;
  position: relative;
  display: inline-block;
  color: #000;
  text-transform: uppercase;
  animation: waviy 2s infinite;
  animation-delay: calc(.1s * var(--i));

}
@keyframes waviy {
  0%,40%,100% {
    transform: translateY(0)
  }
  20% {
    transform: translateY(-20px)
  }
}

</style>
<div class="waviy">
   <span style="--i:1">T</span>
   <span style="--i:2">I</span>
   <span style="--i:3">U</span>
   <span style="--i:4">L</span>
   <span style="--i:5">O</span>
   <span style="--i:6">S</span>
   <span style="--i:7"> </span>
   <span style="--i:8">Y</span>
   <span style="--i:9"> </span>
   <span style="--i:10"> E</span>
   <span style="--i:11">N</span>
   <span style="--i:12">C</span>
   <span style="--i:13">A</span>
   <span style="--i:14">B</span>
   <span style="--i:15">E</span>
   <span style="--i:16">Z</span>
   <span style="--i:17">A</span>
   <span style="--i:18">D</span>
   <span style="--i:19">O</span>
   <span style="--i:20">S</span>
  </div>
''',width=1000, height=100)

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

html('''
<style>


@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap');
* {
  padding: 10px;
  margin: 1;
  box-sizing: border-box;
}


.waviy {
  position: relative;
  -webkit-box-reflect: below -20px linear-gradient(transparent, rgba(0,0,0,.2));
  font-size: 20px;
}
.waviy span {
  font-family: 'Alfa Slab One', cursive;
  position: relative;
  display: inline-block;
  color: #000;
  text-transform: uppercase;
  animation: waviy 2s infinite;
  animation-delay: calc(.1s * var(--i));

}
@keyframes waviy {
  0%,40%,100% {
    transform: translateY(0)
  }
  20% {
    transform: translateY(-20px)
  }
}

</style>
<div class="waviy">
   <span style="--i:1">T</span>
   <span style="--i:2">E</span>
   <span style="--i:3">X</span>
   <span style="--i:4">T</span>
   <span style="--i:5">O</span>

  </div>
''',width=1000, height=100)

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
