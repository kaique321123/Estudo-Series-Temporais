# Séries Temporais com Pandas, NumPy e Modelos Estatísticos
___

Durante os estudos, explorei técnicas avançadas de análise e modelagem de séries temporais usando bibliotecas como **Pandas**, **NumPy** e ferramentas de visualização como **Matplotlib**. Também foram implementados modelos estatísticos, como ETS, EWMA e métodos de Holt-Winters, para análise de componentes como tendência, sazonalidade e ciclos.

---

## Conceitos Fundamentais de Séries Temporais

1. **Tendência (Trend):**  
   Movimento de longo prazo da série temporal, podendo ser linear ou não linear.  
   Exemplos: crescimento constante de vendas ao longo dos anos.

2. **Sazonalidade (Seasonality):**  
   Padrões que se repetem em intervalos regulares.  
   Exemplo: aumento de vendas no Natal.

3. **Ciclo (Cycle):**  
   Padrões recorrentes sem periodicidade fixa, geralmente influenciados por fatores econômicos ou sociais.

### Fórmula Geral:
- Modelo Aditivo:  
  
  #### y(t) = Tendência (t)  + Sazonalidade (t)  + Erro (t) 
  
- Modelo Multiplicativo:  
  
  #### y(t) = Tendência (t)  * Sazonalidade (t)  * Erro (t) 
  

---

## Modelos Estatísticos Utilizados

### 1. Modelos ETS (Erro-Tendência-Sazonalidade)
Decompõem séries temporais em três componentes: erro, tendência e sazonalidade.  
- **Aditivo:** Útil para variações constantes ao longo do tempo.  
- **Multiplicativo:** Recomendado para variações proporcionais ao nível dos dados.

**Exemplo de Implementação:**  
```python
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['Valores'], model='multiplicative')
result.plot()
plt.show()
```

### 2. Modelos de Médias Móveis
- **SMA (Simple Moving Averages):** Média simples dos últimos N períodos.
- **EWMA (Exponential Weighted Moving Averages):** Média ponderada com maior peso para os dados mais recentes.

**Fórmula EWMA:**

#### S<small>t</small> = α * X<small>t</small> + (1 - α) * S <small>t-1</small>

Onde:
- `α = 2 / (N + 1)`

- **α** maior → Mais responsivo.
- **α** menor → Suavização maior.

**Exemplo de Implementação:**  
```python
df['EWMA-12'] = df['Valores'].ewm(span=12).mean()
```

### 3. Métodos de Holt-Winters (Tripla Suavização Exponencial)
- **Aditivo:** Melhor para crescimento constante.  
- **Multiplicativo:** Indicado para crescimento exponencial.


**Parâmetros do Modelo Holt-Winters:**
- **Alpha (α)**: Controla o peso dos dados mais recentes na previsão.
- **Beta (β)**: Relacionado à tendência.
- **Gamma (γ)**: Relacionado à sazonalidade.

Ajustar esses parâmetros é essencial para melhorar a previsão, considerando a sensibilidade a tendências e sazonalidades.
Valores mais altos de **α** tornam o modelo mais sensível a mudanças recentes, enquanto valores menores suavizam mais os dados.

**Fórmula Geral:**

#### <small>**yt**</small> = (L<small>t-1</small> + T<small>t-1</small>) * S<small>t-s</small> + E<small>t</small>

Onde:
- **L<small>t</small>**: Nível estimado da série.
- **T<small>t</small>**: Tendência estimada.
- **S<small>t</small>**: Componente sazonal.
- **s**: Período sazonal.

**Exemplo de Implementação:**  
```python
model = ExponentialSmoothing(
    df['Valores'],
    trend='add',
    seasonal='add',
    seasonal_periods=12 # Ciclo sazonal
).fit(smoothing_level=0.8, smoothing_slope=0.2, smoothing_seasonal=0.5) # alpha (α), beta (β) e gamma (γ) respectivamente
df['HW'] = model.fittedvalues
df[['Valores', 'HW']].plot(figsize=(12, 6))

```
É possível deixar o ``fit()`` otimizar os parâmetros automaticamente, mas é recomendado ajustá-los manualmente para melhorar a previsão.

---

## Visualização e Manipulação de Dados

### Manipulação de Frequências
Configurar corretamente a frequência do índice das séries temporais é essencial para modelos estatísticos:
- Frequências comuns: `D` (diária), `MS` (mensal), `A` (anual), `Q` para trimestral, `W` para semanal.  

### Visualização
Usando `Matplotlib` para observar tendências e sazonalidades:
```python
df['Valores'].plot()
plt.title('Série Temporal')
plt.show()
```

### Rolagens e Expansões
- **Médias móveis:** Identificar tendências locais.  
- **Expansões:** Considerar dados cumulativos para tendências globais.

---

## Exemplos Reais de Aplicação

### Previsão de Passageiros Aéreos

Este exemplo utiliza séries temporais reais para prever o número de passageiros aéreos ao longo do tempo. Técnicas como decomposição sazonal, suavização exponencial e métodos de Holt-Winters ajudam a identificar padrões e realizar previsões.

1. **Decomposição Sazonal:**  
   Separar a série em tendência, sazonalidade e erro.  
   **Exemplo:**
   ```python
   result = seasonal_decompose(airline['Passengers'], model='multiplicative')
   result.plot()
   plt.show()
   ```

2. **Suavização Exponencial Simples (SES):**  
   Técnica para modelar séries **não sazonais**.  
   **Exemplo:**
   ```python
   from statsmodels.tsa.holtwinters import SimpleExpSmoothing
   model = SimpleExpSmoothing(airline['Passengers']).fit()
   airline['SES'] = model.fittedvalues
   ```

3. **Modelo Holt-Winters (Tripla Suavização Exponencial):**  
   Incorpora tendência e sazonalidade.  
   **Exemplo:**
   ```python
   airline['TES'] = ExponentialSmoothing(
       airline['Passengers'],
       seasonal='mul',
       seasonal_periods=12
   ).fit().fittedvalues
   ```

---

1. **Resample Usado para Alterar a Frequência dos Dados para Agregação por Ano:**

    **Exemplo:**
      ```python
      df['Close'].resample('A').mean().plot.bar()
      plt.show()
      ```

2. **Visualização com SMA:**  

    **Exemplo:**
   ```python
   df['30-Day SMA'] = df['Close'].rolling(window=30).mean()
   df[['Close', '30-Day SMA']].plot(figsize=(12, 6))
   plt.show()
   ```