# 🏝️ Perdido na Ilha --- Caminhos com Abordagem Gulosa, Aleatória e Fixa

Este projeto implementa três estratégias diferentes para percorrer uma
matriz 10x10:\
**abordagem gulosa**, **abordagem aleatória** e **caminho fixo**,
comparando o custo total de cada método ao tentar ir do ponto **(9, 0)**
até **(0, 9)**.

------------------------------------------------------------------------

## 🚀 Funcionalidades

### 🔹 1. Caminho Fixo

Segue uma sequência pré-definida de movimentos (`010101...`), sempre
andando para cima ou para a direita.\
Cada passo coleta o "custo" da casa na matriz.

### 🔹 2. Caminho Aleatório

Gera aleatoriamente uma lista de passos contendo 0 (direita) e 1
(cima).\
Executa 10 simulações diferentes e exibe o custo total de cada uma.

### 🔹 3. Caminho Guloso

Em cada passo compara o custo das duas casas possíveis: - acima\
- direita

E escolhe **sempre a casa de menor custo imediato**.\
Também mostra o estado da matriz a cada 5 passos.

------------------------------------------------------------------------

## ▶️ Como Executar

 bash
git clone https://github.com/saulobeltramne/perdido-na-ilha.git
cd perdido-na-ilha
python perdido_na_ilha.py

------------------------------------------------------------------------
##FIXA
<img width="337" height="673" alt="image" src="https://github.com/user-attachments/assets/741a3e9a-f105-4055-af22-48937b9299bb" />
##ALEATÓRIA 
<img width="682" height="766" alt="image" src="https://github.com/user-attachments/assets/a0c7f34d-d16a-4424-a206-127402d0ae33" />
##GULOSA
<img width="367" height="656" alt="image" src="https://github.com/user-attachments/assets/85bd46c3-4c8b-4b30-9c9b-a89408266a43" />


