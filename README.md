# 🪢 Jogo da Forca

Implementação de um **jogo da forca para dois jogadores** em Python puro, desenvolvida como exercício prático de lógica de programação do curso de Introdução à Programação com Python. O programa roda diretamente no terminal, sem dependências externas.

---

## Como funciona

O jogo seleciona uma palavra secreta a partir de um número digitado pelo primeiro jogador, usando a fórmula:

```
índice = (número × 776) % len(lista_de_palavras)
```

Isso garante que a palavra seja determinística — o jogador 1 digita um número, afasta-se do teclado, e o jogador 2 tenta adivinhar a palavra letra por letra.

A forca é desenhada no terminal com arte ASCII e atualizada a cada erro. O jogo termina quando o jogador 2 descobre a palavra ou acumula **6 erros**.

---

## Demonstração

```
======== Exercício 7.10 ========

Digite um número: 42
......
Digite uma letra: a
......
X==:==
X  :  
X     
X     
X     
X     
===========
Você errou!
```

**Progressão da forca (6 estágios de erro):**

| Erros | Parte desenhada |
|-------|----------------|
| 1     | Cabeça (`O`)   |
| 2     | Corpo (`\|`)   |
| 3     | Braço esquerdo (`\`) |
| 4     | Braço direito (`/`)  |
| 5     | Perna esquerda (`/`) |
| 6     | Perna direita (`\`) → **Enforcado!** |

---

## Pré-requisitos

- Python 3.x (sem bibliotecas externas)

---

## Como executar

```bash
# Clone o repositório
git clone https://github.com/leoosalles/introducao-python-exercicio-7-9
cd introducao-python-exercicio-7-9

# Execute o programa
python exercicio_7-9.py
```

---

## Como jogar

1. **Jogador 1** digita um número qualquer e se afasta.
2. **Jogador 2** tenta adivinhar a palavra, digitando uma letra por vez.
3. Letras corretas são reveladas na palavra. Letras erradas constroem a forca.
4. O jogo termina com vitória (palavra completa) ou derrota (6 erros).

---

## Lista de palavras

O jogo conta com 13 palavras do vocabulário cotidiano:

```
faca, garfo, prato, colher, mesa, cadeiras,
copo, garrafa, comida, sala, sofá, poltrona, cozinha
```

Para adicionar palavras, edite a variável `lista_de_palavras` diretamente no código.

---

## Estrutura do projeto

```
jogo-da-forca/
│
├── forca.py      # Código principal do jogo
└── README.md     # Este arquivo
```

---

## Contexto acadêmico

Desenvolvido como solução para o **Exercício 7.9** de um curso de Introdução à Programação com Python, com foco nos seguintes conceitos:

- Manipulação de listas e strings
- Laços `while` e `for`
- Controle de fluxo com `break` e `continue`
- Representação de arte ASCII via listas de caracteres
- Seleção de elemento por fórmula modular

---

## Licença

Distribuído livremente para fins educacionais.
