
import os
import pytest
from pychara.session import Session, LOGIN, LOGOUT

class TestApplySchedule():
    def test_fetch_apply_schedule(self):
        secrets_path = os.environ.get('SECRETS', 'secrets')
        with open(secrets_path, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
        session = Session()
        enable = session.apply_enable()
        assert isinstance(enable, bool)
