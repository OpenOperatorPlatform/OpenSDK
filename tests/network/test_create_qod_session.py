# -*- coding: utf-8 -*-
import time

import pytest

from sunrise6g_opensdk.common.sdk import Sdk as sdkclient
from sunrise6g_opensdk.network.core.common import CoreHttpError
from sunrise6g_opensdk.network.core.network_interface import NetworkManagementInterface
from tests.network.test_cases import test_cases


@pytest.fixture(scope="module", name="network_client")
def instantiate_network_client(request):
    """Fixture to create and share a network client across tests"""
    client_specs = request.param
    clients = sdkclient.create_clients_from(client_specs)
    return clients.get("network")


def id_func(val):
    return val["network"]["client_name"]


@pytest.mark.parametrize(
    "network_client",
    test_cases,
    ids=id_func,
    indirect=True,
)
def test_valid_input_open5gs(network_client: NetworkManagementInterface):
    camara_session = {
        "duration": 3600,
        "device": {
            "ipv4Address": {"publicAddress": "10.45.0.3", "privateAddress": "10.45.0.3"}
        },
        "applicationServer": {"ipv4Address": "10.45.0.1"},
        "devicePorts": {"ranges": [{"from": 0, "to": 65535}]},
        "applicationServerPorts": {"ranges": [{"from": 0, "to": 65535}]},
        "qosProfile": "qos-e",
        "sink": "https://endpoint.example.com/sink",
    }
    network_client._build_qod_subscription(camara_session)


@pytest.fixture(scope="module")
def qod_session_id(network_client: NetworkManagementInterface):
    camara_session = {
        "duration": 3600,
        "device": {
            "ipv4Address": {
                "publicAddress": "10.45.0.3",
                "privateAddress": "10.45.0.3",
            }
        },
        "applicationServer": {"ipv4Address": "10.45.0.1"},
        "devicePorts": {"ranges": [{"from": 0, "to": 65535}]},
        "applicationServerPorts": {"ranges": [{"from": 0, "to": 65535}]},
        "qosProfile": "qos-e",
        "sink": "https://endpoint.example.com/sink",
    }
    try:
        response = network_client.create_qod_session(camara_session)
        assert response is not None, "Response should not be None"
        assert isinstance(response, dict), "Response should be a dictionary"
        assert "sessionId" in response, "Response should contain 'sessionId'"
        yield str(response["sessionId"])
    finally:
        pass


@pytest.mark.parametrize(
    "network_client",
    test_cases,
    ids=id_func,
    indirect=True,
)
def test_create_qod_session(qod_session_id):
    assert qod_session_id is not None


@pytest.mark.parametrize("network_client", test_cases, ids=id_func, indirect=True)
def test_timer_wait_5_seconds(network_client):
    time.sleep(5)


@pytest.mark.parametrize("network_client", test_cases, ids=id_func, indirect=True)
def test_get_qod_session(network_client: NetworkManagementInterface, qod_session_id):
    try:
        network_client.get_qod_session(qod_session_id)
    except CoreHttpError as e:
        pytest.fail(f"Failed to retrieve qod session: {e}")


@pytest.mark.parametrize("network_client", test_cases, ids=id_func, indirect=True)
def test_delete_qod_session(network_client: NetworkManagementInterface, qod_session_id):
    try:
        network_client.delete_qod_session(qod_session_id)
    except CoreHttpError as e:
        pytest.fail(f"Failed to retrieve qod session: {e}")
