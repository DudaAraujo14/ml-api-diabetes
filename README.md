# 🧠 API de Predição de Diabetes

## 📌 Descrição

Este projeto tem como objetivo desenvolver e disponibilizar um modelo de Machine Learning como uma API acessível via HTTP. O modelo é capaz de prever a ocorrência de diabetes com base em dados clínicos de pacientes.

A API foi construída utilizando **FastAPI** e o modelo foi treinado com dados do dataset *Pima Indians Diabetes*.

---

## 🚀 Tecnologias Utilizadas

* Python
* FastAPI
* Scikit-learn
* Pandas
* Numpy
* Uvicorn

---

## 📊 Modelo de Machine Learning

Foi utilizado um modelo de **Regressão Logística**, treinado com dados biomédicos para classificação de pacientes com ou sem diabetes.

---

## 📁 Estrutura do Projeto

```
ml-api-diabetes/
│
├── app.py                  # API FastAPI
├── model_diabetes.pkl      # Modelo treinado
├── requirements.txt        # Dependências
├── README.md               # Documentação
├── notebook.ipynb          # Treinamento do modelo
```

---

## ⚙️ Como Executar o Projeto

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/DudaAraujo14/ml-api-diabetes.git
cd ml-api-diabetes
```

### 🔹 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
# ou
venv\Scripts\activate          # CMD
```

### 🔹 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 🔹 4. Executar a API

```bash
uvicorn app:app --reload
```

---

## 🌐 API em Produção

A API está disponível em:

👉 https://ml-api-diabetes-4y0l.onrender.com/docs

---

## 🔥 Endpoint de Predição

### 📌 POST `/predict`

Realiza a predição de diabetes com base nos dados informados.

### 📥 Exemplo de entrada:

```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 85,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

### 📤 Exemplo de resposta:

```json
{
  "prediction": 0,
  "descricao": "Paciente sem diabetes"
}
```

---

## 📈 Resultado

O modelo apresentou boa performance na classificação, sendo capaz de identificar padrões nos dados e realizar previsões com acurácia satisfatória.

---

## 👩‍💻 Autora

Maria Eduarda Araujo Penas

---

## 📌 Observações

Este projeto foi desenvolvido como parte de atividade acadêmica com foco em:

* Treinamento de modelos de Machine Learning
* Criação de APIs
* Deploy em ambiente de nuvem

---
