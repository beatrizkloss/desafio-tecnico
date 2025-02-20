# 📝 Desafio Técnico

Este repositório contém a resolução de um conjunto de questões de programação e banco de dados, com foco em **Python** e **MySQL**. As soluções abordam desde manipulação de strings até consultas SQL envolvendo criação de tabelas e operações de dados.

## ⚙️ Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Banco de Dados**: MySQL

---

## 📚 Descrição das Questões

### 1. Função para Imprimir Linhas 📊
Escreva uma função que receba um valor inteiro como parâmetro de entrada e imprima na tela *n* linhas conforme a estrutura apresentada abaixo. Por exemplo, as seguintes linhas devem ser
apresentadas ser o parâmetro de entrada for 10.

**NOTA:**
- Caso seja inserido um valor menor ou igual a zero, uma crítica deverá ser exibida e o
processo deverá ser abortado.


---

### 2. Função de Compactação de String 🧳
Escreva uma função que receba um parâmetro do tipo string e retorne uma string como resultado. A função deverá "compactar" a string recebida como parâmetro de entrada. A compactação funcionará escrevendo o caractere encontrado seguido da quantidade de vezes que ele ocorre em sequência.

**Exemplo**:
- Parâmetro de entrada: `jjjjooaoo`
- Resultado da função: `j4o2a1o2`

---

### 3. Leitura e Análise de Números 🔢
Escreva um programa que leia números positivos do teclado até que o número zero seja digitado. Após, o programa deverá exibir um relatório na tela descrevendo os seguintes itens:
- Quantos números foram lidos.
- O maior número lido.
- A média dos números lidos.
- O menor número ímpar lido (caso algum número ímpar tenha sido digitado).
- A quantidade de vezes que cada número ocorreu. Exemplo: "O número 7 ocorreu 2 vezes."
  "O número 13 ocorreu 8 vezes".

DICA: Use vetores.

---

### 4. Leitura de Arquivo e Contagem de Vogais/Consoantes 📄
Escreva um programa que leia um arquivo texto (.txt) escolhido pelo usuário. Após a leitura do arquivo, o programa deverá exibir qual linha possui mais vogais e qual linha possui mais consoantes. Por simplicidade, admita que o arquivo conterá apenas letras (sem acentos ou ç) e espaços em branco. Caso ocorra empate, qualquer uma das linhas poderá ser exibida.

---

## 🗃️ Questões de SQL

### 5. Criação das Tabelas `CLIENTES` e `TELEFONES` 🗂️
Escreva o script necessário para a criação de duas tabelas: uma chamada `CLIENTES` e outra chamada `TELEFONES`. A tabela `CLIENTES` deverá possuir os seguintes campos: `NOME`, `CPF` e `IDADE`, sendo o `CPF` a chave primária. A tabela `TELEFONES` deverá possuir três campos: `CPF_CLIENTE`, `DDD` e `TELEFONE`. Para esta tabela, o campo `CPF_CLIENTE` deverá ser a chave primária e estrangeira, referenciando o campo `CPF` da tabela `CLIENTES`.

---

### 6. Consulta de Clientes com Idade Superior a 22 🎂
Escreva uma consulta SQL para obter o nome de todos os clientes que possuam idade igual ou superior a 22 anos. O resultado deverá estar ordenado pela idade de forma crescente.

---

### 7. Consulta de Clientes com Telefones 📞
Escreva uma consulta SQL que exiba o nome dos clientes e a quantidade de telefones encontrados. A consulta deverá exibir somente o nome dos clientes que possuam pelo menos 1 telefone.

---

### 8. Exclusão de Clientes com Sobrenome "Santos" 🗑️
Escreva o comando SQL necessário para excluir todos os clientes que possuam o sobrenome 'Santos'.

---

## 🚀 Como Usar

1. **Clone este repositório**:

   ```bash
   git clone https://github.com/beatrizkloss/desafio-tecnico.git 
   


