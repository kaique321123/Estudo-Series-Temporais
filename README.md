# Séries Temporais com Pandas, NumPy e Modelos Estatísticos

## Introdução
Durante os estudos, explorei conceitos fundamentais de manipulação de dados com **Pandas** e **NumPy**, que fornecem uma base sólida para trabalhar com séries temporais. Esses conhecimentos foram aplicados na análise de tendências, sazonalidades e padrões cíclicos, utilizando também ferramentas estatísticas para modelagem de séries temporais.

---

## Conceitos Fundamentais de Séries Temporais
1. **Tendência (Trend)**  
   Representa o movimento de longo prazo na série, como crescimento ou declínio persistente ao longo do tempo.
   
2. **Sazonalidade (Seasonality)**  
   Refere-se a padrões que se repetem em intervalos fixos, como aumentos regulares de vendas no fim do ano.

3. **Ciclo (Cycle)**  
   Refere-se a padrões que ocorrem em intervalos variáveis, sem periodicidade fixa, influenciados por fatores econômicos ou sociais.

---

## Manipulação de Frequências de Índice no Pandas
Os índices das séries temporais devem ser configurados corretamente para aplicar modelos como ETS e EWMA. No Pandas, usamos a propriedade `freq` para especificar a frequência:
- **`MS` (Month Start)**: Define a frequência para o início de cada mês.
- **`A` (Annual)**: Define a frequência anual.
- **Outras Frequências**:  
   - `D` para diário.  
   - `W` para semanal.  
   - `Q` para trimestral.

### Exemplo
```python
df.index.freq = 'MS'  # Define frequência mensal
```
Isso é essencial para que os modelos estatísticos possam interpretar corretamente os dados temporais.

---

## Modelos Estatísticos Utilizados
1. **ETS (Error-Trend-Seasonality)**  
   Os modelos ETS decompoem a série em três componentes principais:
   - **Erro (Error)**: Representa a incerteza.
   - **Tendência (Trend)**: Mostra a direção dos dados.
   - **Sazonalidade (Seasonality)**: Captura os padrões cíclicos repetitivos.

   ### Modelos Aditivos e Multiplicativos
   - **Aditivo**: Quando a variação é constante ao longo do tempo.  
     Fórmula: \( y(t) = Tendência + Sazonalidade + Erro \)  
   - **Multiplicativo**: Quando a variação é proporcional ao nível dos dados.  
     Fórmula: \( y(t) = Tendência \times Sazonalidade \times Erro \)

2. **EWMA (Exponential Weighted Moving Averages)**  
   É uma versão mais responsiva que dá maior peso aos dados recentes.  
   Usado para suavizar séries temporais e identificar tendências mais claramente.

   ### Configuração de EWMA
   O parâmetro **alpha** controla a reatividade do modelo:  
   - Valores maiores tornam o modelo mais sensível a mudanças recentes.  
   - Valores menores suavizam mais os dados.

   ```python
   span = 12
   alpha = 2 / (span + 1)
   df['EWMA12'] = df['Values'].ewm(alpha=alpha, adjust=False).mean()
   ```

3. **Holt-Winters (Métodos de Suavização Exponencial)**  
   - O modelo **aditivo** é ideal para dados com crescimento constante.  
   - O modelo **multiplicativo** é melhor para crescimento exponencial.

---

## Visualização de Componentes
Utilizei **Matplotlib** para visualizar os componentes da série. Exemplo:
```python
result = seasonal_decompose(df['Values'], model='multiplicative')
result.plot()
plt.show()
```

---

## Método Fit
O método **`fit`** ajusta o modelo aos dados, calculando os parâmetros necessários para representar padrões históricos e fazer previsões. 

No contexto de suavização exponencial, ele determina valores como:
- **Alfa (α)**: Peso dos dados recentes.
- **Beta (β)**: Relacionado à tendência.
- **Gama (γ)**: Relacionado à sazonalidade.

#### Exemplo:
```python
model = SimpleExpSmoothing(df['Thousands of Passengers'])
fitted_model = model.fit(smoothing_level=alpha, optimized=False)
```
- **`fit`** ajusta o modelo aos dados, usando o valor de suavização definido (`smoothing_level=alpha`).
- Permite acessar os valores ajustados com **`fittedvalues`** ou fazer previsões futuras.

---

### Mais dados/variáveis melhoram a previsão

Quanto mais dados e variáveis relevantes adicionamos ao modelo, melhor ele consegue capturar os padrões da realidade, tornando a previsão mais próxima do valor real. Isso acontece porque:

1. **Captura de mais dimensões do problema**:  
   Variáveis adicionais podem representar fatores que influenciam diretamente o comportamento da série temporal, como sazonalidade, tendências econômicas, ou eventos específicos.

2. **Redução de incertezas**:  
   Mais dados fornecem maior contexto histórico, ajudando a suavizar variações aleatórias e capturar padrões consistentes.

3. **Modelos mais robustos**:  
   Com mais informações, o modelo pode aprender e ajustar parâmetros com maior precisão, o que diminui o risco de subajuste (quando o modelo é muito simples para representar os dados).

#### Exemplo prático:
Imagine prever o número de passageiros de uma companhia aérea:
- Apenas com os dados de passageiros passados, a previsão considera apenas o histórico.
- Ao incluir variáveis como **estação do ano**, **feriados**, e **eventos econômicos**, o modelo compreende melhor o impacto desses fatores, gerando previsões mais precisas.

### Como isso se reflete matematicamente
Quando mais variáveis ou dados relevantes são adicionados:
- O **erro residual** (diferença entre o valor real e a previsão) diminui.
- O modelo se ajusta melhor aos dados históricos, mas deve-se evitar o excesso de complexidade, para não "memorizar" os dados (sobreajuste).
___

### SimpleExpSmoothing, model.fit, e fittedvalues.shift

- **`SimpleExpSmoothing`**: Método de suavização exponencial simples para modelar séries temporais **não sazonais**. Dá maior peso aos dados mais recentes, útil para previsões de curto prazo.

- **`model.fit`**: Ajusta o modelo aos dados, calculando os parâmetros (como **`α`**, o nível de suavização). Retorna previsões ajustadas em **`fittedvalues`**.

- **`fittedvalues.shift`**:
  - **`shift(-1)`**: Desloca previsões para frente, usado para prever o próximo valor na série.
  - **`shift(1)`**: Desloca previsões para trás, útil para alinhar previsões com os dados reais observados.

**Quando usar?**
- Use **`SimpleExpSmoothing`** e **`fit`** para ajustar modelos em dados simples e não sazonais.
- Ajuste o **`shift`** conforme a necessidade de prever valores futuros ou comparar com dados passados.

#### Exemplo:
````python
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Dados de exemplo
data = [10, 12, 13, 14, 15]

# Criando o modelo
model = SimpleExpSmoothing(data)

# Ajustando o modelo
fitted_model = model.fit(smoothing_level=alpha, optimized=False)

# Obtendo valores ajustados
fitted_values = fitted_model.fittedvalues

# Deslocando as previsões
fitted_values_shifted_forward = fitted_values.shift(-1)  # Para prever o próximo valor
fitted_values_shifted_backward = fitted_values.shift(1)  # Para alinhar ao período anterior
````
___

### seasonal_periods

O **`seasonal_periods`** define o ciclo da sazonalidade em séries temporais, ou seja, o intervalo em que os padrões se repetem. É usado em modelos como `ExponentialSmoothing` para capturar comportamentos sazonais e melhorar a precisão das previsões. Por exemplo, para dados mensais com repetição anual, usa-se **`seasonal_periods=12`**. É essencial para modelar séries com ciclos bem definidos, como vendas sazonais ou padrões climáticos.

#### Exemplo:
```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Série com padrão sazonal mensal
model = ExponentialSmoothing(
    df['Thousands of Passengers'],
    trend='add',
    seasonal='add',
    seasonal_periods=12  # 12 meses em um ano
)
fitted_model = model.fit()
```

___