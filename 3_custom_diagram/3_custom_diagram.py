from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.network import Nginx
from diagrams.onprem.network import Tomcat
from diagrams.onprem.inmemory import Memcached
from diagrams.onprem.queue import Rabbitmq
from diagrams.onprem.database import Mongodb
from diagrams.onprem.database import Mysql
from diagrams.elastic.elasticsearch import Elasticsearch



with Diagram("Web Architecture", show=False, outformat="jpg", filename="custom_diagram", direction="LR"):
  
  with Cluster("Public Network"):
     android = Custom("Android", "./my_resources/android.png")
     chrome = Custom("Google Chrome", "./my_resources/chrome.png")
     firefox = Custom("Mozilla Firefox", "./my_resources/firefox.png")
     loadbalancer = Custom("Load Balancer", "./my_resources/loadbalancer.png")
                 
  android >> Edge(label = "Request 1") >> loadbalancer
  chrome >> Edge(label = "Request 2") >> loadbalancer
  firefox >> Edge(label = "Request 3") >> loadbalancer
  
  with Cluster("Private Network"):
     with Cluster("Web Tier"):
        nginx_cluster = Nginx("Nginx")
     with Cluster("App Tier"):
        tomcat_cluster = Tomcat("Tomcat")
     with Cluster("Backend Service"):
        with Cluster("Queuing"):
            rabbitmq = Rabbitmq("Rabbit MQ")
        with Cluster("Cache"):
            memcached = Memcached("MemcacheD")
        with Cluster("DB Tier"):
            db_cluster = [Mysql("MySQL"),Mongodb("MongoDB")]
        with Cluster("Indexing"):
            elasticsearch = Elasticsearch("Elasticsearch")
        
  loadbalancer >> nginx_cluster >> tomcat_cluster >> rabbitmq >> memcached
  rabbitmq >> db_cluster
  db_cluster >> elasticsearch
  tomcat_cluster >> elasticsearch
   
  