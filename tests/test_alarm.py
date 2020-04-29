from src.alarm import Alarm
from src.sensor import Sensor
import pytest
from unittest.mock import Mock


@pytest.fixture
def alarm():
    return Alarm()


def test_alarm_is_off_by_default(alarm):
    assert not alarm.is_alarm_on


class StubSensor:
    def sample_pressure(self):
        return 15


def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor=StubSensor())
    alarm.check()
    assert alarm.is_alarm_on


def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 18
    alarm = Alarm(stub_sensor)
    alarm.check()
    assert not alarm.is_alarm_on