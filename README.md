# Airflow Set Up

## Helm chart sourced from
```sh
helm pull oci://registry-1.docker.io/bitnamicharts/airflow
```

## Deploying to OpenShift
```sh
helm install dev-release-af .
```

## Get the application running with these commands:
```sh
oc --namespace a1b9b0-dev port-forward svc/dev-release-af-airflow 8080:8080
```

## Upgrade OpenShift Deployment
```sh 
helm upgrade dev-release-af . --version 16.1.2  
```

## Create OpenShift ConfigMaps for DAGs and requirements.txt: 
```sh
oc create configmap airflow-requirements --from-file=requirements.txt
```
```sh
oc create configmap airflow-dags --from-file=dags
```
Delete if already exists: 
```sh
oc delete configmap airflow-dags
```



More info: https://apps.nrs.gov.bc.ca/int/confluence/x/zQ09Cg

