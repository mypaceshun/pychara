import os
import pytest
from pychara.session import Session, LOGIN, LOGOUT

class TestFetchApplyEvents():
    def test_fetch_apply_events(self):
        secrets_path = os.environ.get('SECRETS', 'secrets')
        with open(secrets_path, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
        session = Session()
        if session.fetch_apply_enable():
            event_list = session.fetch_apply_events()
            assert isinstance(event_list, list)
