# -*- coding: utf-8 -*-
# Mocked API for testing purposes
from typing import Dict, List, Optional

from src.edgecloud.core.edgecloud_interface import EdgeCloudManagementInterface


class EdgeApplicationManager(EdgeCloudManagementInterface):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def onboard_app(self, app_manifest: Dict) -> Dict:
        print(f"Submitting application: {app_manifest}")
        return {"appId": "1234-5678"}

    def get_all_onboarded_apps(self) -> List[Dict]:
        return [{"appId": "1234-5678", "name": "TestApp"}]

    def get_onboarded_app(self, app_id: str) -> Dict:
        return {"appId": app_id, "name": "TestApp"}

    def delete_onboarded_app(self, app_id: str) -> None:
        print(f"Deleting application: {app_id}")

    def deploy_app(self, app_id: str, app_zones: List[Dict]) -> Dict:
        return {"appInstanceId": "abcd-efgh"}

    def get_all_deployed_apps(
        self,
        app_id: Optional[str] = None,
        app_instance_id: Optional[str] = None,
        region: Optional[str] = None,
    ) -> List[Dict]:
        return [{"appInstanceId": "abcd-efgh", "status": "ready"}]

    def undeploy_app(self, app_instance_id: str) -> None:
        print(f"Deleting app instance: {app_instance_id}")

    def get_edge_cloud_zones(
        self, region: Optional[str] = None, status: Optional[str] = None
    ) -> List[Dict]:
        return [{"edgeCloudZoneId": "zone-1", "status": "active"}]

    def get_edge_cloud_zones_details(
        self, zone_id: str, flavour_id: Optional[str] = None
    ) -> Dict:
        # Minimal mocked response based on required fields of 'ZoneRegisteredData' in GSMA OPG E/WBI API
        return {
            "zoneId": zone_id,
            "reservedComputeResources": [
                {
                    "cpuArchType": "ISA_X86_64",
                    "numCPU": "4",
                    "memory": 8192,
                }
            ],
            "computeResourceQuotaLimits": [
                {
                    "cpuArchType": "ISA_X86_64",
                    "numCPU": "8",
                    "memory": 16384,
                }
            ],
            "flavoursSupported": [
                {
                    "flavourId": "medium-x86",
                    "cpuArchType": "ISA_X86_64",
                    "supportedOSTypes": [
                        {
                            "architecture": "x86_64",
                            "distribution": "UBUNTU",
                            "version": "OS_VERSION_UBUNTU_2204_LTS",
                            "license": "OS_LICENSE_TYPE_FREE",
                        }
                    ],
                    "numCPU": 4,
                    "memorySize": 8192,
                    "storageSize": 100,
                }
            ],
        }
