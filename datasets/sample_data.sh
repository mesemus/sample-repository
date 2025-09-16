./run.sh invenio users create -a -c "demo@test.com" --password "demodemo" --profile '{"full_name": "Demo user"}'

token=$(./run.sh invenio tokens create -n demo-data -u demo@test.com)

# 1. Create draft
response=$(curl -sk -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $token" \
  -d '{
    "metadata": {
      "title": "Sample Dataset",
      "description": "This is a sample dataset."
    }
  }' \
  https://127.0.0.1:5000/api/datasets)

# 2. Extract the ID
id=$(echo $response | jq -r '.id')

# 3. Publish using the ID
curl -sk -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $token" \
  -d "$response" \
  https://127.0.0.1:5000/api/records/$id/draft/actions/publish
