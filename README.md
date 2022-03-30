This repository contains python script to build simple way to machine learning models to predict hepatitis B viral load in hepatitis B infected population. The repository does not contain the data file for the work as the data is the product of original research work, which may be made available publicly in the later stage. The app developed during the project analyzes the data of 349 hepatitis B patients.

About the data: The data contains age, gender, Hepatitis B serface Antigen (HBsAg) levels, Hepatitis B e Antigen (HBeAg) levels and HBV DNA load. HBV DNA load was the target of the model and other features were the predictors.

About the App: The app shows the prediction by regression models for HBV DNA load. This kind of prediction is extremely helpful for the clinicians to select a therapy. HBsAg and HBeAg play a critical in such decision. The app has been deployed online on herokuapp.com and can be viewed at : https://aseem-hbv-ml-models.herokuapp.com/

Deployment method: The app has been developed using explainer dashboard and has been deployed on heroku app. The following steps can help you to deploy your dashboard:

1. Save your dashboard.py and data file in a directory.
2. After completing your explainer dashboard script, add the following command at the bottom of dashboard.py file:
	>> db.to_yaml("dashboard.yaml", explainerfile="explainer.joblib", dump_explainer=True)   ### Do not forget to 			'shap_interaction=False' in side your ExplainerDashboard
3. Open the linux terminal in the directory and run your dashboard.py file in terminal by:
	$ python dashboard.py
4. Then open the dashboard.py file and paste the following command at the bottom.
	>> db = ExplainerDashboard.from_config("dashboard.yaml")
	>> app = db.flask_server()
5. Start the gunicorn server by the following command:

	$ gunicorn dashboard:app
	
		or
		
	$ gunicorn -w 3 -b localhost:8050 dashboard:app
6. Now for deploying at heroku follow the instructions from here https://github.com/asimanshu/Interactive_COVID_19_Dashboard_deployed_using_heroku

### Do not forget to install gunicorn from your requirement file. 
### If problem persists in deplyoment, do run '$ heroku logs --tail' on your terminal from the directory or '$ heroku logs --tail --app your_app_name' from outside the directory.

Based on the complexity of your dataset, it may incur problem sometimes during reload after the deployment, please try to reload it several times or update the deployment. 

This project is at its juvenile stage. I am planning to build dashboard with regression and classifier for the prediction of HBV DNA load or its grading sytem in near future.

 
