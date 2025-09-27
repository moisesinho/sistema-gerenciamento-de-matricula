import psycopg2
from psycopg2 import sql
import sys

class GerenciadorAlunos:
    def __init__(self):
        self.conexao = None
        self.cursor = None
        
    def conectar_banco(self):
        """Conecta ao banco de dados PostgreSQL"""
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="student_db",
                user="postgres",
                password="0",
                port="5432"
            )
            self.cursor = self.conexao.cursor()
            print("Conexão com PostgreSQL estabelecida com sucesso!")
            return True
        except psycopg2.Error as e:
            print(f"Erro ao conectar com PostgreSQL: {e}")
            return False
    
    def criar_tabela(self):
        """Cria a tabela alunos se não existir"""
        try:
            query_criar_tabela = """
            CREATE TABLE IF NOT EXISTS alunos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                curso VARCHAR(255) NOT NULL,
                matriculado VARCHAR(3) CHECK (matriculado IN ('Sim', 'Não')) NOT NULL,
                semestre INTEGER NOT NULL
            );
            """
            self.cursor.execute(query_criar_tabela)
            self.conexao.commit()
            print("✅ Tabela 'alunos' criada/verificada com sucesso!")
        except psycopg2.Error as e:
            print(f"Erro ao criar tabela: {e}")
    
    def cadastrar_aluno(self):
        """Cadastra um novo aluno"""
        print("\n--- Cadastrar Novo Aluno ---")
        
        nome = input("Nome do aluno: ").strip()
        if not nome:
            print("Nome não pode estar vazio!")
            return
        
        curso = input("Curso: ").strip()
        if not curso:
            print("Curso não pode estar vazio!")
            return
        
        while True:
            matriculado = input("Matriculado (Sim/Não): ").strip()
            if matriculado in ['Sim', 'Não']:
                break
            print("Digite apenas 'Sim' ou 'Não'")
        
        while True:
            try:
                semestre = int(input("Semestre: "))
                if semestre > 0:
                    break
                else:
                    print("Semestre deve ser um número positivo!")
            except ValueError:
                print("Digite um número válido para o semestre!")
        
        try:
            query_inserir = """
            INSERT INTO alunos (nome, curso, matriculado, semestre)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query_inserir, (nome, curso, matriculado, semestre))
            self.conexao.commit()
            print(f"Aluno '{nome}' cadastrado com sucesso!")
        except psycopg2.Error as e:
            print(f"Erro ao cadastrar aluno: {e}")
    
    def listar_alunos(self):
        """Lista todos os alunos cadastrados"""
        print("\n--- Lista de Alunos ---")
        
        try:
            query_selecionar = "SELECT id, nome, curso, matriculado, semestre FROM alunos ORDER BY id"
            self.cursor.execute(query_selecionar)
            alunos = self.cursor.fetchall()
            
            if not alunos:
                print("Nenhum aluno cadastrado.")
                return
            
            print(f"{'ID':<5} {'Nome':<25} {'Curso':<25} {'Matriculado':<12} {'Semestre':<10}")
            print("-" * 80)
            
            for aluno in alunos:
                id_aluno, nome, curso, matriculado, semestre = aluno
                print(f"{id_aluno:<5} {nome:<25} {curso:<25} {matriculado:<12} {semestre:<10}")
                
        except psycopg2.Error as e:
            print(f"Erro ao listar alunos: {e}")
    
    def atualizar_aluno(self):
        """Atualiza dados de um aluno"""
        print("\n--- Atualizar Aluno ---")
        
        self.listar_alunos()
        
        try:
            id_aluno = int(input("\nDigite o ID do aluno a ser atualizado: "))
        except ValueError:
            print("ID deve ser um número!")
            return
        
        try:
            query_verificar = "SELECT nome, curso, matriculado, semestre FROM alunos WHERE id = %s"
            self.cursor.execute(query_verificar, (id_aluno,))
            aluno = self.cursor.fetchone()
            
            if not aluno:
                print("Aluno não encontrado!")
                return
            
            nome_atual, curso_atual, matriculado_atual, semestre_atual = aluno
            print(f"\nDados atuais: {nome_atual} | {curso_atual} | {matriculado_atual} | Semestre {semestre_atual}")
            
        except psycopg2.Error as e:
            print(f"Erro ao buscar aluno: {e}")
            return
        
        print("\n(Pressione Enter para manter o valor atual)")
        
        novo_nome = input(f"Novo nome [{nome_atual}]: ").strip() or nome_atual
        novo_curso = input(f"Novo curso [{curso_atual}]: ").strip() or curso_atual
        
        while True:
            novo_matriculado = input(f"Matriculado [{matriculado_atual}] (Sim/Não): ").strip()
            if not novo_matriculado:
                novo_matriculado = matriculado_atual
                break
            elif novo_matriculado in ['Sim', 'Não']:
                break
            else:
                print("Digite apenas 'Sim' ou 'Não'")
        
        while True:
            novo_semestre_input = input(f"Novo semestre [{semestre_atual}]: ").strip()
            if not novo_semestre_input:
                novo_semestre = semestre_atual
                break
            try:
                novo_semestre = int(novo_semestre_input)
                if novo_semestre > 0:
                    break
                else:
                    print("Semestre deve ser um número positivo!")
            except ValueError:
                print("Digite um número válido para o semestre!")
        
        try:
            query_atualizar = """
            UPDATE alunos 
            SET nome = %s, curso = %s, matriculado = %s, semestre = %s 
            WHERE id = %s
            """
            self.cursor.execute(query_atualizar, (novo_nome, novo_curso, novo_matriculado, novo_semestre, id_aluno))
            self.conexao.commit()
            print(f"✅ Aluno ID {id_aluno} atualizado com sucesso!")
            
        except psycopg2.Error as e:
            print(f"Erro ao atualizar aluno: {e}")
    
    def excluir_aluno(self):
        """Exclui um aluno"""
        print("\n--- Excluir Aluno ---")
        
        self.listar_alunos()
        
        try:
            id_aluno = int(input("\nDigite o ID do aluno a ser excluído: "))
        except ValueError:
            print("ID deve ser um número!")
            return
        
        try:
            query_verificar = "SELECT nome FROM alunos WHERE id = %s"
            self.cursor.execute(query_verificar, (id_aluno,))
            aluno = self.cursor.fetchone()
            
            if not aluno:
                print("Aluno não encontrado!")
                return
            
            nome_aluno = aluno[0]
            
            confirmacao = input(f"Tem certeza que deseja excluir o aluno '{nome_aluno}'? (s/N): ").strip().lower()
            if confirmacao != 's':
                print("Operação cancelada.")
                return
            
            query_deletar = "DELETE FROM alunos WHERE id = %s"
            self.cursor.execute(query_deletar, (id_aluno,))
            self.conexao.commit()
            print(f"Aluno '{nome_aluno}' excluído com sucesso!")
            
        except psycopg2.Error as e:
            print(f"Erro ao excluir aluno: {e}")
    
    def mostrar_menu(self):
        """Exibe o menu principal"""
        print("\n" + "="*40)
        print("--- Sistema de Matrículas ---")
        print("="*40)
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Excluir aluno")
        print("0 - Sair")
        print("="*40)
    
    def executar(self):
        """Executa o sistema principal"""
        print("🎓 Sistema de Gerenciamento de Matrículas")
        print("Conectando ao PostgreSQL...")
        
        if not self.conectar_banco():
            print("Não foi possível conectar ao banco de dados.")
            print("Verifique se o PostgreSQL está rodando e as credenciais estão corretas.")
            return
        
        self.criar_tabela()
        
        while True:
            self.mostrar_menu()
            
            try:
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == '1':
                    self.cadastrar_aluno()
                elif opcao == '2':
                    self.listar_alunos()
                elif opcao == '3':
                    self.atualizar_aluno()
                elif opcao == '4':
                    self.excluir_aluno()
                elif opcao == '0':
                    print("Encerrando sistema...")
                    break
                else:
                    print("Opção inválida! Digite um número de 0 a 4.")
                    
            except KeyboardInterrupt:
                print("\n\nSistema encerrado pelo usuário.")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")
        
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
        print("Conexão com banco de dados encerrada.")

def main():
    """Função principal"""
    sistema = GerenciadorAlunos()
    sistema.executar()

if __name__ == "__main__":
    main()