curl https://sdk.cloud.google.com | bash
exec -l $SHELL

gcloud auth activate-service-account --key-file= gcp-compute-admin-key.json
gcloud config set project gcp-compute-admin

gcloud compute instances create web-server-instance \ 
     --zone = asia-east1-b    \
     --machine_type = e2-medium   \
     --image-family = debian-11    \
     --image-project = debian-cloud

gcloud compute firewall-rules create allow-ssh --allow=tcp:22 --source-ranges=0.0.0.0/0
