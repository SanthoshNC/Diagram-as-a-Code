from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.network import ELB, Route53
from diagrams.aws.database import RDS
from diagrams.onprem.client import User

graph_attr = {
    "fontsize": "25",
    "bgcolor": "transparent"
}

with Diagram("Simple Diagram", show=False, outformat="jpg", filename="my_diagram"):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        web_service_group = [ECS("web1"), ECS("web2")]

    with Cluster("DB Cluster"):
        db_master = RDS("db1 master")
        db_master - [RDS("db1 read only")]

    User("User") >> dns >> lb >> web_service_group
    web_service_group >> db_master
    web_service_group << db_master
