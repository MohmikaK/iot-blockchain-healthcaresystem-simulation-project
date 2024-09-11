//21BCT0027
// SPDX-License-Identifier: MIT

pragma solidity 0.8.21;

contract HealthcareSensors {
    address public owner;

    struct Data {
        uint256 ecg;
        uint256 temperature;
        uint256 spo2;
        uint256 timestamp;
    }

    Data[] public dataRecords;

    event SensorDataRecorded(address indexed sender, uint256 timestamp, uint256 ecg, uint256 temperature, uint256 spo2);

    constructor() {
        owner = msg.sender;
    }

    function recordSensorData(uint256 _ecg, uint256 _temperature, uint256 _spo2) public {
        dataRecords.push(Data({
            ecg: _ecg,
            temperature: _temperature,
            spo2: _spo2,
            timestamp: block.timestamp
        }));
        emit SensorDataRecorded(msg.sender, block.timestamp, _ecg, _temperature, _spo2);
    }

    function getAllTimestamps() public view returns (uint256[] memory) {
        uint256[] memory timestamps = new uint256[](dataRecords.length);
        for (uint256 i = 0; i < dataRecords.length; i++) {
            timestamps[i] = dataRecords[i].timestamp;
        }
        return timestamps;
    }

    function getSensorData(uint256 _timestamp) public view returns (uint256 ecg, uint256 temperature, uint256 spo2) {
        for (uint256 i = 0; i < dataRecords.length; i++) {
            if (dataRecords[i].timestamp == _timestamp) {
                return (dataRecords[i].ecg, dataRecords[i].temperature, dataRecords[i].spo2);
            }
        }
        revert("Data for the given timestamp not found.");
    }
}
