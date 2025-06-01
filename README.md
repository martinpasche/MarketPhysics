
# MarketPhysics

📈 **MarketPhysics** is a comprehensive project developed as part of the *Physique des Marchés* course at CentraleSupélec, instructed by Damian Challet. The project delves into the dynamics of financial markets through empirical analysis, strategy development, and agent-based modeling.

---

## 🗂️ Repository Structure

```
MarketPhysics/
├── TP1/                        # Stylized Facts Analysis
├── TP2/                        # Investment Strategies
├── TP3/                        # Strategy Selection
├── TP4/                        # Market States Clustering
├── TP5/                        # Agent-Based Modeling (ABM) - Minority Game
├── TP6/                        # ABM - Market Impact Analysis
├── TP7/                        # Advanced ABM Studies
├── requirements.txt            # Project dependencies
├── README.md                   # Project overview
└── LICENSE                     # MIT License
```

---

## 📚 Project Overview

### TP1: Stylized Facts in Financial Data

* **Objective**: Analyze daily and intraday financial data to identify stylized facts.
* **Tasks**:

  * Fetch historical data using `yfinance`.
  * Compute log-returns and analyze their distribution.
  * Assess the presence of heavy tails and fit power-law distributions.
  * Compare market behaviors during bullish and bearish periods.

### TP2: Development of Investment Strategies

* **Objective**: Implement and evaluate various trading strategies.
* **Strategies**:

  * Moving Average Crossovers.
  * Mean Reversion Techniques.
  * Conditional Strategies based on market states.
* **Analysis**:

  * Performance evaluation using heatmaps.
  * Stationarity assessment over different time frames.

### TP3: Strategy Selection Using Statistical Methods

* **Objective**: Apply statistical techniques to select robust trading strategies.
* **Methods**:

  * Calculate performance metrics with transaction costs.
  * Perform t-tests to evaluate strategy significance.
  * Implement False Discovery Rate (FDR) control for multiple hypothesis testing.

### TP4: Clustering Market States

* **Objective**: Identify distinct market states using clustering algorithms.
* **Approach**:

  * Apply the Leiden algorithm for clustering.
  * Analyze the temporal evolution of market states.
  * Develop state-dependent trading strategies.

### TP5: Agent-Based Modeling - Minority Game

* **Objective**: Simulate market dynamics using the Minority Game framework.
* **Features**:

  * Model speculators and producers with varying strategies.
  * Analyze the impact of agent participation on market volatility.
  * Study the emergence of market predictability.

### TP6: Market Impact Analysis in ABM

* **Objective**: Investigate the effects of individual agents on market dynamics.
* **Focus Areas**:

  * Assess gains of different investor categories.
  * Examine the discrepancy between expected and realized gains.
  * Evaluate the influence of a single agent's actions on the market.

### TP7: Advanced Studies in Agent-Based Modeling

* **Objective**: Explore complex behaviors in agent-based market models.
* **Topics**:

  * Analyze the relationship between agent activity frequency and profitability.
  * Study the effects of agents accounting for their market impact.
  * Investigate the stability of market dynamics under various conditions.

---

## 🛠️ Installation and Requirements

To set up the project environment, ensure you have Python installed and run:

```bash
pip install -r requirements.txt
```

**Key Libraries**:

* Data Handling: `numpy`, `pandas`
* Visualization: `matplotlib`, `seaborn`
* Statistical Analysis: `scipy`, `statsmodels`, `powerlaw`
* Machine Learning: `scikit-learn`
* Financial Data: `yfinance`

---

## 📈 Usage

1. **Navigate** to the respective TP folder.
2. **Open** the Jupyter Notebook (`.ipynb`) files using Jupyter Lab or Notebook.
3. **Execute** the cells sequentially to reproduce the analyses and results.
4. **Modify** parameters or data sources as needed for experimentation.

---

## 🤝 Collaborators

| Name             | Role                      | GitHub                                          |
| ---------------- | ------------------------- | ----------------------------------------------- |
| Martin Pasche    | Team member | [martinpasche](https://github.com/martinpasche) |
| Hugo Yeremian  | Team member     | [h-yer](https://github.com/h-yer)           |


---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Acknowledgements

* **Instructor**: Damian Challet
* **Institution**: CentraleSupélec
* **Course**: Physique des Marchés


