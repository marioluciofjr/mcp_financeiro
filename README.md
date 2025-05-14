# mcp_financeiro

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
![license - MIT](https://img.shields.io/badge/license-MIT-green)
![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)
![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como instalar no Claude Desktop](#como-instalar-no-claude-desktop)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

Este projeto `mcp_financeiro` oferece uma ferramenta para análise e planejamento financeiro pessoal. Ele calcula uma "grana ideal" baseada nos gastos totais e horas trabalhadas no mês, determinando a receita mensal ideal e o valor da hora de trabalho. Além disso, a ferramenta avalia a saúde financeira do usuário com base na receita real e oferece dicas personalizadas, considerando gastos essenciais, objetivos, aposentadoria, educação e gastos livres.

## Estrutura do projeto

Este projeto leva em consideração as explicações do professor Sandeco Macedo, da UFG (Universidade Federal de Goiás), sobre MCPs por meio do livro [MCP e A2A para Leigos
](https://physia.com.br/mcp/). É um MCP-Server simples que utiliza somente o pacote FastMCP, seguindo também as orientações do repositório oficial do [Model Context Protol](https://github.com/modelcontextprotocol/python-sdk), da Anthropic.

Como referência para a fórmula de economia 70/30, utilizada neste MCP-server, utilizei os ensinamentos do livro ["Me Poupe! 10 passos para nunca mais faltar dinheiro no seu bolso"](https://www.amazon.com.br/Me-Poupe-passos-dinheiro-atualizada/dp/6555640782/ref=asc_df_6555640782?mcid=c13b4ef3aef33da8ac51c61d8f504eb3&tag=googleshopp00-20&linkCode=df0&hvadid=709857900366&hvpos=&hvnetw=g&hvrand=10869634334101385047&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9196805&hvtargid=pla-1041484830851&psc=1&language=pt_BR&gad_source=1)

Este MCP-Server tem as seguintes classes: 

* tool --> É uma tool que calcula o valor ideal mensal que a pessoa deve receber e quanto custa a hora dela. Sendo que o argumento 'gastos_totais' é o valor total que a pessoa gasta no mês e 'horas_mes' é a quantidade de horas que a
	pessoa trabalha no mês. A partir disso, a função retorna uma string com uma explicação do cenário atual da pessoa.
* resource --> Retorna o conteúdo bruto do arquivo [`dicas_financeiras.md`](https://github.com/marioluciofjr/mcp_financeiro/blob/main/mcp_financeiro/dicas_financeiras.md) do projeto.
* prompt --> Prompt para acionar a tool 'grana_ideal' e, a partir disso, fazer uma análise da saúde financeira. O argumento 'gastos_totais' é o valor total que a pessoa gasta no mês, 'horas_mes' é a quantidade de horas que a
	pessoa trabalha no mês, 'receita_real' é a média de quanto a pessoa ganha por mês, 'perfil_de_investimento' é o perfil de investimento da pessoa (conservador, moderado ou arrojado), 'trabalho' é o que a pessoa faz para ganhar dinheiro e 'hobby' é o que a pessoa costuma fazer para se entreter.

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/c0604008-f730-413f-9c4e-9b06c0912692" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/cf957637-962d-4548-87d4-bbde91fadc22" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/18c95cc3-d8bc-486c-b0cf-b5d128980176" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/abafaea5-eb57-4965-9130-7816280a8d84" />&nbsp;&nbsp;&nbsp; 
</div>

## Requisitos

* Python instalado (versão 3.10 ou superior);
* Pacote `uv` instalado;
* Claude Desktop instalado.

## Como instalar no Claude Desktop

Agora vou detalhar um passo a passo no Windows 11, utilizando o terminal (atalho `CTRL` + `J`) no VSCode: 

1. Instalei a [versão mais atualizada do Python](https://www.python.org/downloads/)
2. Já no VSCode, eu utizei o terminal para verificiar a versão do python com o comando
   ```powershell
   python --version
   ```
3. Depois eu instalei o `uv` com o comando
   ```powershell
   pip install uv
   ```
4. Para conferir se estava tudo certo, eu utilizei o comando
   ```powershell
   uv
   ```
5. Para criar a pasta do projeto, eu utilizei este comando
   ```powershell
   mkdir “C:\Users\meu_usuario\OneDrive\area_de_trabalho\MCPs\mcp_financeiro”
   ```

  > [!IMPORTANT]
  > Não necessariamente quer dizer que você utilizará o mesmo caminho, pode ser que você queira utilizar outro caminho, como este abaixo
  > ```powershell
  >   mkdir "C:\Users\seu_usuario\mcp_financeiro"
  >   ```
  >   Ou você pode simplesmente fazer o download do zip desse projeto para a sua máquina pelo caminho `Code` > `Download ZIP` aqui mesmo no GitHub

6. Chamei a pasta que eu tinha acabado de criar
   ```powershell
   cd “C:\Users\meu_usuario\OneDrive\area_de_trabalho\MCPs\mcp_financeiro”
   ```
7. Utilizei o comando abaixo para abrir outra janela do VSCode e continuar com os demais comandos direto na pasta
   ```
   code .
   ```

  > [!IMPORTANT]
  > Se não quiser criar a pasta via terminal, você pode criar uma nova pasta na sua área de trabalho ou outro local que se lembre facilmente, a fim de utilizar o atalho no VSCode
  > `CTRL` + `O`
  > Depois é só procurar a pasta que acabou de criar, clicar nela e abrir no VSCode. Ou somente importar a pasta completa desse repositório no seu VSCode.

8. Voltando ao terminal, utilizei o comando abaixo para inicializar um novo projeto Python, criando arquivos de configuração e dependências automaticamente
   ```powershell
   uv init
   ```
9. Adicionei a dependência MCP, necessária para o projeto
    ```powershell
    uv add mcp[cli]
    ```
10. Verifiquei se estava tudo ok, com o comando abaixo
    ```powershell
    mcp
    ```

> [!IMPORTANT]
> Se aparecer esta informação abaixo no seu terminal é porque está tudo certo
> 
> ![Image](https://github.com/user-attachments/assets/7c692a88-929e-4b8c-84df-b8ce0f004139)

11. Para criar o arquivo `server.py`, eu utilizei esse comando
    ```powershell
    uv init --script server.py
    ```

> [!TIP]
> Como você pode já ter baixado a pasta desse repositório, então o arquivo `server.py`já estará lá no seu VSCode nessa altura do campeonato.

12. Instalei o json abaixo do MCP-Server diretamente no arquivo `claude_desktop_config.json`
    ```json
    "financeiro": {
      "command": "uv",
      "args": [
        "--directory",
        "C://Users//meu_usuario//OneDrive//area_de_trabalho//MCPs//mcp_financeiro",
        "run",
        "server.py"
      ]
    }
    ```

> [!IMPORTANT]
> Se você já instalou o Claude Desktop corretamente, siga o caminho para acessar o arquivo `claude_desktop_config.json` no seu computador\
> 12a. Com o Claude Desktop aberto, utilize o atalho `CTRL` + `,`\
> 12b. Clique na aba `Desenvolvedor` e depois em `Editar configuração`\
> 12c. Procure o arquivo `claude_desktop_config.json` e edite no VSCode corretamente\
> 12d. Salve o arquivo com `CTRL` + `S`\
> 12e. Feche o Claude Desktop e abra novamente depois de alguns segundos\
> 12f. Confira no ícone de configuração se a ferramenta do MCP "mcp_financeiro" está instalada corretamente
>
> ![Image](https://github.com/user-attachments/assets/6553bcd2-1f3c-4963-9d6a-15b0dc614edd)
>
> A ferramenta foi nomeada como `grana_ideal`.
>
> 12g. Para utilizar, você deve clicar no ícone de '+' e, na opção `Adicionar do financeiro`, clicar no resourse `file://dicas_financeiras`. Refaça o caminho e clique no prompt chamado `saude_financeira` também.
>
> ![Image](https://github.com/user-attachments/assets/8f45164f-be84-46ee-b57d-fdac0b1f04d0)
>
> 12h. Ao clicar no prompt `saude_financeira`, aparecerá um formulário. Basta preencher e clicar no botão `Adicionar prompt` e executar no Claude Desktop.
>
> ![Image](https://github.com/user-attachments/assets/95054f46-b8fa-4f30-82dc-a7a65f795849)

## Links úteis

* [Documentação oficial do Model Context Protocol](https://modelcontextprotocol.io/introduction) - Você saberá todos os detalhes dessa inovação da Anthropic
* [Site oficial da Anthropic](https://www.anthropic.com/) - Para ficar por dentro das novidaddes e estudos dos modelos Claude
* [Como baixar o Claude Desktop](https://claude.ai/download) - Link direto para download
* [Como instalar o VSCode](https://code.visualstudio.com/download)- Link direto para download
* [Documentação oficial do pacote uv](https://docs.astral.sh/uv/) - Você saberá todos os detalhes sobre o `uv` e como ele é importante no python
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Conjunto de ícones de modelos de IA/LLM](https://lobehub.com/pt-BR/icons) - site muito bom para conseguir ícones do ecossistema de IA
* [Devicon](https://devicon.dev/) - site bem completo também com ícones gerais sobre tecnologia
* [Simulador do Tesouro Direto](https://www.tesourodireto.com.br/simulador/) - simulador que possibilita entender qual é o melhor título público de acordo com o seu perfil de investimento
* [Status Invest](https://statusinvest.com.br/) - site referência no quesito de análise fundamentalista
* [Trading Economics](https://tradingeconomics.com/) - Site com vários indicadores, excelente para análises econômicas e geopolíticas

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/mcp_content/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 


