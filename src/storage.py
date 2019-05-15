"A few utility functions to support persisting report data to cloud"

from datetime import date

from google.cloud import storage


CLOUD_STORAGE_BUCKET = 'tf2up'
GSC_FOLDER = 'reports'

class FileStorage(object):

    def __init__(self, gs_bucket=CLOUD_STORAGE_BUCKET):
        self._gs_bucket = gs_bucket
        self._auth()

    def _auth(self) -> None:
        """Auth with credentials provided via GOOGLE_APPLICATION_CREDENTIALS"""

        self._gs_client = storage.Client()

    @staticmethod
    def gen_filename(filename: str, github_hash: str) -> str:
        """Generate a filename for GCS"""

        today = date.today().isoformat()
        filename = f"{GSC_FOLDER}/{today}_{github_hash}_report.txt"

        return filename

    def save_file(self, filename: str, github_hash: str):
        """Store file to GCS"""

        remote_filename = FileStorage.gen_filename(filename, github_hash)

        bucket = self._gs_client.bucket(self._gs_bucket)
        blob = bucket.blob(remote_filename)
        blob.upload_from_filename(filename)


if __name__ == "__main__":
    # TODO: move this to tests
    storage = FileStorage()
    storage.save_file('/srv/labs.brainscode/tf2up/cluster_setup/helm_init.sh', 'abs')
    print("All amazing so far")
