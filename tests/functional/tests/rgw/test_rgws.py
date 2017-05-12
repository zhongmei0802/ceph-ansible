import pytest


class TestRGWs(object):

    @pytest.mark.no_docker
    def test_rgw_services_are_running(self, node, host):
        service_name = "ceph-radosgw@rgw.ceph-{hostname}".format(
            hostname=node["vars"]["inventory_hostname"]
        )
        assert host.service(service_name).is_running

    @pytest.mark.no_docker
    def test_rgw_services_are_enabled(self, node, host):
        service_name = "ceph-radosgw@rgw.ceph-{hostname}".format(
            hostname=node["vars"]["inventory_hostname"]
        )
        assert host.service(service_name).is_enabled

    @pytest.mark.no_docker
    def test_rgw_http_endpoint(self, node, host):
        # rgw frontends ip_addr is configured on eth0
        ip_addr = host.interface("eth0").addresses[0]
        assert host.socket("tcp://{ip_addr}:{port}".format(ip_addr=ip_addr, port=8080)).is_listening

