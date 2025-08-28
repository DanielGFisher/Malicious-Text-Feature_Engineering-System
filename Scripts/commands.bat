# OpenShift Deployment Commands for Iranian Tweets Pipeline

# 1. Log in to OpenShift
oc login <OC LOGIN> --token=<JSDDNAS748391> --namespace=<Malicious-Text-Feature_Engineering-System>

# Check current project
oc project

# 2. Create a new project / namespace (if needed)
oc new-project iran_tweets_pipeline

# 3. Deploy services from Docker images
oc create deployment preprocessor --image=isaac10/preprocessor:latest
oc create deployment enricher --image=isaac10/enricher:latest
oc create deployment persister --image=isaac10/persister:latest
oc create deployment dataretrieval --image=isaac10/dataretrieval:latest

# 4. Expose services as needed (REST API for DataRetrieval)
oc expose deployment dataretrieval --port=8000 --target-port=8000 --name=dataretrieval-service
oc expose svc/dataretrieval-service

# 5. Set environment variables
oc set env deployment/preprocessor MONGO_URI="mongodb://mongo:27017"
oc set env deployment/enricher KAFKA_BROKERS="kafka:9092"
# Add any additional variables (weapons file path, Atlas credentials, etc.)

# 6. Scale deployments
oc scale deployment preprocessor --replicas=2
oc scale deployment enricher --replicas=2
oc scale deployment persister --replicas=1
oc scale deployment dataretrieval --replicas=1

# 7. View logs
oc logs -f deployment/preprocessor
oc logs -f deployment/enricher
oc logs -f deployment/persister
oc logs -f deployment/dataretrieval

# 8. Delete deployments / cleanup
oc delete deployment preprocessor
oc delete deployment enricher
oc delete deployment persister
oc delete deployment dataretrieval
oc delete project iran_tweets_pipeline