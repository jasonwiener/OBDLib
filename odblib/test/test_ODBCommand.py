from __future__ import absolute_import

import unittest
from ..ODBUtils import ODBCommand, DATA_SIZE
from mock import MagicMock, call


class TestODBCommand(unittest.TestCase):
    def setUp(self):
        self.bluetooth_device_mock = MagicMock()

        self.odb_command = ODBCommand(self.bluetooth_device_mock, "AT Z")

    def test_send(self):
        self.bluetooth_device_mock.recv = MagicMock(side_effect=["ELM327 v2.1", ""])

        self.odb_command.send()

        self.bluetooth_device_mock.send.assert_called_once_with("AT Z\r")
        self.bluetooth_device_mock.recv.assert_has_calls([call(DATA_SIZE), call(DATA_SIZE)])

if __name__ == '__main__':
    unittest.main()