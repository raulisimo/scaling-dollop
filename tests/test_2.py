import pytest

from task_1.device_controller_oop import DeviceController


class TestDeviceController:

    @pytest.fixture
    def device_controller(self):
        return DeviceController(serial_port="COM1")

    def test_connect(self, device_controller):
        device_controller.connect()
        assert device_controller.ser.is_open
        device_controller.disconnect()

    def test_program_digital_outputs(self, device_controller):
        device_controller.connect()
        device_controller.program_digital_outputs(active_devices=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])
        # You can add assertions here to check that the program_digital_outputs function worked correctly,
        # such as by reading the state of the digital outputs or by using a microcontroller emulator
        device_controller.disconnect()
