import streamlit as st
import sqlite3

nome = st.text_input('Nome')
email = st.text_input('E-mail:')

btn_salvar = st.button('Salvar')

if btn_salvar:
    registro = (nome, email)

    try:
        conexao = sqlite3.connect('databases/loja.db')

        sql = ''' INSERT INTO clientes(nome, email) VALUES(?,?) '''
        cur = conexao.cursor()
        cur.execute(sql, registro)
        conexao.commit()

        st.success('Registro inserido com sucesso!')

    except sqlite3.Error as e:
        st.error('Erro ao inserir cliente!')
    finally:
        conexao.close()