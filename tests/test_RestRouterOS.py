from RestRouterOS.api import RestRouterOS
from pytest_httpx import HTTPXMock


def test_identity(httpx_mock: HTTPXMock):
    data = {"name": "MikroTik"}
    httpx_mock.add_response(url="https://test_api:8443/rest/system/identity",json=data)
    
    router = RestRouterOS("test_api", "user", "pass")
    response = router.identity()
    assert response['name'] == 'MikroTik'

def test_routerboard(httpx_mock: HTTPXMock):
    data = {
        "current-firmware": "7.17",
        "factory-firmware": "3.35",
        "firmware-type": "ipq8060",
        "model": "RB3011UiAS",
        "routerboard": "true",
        "serial-number": "0000000000",
        "upgrade-firmware": "7.17"
    }
    httpx_mock.add_response(url="https://test_api:8443/rest/system/routerboard",json=data)
    
    router = RestRouterOS("test_api", "user", "pass")
    response = router.routerboard()
    assert response['current-firmware'] == '7.17'
    assert response['factory-firmware'] == '3.35'
    assert response['firmware-type'] == 'ipq8060'
    assert response['model'] == 'RB3011UiAS'
    assert response['routerboard'] == 'true'
    assert response['serial-number'] == '0000000000'
    assert response['upgrade-firmware'] == '7.17'

def test_health(httpx_mock: HTTPXMock):
    data = [
        {
            ".id": "*D",
            "name": "voltage",
            "type": "V",
            "value": "24.2"
        },
        {
            ".id": "*E",
            "name": "temperature",
            "type": "C",
            "value": "36"
        }
    ]
    httpx_mock.add_response(url="https://test_api:8443/rest/system/health",json=data)
    
    router = RestRouterOS("test_api", "user", "pass")
    response = router.health()
    assert response[0]['name'] == 'voltage'
    assert response[0]['value'] == '24.2'
    assert response[0]['type'] == 'V'
    assert response[1]['name'] == 'temperature'
    assert response[1]['value'] == '36'
    assert response[1]['type'] == 'C'

def test_resources(httpx_mock: HTTPXMock):
    data = {
        "architecture-name": "arm",
        "bad-blocks": "0.2",
        "board-name": "RB3011UiAS",
        "build-time": "2025-01-16 08:19:28",
        "cpu": "ARM",
        "cpu-count": "2",
        "cpu-frequency": "1400",
        "cpu-load": "3",
        "factory-software": "6.35.3",
        "free-hdd-space": "92110848",
        "free-memory": "973053952",
        "platform": "MikroTik",
        "total-hdd-space": "134217728",
        "total-memory": "1073741824",
        "uptime": "6d23h19m23s",
        "version": "7.17 (stable)",
        "write-sect-since-reboot": "14202",
        "write-sect-total": "58109"
    }
    httpx_mock.add_response(url="https://test_api:8443/rest/system/resource",json=data)
    
    router = RestRouterOS("test_api", "user", "pass")
    response = router.resource()
    assert response['architecture-name'] == 'arm'
    assert response['bad-blocks'] == '0.2'
    assert response['board-name'] == 'RB3011UiAS'
    assert response['build-time'] == '2025-01-16 08:19:28'
    assert response['cpu'] == 'ARM'
    assert response['cpu-count'] == '2'
    assert response['cpu-frequency'] == '1400'
    assert response['cpu-load'] == '3'
    assert response['factory-software'] == '6.35.3'
    assert response['free-hdd-space'] == '92110848'
    assert response['free-memory'] == '973053952'
    assert response['platform'] == 'MikroTik'
    assert response['total-hdd-space'] == '134217728'
    assert response['total-memory'] == '1073741824'
    assert response['uptime'] == '6d23h19m23s'
    assert response['version'] == '7.17 (stable)'
    assert response['write-sect-since-reboot'] == '14202'
    assert response['write-sect-total'] == '58109'
    
