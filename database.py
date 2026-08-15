import sqlite3
from datetime import datetime

def criar_tabela():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas 
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    titulo TEXT NOT NULL, status TEXT NOT NULL, data_criacao TEXT NOT NULL)''')
    conn.commit()
    conn.close()
def criar_tarefa(titulo):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    status = 'pendente'
    data_criacao = datetime.now().strftime('%d/%m/%Y')
    cursor.execute('''INSERT INTO tarefas (titulo, status, data_criacao) 
    VALUES (?, ?, ?)''', (titulo, status , data_criacao ))
    conn.commit()
    conn.close()
def listar_tarefa():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM tarefas''')
    resultados = cursor.fetchall()
    for tarefa in resultados:
        print(tarefa)
    conn.close()
def concluir_tarefa(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET status = ? WHERE id = ?',('concluida', id_tarefa))
    conn.commit()
    linhas_afetadas = cursor.rowcount
    conn.close()
    return linhas_afetadas
def deletar_tarefa(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?',(id_tarefa,))
    conn.commit()
    linhas_afetadas = cursor.rowcount
    conn.close()
    return linhas_afetadas
if __name__ == '__main__':
   # criar_tabela()
   # criar_tarefa('Estudar SQL')
    concluir_tarefa(1)
    deletar_tarefa(2)
    listar_tarefa()
