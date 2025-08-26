./run.sh invenio users create -a -c "demo@test.com" --password "demodemo" --profile '{"full_name": "Demo user"}'

token=$(./run.sh invenio tokens create -n demo-data -u demo@test.com)

curl -k -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" -d '{
  "metadata": {
    "title": "Sample Dataset",
    "description": "This is a sample dataset."
  }
}' https://localhost:5000/api/datasets
