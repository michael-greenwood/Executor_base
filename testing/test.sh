#!/bin/bash

BASE_URL="http://132.156.103.106:8999/remote_ctrl/sim"
UUID="11111111-1111-1111-1111-111111111111"
FINGERPRINT="22222222-2222-2222-2222-222222222222"

echo "== Create experiment =="
curl -s -X POST "$BASE_URL/experiment/new" \
  -H "Content-Type: application/json" \
  -d "{
    \"experiment_name\": \"test_exp\",
    \"campaign_name\": \"test_campaign\",
    \"experiment_uuid\": \"$UUID\",
    \"exp_exec_fingerprint\": \"$FINGERPRINT\"
  }"
echo -e "\n"

echo "== Configure module_A =="
curl -s -X POST "$BASE_URL/experiment/$UUID/config/module_A" \
  -H "Content-Type: application/json" \
  -d '{ "x": 5 }'
echo -e "\n"

echo "== Queue experiment =="
curl -s -X PUT "$BASE_URL/queue/$UUID"
echo -e "\n"

echo "== Poll experiment status =="
for i in {1..6}; do
  curl -s "$BASE_URL/experiment/$UUID/status"
  echo
  sleep 3
done

echo "== Get module_A result =="
curl -s "$BASE_URL/experiment/$UUID/results/module_A"
echo
