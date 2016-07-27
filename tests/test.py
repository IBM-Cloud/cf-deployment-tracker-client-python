import unittest
from cf_deployment_tracker import track

###########################
#        Unit Tests       #
###########################


class DeployEventTestCase(unittest.TestCase):
    """Tests for `cf_deployment_tracker/__init__.py - track()`."""

    def deploy_event_test(self):
        """Send a sample test event to the dev deployment tracker"""

        dev_deployment_tracker_url = 'https://deployment-tracker-dev.mybluemix.net/api/v1/track'
        self.assertTrue(track(dev_deployment_tracker_url) is None)

if __name__ == '__main__':
    unittest.main()
