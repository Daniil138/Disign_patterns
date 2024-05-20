#! /bin/bash


curl -X DELETE -H "Content-Type: application/json" -d @nomenclature.json http:/127.0.0.1:5000/api/nomenculature