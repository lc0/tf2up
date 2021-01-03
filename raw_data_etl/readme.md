# How to generate stats

Export [service account config from GCP](https://console.cloud.google.com/identity/serviceaccounts)
```sh
export GOOGLE_APPLICATION_CREDENTIALS=./brainscode-140622-977bffaaf3e2.json
```

Process all files from Google Storage
```python
python process.py --input gs://tf2up/reports/ --output result.txt
```

Or specific rage with a regex
```
python process.py --input 'gs://tf2up/reports/2021*' --output result.txt
```

Now the data cuild be queried from BigQuery
```sql
SELECT
  FORMAT_DATE("%Y-%b", date) as period,
  count(*) as proposed_changes,
  count(DISTINCT file_hash) as processed_files
FROM `brainscode-140622.tf2up.conversions`
WHERE file_hash != '7fa4f7b5ede5f6c12885e8ae2766eac0'
GROUP BY
  1
ORDER BY
  1 desc
```
