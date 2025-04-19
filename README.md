# DS5105 Exercise 2

This project estimates the causal effect of a carbon offset program using linear regression,
and provides a Flask API to predict stakeholder engagement scores in a reproducible containerized environment.
It also added the "attempt 'resolving a merge conflict'" question that was not completed in Exercise 1.

## Assumptions for Causal Interpretation (Rubin Causal Model)
The estimated ATE (τ̂) can be interpreted as causal under these assumptions:
1. Unconfoundedness: Treatment assignment is independent of potential outcomes.
2. SUTVA: No interference between units, and consistent treatment definition.
3. Overlap: Each unit has a non-zero probability of receiving treatment or control.

## Contents
- `regression_analysis.py`: Compares models with and without covariates, saves trained model, and plots residuals.
- `app.py`: Flask API exposing both GET and POST prediction endpoints.
- `data/engagement_data.csv`: Input dataset.
- `model/trained_model.pkl`: Trained linear model.
- `figures/residual_plot.png`: Residual analysis.
- `requirements.txt`: Required Python packages.
- `Dockerfile`: For containerization.

## How to Use
1. Train the model:
```
python regression_analysis.py
```

2. Start the Flask server:
```
python app.py
```

3. Example GET call:
```
http://localhost:5000/predict?W=1&X=20
```

4. Example POST call:
```json
POST /predict
{ "W": 1, "X": 20 }
```

## ✅ Bonus Features
- Model comparison: With/without covariate.
- Residual plot to validate regression assumptions.
- Input validation and POST/GET support in API.
