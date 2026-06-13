import streamlit as st
from fila import Fila

st.set_page_config(page_title="Clínica Médica")

st.title("🏥 Sistema de Atendimento")

# Cria a fila apenas uma vez
if "fila" not in st.session_state:
    st.session_state.fila = Fila()

fila = st.session_state.fila

# Cadastro de pacientes
st.header("Adicionar Paciente")

nome = st.text_input("Nome do paciente")

if st.button("Entrar na fila"):

    if nome:
        fila.enfileirar(nome)
        st.success(f"{nome} adicionado à fila!")
    else:
        st.error("Digite um nome.")

st.divider()

# Exibição da fila
st.header("Fila de Espera")

if fila.esta_vazia():
    st.info("Nenhum paciente aguardando.")
else:

    for posicao, paciente in enumerate(fila.listar(), start=1):
        st.write(f"{posicao}º - {paciente}")

st.divider()

# Atendimento
st.header("Atendimento")

if st.button("Chamar Próximo"):

    paciente = fila.desenfileirar()

    if paciente:
        st.success(f"Paciente chamado: {paciente}")
    else:
        st.warning("Fila vazia.")

st.divider()

# Estatísticas
st.header("Estatísticas")

col1, col2 = st.columns(2)

with col1:
    st.metric("Pacientes na fila", fila.tamanho())

with col2:

    if fila.frente():
        st.metric("Próximo paciente", fila.frente())
    else:
        st.metric("Próximo paciente", "-")
