"A few utility functions to support persisting report data to cloud"

from datetime import date

from google.cloud import storage
# from google.cloud import bigquery

# TODO: move this to config
CLOUD_STORAGE_BUCKET = 'tf2up'
GSC_FOLDER = 'reports'

class Storage(object):

    def __init__(self, dataset_id: str, table_id: str, dataset_location='US'):
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.dataset_location = dataset_location

        self._auth()

    def _auth(self) -> None:
        """Auth with credentials provided via GOOGLE_APPLICATION_CREDENTIALS"""

        # self._bq_client = bigquery.Client()
        self._gs_client = storage.Client(project=self.dataset_id)

    @staticmethod
    def gen_filename(filename: str, github_hash: str) -> str:
        """Generate a filename for GCS"""

        today = date.today().isoformat()
        filename = f"{GSC_FOLDER}/{today}_{github_hash}_report.txt"

        return filename

    def save_file(self, filename: str, github_hash: str):
        """Store file to GCS"""

        remote_filename = Storage.gen_filename(filename, github_hash)

        bucket = self._gs_client.bucket(CLOUD_STORAGE_BUCKET)
        blob = bucket.blob(remote_filename)
        blob.upload_from_filename(filename)

    # def _normalize_bq_file(self, file):
    #     """
    #     Transform a raw file to be able to store in a reasonable format in BQ
    #     """

    #     pass

    # def save_to_bq(self, filename,
    #               source_format=bigquery.SourceFormat.CSV):
    #     dataset_ref = self._bq_client.dataset(self.dataset_id)
    #     table_ref = dataset_ref.table(self.table_id)

    #     job_config = bigquery.LoadJobConfig()
    #     job_config.source_format = source_format
    #     job_config.skip_leading_rows = 1
    #     job_config.autodetect = True

    #     with open(filename, "rb") as source_file:
    #         job = self._bq_client.load_table_from_file(
    #             source_file,
    #             table_ref,
    #             location=self.dataset_location,
    #             job_config=job_config,
    #         )

    #     job.result()  # Waits for table load to complete.


if __name__ == "__main__":
    # TODO: move this to tests
    storage = Storage(dataset_id='foo', table_id='bar')
    storage.save_file('/srv/labs.brainscode/tf2up/cluster_setup/helm_init.sh', 'abs')
    print("All amazing so far")
