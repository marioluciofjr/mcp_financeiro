# server.py

from mcp.server.fastmcp import FastMCP 
from typing import Annotated
from pydantic import Field

# Inicializa o servidor FastMCP 
mcp = FastMCP("financeiro")

@mcp.tool(name="grana_ideal")
def grana_ideal(gastos_totais: float, horas_mes: int) -> str:
    """
    É uma tool que calcula o valor ideal mensal que a pessoa deve receber e quanto custa a hora dela. Sendo que
    o argumento 'gastos_totais' é o valor total que a pessoa gasta no mês e 'horas_mes' é a quantidade de horas que a
	pessoa trabalha no mês. 
    A partir disso, a função retorna uma string com uma explicação do cenário atual da pessoa.
 
    """

    receita_ideal = gastos_totais / 0.55
    objetivos = receita_ideal * 0.20
    aposentadoria = receita_ideal * 0.10
    educa = receita_ideal * 0.05
    livre = receita_ideal * 0.10
    valor_hora = receita_ideal / horas_mes

    return f"""
    Levando em consideração os seus gastos totais de R$ {gastos_totais}, o ideal é que você tenha uma 
    receita mensal de R$ {round(receita_ideal,2)}. Estando tudo certo com essa meta, pense em alocar o seu dinheiro de 
    acordo com a fórmula 70/30 da Natália Arcuri: 

    * gastos essenciais = R$ {gastos_totais};
    * objetivos de curto, médio e longo prazo = R$ {round(objetivos,2)};
    * aposentadoria = R$ {round(aposentadoria,2)};
    * educação = R$ {round(educa,2)};
    * gastos livres = R$ {round(livre,2)}.

    Sua hora de trabalho ideal é de R$ {round(valor_hora,2)}.

    """

@mcp.resource("file://dicas_financeiras")
def dicas_financeiras() -> bytes:
    """Retorna o conteúdo bruto do arquivo dicas_financeiras.md do projeto."""
    with open("dicas_financeiras.md", "rb") as f:
        return f.read()

@mcp.prompt() 
def saude_financeira(
    gastos_totais: Annotated[float, Field(description="""Gastos totais no mês. Ex: 3000.00""")], 
	horas_mes: Annotated[int, Field(description="""Horas trabalhadas no mês. Ex: 160""")], 
    receita_real: Annotated[float, Field(description="""Receita média mensal. Ex: 4000.00""")], 
    perfil_de_investimento: Annotated[str, Field(description="""Escolha entre conservador, moderado ou arrojado""")],
  	trabalho: Annotated[str, Field(description="""Descreva com o que você trabalha""")],
	hobby: Annotated[str, Field(description="""Descreva com o que você costuma se entreter""")] 
    ) -> str:
	"""
	Prompt para acionar a tool 'grana_ideal' e, a partir disso, fazer uma análise da saúde financeira. O 
    	argumento 'gastos_totais' é o valor total que a pessoa gasta no mês, 'horas_mes' é a quantidade de horas que a
	pessoa trabalha no mês, 'receita_real' é a média de quanto a pessoa ganha por mês, 'perfil_de_investimento' é o
	perfil de investimento da pessoa (conservador, moderado ou arrojado), 'trabalho' é o que a pessoa faz para ganhar dinheiro e
	'hobby' é o que a pessoa costuma fazer para se entreter.
	"""
    
	receita_ideal = gastos_totais / 0.55

	prompt = f"""
	<função>
	Você atuará como um profissional de finanças experiente, que sabe analisar diversos cenários econômicos. 
	Você tem especialização em finanças comportamentais, tem consciência de classe e é capaz de entender o contexto social e econômico.
        Você é objetivo, mas didático e respeitoso. Você evita jargões financeiros e explica termos técnicos de forma simples.
	</função>

	<contexto>
	Em resource estão dicas financeiras que vão nortear as informações passadas para a pessoa usuária.
	</contexto>

	<tarefa>
        ## Distribuição ideal
    
        Chame a tool 'grana_ideal' e print o resultado dela.
    
        Em seguida, envie a seguinte mensagem:
        "Sua receita real é de R$ {round(receita_real, 2)}, sendo que sua receita ideal deveria ser de R$ {round(receita_ideal, 2)}. 
        Ou seja, atualmente você ganha {(receita_real/receita_ideal)* 100:.2f}% do que deveria ganhar."
    
	## Avaliação da saúde financeira 

        <regra>
        Respeite as condicionantes abaixo para classificar a saúde financeira da pessoa e dar dicas financeiras.
        </regra>   

	Se o valor da receita real (R$ {receita_real}) for menor ou igual aos gastos totais (R$ {gastos_totais}), dê apenas 5 dicas 
	de como a pessoa pode enxugar gastos e renegociar dívidas. Formato de saída será de até 100 palavras. Finalize em seguida com o disclaimer.

	Se o valor da receita real (R$ {receita_real}) for maior que os gastos totais e ficar abaixo de 25%
	da receita ideal de R$ {round(receita_ideal, 2)}), 
        classifique a saúde financeira como péssima e dê 5 dicas de como a pessoa pode aumentar a receita. Formato de saída será de até 100 palavras. Finalize em seguida com o disclaimer.

        Se o valor da receita real (R$ {receita_real}) for maior que os gastos totais e ficar entre 25% e 50%
	da receita ideal de R$ {round(receita_ideal, 2)}), 
        classifique a saúde financeira como ruim e dê 5 dicas de como a pessoa pode aumentar a receita. Formato de saída será de até 100 palavras. Finalize em seguida com o disclaimer.

	Se o valor da receita real (R$ {receita_real}) for maior que os gastos totais e ficar entre 50% e 75%
	da receita ideal de R$ {round(receita_ideal, 2)}), 
        classifique a saúde financeira como regular e dê 5 dicas de como a pessoa pode aumentar a receita. Formato de saída será de até 100 palavras. Finalize em seguida com o disclaimer.

        Se o valor da receita real (R$ {receita_real}) for maior que os gastos totais e ficar entre 75% e 90%
	da receita ideal de R$ {round(receita_ideal, 2)}), 
        classifique a saúde financeira como boa e dê 5 dicas de como a pessoa pode aumentar a receita. Formato de saída será de até 100 palavras. Finalize em seguida com o disclaimer.
     
        Agora se o valor da receita real (R$ {receita_real}) for maior que os gastos totais e for maior que 90%
	da receita ideal de R$ {round(receita_ideal, 2)}), classifique a saúde financeira como ótima e dê 3 dicas profissionais de alocação de recursos financeiros, para cada categoria, levando em consideração o resultado da tool 'grana_ideal', o perfil de investimento definido como {perfil_de_investimento}, 
	o trabalho definido como {trabalho}, as horas trabalhadas no mês definidas como {horas_mes} e o hobby definido como {hobby}. 
        Formato de saída será de até 300 palavras organizadas por categoria assim:
    
        ### Objetivos de curto, médio e longo prazo    
        Disponível: R$ {round(receita_real * 0.20, 2)}
     
        Apresente aqui dicas financeiras para os objetivos de curto, médio e longo prazo de acordo com o objetivo da tool 'grana_ideal', perfil de investimento e trabalho da pessoa.
    
        ### Aposentadoria    
	Disponível: R$ {round(receita_real * 0.10, 2)}
    
        Apresente aqui dicas financeiras para aposentadoria com base no perfil de investimento e trabalho da pessoa.
    
        ### Educação    
	Disponível: R$ {round(receita_real * 0.05, 2)}
	 
	Apresente aqui dicas financeiras para educação com base no perfil de investimento, trabalho e hobby da pessoa.
	
	### Gastos livres     
	Disponível: R$ {round(receita_real * 0.10, 2)}
     
	Apresente aqui dicas financeiras para gastos livres com base no perfil de investimento, trabalho, horas trabalhadas e hobby da pessoa.

	## Disclaimer

	Ao final, envie esta mensagem: "A IA generativa apenas oferece sugestões e que essa é uma simulação para fomentar a educação financeira. Torna-se essencial consultar uma pessoa especialista 
	financeira, bem como estudar a fundo sobre perfil de investimento, tipos de investimento, juros compostos, inflação, taxa SELIC, CDI etc."
	</tarefa>

	"""

	return prompt

if __name__ == "__main__":
    mcp.run(transport='stdio')
